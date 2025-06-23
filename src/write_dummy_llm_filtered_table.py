import boto3
import random
from tqdm import tqdm
from decimal import Decimal

# 設定 DynamoDB table 名稱
SOURCE_TABLE = 'embedding-filtered-resume'
TARGET_TABLE = 'llm-filtered-resume'

# 初始化 DynamoDB
session = boto3.Session()
dynamodb = session.resource('dynamodb')
source_table = dynamodb.Table(SOURCE_TABLE)
target_table = dynamodb.Table(TARGET_TABLE)

def table_exists(table_name):
    """
    檢查表格是否存在
    """
    try:
        dynamodb.Table(table_name).load()
        return True
    except:
        return False

def create_table_with_same_schema(source_table_name, target_table_name):
    """
    根據源表格創建相同結構的目標表格
    """
    print(f"Creating table {target_table_name} with same schema as {source_table_name}...")
    
    # 獲取源表格的描述
    source_response = dynamodb.meta.client.describe_table(TableName=source_table_name)
    source_table_info = source_response['Table']
    
    # 創建目標表格，使用相同的結構
    table = dynamodb.create_table(
        TableName=target_table_name,
        KeySchema=source_table_info['KeySchema'],
        AttributeDefinitions=source_table_info['AttributeDefinitions'],
        BillingMode='PAY_PER_REQUEST'
    )
    table.wait_until_exists()
    print(f"Table {target_table_name} created successfully")

def clear_table(table):
    """
    清空表格中的所有項目
    """
    print(f"Clearing table {table.name}...")
    scan_kwargs = {}
    done = False
    start_key = None
    deleted_count = 0
    
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        items = response.get('Items', [])
        
        if items:
            with table.batch_writer() as batch:
                for item in items:
                    # 構建刪除鍵
                    delete_key = {}
                    for key_attr in table.key_schema:
                        delete_key[key_attr['AttributeName']] = item[key_attr['AttributeName']]
                    batch.delete_item(Key=delete_key)
                    deleted_count += 1
        
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
    
    print(f"Deleted {deleted_count} items from {table.name}")

def scan_table(table):
    """
    掃描整個 DynamoDB 表格
    """
    items = []
    scan_kwargs = {}
    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        items.extend(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
    return items

def generate_llm_recommendation():
    """
    生成 LLM 推薦結果
    """
    llm_score = round(random.random(), 2)  # 0-1 之間的分數，保留2位小數
    
    # 根據分數生成不同的推薦理由
    if llm_score >= 0.9:
        reasons = [
            "經驗豐富且技能完全符合職缺要求，是理想的候選人。",
            "背景與職位高度匹配，具備所需的核心能力。",
            "專業技能突出，過往成就令人印象深刻。"
        ]
    elif llm_score >= 0.7:
        reasons = [
            "具備大部分所需技能，有潛力勝任此職位。",
            "經驗相關性良好，可以快速上手工作。",
            "技能組合符合職位要求，值得考慮。"
        ]
    elif llm_score >= 0.5:
        reasons = [
            "部分技能符合要求，需要一些培訓時間。",
            "背景有一定相關性，但需要更多學習。",
            "具備基礎能力，可以考慮作為備選。"
        ]
    else:
        reasons = [
            "技能與職位要求相關性較低，不建議優先考慮。",
            "經驗與此職缺匹配度不高，可能需要更多培訓。",
            "背景與職位需求差異較大，建議尋找更合適的候選人。"
        ]
    
    reason = random.choice(reasons)
    
    return {
        "llm_score": Decimal(str(llm_score)),
        "reason": reason
    }

def main():
    # 檢查目標表格是否存在
    if not table_exists(TARGET_TABLE):
        # 如果表格不存在，創建一個與源表格相同結構的表格
        create_table_with_same_schema(SOURCE_TABLE, TARGET_TABLE)
    else:
        # 如果表格存在，清空它
        clear_table(target_table)
    
    # 讀取源表格資料
    print(f"Reading data from {SOURCE_TABLE}...")
    items = scan_table(source_table)
    
    print(f"Processing {len(items)} items...")
    # 為每個項目添加 LLM 推薦結果
    for item in items:
        item['llm_recommendation_results'] = generate_llm_recommendation()
    
    # 批次寫入目標表格
    print(f"Writing data to {TARGET_TABLE}...")
    with target_table.batch_writer() as batch:
        for item in tqdm(items, desc='Uploading to DynamoDB'):
            batch.put_item(Item=item)
            
    print(f"Successfully uploaded {len(items)} items to {TARGET_TABLE}")

if __name__ == '__main__':
    main()
