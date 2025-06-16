import boto3
import pandas as pd
import ast
import os
from tqdm import tqdm

# 設定 DynamoDB table 名稱
TABLE_NAME = 'embedding-filtered-resume'
CSV_PATH = os.path.join(os.path.dirname(__file__), '../data/dynamodb/resumes_with_matched_job_ids.csv')

# 初始化 DynamoDB
session = boto3.Session()
dynamodb = session.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def parse_value(val):
    """
    將字串型態的 list/dict 轉回原生型態，否則保持原樣。
    """
    if pd.isna(val):
        return None
    if isinstance(val, str):
        val = val.strip()
        # 嘗試解析 list/dict 字串
        if (val.startswith('[') and val.endswith(']')) or (val.startswith('{') and val.endswith('}')):
            try:
                return ast.literal_eval(val)
            except Exception:
                return val
    return val

def main():
    # 讀取 CSV
    df = pd.read_csv(CSV_PATH)
    # 轉換欄位型態
    items = df.to_dict(orient='records')
    for item in items:
        for k, v in item.items():
            item[k] = parse_value(v)

    # 批次寫入 DynamoDB
    with table.batch_writer(overwrite_by_pkeys=['resume_id']) as batch:
        for item in tqdm(items, desc='Uploading to DynamoDB'):
            # 移除 NaN/None 欄位
            clean_item = {k: v for k, v in item.items() if v is not None and v == v}
            batch.put_item(Item=clean_item)
    print(f"Uploaded {len(items)} items to DynamoDB table '{TABLE_NAME}'")

if __name__ == '__main__':
    main()
