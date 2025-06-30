import requests
from requests_aws4auth import AWS4Auth
import boto3
import json

OPENSEARCH_HOST = "https://c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com"
INDEX = "haire-vector-db-jobs-chunks-embeddings"  # 你用得出 GET 就用這個

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

# Step 1: 搜尋你要刪除的所有 job_id
search_url = f"{OPENSEARCH_HOST}/{INDEX}/_search"
search_query = {
    "query": {
        "term": {"job_id.keyword": "TESTTEST"}
    },
    "size": 1000  # 一次最多拿1000筆，夠用
}

search_res = requests.get(
    search_url,
    auth=awsauth,
    headers={"Content-Type": "application/json"},
    data=json.dumps(search_query)
)

print("Search status code:", search_res.status_code)
search_data = search_res.json()
print("Find documents:", len(search_data.get("hits", {}).get("hits", [])))

# Step 2: 逐筆用 _id 刪除
for hit in search_data.get("hits", {}).get("hits", []):
    doc_id = hit["_id"]
    del_url = f"{OPENSEARCH_HOST}/{INDEX}/_doc/{doc_id}"
    del_res = requests.delete(
        del_url,
        auth=awsauth,
        headers={"Content-Type": "application/json"}
    )
    print(f"Deleted _id: {doc_id}, status: {del_res.status_code}")

print("Done.")
