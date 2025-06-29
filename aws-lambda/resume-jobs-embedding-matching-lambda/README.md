# Resume-Jobs Embedding Matching Lambda

This AWS Lambda function calculates embedding similarities between resume chunks and job chunks stored in OpenSearch, and updates DynamoDB tables with the results.

## Overview

The function performs the following operations:

1. **Loads chunk data** from OpenSearch indices:
   - `haire-vector-db-resume-chunks-embeddings`
   - `haire-vector-db-jobs-chunks-embeddings`

2. **Calculates similarities** between resume and job chunks:
   - For each resume chunk, finds matching job chunks by `job_id`
   - Calculates cosine similarity between embeddings
   - Takes the maximum similarity score for each resume chunk
   - Averages the max scores for each resume-job pair

3. **Writes results** to DynamoDB:
   - `resume-jobs-similarity`: Raw similarity scores
   - `embedding-filtered-resume-test`: Enhanced resume data with similarity scores

## Architecture

```
OpenSearch Indices → Lambda → DynamoDB Tables
     ↓                    ↓           ↓
Resume Chunks    → Similarity → resume-jobs-similarity
Job Chunks       → Calculation → embedding-filtered-resume-test
```

## Configuration

### OpenSearch
- **Endpoint**: `c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com`
- **Resume Index**: `haire-vector-db-resume-chunks-embeddings`
- **Jobs Index**: `haire-vector-db-jobs-chunks-embeddings`

### DynamoDB Tables
- **Source**: `benson-haire-parsed_resume` (original resume data)
- **Target**: `embedding-filtered-resume-test` (enhanced with similarity scores)
- **Similarity**: `resume-jobs-similarity` (raw similarity data)

## Similarity Calculation Logic

For each unique `resume_id`:

1. Get all resume chunks for that `resume_id`
2. Group chunks by `job_id`
3. For each `job_id` group:
   - Get all job chunks for that `job_id`
   - For each resume chunk, calculate similarity with all job chunks
   - Take the maximum similarity score for each resume chunk
   - Average all max scores to get final similarity for this resume-job pair

## Output Format

### resume-jobs-similarity Table
```json
{
  "resume_id": "string",
  "job_id": "string", 
  "embedding_similarity_score": 0.85,
  "num_chunk_pairs": 5
}
```

### embedding-filtered-resume-test Table
```json
{
  "resume_id": "string",
  // ... original resume fields ...
  "embedding_similarity_scores": [
    {
      "job_id": "string",
      "score": 0.85,
      "num_chunk_pairs": 5
    }
  ],
  "avg_embedding_similarity_score": 0.85
}
```

## Deployment

1. Run the deployment script:
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

2. Upload the generated `resume_jobs_matching_lambda_deployment.zip` to AWS Lambda

3. Configure the Lambda function:
   - **Handler**: `resume_jobs_embedding_matching.lambda_handler`
   - **Timeout**: 15 minutes (900 seconds)
   - **Memory**: 2048 MB (recommended for numpy operations)
   - **Runtime**: Python 3.9+

## IAM Permissions Required

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:CreateTable",
        "dynamodb:DescribeTable"
      ],
      "Resource": [
        "arn:aws:dynamodb:ap-southeast-1:*:table/benson-haire-parsed_resume",
        "arn:aws:dynamodb:ap-southeast-1:*:table/embedding-filtered-resume-test",
        "arn:aws:dynamodb:ap-southeast-1:*:table/resume-jobs-similarity"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "aoss:APIAccessAll"
      ],
      "Resource": "arn:aws:aoss:ap-southeast-1:*:collection/haire-vector-db"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:ap-southeast-1:*:*"
    }
  ]
}
```

## Usage

### Manual Execution
The Lambda can be triggered manually with an empty event:
```json
{}
```

### Scheduled Execution
Set up EventBridge rule for periodic execution:
- **Cron expression**: `0 */6 * * ? *` (every 6 hours)
- **Target**: Your Lambda function

## Monitoring

Check CloudWatch Logs for:
- Processing statistics
- Missing data warnings
- Error messages
- Summary statistics

## Troubleshooting

### Common Issues

1. **No similarities calculated**
   - Check if OpenSearch indices have data
   - Verify resume chunks have `job_id` and `embedding` fields
   - Check if job chunks have `embedding` fields

2. **DynamoDB table creation errors**
   - Verify IAM permissions
   - Check if table already exists with different schema

3. **Timeout errors**
   - Increase Lambda timeout
   - Increase memory allocation
   - Consider processing in batches

### Debug Mode

Set logging level to DEBUG for detailed information:
```python
logger.setLevel(logging.DEBUG)
```

## Performance Considerations

- **Memory**: 2048 MB recommended for numpy operations
- **Timeout**: 15 minutes for large datasets
- **Batch processing**: Consider splitting large datasets
- **Caching**: OpenSearch queries are not cached, consider optimization for large datasets 