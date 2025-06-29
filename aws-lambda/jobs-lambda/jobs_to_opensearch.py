import boto3
import requests
import json
from requests_aws4auth import AWS4Auth
import logging
from boto3.dynamodb.types import TypeDeserializer

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configuration
CHUNK_SIZE = 256
BEDROCK_MODEL_ID = 'cohere.embed-multilingual-v3'
OPENSEARCH_COLLECTION_ENDPOINT = "c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com"
OPENSEARCH_INDEX = "haire-vector-db-jobs-chunks-embeddings"

# Auth for OpenSearch
def get_aws_auth():
    session = boto3.Session()
    credentials = session.get_credentials().get_frozen_credentials()
    region = session.region_name or "ap-southeast-1"
    return AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        region,
        'aoss',
        session_token=credentials.token
    )

# Helper: break text into fixed-size chunks
def chunk_text(text, chunk_size):
    if not text:
        return []
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Helper: join list or str safely
def safe_join_fields(fields):
    result = []
    for f in fields:
        if isinstance(f, list):
            result.extend([str(x) for x in f])
        elif isinstance(f, str):
            result.append(f)
        else:
            result.append(str(f))
    return " ".join(result).strip()

# Bedrock embedding generation
def generate_embedding(bedrock_client, text_chunk):
    request_body = {
        "texts": [text_chunk],
        "input_type": "search_document"
    }
    response = bedrock_client.invoke_model(
        modelId=BEDROCK_MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(request_body)
    )
    result = json.loads(response['body'].read())
    return result['embeddings'][0]

# Delete existing chunks in OpenSearch for job_id
def delete_chunks_for_job(job_id, awsauth):
    logger.info(f"[DELETE] Removing all chunks for job_id={job_id}")
    query = {
        "query": {
            "term": {"job_id": job_id}
        }
    }
    url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{OPENSEARCH_INDEX}/_delete_by_query"
    res = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        auth=awsauth,
        data=json.dumps(query),
        timeout=30
    )
    if res.status_code == 200:
        logger.info(f"      └─ [OpenSearch] ✅ Deleted existing chunks for job_id={job_id}")
    else:
        logger.warning(f"      └─ [OpenSearch] ❌ Failed to delete. Status={res.status_code}, Response={res.text}")

# Process one DynamoDB item
def process_job_item(item, bedrock_client, awsauth):
    job_id = item.get('job_id')
    logger.info(f"[START] Processing job_id={job_id}")

    # Extract and flatten text
    required_skills = item.get('required_skills', '')
    requirements = item.get('requirements', '')
    responsibilities = item.get('responsibilities', '')
    descriptions = safe_join_fields([required_skills, requirements, responsibilities])
    logger.info(f"[INFO] Extracted total description length: {len(descriptions)} characters")

    if not descriptions:
        logger.warning(f"[SKIP] No descriptions found for job_id={job_id}")
        return []

    chunks = chunk_text(descriptions, CHUNK_SIZE)
    logger.info(f"[INFO] Split into {len(chunks)} chunks")

    chunk_data_list = []
    for idx, chunk in enumerate(chunks):
        chunk_id = f"{job_id}_{idx}"
        try:
            embedding = generate_embedding(bedrock_client, chunk)
            chunk_data = {
                'chunk_id': chunk_id,
                'job_id': job_id,
                'chunk': chunk,
                'embedding': embedding
            }
            url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{OPENSEARCH_INDEX}/_doc"
            res = requests.post(
                url,
                headers={"Content-Type": "application/json"},
                auth=awsauth,
                data=json.dumps(chunk_data),
                timeout=30
            )
            if res.status_code == 201:
                logger.info(f"      └─ [OpenSearch] ✅ Chunk {chunk_id} written successfully")
                chunk_data_list.append(chunk_data)
            else:
                logger.error(f"      └─ [OpenSearch] ❌ Failed to write chunk {chunk_id}. Status={res.status_code}, Response={res.text}")
        except Exception as e:
            logger.error(f"      └─ [ERROR] Failed to process chunk {chunk_id}: {e}")
            continue

    logger.info(f"[DONE] Finished job_id={job_id}, total chunks={len(chunk_data_list)}\n")
    return chunk_data_list

# Deserialize DynamoDB stream item
def deserialize_dynamodb_item(dynamodb_item):
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in dynamodb_item.items()}

# Lambda entry point
def lambda_handler(event, context):
    try:
        logger.info("=== Lambda triggered from DynamoDB Streams ===")
        bedrock_client = boto3.client('bedrock-runtime')
        awsauth = get_aws_auth()

        for record in event.get("Records", []):
            event_type = record.get("eventName")
            new_image = record.get("dynamodb", {}).get("NewImage")
            old_image = record.get("dynamodb", {}).get("OldImage")
            job_key = record.get("dynamodb", {}).get("Keys", {}).get("job_id", {}).get("S", "UNKNOWN")
            logger.info(f"[EVENT] Type={event_type}, Job ID={job_key}")

            if event_type == "INSERT":
                item = deserialize_dynamodb_item(new_image)
                process_job_item(item, bedrock_client, awsauth)

            elif event_type == "MODIFY":
                old_item = deserialize_dynamodb_item(old_image)
                delete_chunks_for_job(old_item.get("job_id"), awsauth)
                item = deserialize_dynamodb_item(new_image)
                process_job_item(item, bedrock_client, awsauth)

            elif event_type == "REMOVE":
                old_item = deserialize_dynamodb_item(old_image)
                delete_chunks_for_job(old_item.get("job_id"), awsauth)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Stream events processed.'})
        }

    except Exception as e:
        logger.error(f"[FATAL] Lambda execution error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
