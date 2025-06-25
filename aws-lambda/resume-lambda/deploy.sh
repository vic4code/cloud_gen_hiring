#!/bin/bash

# AWS Lambda deployment script for Resume Lambda
set -e

echo "Starting Resume Lambda deployment..."

# Create deployment directory
DEPLOY_DIR="lambda_deployment"
rm -rf $DEPLOY_DIR
mkdir -p $DEPLOY_DIR

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt -t $DEPLOY_DIR

# Copy Lambda function
echo "Copying Lambda function..."
cp resume_to_opensearch.py $DEPLOY_DIR/

# Create deployment package
echo "Creating deployment package..."
cd $DEPLOY_DIR
zip -r ../resume_lambda_deployment.zip .
cd ..

echo "Deployment package created: resume_lambda_deployment.zip"
echo ""
echo "To deploy to AWS Lambda:"
echo "1. Go to AWS Lambda Console"
echo "2. Create or update your resume processing function"
echo "3. Upload resume_lambda_deployment.zip"
echo "4. Set handler to: resume_to_opensearch.lambda_handler"
echo "5. Set timeout to at least 15 minutes (900 seconds)"
echo "6. Set memory to at least 1024 MB"
echo ""
echo "Required IAM permissions:"
echo "- DynamoDB: Scan on benson-haire-parsed_resume table"
echo "- Bedrock: InvokeModel for cohere.embed-multilingual-v3"
echo "- OpenSearch: Full access to haire-vector-db collection"
echo ""
echo "DynamoDB Streams Configuration:"
echo "- Enable streams on benson-haire-parsed_resume table"
echo "- Set stream type to 'New and old images'"
echo "- Configure Lambda trigger for stream events"
