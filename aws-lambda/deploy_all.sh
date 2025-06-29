#!/bin/bash

# AWS Lambda deployment script for all Lambda functions
set -e

echo "Starting deployment of all AWS Lambda functions..."

# Deploy Resume Lambda
echo ""
echo "=== Deploying Resume Lambda ==="
cd resume-lambda
chmod +x deploy.sh
./deploy.sh
cd ..

# Deploy Jobs Lambda
echo ""
echo "=== Deploying Jobs Lambda ==="
cd jobs-lambda
chmod +x deploy.sh
./deploy.sh
cd ..

# Deploy Resume-Jobs Embedding Matching Lambda
echo ""
echo "=== Deploying Resume-Jobs Embedding Matching Lambda ==="
cd resume-jobs-embedding-matching-lambda
chmod +x deploy.sh
./deploy.sh
cd ..

echo ""
echo "=== All Lambda functions deployed successfully! ==="
echo ""
echo "Deployment Summary:"
echo "- Resume Lambda: resume_lambda_deployment.zip"
echo "- Jobs Lambda: jobs_lambda_deployment.zip"
echo "- Resume-Jobs Embedding Matching Lambda: resume_jobs_embedding_matching_lambda_deployment.zip"
echo ""
echo "Next steps:"
echo "1. Upload deployment packages to AWS Lambda Console"
echo "2. Configure Lambda functions with appropriate settings"
echo "3. Set up DynamoDB Streams triggers"
echo "4. Configure IAM permissions"
echo ""
echo "See README.md for detailed configuration instructions."
