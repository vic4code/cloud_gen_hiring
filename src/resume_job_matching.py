import boto3
import json
import logging
from tqdm import tqdm
from decimal import Decimal

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize AWS session
session = boto3.Session()
dynamodb = session.resource('dynamodb')

# DynamoDB table names
SOURCE_TABLE = 'benson-haire-parsed_resume'
TARGET_TABLE = 'embedding-filtered-resume-test'

def load_similarity_scores():
    """Load similarity scores from the JSON file"""
    try:
        with open('similarity_results.json', 'r', encoding='utf-8') as f:
            similarity_data = json.load(f)
        
        # Create a mapping from (resume_id, job_id) to similarity_score
        similarity_map = {}
        for item in similarity_data:
            key = (item['resume_id'], item['job_id'])
            similarity_map[key] = item['similarity_score']
        
        logging.info(f"Loaded {len(similarity_map)} similarity scores")
        return similarity_map
    except Exception as e:
        logging.error(f"Error loading similarity scores: {e}")
        return {}

def scan_dynamodb_table(table_name):
    """Scan all items from DynamoDB table"""
    table = dynamodb.Table(table_name)
    items = []
    
    try:
        response = table.scan()
        items.extend(response['Items'])
        
        # Handle pagination if needed
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])
        
        logging.info(f"Scanned {len(items)} items from {table_name}")
        return items
    except Exception as e:
        logging.error(f"Error scanning table {table_name}: {e}")
        return []

def create_table_if_not_exists(table_name):
    """Create the target table if it doesn't exist"""
    try:
        # Check if table exists
        table = dynamodb.Table(table_name)
        table.load()
        logging.info(f"Table {table_name} already exists")
        return True
    except Exception:
        # Table doesn't exist, create it with a simple schema
        try:
            # Create table with basic schema (assuming resume_id is the primary key)
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': 'resume_id',
                        'KeyType': 'HASH'  # Partition key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'resume_id',
                        'AttributeType': 'S'  # String
                    }
                ],
                BillingMode='PAY_PER_REQUEST'  # On-demand billing
            )
            
            # Wait for table to be created
            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
            logging.info(f"Created table {table_name}")
            return True
        except Exception as e:
            logging.error(f"Error creating table {table_name}: {e}")
            return False

def write_items_to_table(table_name, items):
    """Write items to DynamoDB table using batch operations"""
    table = dynamodb.Table(table_name)
    
    # DynamoDB batch write limit is 25 items per request
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
            # Continue with next batch

def main():
    logging.info("Starting resume-job matching and table creation...")
    
    # Load similarity scores
    similarity_map = load_similarity_scores()
    if not similarity_map:
        logging.error("No similarity scores found. Please run similarity_calculator.py first.")
        return
    
    # Scan source table
    source_items = scan_dynamodb_table(SOURCE_TABLE)
    if not source_items:
        logging.error(f"No items found in source table {SOURCE_TABLE}")
        return
    
    # Create target table if it doesn't exist
    if not create_table_if_not_exists(TARGET_TABLE):
        logging.error(f"Failed to create target table {TARGET_TABLE}")
        return
    
    # Process items and add similarity scores
    processed_items = []
    
    for item in tqdm(source_items, desc='Processing items'):
        # Create a copy of the item
        new_item = item.copy()
        
        # Get resume_id and job_id from the item
        resume_id = item.get('resume_id')
        job_id = item.get('job_id')
        
        if resume_id and job_id:
            # Look up similarity score and convert to Decimal
            similarity_score = similarity_map.get((resume_id, job_id), 0.0)
            new_item['embedding_similarity_score'] = Decimal(str(similarity_score))
        else:
            # If no job_id, set similarity score to 0
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