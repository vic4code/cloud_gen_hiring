import boto3
import json
import os
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import uuid

# --- Configuration ---
# Replace with your AWS region, OpenSearch host, and DynamoDB table names
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
OPENSEARCH_HOST = os.environ.get("OPENSEARCH_HOST", "") # e.g., 'search-your-domain.us-east-1.es.amazonaws.com'
BEDROCK_MODEL_ID = "cohere.embed-multilingual-v3"

DYNAMODB_TABLES_CONFIG = {
    "haire-jobs": {
        "opensearch_index": "haire-jobs-index",
        "fields_to_concatenate": ["job_title", "job_description", "company_name", "location"] # Replace with actual fields
    },
    "benson-haire-parsed_resume": {
        "opensearch_index": "benson-haire-parsed-resume-index",
        "fields_to_concatenate": ["candidate_name", "skills", "experience", "education"] # Replace with actual fields
    }
}

# --- Boto3 and OpenSearch Clients ---
boto3_session = boto3.Session(region_name=AWS_REGION)
dynamodb = boto3_session.resource('dynamodb')
bedrock_runtime = boto3_session.client('bedrock-runtime', region_name=AWS_REGION)

# It's recommended to use IAM roles for authentication with OpenSearch
# when running in a Lambda function.
service = 'es'
credentials = boto3_session.get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, AWS_REGION, service, session_token=credentials.token)

opensearch_client = OpenSearch(
    hosts=[{'host': OPENSEARCH_HOST, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# --- Helper Functions ---

def scan_dynamodb_table(table_name):
    """Scans and returns all items from a DynamoDB table."""
    print(f"Scanning DynamoDB table: {table_name}")
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response.get('Items', [])
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response.get('Items', []))
    print(f"Found {len(items)} items in {table_name}.")
    return items

def get_text_chunks(text, chunk_size=500, overlap=50):
    """Splits text into overlapping chunks."""
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def get_embedding(text_chunks, model_id):
    """Generates embeddings for a list of text chunks using Bedrock."""
    embeddings = []
    for chunk in text_chunks:
        body = json.dumps({
            "texts": [chunk],
            "input_type": "search_document"
        })
        response = bedrock_runtime.invoke_model(
            body=body,
            modelId=model_id,
            accept="*/*",
            contentType="application/json"
        )
        response_body = json.loads(response.get("body").read())
        embedding = response_body.get("embeddings")[0]
        embeddings.append(embedding)
    return embeddings

def index_to_opensearch(index_name, original_item, text_chunks, embeddings):
    """Indexes document chunks and their embeddings into OpenSearch."""
    print(f"Indexing {len(text_chunks)} chunks to OpenSearch index: {index_name}")
    for i, chunk in enumerate(text_chunks):
        document = {
            "vector_field": embeddings[i],
            "text_field": chunk,
            "metadata": {key: str(value) for key, value in original_item.items()} # Store original item data as metadata
        }
        # Use a unique ID for each chunk, e.g., combining original item ID and chunk index
        # This assumes your DynamoDB items have a unique 'id' field.
        # If not, generate a new UUID or use a combination of primary keys.
        item_id = original_item.get('id', str(uuid.uuid4()))
        document_id = f"{item_id}_{i}"
        
        try:
            opensearch_client.index(
                index=index_name,
                body=document,
                id=document_id,
                refresh='wait_for'
            )
        except Exception as e:
            print(f"Error indexing document {document_id}: {e}")

# --- Main Lambda Handler ---

def lambda_handler(event, context):
    """
    Lambda handler to read from DynamoDB, generate embeddings, and index to OpenSearch.
    """
    if not OPENSEARCH_HOST:
        raise ValueError("OPENSEARCH_HOST environment variable is not set.")

    for table_name, config in DYNAMODB_TABLES_CONFIG.items():
        opensearch_index = config["opensearch_index"]
        fields_to_concat = config["fields_to_concatenate"]
        
        # Create OpenSearch index if it doesn't exist
        if not opensearch_client.indices.exists(index=opensearch_index):
            # Customize the mapping based on your needs, e.g., number of dimensions for the vector
            # Cohere multilingual v3 has 1024 dimensions
            index_body = {
                "settings": {
                    "index": {
                        "knn": True
                    }
                },
                "mappings": {
                    "properties": {
                        "vector_field": {
                            "type": "knn_vector",
                            "dimension": 1024
                        },
                        "text_field": {
                            "type": "text"
                        },
                        "metadata": {
                            "type": "object"
                        }
                    }
                }
            }
            print(f"Creating OpenSearch index: {opensearch_index}")
            opensearch_client.indices.create(opensearch_index, body=index_body)

        items = scan_dynamodb_table(table_name)
        
        for item in items:
            # Concatenate specified fields
            concatenated_text = " ".join([str(item.get(field, '')) for field in fields_to_concat])
            
            if not concatenated_text.strip():
                print(f"Skipping item with empty concatenated text: {item}")
                continue

            # Split text into chunks
            chunks = get_text_chunks(concatenated_text)
            
            if not chunks:
                continue

            # Generate embeddings
            embeddings = get_embedding(chunks, BEDROCK_MODEL_ID)
            
            # Index to OpenSearch
            index_to_opensearch(opensearch_index, item, chunks, embeddings)

    return {
        'statusCode': 200,
        'body': json.dumps('Vector indexing process completed successfully!')
    }

# Example of running the handler locally (for testing purposes)
if __name__ == '__main__':
    # Mock event and context
    mock_event = {}
    mock_context = {}
    
    # You would need to set up local credentials (e.g., via AWS CLI)
    # and provide the OPENSEARCH_HOST environment variable for this to work.
    # For example:
    # export AWS_REGION="us-east-1"
    # export OPENSEARCH_HOST="your-opensearch-host.es.amazonaws.com"
    # python vector_indexing.py
    
    print("Running vector indexing locally...")
    # lambda_handler(mock_event, mock_context) # Uncomment to run
    print("Local run finished. Note: This is a dry run without actual execution.")
    print("Please deploy as a Lambda and configure environment variables.")
