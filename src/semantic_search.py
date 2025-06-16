import boto3
import json
import os
from opensearchpy import OpenSearch, RequestsHttpConnection
from opensearchpy.helpers import bulk
import numpy as np
from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SemanticSearch:
    def __init__(self, 
                 aws_access_key: str,
                 aws_secret_key: str,
                 region_name: str,
                 opensearch_host: str,
                 opensearch_port: int = 443,
                 similarity_threshold: float = 0.7):
        """
        Initialize the semantic search service.
        
        Args:
            aws_access_key: AWS access key
            aws_secret_key: AWS secret key
            region_name: AWS region name
            opensearch_host: OpenSearch host URL
            opensearch_port: OpenSearch port (default: 443)
            similarity_threshold: Minimum similarity score to consider a match (default: 0.7)
        """
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name
        )
        
        self.opensearch_client = OpenSearch(
            hosts=[{'host': opensearch_host, 'port': opensearch_port}],
            http_auth=None,  # Add authentication if needed
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )
        
        self.similarity_threshold = similarity_threshold
        self.index_name = 'resumes'

    def read_from_s3(self, bucket: str, key: str) -> Dict[str, Any]:
        """Read a JSON file from S3."""
        try:
            response = self.s3_client.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8')
            return json.loads(content)
        except Exception as e:
            logger.error(f"Error reading from S3: {e}")
            raise

    def write_to_s3(self, bucket: str, key: str, data: Dict[str, Any]):
        """Write data to S3 as JSON."""
        try:
            self.s3_client.put_object(
                Bucket=bucket,
                Key=key,
                Body=json.dumps(data, ensure_ascii=False, indent=2),
                ContentType='application/json'
            )
        except Exception as e:
            logger.error(f"Error writing to S3: {e}")
            raise

    def list_resumes(self, bucket: str, prefix: str) -> List[str]:
        """List all resume files in the specified S3 prefix."""
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=bucket,
                Prefix=prefix
            )
            return [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.json')]
        except Exception as e:
            logger.error(f"Error listing resumes: {e}")
            raise

    def search_similar_resumes(self, job_description: Dict[str, Any], resumes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Search for resumes similar to the job description using OpenSearch.
        
        Args:
            job_description: Job description dictionary
            resumes: List of resume dictionaries
            
        Returns:
            List of matching resumes with similarity scores
        """
        matching_resumes = []
        
        # Prepare the search query
        query = {
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                        "params": {"query_vector": self._get_embedding(job_description)}
                    }
                }
            }
        }
        
        try:
            # Search in OpenSearch
            response = self.opensearch_client.search(
                index=self.index_name,
                body=query
            )
            
            # Process results
            for hit in response['hits']['hits']:
                score = hit['_score']
                if score >= self.similarity_threshold:
                    resume_data = hit['_source']
                    resume_data['similarity_score'] = score
                    matching_resumes.append(resume_data)
                    
        except Exception as e:
            logger.error(f"Error searching resumes: {e}")
            raise
            
        return matching_resumes

    def _get_embedding(self, text: Dict[str, Any]) -> List[float]:
        """
        Get embedding vector for the input text.
        This is a placeholder - you'll need to implement the actual embedding generation
        using your preferred model (e.g., OpenAI, Sentence Transformers, etc.)
        """
        # TODO: Implement actual embedding generation
        # This is just a placeholder that returns random vectors
        return np.random.rand(384).tolist()

def main():
    # Configuration
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    OPENSEARCH_HOST = os.getenv('OPENSEARCH_HOST')
    S3_BUCKET = os.getenv('S3_BUCKET')
    JOB_DESCRIPTION_KEY = 'job_description.json'
    RESUMES_PREFIX = 'resumes/'
    OUTPUT_PREFIX = 'matching_resumes/'
    
    # Initialize semantic search
    semantic_search = SemanticSearch(
        aws_access_key=AWS_ACCESS_KEY,
        aws_secret_key=AWS_SECRET_KEY,
        region_name=AWS_REGION,
        opensearch_host=OPENSEARCH_HOST
    )
    
    try:
        # Read job description
        job_description = semantic_search.read_from_s3(S3_BUCKET, JOB_DESCRIPTION_KEY)
        
        # List and read all resumes
        resume_keys = semantic_search.list_resumes(S3_BUCKET, RESUMES_PREFIX)
        resumes = [semantic_search.read_from_s3(S3_BUCKET, key) for key in resume_keys]
        
        # Find matching resumes
        matching_resumes = semantic_search.search_similar_resumes(job_description, resumes)
        
        # Save results
        output_key = f"{OUTPUT_PREFIX}matches.json"
        semantic_search.write_to_s3(S3_BUCKET, output_key, {
            'job_description': job_description,
            'matching_resumes': matching_resumes,
            'total_matches': len(matching_resumes)
        })
        
        logger.info(f"Found {len(matching_resumes)} matching resumes")
        
    except Exception as e:
        logger.error(f"Error in main process: {e}")
        raise

if __name__ == "__main__":
    main() 