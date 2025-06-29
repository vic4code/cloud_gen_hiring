import boto3
import json
import logging
import numpy as np
from tqdm import tqdm
from decimal import Decimal
import requests
from requests_aws4auth import AWS4Auth
from collections import defaultdict

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize AWS session
session = boto3.Session()
dynamodb = session.resource('dynamodb')

# OpenSearch configuration
OPENSEARCH_COLLECTION_ENDPOINT = "c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com"
RESUME_INDEX = 'haire-vector-db-resume-chunks-embeddings'
JOBS_INDEX = 'haire-vector-db-jobs-chunks-embeddings'

# DynamoDB table names
SOURCE_TABLE = 'benson-haire-parsed_resume'
TARGET_TABLE = 'embedding-filtered-resume-test'
SIMILARITY_TABLE = 'resume-jobs-similarity'

# Initialize OpenSearch auth
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

awsauth = get_aws_auth()

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product / (norm1 * norm2)

def get_all_documents_from_index(index_name):
    """Get all documents from OpenSearch index"""
    url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{index_name}/_search"
    query = {
        "size": 10000,  # Adjust based on your data size
        "query": {"match_all": {}}
    }
    
    try:
        response = requests.post(url, headers={"Content-Type": "application/json"}, auth=awsauth, data=json.dumps(query))
        if response.status_code == 200:
            data = response.json()
            return data['hits']['hits']
        else:
            logging.error(f"Failed to get documents from {index_name}: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        logging.error(f"Error getting documents from {index_name}: {e}")
        return []

def create_table_if_not_exists(table_name, key_schema=None):
    """Create DynamoDB table if it doesn't exist"""
    try:
        table = dynamodb.Table(table_name)
        table.load()
        logging.info(f"Table {table_name} already exists")
        return True
    except Exception:
        try:
            if key_schema is None:
                key_schema = [
                    {
                        'AttributeName': 'resume_id',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'job_id',
                        'KeyType': 'RANGE'
                    }
                ]
            # 根據 key_schema 動態產生 attribute definitions
            attribute_definitions = []
            for key in key_schema:
                attribute_definitions.append({
                    'AttributeName': key['AttributeName'],
                    'AttributeType': 'S'  # 預設都用 String
                })
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=key_schema,
                AttributeDefinitions=attribute_definitions,
                BillingMode='PAY_PER_REQUEST'
            )
            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
            logging.info(f"Created table {table_name}")
            return True
        except Exception as e:
            logging.error(f"Error creating table {table_name}: {e}")
            return False

def write_similarity_results(similarity_results):
    """Write similarity results to DynamoDB"""
    table = dynamodb.Table(SIMILARITY_TABLE)
    
    for result in tqdm(similarity_results, desc='Writing similarity results'):
        try:
            item = {
                'resume_id': result['resume_id'],
                'job_id': result['job_id'],
                'embedding_similarity_score': Decimal(str(result['embedding_similarity_score']))
            }
            table.put_item(Item=item)
        except Exception as e:
            logging.error(f"Error writing similarity result: {e}")

def scan_dynamodb_table(table_name):
    """Scan all items from DynamoDB table"""
    table = dynamodb.Table(table_name)
    items = []
    
    try:
        response = table.scan()
        items.extend(response['Items'])
        
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])
        
        logging.info(f"Scanned {len(items)} items from {table_name}")
        return items
    except Exception as e:
        logging.error(f"Error scanning table {table_name}: {e}")
        return []

def write_items_to_table(table_name, items):
    """Write items to DynamoDB table using batch operations"""
    table = dynamodb.Table(table_name)
    batch_size = 25
    total_items = len(items)
    
    for i in tqdm(range(0, total_items, batch_size), desc=f'Writing to {table_name}'):
        batch = items[i:i + batch_size]
        
        try:
            with table.batch_writer() as batch_writer:
                for item in batch:
                    batch_writer.put_item(Item=item)
        except Exception as e:
            logging.error(f"Error writing batch {i//batch_size + 1}: {e}")

def calculate_chunk_similarities():
    """Calculate similarities between resume and job chunks, with debug logging for missing data"""
    logging.info("Loading documents from OpenSearch indices...")
    
    # Get all documents from both indices
    resume_docs = get_all_documents_from_index(RESUME_INDEX)
    jobs_docs = get_all_documents_from_index(JOBS_INDEX)
    
    if not resume_docs or not jobs_docs:
        logging.error("No documents found in OpenSearch indices")
        return []
    
    logging.info(f"Loaded {len(resume_docs)} resume chunks and {len(jobs_docs)} job chunks")
    
    # Group documents by resume_id and job_id
    resume_chunks_by_id = defaultdict(list)
    job_chunks_by_id = defaultdict(list)
    
    missing_resume_jobid = set()
    missing_resume_embedding = set()
    missing_job_embedding = set()
    resume_jobid_match_count = defaultdict(int)
    
    for doc in resume_docs:
        source = doc['_source']
        resume_id = source.get('resume_id')
        job_id = source.get('job_id')
        if not job_id:
            missing_resume_jobid.add(source.get('resume_id', 'UNKNOWN'))
        if not source.get('embedding'):
            missing_resume_embedding.add((resume_id, job_id))
        if resume_id and job_id:
            resume_chunks_by_id[resume_id].append(source)
    
    for doc in jobs_docs:
        source = doc['_source']
        job_id = source.get('job_id')
        if not source.get('embedding'):
            missing_job_embedding.add(job_id)
        if job_id:
            job_chunks_by_id[job_id].append(source)
    
    logging.info(f"Grouped into {len(resume_chunks_by_id)} resume groups and {len(job_chunks_by_id)} job groups")
    if missing_resume_jobid:
        logging.debug(f"Resume chunks missing job_id: {missing_resume_jobid}")
    if missing_resume_embedding:
        logging.debug(f"Resume chunks missing embedding: {missing_resume_embedding}")
    if missing_job_embedding:
        logging.debug(f"Job chunks missing embedding: {missing_job_embedding}")
    
    # Calculate similarities
    similarity_results = []
    resume_jobid_matched = defaultdict(list)
    
    for resume_id in tqdm(resume_chunks_by_id.keys(), desc='Calculating similarities'):
        resume_chunks = resume_chunks_by_id[resume_id]
        
        # Get unique job_ids from resume chunks
        job_ids = set()
        for chunk in resume_chunks:
            job_id = chunk.get('job_id')
            if job_id:
                job_ids.add(job_id)
        
        for job_id in job_ids:
            job_chunks = job_chunks_by_id.get(job_id, [])
            
            if not job_chunks:
                logging.debug(f"No job chunks found for job_id={job_id} (resume_id={resume_id})")
                continue
            
            max_scores_per_pair = []
            
            # For each resume chunk, find the best matching job chunk
            for resume_chunk in resume_chunks:
                if resume_chunk.get('job_id') != job_id:
                    continue
                
                max_score = 0.0
                resume_embedding = resume_chunk.get('embedding')
                
                if not resume_embedding:
                    continue
                
                # Compare with all job chunks for this job_id
                for job_chunk in job_chunks:
                    job_embedding = job_chunk.get('embedding')
                    if not job_embedding:
                        continue
                    score = cosine_similarity(resume_embedding, job_embedding)
                    max_score = max(max_score, score)
                
                max_scores_per_pair.append(max_score)
            
            # Calculate mean of max scores
            if max_scores_per_pair:
                mean_score = sum(max_scores_per_pair) / len(max_scores_per_pair)
                similarity_results.append({
                    'resume_id': resume_id,
                    'job_id': job_id,
                    'embedding_similarity_score': mean_score
                })
                resume_jobid_matched[resume_id].append(job_id)
            else:
                logging.debug(f"No valid chunk match for resume_id={resume_id}, job_id={job_id}")
    
    # Log summary of match results
    for resume_id in resume_chunks_by_id.keys():
        matched = resume_jobid_matched.get(resume_id, [])
        logging.info(f"resume_id={resume_id} matched job_ids: {matched if matched else 'None'}")
    
    logging.info(f"Calculated {len(similarity_results)} similarity scores")
    return similarity_results

def main():
    logging.info("Starting OpenSearch-based resume-job matching...")
    
    # Create similarity table
    if not create_table_if_not_exists(SIMILARITY_TABLE):
        logging.error(f"Failed to create similarity table {SIMILARITY_TABLE}")
        return
    
    # Calculate similarities
    similarity_results = calculate_chunk_similarities()
    if not similarity_results:
        logging.error("No similarity results calculated")
        return
    
    # Write similarity results to DynamoDB
    write_similarity_results(similarity_results)
    
    # Create target table
    if not create_table_if_not_exists(TARGET_TABLE, [
        {'AttributeName': 'resume_id', 'KeyType': 'HASH'}
    ]):
        logging.error(f"Failed to create target table {TARGET_TABLE}")
        return
    
    # Load source data
    source_items = scan_dynamodb_table(SOURCE_TABLE)
    if not source_items:
        logging.error(f"No items found in source table {SOURCE_TABLE}")
        return
    
    # Create similarity mapping
    similarity_map = {}
    for result in similarity_results:
        key = (result['resume_id'], result['job_id'])
        similarity_map[key] = result['embedding_similarity_score']
    
    # Process items and add similarity scores
    processed_items = []
    
    for item in tqdm(source_items, desc='Processing items'):
        new_item = item.copy()
        resume_id = item.get('resume_id')
        job_id = item.get('job_id')
        
        if resume_id and job_id:
            similarity_score = similarity_map.get((resume_id, job_id), 0.0)
            new_item['embedding_similarity_score'] = Decimal(str(similarity_score))
        else:
            new_item['embedding_similarity_score'] = Decimal('0.0')
        
        processed_items.append(new_item)
    
    logging.info(f"Processed {len(processed_items)} items with similarity scores")
    
    # Write to target table
    write_items_to_table(TARGET_TABLE, processed_items)
    
    logging.info(f"Successfully created table {TARGET_TABLE} with {len(processed_items)} items")
    
    # Print summary statistics
    scores = [float(item['embedding_similarity_score']) for item in processed_items]
    if scores:
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        logging.info(f"Similarity score statistics:")
        logging.info(f"  Average: {avg_score:.4f}")
        logging.info(f"  Maximum: {max_score:.4f}")
        logging.info(f"  Minimum: {min_score:.4f}")

if __name__ == "__main__":
    main() 