import os
import json
import time
import re
import random
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field, ValidationError
import backoff

# Load environment variables
load_dotenv()

# 定義Pydantic模型來驗證履歷結構
class ResumeMetadata(BaseModel):
    generated_date: str
    resume_type: str
    index: int
    diversity_traits: Dict[str, str]

class BaseResume(BaseModel):
    metadata: Optional[ResumeMetadata] = None
    
    class Config:
        extra = "allow"  # 允許額外欄位，因為不同類型的履歷結構不同

def read_api_key_from_env_file():
    """直接從.env文件讀取API key"""
    env_path = Path(".env")
    if not env_path.exists():
        raise ValueError(".env file not found")
        
    with open(env_path, 'r') as f:
        for line in f:
            if line.startswith('OPENAI_API_KEY='):
                return line.strip().split('=', 1)[1]
    
    raise ValueError("OPENAI_API_KEY not found in .env file")

def load_sample_schemas(resume_type: str) -> List[Dict[str, Any]]:
    """載入指定類型的所有樣本schema"""
    resume_dir = Path("data/resume")
    schemas = []
    
    for file_path in resume_dir.glob(f"{resume_type}_sample*.json"):
        with open(file_path, 'r', encoding='utf-8') as f:
            schemas.append(json.load(f))
    
    return schemas

def get_simplified_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
    """獲取簡化的schema結構，減少複雜性但保留重要結構"""
    # 不再为MLE类型使用固定模板，而是基于原始schema简化
    if "data" in schema and isinstance(schema["data"], dict):
        # 保留原始的主要结构，但简化内容
        # 这种方式保持数据层次结构，但减少每个部分的复杂性
        simplified = {}
        
        # 复制主要部分但简化内容
        if "data" in schema:
            simplified["data"] = {}
            
            # 复制sidebar结构
            if "sidebar" in schema["data"]:
                simplified["data"]["sidebar"] = schema["data"]["sidebar"]
            
            # 复制profile部分但简化
            if "profile" in schema["data"]:
                simplified["data"]["profile"] = {
                    "key": "example_key",
                    "nickname": "範例姓名",
                    "title": {
                        "workExperience": 0,
                        "companyName": "範例公司",
                        "jobName": "機器學習工程師"
                    },
                    "aboutMe": "個人簡介範例",
                    "abilities": ["技能1", "技能2"]
                }
            
            # 复制其他主要部分
            for key in ["education", "experience", "skill", "certificate", "language", "project"]:
                if key in schema["data"]:
                    simplified["data"][key] = {
                        # 保留主要结构但简化内容
                        "placeholder": f"{key}結構示例 - 請遵循原始schema格式"
                    }
        
        return simplified
    return schema

def extract_json_from_text(text: str) -> str:
    """從文本中提取JSON"""
    # 尋找最外層的花括號內容
    opening_braces = 0
    closing_braces = 0
    start_index = -1
    end_index = -1
    
    for i, char in enumerate(text):
        if char == '{':
            opening_braces += 1
            if start_index == -1:
                start_index = i
        elif char == '}':
            closing_braces += 1
            if opening_braces == closing_braces and opening_braces > 0:
                end_index = i + 1
                break
    
    if start_index != -1 and end_index != -1:
        return text[start_index:end_index]
    
    # 如果上面的方法失敗，使用正則表達式
    pattern = r'(\{[\s\S]*\})'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    
    return text

def fix_json(broken_json: str) -> str:
    """使用更强大的方法修复破损的JSON"""
    # 修复常见JSON格式问题
    
    # 移除不可见控制字符
    json_str = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', broken_json)
    
    # 移除markdown代码块标记
    json_str = re.sub(r'```json\s*', '', json_str)
    json_str = re.sub(r'```\s*$', '', json_str)
    
    # 删除注释
    json_str = re.sub(r'//.*?\n', '\n', json_str)
    
    # 修复引号问题
    fixed = ""
    in_string = False
    escape_next = False
    
    for char in json_str:
        if char == '\\':
            escape_next = not escape_next
            fixed += char
            continue
            
        if char == '"' and not escape_next:
            in_string = not in_string
            
        if not in_string and char in ['\n', '\r', '\t']:
            fixed += ' '
        else:
            fixed += char
            
        escape_next = False
    
    # 修复缺失的引号 (对象中的键)
    fixed = re.sub(r'([{,]\s*)([a-zA-Z0-9_]+)(\s*:)', r'\1"\2"\3', fixed)
    
    # 修复结尾的逗号
    fixed = re.sub(r',(\s*[}\]])', r'\1', fixed)
    
    # 修复缺失的引号 (字符串值)
    fixed = re.sub(r':\s*([a-zA-Z0-9_]+)([,}])', r': "\1"\2', fixed)
    
    # 更加激进地处理未闭合的引号
    try:
        json.loads(fixed)
    except json.JSONDecodeError as e:
        error_msg = str(e)
        if "Unterminated string" in error_msg:
            # 尝试修复未终止的字符串
            line_col = re.search(r'line (\d+) column (\d+)', error_msg)
            if line_col:
                line, col = int(line_col.group(1)), int(line_col.group(2))
                lines = fixed.split('\n')
                if line <= len(lines):
                    problem_line = lines[line-1]
                    if col <= len(problem_line):
                        # 添加缺失的引号
                        fixed_line = problem_line[:col] + '"' + problem_line[col:]
                        lines[line-1] = fixed_line
                        fixed = '\n'.join(lines)
        
        if "Expecting ',' delimiter" in error_msg:
            # 尝试修复缺失的逗号
            line_col = re.search(r'line (\d+) column (\d+)', error_msg)
            if line_col:
                line, col = int(line_col.group(1)), int(line_col.group(2))
                lines = fixed.split('\n')
                if line <= len(lines):
                    problem_line = lines[line-1]
                    if col <= len(problem_line):
                        # 添加缺失的逗号
                        fixed_line = problem_line[:col] + ',' + problem_line[col:]
                        lines[line-1] = fixed_line
                        fixed = '\n'.join(lines)
    
    # 检查所有开始和结束括号
    brace_count = 0
    bracket_count = 0
    
    for char in fixed:
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
        elif char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
    
    # 添加缺失的括号
    while brace_count > 0:
        fixed += '}'
        brace_count -= 1
    
    while bracket_count > 0:
        fixed += ']'
        bracket_count -= 1
    
    # 检查负值 (过多的关闭括号)
    if brace_count < 0 or bracket_count < 0:
        # 尝试更简单的方法 - 从第一个 { 到最后一个 }
        start = fixed.find('{')
        end = fixed.rfind('}') + 1
        if start >= 0 and end > start:
            fixed = fixed[start:end]
    
    # 最后一次尝试 - 使用正则表达式提取最外层的JSON对象
    try:
        json.loads(fixed)
    except:
        pattern = r'(\{[\s\S]*\})'
        match = re.search(pattern, fixed)
        if match:
            extracted = match.group(1)
            try:
                json.loads(extracted)
                fixed = extracted
            except:
                pass
    
    return fixed

def generate_diverse_characteristics():
    """生成多樣化的人物特徵"""
    industries = [
        "金融科技", "電子商務", "醫療健康", "教育科技", "智慧製造", 
        "永續能源", "遊戲開發", "數位媒體", "物聯網", "雲端服務",
        "人工智能", "區塊鏈", "綠色能源", "生物科技", "航太科技"
    ]
    
    work_styles = [
        "創新思考", "團隊合作", "獨立解決問題", "跨領域溝通", "精確細緻", 
        "快速執行", "策略規劃", "分析洞察", "客戶導向", "績效專注",
        "系統思考", "批判性思維", "敏捷開發", "遠端協作", "持續學習"
    ]
    
    career_stages = [
        "應屆畢業生", "初階專業人士", "中階管理者", "資深專家", "領域專家",
        "技術顧問", "轉職工程師", "博士研究員", "實習生", "部門主管"
    ]
    
    project_types = [
        "大數據分析", "預測模型開發", "商業智能實施", "機器學習演算法優化",
        "資料視覺化儀表板", "客戶行為分析", "風險評估模型", "自動化報告系統",
        "市場區隔分析", "實時數據處理", "聊天機器人開發", "推薦系統",
        "NLP應用", "電腦視覺專案", "資料管線建置"
    ]
    
    return {
        "industry": random.choice(industries),
        "work_style": random.choice(work_styles),
        "career_stage": random.choice(career_stages),
        "project_focus": random.choice(project_types)
    }

def stringified_loads(json_str: str) -> Dict[str, Any]:
    """自定义JSON加载函数，将所有非字符串值转为字符串"""
    def visit_and_modify(obj):
        if isinstance(obj, dict):
            return {k: visit_and_modify(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [visit_and_modify(item) for item in obj]
        elif isinstance(obj, (int, float)):
            return str(obj)
        elif isinstance(obj, bool):
            return str(obj).lower()
        return obj
    
    # 先正常加载
    data = json.loads(json_str)
    # 然后递归地将所有非字符串值转为字符串
    return visit_and_modify(data)

@backoff.on_exception(backoff.expo, Exception, max_tries=3, jitter=None)
def generate_resume_with_retry(client: OpenAI, resume_type: str, index: int) -> Dict[str, Any]:
    """使用重試機制生成履歷"""
    return _generate_resume(client, resume_type, index)

def extract_schema_structure(schema: Dict[str, Any]) -> Dict[str, Any]:
    """提取schema结构，将所有值替换为占位符"""
    if isinstance(schema, dict):
        return {k: extract_schema_structure(v) for k, v in schema.items()}
    elif isinstance(schema, list):
        if not schema:
            return []
        # 对于列表，只保留第一个元素作为样本
        return [extract_schema_structure(schema[0])]
    elif isinstance(schema, (int, float)):
        return "NUMBER_PLACEHOLDER"
    elif isinstance(schema, bool):
        return "BOOLEAN_PLACEHOLDER"
    elif schema is None:
        return "NULL_PLACEHOLDER"
    else:
        return "VALUE_PLACEHOLDER"

def generate_values_for_schema(client: OpenAI, schema_with_placeholders: Dict[str, Any], resume_type: str, diverse_traits: Dict[str, str]) -> Dict[str, Any]:
    """为schema中的占位符生成实际值"""
    # 将schema转换为JSON字符串
    schema_str = json.dumps(schema_with_placeholders, ensure_ascii=False, indent=2)
    
    # 为不同类型的占位符创建生成指南
    prompt = f"""我需要你为以下JSON schema中的占位符生成实际值。

schema:
{schema_str}

请注意:
1. "NUMBER_PLACEHOLDER" 应替换为合适的数字
2. "BOOLEAN_PLACEHOLDER" 应替换为 true 或 false
3. "NULL_PLACEHOLDER" 应替换为 null
4. "VALUE_PLACEHOLDER" 应替换为适当的字符串值

生成内容应该:
- 使用繁體中文
- 符合 {resume_type.upper()} 类型的专业履历内容
- 具有以下特点:
  - 產業焦點：{diverse_traits["industry"]}
  - 工作風格：{diverse_traits["work_style"]}
  - 職涯階段：{diverse_traits["career_stage"]}
  - 專案類型：{diverse_traits["project_focus"]}

內容生成要求：

1. 工作經驗描述：
   - 根據職涯階段和工作風格，決定描述的詳細程度
   - 初階職位可以簡潔描述主要職責
   - 資深職位需要更詳細的技術細節和成果
   - 描述要符合實際工作場景，避免過度誇大

2. 專案經驗描述：
   - 根據專案類型和職涯階段調整內容深度
   - 可以包含具體的技術棧和工具
   - 描述要真實合理，避免過度理想化

3. 技能描述：
   - 根據工作經驗和專案經驗來描述相關技能
   - 技能熟練度要符合職涯階段
   - 避免列出過多不相關的技能

4. 教育背景：
   - 根據職涯階段決定是否詳細描述課程內容
   - 可以提到相關的研究或專案經驗
   - 證書和榮譽要符合實際情況

请生成替换后的完整JSON。保持原始结构不变，只替换占位符。"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "你是一個專業的值生成助手。你的任務是為JSON結構中的佔位符生成合適的實際值，確保生成的內容專業、合理、多樣化，且符合履歷的上下文。保持JSON結構不變，只替換佔位符。注意生成內容的多樣性，避免所有履歷都過於詳細或過於簡潔。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=4000
    )
    
    content = response.choices[0].message.content.strip()
    
    try:
        # 尝试解析生成的JSON
        populated_schema = json.loads(content)
        return populated_schema
    except json.JSONDecodeError:
        # 如果解析失败，尝试提取和修复JSON
        try:
            json_text = extract_json_from_text(content)
            populated_schema = json.loads(json_text)
            return populated_schema
        except:
            try:
                fixed_json = fix_json(json_text)
                populated_schema = json.loads(fixed_json)
                return populated_schema
            except:
                # 如果所有尝试都失败，使用递归方法手动填充
                print("JSON parsing failed, using manual value generation...")
                return manually_populate_placeholders(schema_with_placeholders, resume_type, diverse_traits)

def manually_populate_placeholders(schema: Dict[str, Any], resume_type: str, diverse_traits: Dict[str, str]) -> Dict[str, Any]:
    """手动填充schema中的占位符，用于JSON解析失败的情况"""
    if isinstance(schema, dict):
        return {k: manually_populate_placeholders(v, resume_type, diverse_traits) for k, v in schema.items()}
    elif isinstance(schema, list):
        # 根据列表长度和内容随机生成1-3个元素
        if not schema:
            return []
        sample = schema[0]
        count = random.randint(1, 3)
        return [manually_populate_placeholders(sample, resume_type, diverse_traits) for _ in range(count)]
    elif schema == "NUMBER_PLACEHOLDER":
        return random.randint(1, 9999)
    elif schema == "BOOLEAN_PLACEHOLDER":
        return random.choice([True, False])
    elif schema == "NULL_PLACEHOLDER":
        return None
    elif schema == "VALUE_PLACEHOLDER":
        # 根据字段名生成相应的值
        if "name" in str(schema).lower():
            first_names = ["王", "張", "李", "陳", "林"]
            last_names = ["小明", "小華", "大偉", "家豪", "美玲", "雅婷"]
            return f"{random.choice(first_names)}{random.choice(last_names)}"
        elif "date" in str(schema).lower() or "time" in str(schema).lower():
            year = random.randint(2010, 2023)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            return f"{year}-{month:02d}-{day:02d}"
        elif "description" in str(schema).lower():
            return f"專注於{diverse_traits['industry']}領域的{diverse_traits['career_stage']}，擅長{diverse_traits['work_style']}，參與過{diverse_traits['project_focus']}專案。"
        else:
            # 通用占位符
            generic_values = [
                "專業技能", "項目經驗", "工作職責", "教育背景", 
                "技術專長", "團隊合作", "問題解決", "創新思考"
            ]
            return random.choice(generic_values)
    else:
        return schema

def _generate_resume(client: OpenAI, resume_type: str, index: int) -> Dict[str, Any]:
    """生成單份具有多樣性的履歷"""
    # 隨機選擇一個樣本作為參考
    sample_schemas = load_sample_schemas(resume_type)
    sample_schema = random.choice(sample_schemas)
    
    # 生成多樣化特徵
    diverse_traits = generate_diverse_characteristics()
    
    # 1. 提取schema結構，將值替換為佔位符
    schema_structure = extract_schema_structure(sample_schema)
    
    # 2. 生成佔位符的實際值
    try:
        generated_resume = generate_values_for_schema(client, schema_structure, resume_type, diverse_traits)
        
        # 3. 添加元數據
        if isinstance(generated_resume, dict):
            if 'metadata' not in generated_resume:
                generated_resume['metadata'] = {}
            generated_resume['metadata'].update({
                'generated_date': datetime.now().isoformat(),
                'resume_type': resume_type,
                'index': index,
                'diversity_traits': diverse_traits
            })
        
        return generated_resume
    except Exception as e:
        print(f"Error generating resume values: {str(e)}")
        # 使用樣板直接替換值
        fallback_resume = sample_schema.copy()
        
        # 添加元數據
        if isinstance(fallback_resume, dict):
            if 'metadata' not in fallback_resume:
                fallback_resume['metadata'] = {}
            
            fallback_resume['metadata'].update({
                'generated_date': datetime.now().isoformat(),
                'resume_type': resume_type,
                'index': index,
                'diversity_traits': diverse_traits,
                'error': str(e),
                'recovery': 'fallback to sample schema with metadata'
            })
        
        print("Using fallback resume structure")
        return fallback_resume

def generate_multiple_resumes(client: OpenAI, resume_type: str, count: int = 30) -> None:
    """Generate multiple resumes for a specific type"""
    output_dir = Path("data/generated_resume")
    output_dir.mkdir(exist_ok=True)
    
    for i in range(1, count + 1):
        print(f"Generating {resume_type} resume {i}/{count}")
        
        try:
            # 使用重試機制生成履歷
            resume = generate_resume_with_retry(client, resume_type, i)
            
            if resume:
                output_path = output_dir / f"{resume_type}_generated_{i}.json"
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(resume, f, ensure_ascii=False, indent=2)
                print(f"Saved to {output_path}")
            else:
                print(f"Failed to generate {resume_type} resume {i} after retries")
        except Exception as e:
            print(f"All retry attempts failed for {resume_type} resume {i}: {str(e)}")
            
            # Add a small delay to avoid rate limiting
        time.sleep(2)

def main():
    # Get API key directly from .env file
    try:
        api_key = read_api_key_from_env_file()
        print(f"API key loaded successfully: {api_key[:5]}...{api_key[-5:]}")
    except Exception as e:
        raise ValueError(f"Error loading API key: {str(e)}")
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Generate resumes for each type
    for resume_type in ["mle", "pm"]:  #"ds"
        print(f"\nGenerating {resume_type.upper()} resumes...")
        generate_multiple_resumes(client, resume_type)

if __name__ == "__main__":
    main() 