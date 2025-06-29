# AWS Lambda Directory Structure

## Cleaned Directory Structure

```
aws-lambda/
├── deploy_all.sh                    # Script to deploy all Lambdas
├── README.md                        # Overall documentation
├── STRUCTURE.md                     # This file
├── jobs-lambda/                     # Lambda for processing job data
│   ├── jobs_to_opensearch.py        # Lambda function code
│   ├── requirements.txt             # Python dependencies
│   ├── deploy.sh                    # Individual deployment script
│   ├── README.md                    # Detailed documentation
│   └── jobs_lambda_deployment.zip   # Deployment package (16MB)
├── resume-lambda/                   # Lambda for processing resume data
│   ├── resume_to_opensearch.py      # Lambda function code
│   ├── requirements.txt             # Python dependencies
│   ├── deploy.sh                    # Individual deployment script
│   ├── README.md                    # Detailed documentation
│   └── resume_lambda_deployment.zip # Deployment package (16MB)
└── resume-jobs-matching/            # Lambda for resume-job matching
    ├── resume_jobs_matching.py      # Lambda function code
    ├── requirements.txt             # Python dependencies
    ├── deploy.sh                    # Individual deployment script
    ├── README.md                    # Detailed documentation
    └── resume_jobs_matching_lambda_deployment.zip # Deployment package (25MB)
```

## File Descriptions

### Root Directory Files
- `deploy_all.sh`: One-click deployment for all Lambda functions
- `README.md`: Overall architecture and deployment guide
- `STRUCTURE.md`: This file

### Lambda Directory Files
Each Lambda directory contains:
- `*_to_opensearch.py` or `*_matching.py`: Lambda function main code
- `requirements.txt`: Python dependency packages
- `deploy.sh`: Individual deployment script
- `README.md`: Detailed configuration documentation
- `*_lambda_deployment.zip`: Complete deployment package

## Usage

### Quick Deployment (Recommended)
```bash
chmod +x deploy_all.sh
./deploy_all.sh
```

### Individual Deployment
```bash
# Deploy Resume Lambda
cd resume-lambda && ./deploy.sh

# Deploy Jobs Lambda
cd jobs-lambda && ./deploy.sh

# Deploy Resume-Jobs Matching Lambda
cd resume-jobs-matching && ./deploy.sh
```

## Cleanup Notes

Removed files:
- Old files in root directory (moved to subdirectories)
- Temporary directories `lambda_deployment/` from deployment process
- Duplicate configuration files

Retained files:
- All necessary source code and configuration files
- Complete deployment packages
- Detailed documentation

## Function Overview

### Resume Lambda
- **Purpose**: Process resume data and generate embeddings
- **Input**: DynamoDB Streams from `benson-haire-parsed_resume`
- **Output**: OpenSearch index `haire-vector-db-resume-chunks-embeddings`
- **Trigger**: DynamoDB Streams events

### Jobs Lambda
- **Purpose**: Process job data and generate embeddings
- **Input**: DynamoDB Streams from `haire-jobs`
- **Output**: OpenSearch index `haire-vector-db-jobs-chunks-embeddings`
- **Trigger**: DynamoDB Streams events

### Resume-Jobs Matching Lambda
- **Purpose**: Calculate similarities between resume and job chunks
- **Input**: OpenSearch indices
- **Output**: DynamoDB tables `resume-jobs-similarity`, `embedding-filtered-resume-test`
- **Trigger**: Manual or EventBridge schedule
