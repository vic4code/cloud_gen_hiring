import boto3
import json

# Initialize AWS session
session = boto3.Session()
dynamodb = session.resource('dynamodb')

# DynamoDB table name
SOURCE_TABLE = 'benson-haire-parsed_resume'

def check_table_schema():
    """Check the schema of the source table"""
    try:
        table = dynamodb.Table(SOURCE_TABLE)
        description = table.meta.client.describe_table(TableName=SOURCE_TABLE)
        
        print("=== TABLE SCHEMA ===")
        print(f"Table Name: {description['Table']['TableName']}")
        print(f"Table Status: {description['Table']['TableStatus']}")
        
        print("\n=== KEY SCHEMA ===")
        for key in description['Table']['KeySchema']:
            print(f"  {key['AttributeName']}: {key['KeyType']}")
        
        print("\n=== ATTRIBUTE DEFINITIONS ===")
        for attr in description['Table']['AttributeDefinitions']:
            print(f"  {attr['AttributeName']}: {attr['AttributeType']}")
        
        print("\n=== SAMPLE ITEM KEYS ===")
        # Get a sample item to see the actual key structure
        response = table.scan(Limit=1)
        if response['Items']:
            sample_item = response['Items'][0]
            print("Sample item keys:")
            for key, value in sample_item.items():
                print(f"  {key}: {type(value).__name__} = {value}")
        
    except Exception as e:
        print(f"Error checking table schema: {e}")

if __name__ == "__main__":
    check_table_schema() 