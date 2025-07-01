import boto3
import json
import logging
import numpy as np
from requests_aws4auth import AWS4Auth
from collections import defaultdict
from decimal import Decimal  # <--- 新增
import requests

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS session
session = boto3.Session()
dynamodb = session.resource('dynamodb')

# OpenSearch configuration
OPENSEARCH_COLLECTION_ENDPOINT = "c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com"
RESUME_INDEX = 'haire-vector-db-resume-chunks-embeddings'
JOBS_INDEX = 'haire-vector-db-jobs-chunks-embeddings'

# DynamoDB table names
SOURCE_TABLE = 'benson-haire-parsed_resume'
TARGET_TABLE = 'embedding-filtered-resume'
SIMILARITY_TABLE = 'resume-jobs-similarity'

def get_aws_auth():
    """Get AWS authentication for OpenSearch"""
    credentials = session.get_credentials().get_frozen_credentials()
    region = session.region_name or "ap-southeast-1"
    return AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        region,
        'aoss',
        session_token=credentials.token
    )

def get_all_documents_from_index(index_name):
    """Get all documents from OpenSearch index"""
    awsauth = get_aws_auth()
    url = f"https://{OPENSEARCH_COLLECTION_ENDPOINT}/{index_name}/_search"
    
    query = {
        "size": 10000,  # Adjust based on your data size
        "query": {
            "match_all": {}
        }
    }
    
    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            auth=awsauth,
            data=json.dumps(query),
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            documents = []
            for hit in result.get('hits', {}).get('hits', []):
                doc = hit['_source']
                documents.append(doc)
            logger.info(f"Retrieved {len(documents)} documents from {index_name}")
            return documents
        else:
            logger.error(f"Failed to retrieve documents from {index_name}: {response.status_code}")
            return []
            
    except Exception as e:
        logger.error(f"Error retrieving documents from {index_name}: {e}")
        return []

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    try:
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
            
        return dot_product / (norm1 * norm2)
    except Exception as e:
        logger.error(f"Error calculating cosine similarity: {e}")
        return 0.0

def create_table_if_not_exists(table_name, key_schema=None):
    """Create DynamoDB table if it doesn't exist"""
    try:
        table = dynamodb.Table(table_name)
        table.load()
        logger.info(f"Table {table_name} already exists")
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
                    'AttributeType': 'S'
                })
            
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=key_schema,
                AttributeDefinitions=attribute_definitions,
                BillingMode='PAY_PER_REQUEST'
            )
            table.wait_until_exists()
            logger.info(f"Created table {table_name}")
            return True
        except Exception as e:
            logger.error(f"Error creating table {table_name}: {e}")
            return False

def calculate_chunk_similarities():
    """Calculate similarities between resume and job chunks, with debug logging for missing data"""
    logger.info("Loading documents from OpenSearch indices...")
    
    # Get all documents from both indices
    resume_docs = get_all_documents_from_index(RESUME_INDEX)
    jobs_docs = get_all_documents_from_index(JOBS_INDEX)
    
    if not resume_docs or not jobs_docs:
        logger.error("No documents found in OpenSearch indices")
        return []
    
    logger.info(f"Loaded {len(resume_docs)} resume chunks and {len(jobs_docs)} job chunks")
    
    # Group documents by resume_id and job_id
    resume_chunks_by_id = defaultdict(list)
    job_chunks_by_id = defaultdict(list)
    
    missing_resume_jobid = set()
    missing_resume_embedding = set()
    missing_job_embedding = set()
    
    # Process resume chunks
    for doc in resume_docs:
        resume_id = doc.get('resume_id')
        job_id = doc.get('job_id')
        embedding = doc.get('embedding')
        
        if not resume_id:
            logger.debug(f"Resume chunk missing resume_id: {doc}")
            continue
            
        if not job_id:
            missing_resume_jobid.add(resume_id)
            logger.debug(f"Resume chunk missing job_id for resume_id={resume_id}")
            continue
            
        if not embedding:
            missing_resume_embedding.add(resume_id)
            logger.debug(f"Resume chunk missing embedding for resume_id={resume_id}")
            continue
            
        resume_chunks_by_id[resume_id].append(doc)
    
    # Process job chunks
    for doc in jobs_docs:
        job_id = doc.get('job_id')
        embedding = doc.get('embedding')
        
        if not job_id:
            logger.debug(f"Job chunk missing job_id: {doc}")
            continue
            
        if not embedding:
            missing_job_embedding.add(job_id)
            logger.debug(f"Job chunk missing embedding for job_id={job_id}")
            continue
            
        job_chunks_by_id[job_id].append(doc)
    
    # Log missing data statistics
    logger.info(f"Resume chunks missing job_id: {len(missing_resume_jobid)}")
    logger.info(f"Resume chunks missing embedding: {len(missing_resume_embedding)}")
    logger.info(f"Job chunks missing embedding: {len(missing_job_embedding)}")
    
    # Calculate similarities
    similarities = []
    processed_resume_ids = set()
    
    for resume_id, resume_chunks in resume_chunks_by_id.items():
        logger.debug(f"Processing resume_id={resume_id} with {len(resume_chunks)} chunks")
        
        # Group resume chunks by job_id
        resume_chunks_by_job = defaultdict(list)
        for chunk in resume_chunks:
            job_id = chunk.get('job_id')
            if job_id:
                resume_chunks_by_job[job_id].append(chunk)
        
        for job_id, chunks_for_job in resume_chunks_by_job.items():
            if job_id not in job_chunks_by_id:
                logger.debug(f"No job chunks found for job_id={job_id}")
                continue
                
            job_chunks = job_chunks_by_id[job_id]
            logger.debug(f"Comparing {len(chunks_for_job)} resume chunks with {len(job_chunks)} job chunks for job_id={job_id}")
            
            max_scores_per_pair = []
            
            for resume_chunk in chunks_for_job:
                resume_embedding = resume_chunk.get('embedding')
                if not resume_embedding:
                    continue
                    
                max_score = 0
                
                for job_chunk in job_chunks:
                    job_embedding = job_chunk.get('embedding')
                    if not job_embedding:
                        continue
                        
                    score = cosine_similarity(resume_embedding, job_embedding)
                    max_score = max(max_score, score)
                
                if max_score > 0:
                    max_scores_per_pair.append(max_score)
            
            if max_scores_per_pair:
                avg_score = np.mean(max_scores_per_pair)
                similarity_data = {
                    'resume_id': resume_id,
                    'job_id': job_id,
                    'embedding_similarity_score': Decimal(str(avg_score)),   # <--- 修正
                    'num_chunk_pairs': len(max_scores_per_pair)
                }
                similarities.append(similarity_data)
                processed_resume_ids.add(resume_id)
                logger.debug(f"Calculated similarity for resume_id={resume_id}, job_id={job_id}: {avg_score:.4f}")
    
    logger.info(f"Calculated {len(similarities)} similarity scores")
    logger.info(f"Processed {len(processed_resume_ids)} unique resume_ids")
    
    return similarities

def write_similarities_to_dynamodb(similarities):
    """Write similarity scores to DynamoDB"""
    if not similarities:
        logger.warning("No similarities to write")
        return
    
    # Create similarity table if it doesn't exist
    create_table_if_not_exists(SIMILARITY_TABLE)
    similarity_table = dynamodb.Table(SIMILARITY_TABLE)
    
    logger.info(f"Writing {len(similarities)} similarity scores to {SIMILARITY_TABLE}")
    
    with similarity_table.batch_writer() as batch:
        for similarity in similarities:
            # 確保再次包裝 float 類型（防呆）
            item = dict(similarity)
            if 'embedding_similarity_score' in item:
                item['embedding_similarity_score'] = Decimal(str(item['embedding_similarity_score']))
            batch.put_item(Item=item)
    
    logger.info(f"Successfully wrote {len(similarities)} similarity scores")

def update_resume_table_with_similarities(similarities):
    """Update resume table with average embedding similarity score only"""
    if not similarities:
        logger.warning("No similarities to update")
        return

    # Create target table if it doesn't exist
    create_table_if_not_exists(TARGET_TABLE, [
        {
            'AttributeName': 'resume_id',
            'KeyType': 'HASH'
        }
    ])

    source_table = dynamodb.Table(SOURCE_TABLE)
    target_table = dynamodb.Table(TARGET_TABLE)

    # Group similarities by resume_id
    similarities_by_resume = defaultdict(list)
    for similarity in similarities:
        resume_id = similarity['resume_id']
        similarities_by_resume[resume_id].append(similarity)

    logger.info(f"Updating {len(similarities_by_resume)} resumes with average similarity score")

    updated_count = 0
    for resume_id, resume_similarities in similarities_by_resume.items():
        try:
            # Get original resume data
            response = source_table.get_item(Key={'resume_id': resume_id})
            if 'Item' not in response:
                logger.warning(f"Resume {resume_id} not found in source table")
                continue

            resume_data = response['Item']

            # Calculate average score
            avg_score = np.mean([float(sim['embedding_similarity_score']) for sim in resume_similarities])
            # 新增一個欄位，型別要用 Decimal
            resume_data['embedding_similarity_score'] = Decimal(str(avg_score))

            # 只寫回這一份 dict，不加其他欄位
            target_table.put_item(Item=resume_data)
            updated_count += 1

            logger.debug(f"Updated resume {resume_id} with average similarity score: {avg_score}")

        except Exception as e:
            logger.error(f"Error updating resume {resume_id}: {e}")
            continue

    logger.info(f"Successfully updated {updated_count} resumes")


def lambda_handler(event, context):
    """Lambda handler for resume-job matching"""
    try:
        logger.info("=== Starting Resume-Job Matching Lambda ===")
        
        # Calculate chunk similarities
        similarities = calculate_chunk_similarities()
        
        if not similarities:
            logger.warning("No similarities calculated, exiting")
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'No similarities calculated'})
            }
        
        # Write similarities to DynamoDB
        write_similarities_to_dynamodb(similarities)
        
        # Update resume table with similarity scores
        update_resume_table_with_similarities(similarities)
        
        # Summary statistics
        scores = [float(s['embedding_similarity_score']) for s in similarities]
        summary = {
            'total_similarities': len(similarities),
            'unique_resumes': len(set(s['resume_id'] for s in similarities)),
            'unique_jobs': len(set(s['job_id'] for s in similarities)),
            'avg_score': float(np.mean(scores)),
            'min_score': float(np.min(scores)),
            'max_score': float(np.max(scores)),
            'std_score': float(np.std(scores))
        }
        
        logger.info(f"Processing complete. Summary: {summary}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Resume-job matching completed successfully',
                'summary': summary
            })
        }
        
    except Exception as e:
        logger.error(f"Lambda execution error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
