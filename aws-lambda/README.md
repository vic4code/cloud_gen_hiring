# AWS Lambda Functions for OpenSearch Indexing

This directory contains three independent AWS Lambda functions for processing data from DynamoDB and indexing it into OpenSearch.

## Architecture Overview

```
aws-lambda/
├── resume-lambda/                              # Lambda for processing resume data
│   ├── resume_to_opensearch.py
│   ├── requirements.txt
│   ├── deploy.sh
│   └── README.md
├── jobs-lambda/                                # Lambda for processing job data
│   ├── jobs_to_opensearch.py
│   ├── requirements.txt
│   ├── deploy.sh
│   └── README.md
├── resume-jobs-embedding-matching-lambda/      # Lambda for resume-job embedding matching
│   ├── resume_jobs_embedding_matching.py
│   ├── requirements.txt
│   ├── deploy.sh
│   └── README.md
├── deploy_all.sh                               # Deploy all Lambdas
└── README.md                                   # This file
```

## Lambda Function Descriptions

### 1. Resume Lambda (`resume-lambda/`)
- **Function**: Process resume data and generate embeddings
- **Data Source**: DynamoDB table `benson-haire-parsed_resume`
- **Target Index**: `haire-vector-db-resume-chunks-embeddings`
- **Trigger**: DynamoDB Streams

### 2. Jobs Lambda (`jobs-lambda/`)
- **Function**: Process job data and generate embeddings
- **Data Source**: DynamoDB table `haire-jobs`
- **Target Index**: `haire-vector-db-jobs-chunks-embeddings`
- **Trigger**: DynamoDB Streams

### 3. Resume-Jobs Embedding Matching Lambda (`resume-jobs-embedding-matching-lambda/`)
- **Function**: Calculate similarities between resume and job chunks
- **Data Source**: OpenSearch indices
- **Target Tables**: `resume-jobs-similarity`, `embedding-filtered-resume-test`
- **Trigger**: Manual or EventBridge schedule

## Quick Deployment

### Deploy All Lambda Functions

```bash
# Grant execute permission to deployment script
chmod +x deploy_all.sh

# Execute deployment
./deploy_all.sh
```

### Individual Deployment

```bash
# Deploy Resume Lambda
cd resume-lambda
chmod +x deploy.sh
./deploy.sh

# Deploy Jobs Lambda
cd ../jobs-lambda
chmod +x deploy.sh
./deploy.sh

# Deploy Resume-Jobs Embedding Matching Lambda
cd ../resume-jobs-embedding-matching-lambda
chmod +x deploy.sh
./deploy.sh
```

## AWS Configuration Steps

### 1. Create Lambda Functions

Create three functions in AWS Lambda Console:

#### Resume Lambda
- **Function Name**: `resume-opensearch-indexing`
- **Runtime**: Python 3.9+
- **Handler**: `resume_to_opensearch.lambda_handler`
- **Timeout**: 15 minutes (900 seconds)
- **Memory**: 1024 MB or higher

#### Jobs Lambda
- **Function Name**: `jobs-opensearch-indexing`
- **Runtime**: Python 3.9+
- **Handler**: `jobs_to_opensearch.lambda_handler`
- **Timeout**: 15 minutes (900 seconds)
- **Memory**: 1024 MB or higher

#### Resume-Jobs Embedding Matching Lambda
- **Function Name**: `resume-jobs-embedding-matching`
- **Runtime**: Python 3.9+
- **Handler**: `resume_jobs_embedding_matching.lambda_handler`
- **Timeout**: 15 minutes (900 seconds)
- **Memory**: 2048 MB (recommended for numpy operations)

### 2. Configure DynamoDB Streams

#### Enable Streams for `benson-haire-parsed_resume` table
1. Select the table in DynamoDB Console
2. Click "Exports and streams" tab
3. Click "Enable stream" in "DynamoDB stream details" section
4. Select "New and old images"
5. Click "Enable"

#### Enable Streams for `haire-jobs` table
1. Repeat the above steps
2. Ensure both tables have independent Stream ARNs

### 3. Configure Lambda Triggers

#### Resume Lambda Trigger
1. Click "Add trigger" on Lambda function page
2. Select "DynamoDB"
3. Select Stream ARN of `benson-haire-parsed_resume` table
4. Set batch size to 1
5. Click "Add"

#### Jobs Lambda Trigger
1. Repeat the above steps
2. Select Stream ARN of `haire-jobs` table

### 4. IAM Permission Configuration

Add the following permissions to each Lambda execution role:

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
                "dynamodb:Scan",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:CreateTable",
                "dynamodb:DescribeTable"
            ],
            "Resource": [
                "arn:aws:dynamodb:*:*:table/benson-haire-parsed_resume",
                "arn:aws:dynamodb:*:*:table/haire-jobs",
                "arn:aws:dynamodb:*:*:table/resume-jobs-similarity",
                "arn:aws:dynamodb:*:*:table/embedding-filtered-resume-test"
            ]
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

## Monitoring and Troubleshooting

### CloudWatch Logs
- Each Lambda function has independent CloudWatch Log Group
- Check logs to monitor execution status and errors

### Common Issues
1. **Timeout Errors**: Increase Lambda timeout or memory
2. **Permission Errors**: Check IAM role permissions
3. **OpenSearch Errors**: Check OpenSearch collection capacity and permissions

## Cost Optimization

1. **Memory Configuration**: Adjust memory settings based on data volume
2. **Timeout Settings**: Avoid unnecessary long-running executions
3. **Batch Processing**: Consider batch processing multiple records

## Security Considerations

1. **Principle of Least Privilege**: Only grant necessary IAM permissions
2. **Environment Variables**: Use environment variables for sensitive configurations
3. **VPC Configuration**: Consider placing Lambda in VPC for enhanced security

## Usage Examples

### Manual Execution
```bash
# Test Resume-Jobs Embedding Matching Lambda
aws lambda invoke \
  --function-name resume-jobs-embedding-matching \
  --payload '{}' \
  response.json
```

### Scheduled Execution
Set up EventBridge rule for periodic execution:
- **Cron expression**: `0 */6 * * ? *` (every 6 hours)
- **Target**: Your Lambda function
