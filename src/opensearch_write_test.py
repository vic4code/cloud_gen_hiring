import boto3
import requests
import json
from requests_aws4auth import AWS4Auth

# 你的 endpoint 建議不要加 https://
OPENSEARCH_COLLECTION_ENDPOINT = "c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com"
OPENSEARCH_INDEX = "haire-vector-db-resume-chunks-embeddings"

session = boto3.Session()
credentials = session.get_credentials().get_frozen_credentials()
region = session.region_name or "ap-southeast-1"

awsauth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key,
    region,
    'aoss',
    session_token=credentials.token
)

url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{OPENSEARCH_INDEX}/_doc"
print("🧪 正在寫入 URL:", url)

doc = {
    "name": "Victor Test",
    "embedding": [0.1] * 1024,
    "note": "這是一筆測試資料"
}

res = requests.post(url, headers={"Content-Type": "application/json"}, auth=awsauth, data=json.dumps(doc))
print(res.status_code)
print(res.text)
