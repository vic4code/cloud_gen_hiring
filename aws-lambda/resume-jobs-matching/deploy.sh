#!/bin/bash

# AWS Lambda deployment script for Resume-Jobs Matching Lambda
set -e

echo "Starting Resume-Jobs Matching Lambda deployment..."

# Create deployment directory
DEPLOY_DIR="lambda_deployment"
rm -rf $DEPLOY_DIR
mkdir -p $DEPLOY_DIR

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt -t $DEPLOY_DIR

# Copy Lambda function
echo "Copying Lambda function..."
cp resume_jobs_matching.py $DEPLOY_DIR/

# Create deployment package
echo "Creating deployment package..."
cd $DEPLOY_DIR
zip -r ../resume_jobs_matching_lambda_deployment.zip .
cd ..

echo "Deployment package created: resume_jobs_matching_lambda_deployment.zip"
echo ""
echo "To deploy to AWS Lambda:"
echo "1. Go to AWS Lambda Console"
echo "2. Create or update your resume-jobs matching function"
echo "3. Upload resume_jobs_matching_lambda_deployment.zip"
echo "4. Set handler to: resume_jobs_matching.lambda_handler"
echo "5. Set timeout to at least 15 minutes (900 seconds)"
echo "6. Set memory to at least 2048 MB (recommended for numpy operations)"
echo ""
echo "Required IAM permissions:"
echo "- DynamoDB: Full access to benson-haire-parsed_resume, embedding-filtered-resume-test, resume-jobs-similarity tables"
echo "- OpenSearch: Full access to haire-vector-db collection"
echo "- CloudWatch Logs: CreateLogGroup, CreateLogStream, PutLogEvents"
echo ""
echo "Lambda Configuration:"
echo "- Runtime: Python 3.9 or later"
echo "- Architecture: x86_64"
echo "- Environment variables: None required (all configs are hardcoded)"
echo ""
echo "Usage:"
echo "- This Lambda can be triggered manually or via EventBridge schedule"
echo "- For periodic execution, set up EventBridge rule with cron expression"
echo "- Example cron: '0 */6 * * ? *' (every 6 hours)" 