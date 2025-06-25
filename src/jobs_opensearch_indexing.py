import boto3
import requests
import json
from requests_aws4auth import AWS4Auth
from config import CHUNK_SIZE, BEDROCK_MODEL_ID, JOBS_TABLE, JOBS_INDEX, OPENSEARCH_COLLECTION_ENDPOINT
from tqdm import tqdm
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize AWS session and credentials
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

# Initialize Bedrock client with runtime
bedrock_client = boto3.client('bedrock-runtime')

# Function to chunk text
def chunk_text(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Function to generate embeddings using Bedrock API
def generate_embedding(text_chunk):
    try:
        # Prepare the request body for Cohere embedding model
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
        # Extract embeddings from the response
        embeddings = result['embeddings'][0]
        return embeddings
        
    except Exception as e:
        logging.error(f"Error in generate_embedding: {e}")
        raise e

# Clear the OpenSearch index before writing new data
logging.info("Clearing OpenSearch jobs index...")
try:
    # First, check if index exists - fix URL format by removing https:// prefix
    index_url = f"{OPENSEARCH_COLLECTION_ENDPOINT}/{JOBS_INDEX}"
    index_check = requests.head(index_url, auth=awsauth)
    
    if index_check.status_code == 200:
        logging.info(f"Index {JOBS_INDEX} exists, proceeding to clear it...")
        
        # Try to delete the entire index and recreate it
        delete_index_url = f"{OPENSEARCH_COLLECTION_ENDPOINT}/{JOBS_INDEX}"
        delete_response = requests.delete(delete_index_url, auth=awsauth)
        
        if delete_response.status_code in [200, 201, 404]:
            logging.info("Successfully deleted OpenSearch jobs index")
            # Wait a moment for the deletion to complete
            time.sleep(3)
        else:
            logging.warning(f"Failed to delete index. Status: {delete_response.status_code}, Response: {delete_response.text}")
            # Continue anyway, we'll overwrite existing documents
    else:
        logging.info(f"Index {JOBS_INDEX} does not exist, will be created when first document is written")
        
except Exception as e:
    logging.warning(f"Error during index clearing: {e}")
    logging.info("Continuing with data processing...")

# Initialize a session using Amazon DynamoDB
dynamodb = session.resource('dynamodb')

# Select your DynamoDB table
jobs_table = dynamodb.Table(JOBS_TABLE)

# Scan the table to get all items
response = jobs_table.scan()
items = response['Items']

# Set up OpenSearch URL - fix URL format by removing https:// prefix
url = f"{OPENSEARCH_COLLECTION_ENDPOINT}/{JOBS_INDEX}/_doc"

# Helper function to extract text from different data types
def extract_text(field_value):
    if isinstance(field_value, list):
        return " ".join([str(item) for item in field_value])
    elif isinstance(field_value, str):
        return field_value
    else:
        return str(field_value) if field_value else ""

# Process each item with progress tracking
final_data = []
for item in tqdm(items, desc='Processing jobs'):
    job_id = item.get('job_id')
    
    # Extract descriptions from multiple fields and handle different data types
    required_skills = extract_text(item.get('required_skills', ''))
    requirements = extract_text(item.get('requirements', ''))
    responsibilities = extract_text(item.get('responsibilities', ''))
    
    # Concatenate all fields
    descriptions = " ".join([required_skills, requirements, responsibilities]).strip()
    
    if not descriptions:
        logging.warning(f"No descriptions found for job_id: {job_id}")
        continue
        
    logging.info(f"Extracted descriptions for job_id: {job_id}")
    
    # Chunk the descriptions
    chunks = chunk_text(descriptions, CHUNK_SIZE)
    logging.info(f"Processing job_id: {job_id}, number of chunks: {len(chunks)}")
    
    # Generate embeddings for each chunk
    for idx, chunk in enumerate(chunks):
        try:
            logging.debug(f"Generating embedding for chunk {idx}: {chunk}")
            embedding = generate_embedding(chunk)
            logging.debug(f"Generated embedding for chunk {idx}: {embedding}")
        except Exception as e:
            logging.error(f"Error generating embedding for chunk {idx}: {e}")
            continue
        
        # Create a new entry for each chunk
        chunk_data = {
            'chunk_id': f"{job_id}_{idx}",
            'job_id': job_id,
            'chunk': chunk,
            'embedding': embedding
        }
        final_data.append(chunk_data)
        
        # Write to OpenSearch
        try:
            res = requests.post(url, headers={"Content-Type": "application/json"}, auth=awsauth, data=json.dumps(chunk_data))
            if res.status_code == 201:
                logging.info(f"Successfully wrote job chunk {chunk_data['chunk_id']} to OpenSearch.")
            else:
                logging.error(f"Failed to write job chunk {chunk_data['chunk_id']} to OpenSearch. Status code: {res.status_code}, Response: {res.text}")
        except Exception as e:
            logging.error(f"Error writing job chunk {chunk_data['chunk_id']} to OpenSearch: {e}")

logging.info(f"Completed processing {len(items)} jobs with {len(final_data)} total chunks") 