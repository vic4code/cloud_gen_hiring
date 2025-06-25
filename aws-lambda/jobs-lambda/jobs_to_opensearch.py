import boto3
import requests
import json
from requests_aws4auth import AWS4Auth
import logging
import time
import os

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configuration - inline for Lambda deployment
CHUNK_SIZE = 256
BEDROCK_MODEL_ID = 'cohere.embed-multilingual-v3'
JOBS_TABLE = 'haire-jobs'

# OpenSearch configuration
OPENSEARCH_COLLECTION_ENDPOINT = "c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com"
OPENSEARCH_INDEX = "haire-vector-db-jobs-chunks-embeddings"

def get_aws_auth():
    """Get AWS authentication for OpenSearch"""
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
    """Split text into chunks of specified size"""
    if not text:
        return []
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def generate_embedding(bedrock_client, text_chunk):
    """Generate embedding for text chunk using Bedrock"""
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

def extract_text(field_value):
    """Helper function to extract text from different data types"""
    if isinstance(field_value, list):
        return " ".join([str(item) for item in field_value])
    elif isinstance(field_value, str):
        return field_value
    else:
        return str(field_value) if field_value else ""

def clear_opensearch_index(awsauth):
    """Clear existing OpenSearch index"""
    logger.info("Clearing OpenSearch jobs index...")
    try:
        index_url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{OPENSEARCH_INDEX}"
        index_check = requests.head(index_url, auth=awsauth, timeout=30)
        
        if index_check.status_code == 200:
            logger.info(f"Index {OPENSEARCH_INDEX} exists, proceeding to clear it...")
            
            delete_index_url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{OPENSEARCH_INDEX}"
            delete_response = requests.delete(delete_index_url, auth=awsauth, timeout=30)
            
            if delete_response.status_code in [200, 201, 404]:
                logger.info("Successfully deleted OpenSearch jobs index")
                time.sleep(3)
            else:
                logger.warning(f"Failed to delete index. Status: {delete_response.status_code}, Response: {delete_response.text}")
        else:
            logger.info(f"Index {OPENSEARCH_INDEX} does not exist, will be created when first document is written")
            
    except Exception as e:
        logger.warning(f"Error during index clearing: {e}")
        logger.info("Continuing with data processing...")

def process_job_item(item, bedrock_client, awsauth):
    """Process a single job item and create embeddings"""
    job_id = item.get('job_id')
    
    # Extract descriptions from multiple fields and handle different data types
    required_skills = extract_text(item.get('required_skills', ''))
    requirements = extract_text(item.get('requirements', ''))
    responsibilities = extract_text(item.get('responsibilities', ''))
    
    # Concatenate all fields
    descriptions = " ".join([required_skills, requirements, responsibilities]).strip()
    
    if not descriptions:
        logger.warning(f"No descriptions found for job_id: {job_id}")
        return []
        
    logger.info(f"Extracted descriptions for job_id: {job_id}")
    
    chunks = chunk_text(descriptions, CHUNK_SIZE)
    logger.info(f"Processing job_id: {job_id}, number of chunks: {len(chunks)}")
    
    chunk_data_list = []
    for idx, chunk in enumerate(chunks):
        try:
            embedding = generate_embedding(bedrock_client, chunk)
            
            chunk_data = {
                'chunk_id': f"{job_id}_{idx}",
                'job_id': job_id,
                'chunk': chunk,
                'embedding': embedding
            }
            
            # Write to OpenSearch
            url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{OPENSEARCH_INDEX}/_doc"
            res = requests.post(
                url, 
                headers={"Content-Type": "application/json"}, 
                auth=awsauth, 
                data=json.dumps(chunk_data),
                timeout=30
            )
            
            if res.status_code == 201:
                logger.info(f"Successfully wrote job chunk {chunk_data['chunk_id']} to OpenSearch.")
                chunk_data_list.append(chunk_data)
            else:
                logger.error(f"Failed to write job chunk {chunk_data['chunk_id']} to OpenSearch. Status code: {res.status_code}")
                
        except Exception as e:
            logger.error(f"Error processing chunk {idx} for job {job_id}: {e}")
            continue
            
    return chunk_data_list

def lambda_handler(event, context):
    """Main Lambda handler function for jobs processing"""
    try:
        logger.info("Starting jobs processing Lambda function")
        
        # Initialize clients
        dynamodb = boto3.resource('dynamodb')
        bedrock_client = boto3.client('bedrock-runtime')
        awsauth = get_aws_auth()
        
        # Get items from DynamoDB
        jobs_table = dynamodb.Table(JOBS_TABLE)
        response = jobs_table.scan()
        items = response['Items']
        
        logger.info(f"Found {len(items)} items in DynamoDB table")
        
        # Clear existing index
        clear_opensearch_index(awsauth)
        
        # Process all items
        all_chunk_data = []
        processed_count = 0
        
        for item in items:
            try:
                chunk_data_list = process_job_item(item, bedrock_client, awsauth)
                all_chunk_data.extend(chunk_data_list)
                processed_count += 1
                
                # Log progress every 10 items
                if processed_count % 10 == 0:
                    logger.info(f"Processed {processed_count}/{len(items)} items")
                    
            except Exception as e:
                logger.error(f"Error processing item {item.get('job_id', 'unknown')}: {e}")
                continue
            
        logger.info(f"Successfully processed {processed_count} jobs and created {len(all_chunk_data)} chunks")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Successfully processed {processed_count} jobs and created {len(all_chunk_data)} chunks',
                'processed_items': processed_count,
                'total_chunks': len(all_chunk_data)
            })
        }
        
    except Exception as e:
        logger.error(f"Error in lambda execution: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
