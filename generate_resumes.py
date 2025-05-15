import json
import os
import openai
from typing import Dict, List, Any
import random

# 設置 OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_schema(file_path: str) -> Dict:
    """載入履歷 schema"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_resume(resume_type: str, schema: Dict) -> Dict:
    """使用 OpenAI API 生成履歷資料"""
    prompt = f"""請根據以下 schema 生成一份{resume_type}履歷資料。要求：
1. 資料要真實合理
2. 保持與原始 schema 結構一致
3. 生成中文履歷內容
4. 不要包含任何個人隱私資訊

Schema:
{json.dumps(schema, ensure_ascii=False, indent=2)}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "你是一個專業的履歷生成助手，擅長生成真實合理的履歷資料。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    try:
        return json.loads(response.choices[0].message.content)
    except:
        print(f"Error parsing response for {resume_type}")
        return None

def main():
    # 載入三種履歷的 schema
    ds_schema = load_schema("data/resume/ds_sample1.json")
    mle_schema = load_schema("data/resume/mle_sample1.json")
    pm_schema = load_schema("data/resume/pm_sample1.json")
    
    # 創建輸出目錄
    output_dir = "data/generated_resumes"
    os.makedirs(output_dir, exist_ok=True)
    
    # 為每種履歷類型生成 30 份資料
    for resume_type, schema in [
        ("ds", ds_schema),
        ("mle", mle_schema),
        ("pm", pm_schema)
    ]:
        for i in range(30):
            resume = generate_resume(resume_type, schema)
            if resume:
                output_file = os.path.join(output_dir, f"{resume_type}_generated_{i+1}.json")
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(resume, f, ensure_ascii=False, indent=2)
                print(f"Generated {resume_type} resume {i+1}/30")

if __name__ == "__main__":
    main() 