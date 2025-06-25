#!/bin/bash

# Deploy both Lambda functions
set -e

echo "=== Deploying Both Lambda Functions ==="
echo ""

# Deploy Resume Lambda
echo "1. Deploying Resume Lambda..."
cd resume-lambda
chmod +x deploy.sh
./deploy.sh
cd ..

echo ""
echo "2. Deploying Jobs Lambda..."
cd jobs-lambda
chmod +x deploy.sh
./deploy.sh
cd ..

echo ""
echo "=== Deployment Complete ==="
echo ""
echo "Generated deployment packages:"
echo "- resume-lambda/resume_lambda_deployment.zip"
echo "- jobs-lambda/jobs_lambda_deployment.zip"
echo ""
echo "Next steps:"
echo "1. Create two Lambda functions in AWS Console"
echo "2. Upload respective deployment packages"
echo "3. Configure DynamoDB Streams for both tables"
echo "4. Set up Lambda triggers for DynamoDB Streams"
echo ""
echo "Resume Lambda:"
echo "- Handler: resume_to_opensearch.lambda_handler"
echo "- Table: benson-haire-parsed_resume"
echo "- Index: haire-vector-db-resume-chunks-embeddings"
echo ""
echo "Jobs Lambda:"
echo "- Handler: jobs_to_opensearch.lambda_handler"
echo "- Table: haire-jobs"
echo "- Index: haire-vector-db-jobs-chunks-embeddings"
