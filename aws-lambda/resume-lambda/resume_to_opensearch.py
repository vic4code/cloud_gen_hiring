import boto3
import requests
import json
from requests_aws4auth import AWS4Auth
import logging
import time
import os
from boto3.dynamodb.types import TypeDeserializer

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configuration
CHUNK_SIZE = 256
BEDROCK_MODEL_ID = 'cohere.embed-multilingual-v3'
OPENSEARCH_COLLECTION_ENDPOINT = "c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com"
OPENSEARCH_INDEX = "haire-vector-db-resume-chunks-embeddings"

def get_aws_auth():
    try:
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
    except Exception as e:
        logger.error(f"Error getting AWS auth: {e}")
        raise e

def chunk_text(text, chunk_size):
    if not text:
        return []
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def generate_embedding(bedrock_client, text_chunk):
    try:
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
    except Exception as e:
        logger.error(f"Error in generate_embedding: {e}")
        raise e

def delete_chunks_for_resume(resume_id, awsauth):
    logger.info(f"[DELETE] Removing all chunks for resume_id={resume_id}")
    search_url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{OPENSEARCH_INDEX}/_search"
    search_query = {
        "query": {
            "term": {"resume_id.keyword": resume_id}
        },
        "size": 1000
    }
    try:
        res = requests.get(
            search_url,
            headers={"Content-Type": "application/json"},
            auth=awsauth,
            data=json.dumps(search_query),
            timeout=30
        )
        if res.status_code != 200:
            logger.warning(f"      └─ [OpenSearch] ❌ Failed to query docs for resume_id={resume_id}. Status={res.status_code}, Response={res.text}")
            return
        hits = res.json().get("hits", {}).get("hits", [])
        logger.info(f"      └─ [OpenSearch] Found {len(hits)} chunks to delete for resume_id={resume_id}")

        for hit in hits:
            doc_id = hit["_id"]
            del_url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{OPENSEARCH_INDEX}/_doc/{doc_id}"
            del_res = requests.delete(
                del_url,
                headers={"Content-Type": "application/json"},
                auth=awsauth,
                timeout=30
            )
            if del_res.status_code in [200, 202]:
                logger.info(f"         └─ [OpenSearch] ✅ Deleted _id={doc_id}")
            else:
                logger.warning(f"         └─ [OpenSearch] ❌ Failed to delete _id={doc_id}. Status={del_res.status_code}, Response={del_res.text}")

    except Exception as e:
        logger.error(f"      └─ [ERROR] Exception during deletion: {e}")


def process_resume_item(item, bedrock_client, awsauth):
    resume_id = item.get('resume_id')
    job_id = item.get('job_id')
    profile = item.get('profile', {})

    logger.info(f"[START] Processing resume_id={resume_id}, job_id={job_id}")

    professional_experiences = profile.get('professional_experiences', [])
    if not professional_experiences:
        logger.warning(f"[SKIP] No professional experiences for resume_id={resume_id}")
        return []

    descriptions = " ".join([exp.get('description', '') for exp in professional_experiences])
    logger.info(f"[INFO] Extracted total description length: {len(descriptions)} characters")

    chunks = chunk_text(descriptions, CHUNK_SIZE)
    logger.info(f"[INFO] Split into {len(chunks)} chunks")

    chunk_data_list = []
    for idx, chunk in enumerate(chunks):
        chunk_id = f"{resume_id}_{idx}"
        logger.info(f"  └─ [Chunk {idx+1}/{len(chunks)}] chunk_id={chunk_id}, len={len(chunk)}")
        try:
            embedding = generate_embedding(bedrock_client, chunk)
            logger.info(f"      └─ [Embedding] Success, dim={len(embedding)}")
            chunk_data = {
                'chunk_id': chunk_id,
                'resume_id': resume_id,
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

    logger.info(f"[DONE] Finished resume_id={resume_id}, total chunks={len(chunk_data_list)}\n")
    return chunk_data_list

def deserialize_dynamodb_item(dynamodb_item):
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in dynamodb_item.items()}

def lambda_handler(event, context):
    try:
        logger.info("=== Lambda triggered from DynamoDB Streams ===")
        bedrock_client = boto3.client('bedrock-runtime')
        awsauth = get_aws_auth()

        for record in event.get("Records", []):
            event_type = record.get("eventName")
            new_image = record.get("dynamodb", {}).get("NewImage")
            old_image = record.get("dynamodb", {}).get("OldImage")
            resume_key = record.get("dynamodb", {}).get("Keys", {}).get("resume_id", {}).get("S", "UNKNOWN")

            logger.info(f"[EVENT] Type={event_type}, Resume ID={resume_key}")

            if event_type == "INSERT":
                logger.info("[INSERT] NewImage: " + json.dumps(new_image, indent=2))
                item = deserialize_dynamodb_item(new_image)
                process_resume_item(item, bedrock_client, awsauth)

            elif event_type == "MODIFY":
                logger.info("[MODIFY] OldImage: " + json.dumps(old_image, indent=2))
                logger.info("[MODIFY] NewImage: " + json.dumps(new_image, indent=2))
                old_item = deserialize_dynamodb_item(old_image)
                delete_chunks_for_resume(old_item.get("resume_id"), awsauth)
                item = deserialize_dynamodb_item(new_image)
                process_resume_item(item, bedrock_client, awsauth)

            elif event_type == "REMOVE":
                logger.info("[REMOVE] OldImage: " + json.dumps(old_image, indent=2))
                old_item = deserialize_dynamodb_item(old_image)
                delete_chunks_for_resume(old_item.get("resume_id"), awsauth)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Stream events processed.'
            })
        }

    except Exception as e:
        logger.error(f"[FATAL] Lambda execution error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
