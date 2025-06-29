# Jobs to OpenSearch Lambda Function

This AWS Lambda function processes job data from DynamoDB and indexes it into OpenSearch.

## Features

- Reads job data from DynamoDB table `haire-jobs`
- Extracts required_skills, requirements, responsibilities fields
- Chunks text and generates embeddings using Bedrock
- Writes embeddings to OpenSearch index `haire-vector-db-jobs-chunks-embeddings`

## Deployment Steps

### 1. Prepare Deployment Package

```bash
# Grant execute permission to deployment script
chmod +x deploy.sh

# Execute deployment script
./deploy.sh
```

### 2. AWS Lambda Configuration

1. Create new function or update existing function in AWS Lambda Console
2. Upload the generated `jobs_lambda_deployment.zip`
3. Set the following configuration:
   - **Handler**: `jobs_to_opensearch.lambda_handler`
   - **Runtime**: Python 3.9 or higher
   - **Timeout**: 15 minutes (900 seconds)
   - **Memory**: 1024 MB or higher

### 3. IAM Permissions

Lambda execution role requires the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:DescribeStream",
                "dynamodb:ListStreams"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:Scan"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/haire-jobs"
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": "arn:aws:bedrock:*::foundation-model/cohere.embed-multilingual-v3"
        },
        {
            "Effect": "Allow",
            "Action": [
                "aoss:*"
            ],
            "Resource": "arn:aws:aoss:ap-southeast-1:570851831916:collection/c3qceibouiy9tqnj94d6"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
```

### 4. DynamoDB Streams Configuration

1. Enable Streams for `haire-jobs` table in DynamoDB Console
2. Set Stream type to "New and old images"
3. Add DynamoDB Streams trigger in Lambda Console
4. Select the newly created Stream ARN

### 5. Environment Variables (Optional)

If custom configuration is needed, you can set the following environment variables:

- `CHUNK_SIZE`: Text chunk size (default: 256)
- `BEDROCK_MODEL_ID`: Bedrock model ID (default: cohere.embed-multilingual-v3)
- `JOBS_TABLE`: DynamoDB table name (default: haire-jobs)

## Execution

The function can be triggered in the following ways:

1. **DynamoDB Streams**: Automatically triggered when haire-jobs table is updated
2. **Manual Trigger**: Click "Test" in Lambda Console
3. **API Gateway**: Triggered via HTTP request
4. **EventBridge**: Triggered on schedule

## Output

The function returns the following on successful execution:

```json
{
    "statusCode": 200,
    "body": {
        "message": "Successfully processed X jobs and created Y chunks",
        "processed_items": X,
        "total_chunks": Y
    }
}
```

## Monitoring

- Check CloudWatch Logs to monitor execution status
- Function logs processing progress and error information
- Progress is logged every 10 processed items

## Important Notes

1. Function will clear existing OpenSearch index, ensure this is expected behavior
2. Processing large amounts of data may require adjusting Lambda timeout and memory settings
3. Ensure OpenSearch collection has sufficient capacity to store all embeddings
4. This function runs independently from resume-lambda and will not interfere with each other

## Troubleshooting

### Common Issues

1. **Timeout Errors**: Increase Lambda timeout or memory allocation
2. **Permission Errors**: Check IAM role permissions for DynamoDB, Bedrock, and OpenSearch
3. **OpenSearch Errors**: Verify OpenSearch collection capacity and permissions
4. **Stream Processing Errors**: Check DynamoDB Streams configuration

### Debug Mode

Enable debug logging by setting the log level to DEBUG in the Lambda function:

```python
logger.setLevel(logging.DEBUG)
```

## Performance Considerations

- **Memory**: 1024 MB recommended for embedding generation
- **Timeout**: 15 minutes for large datasets
- **Batch Processing**: Consider processing multiple records in batches
- **Caching**: OpenSearch queries are not cached, consider optimization for large datasets
