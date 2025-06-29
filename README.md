# Cloud Generation Hiring System

A comprehensive AI-powered hiring system that processes resumes and job data, generates embeddings, and provides intelligent matching capabilities using AWS services.

## Project Overview

This project consists of multiple components working together to create an intelligent resume-job matching system:

1. **Resume Data Generation**: Generate synthetic resume data for testing
2. **AWS Lambda Functions**: Process data and generate embeddings
3. **OpenSearch Integration**: Store and search vector embeddings
4. **DynamoDB Storage**: Store processed data and matching results
5. **Similarity Matching**: Calculate embeddings similarity between resumes and jobs

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Resume Data   │    │   Job Data      │    │   AWS Lambda    │
│   Generation    │    │   Processing    │    │   Functions     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   DynamoDB      │    │   OpenSearch    │    │   Similarity    │
│   Tables        │    │   Indices       │    │   Matching      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Components

### 1. Resume Data Generator (`generate_resumes.py`)
- Generates three types of resume data (DS, MLE, PM)
- Creates 30 random samples for each type
- Uses OpenAI API for content generation
- Maintains original schema structure

### 2. AWS Lambda Functions (`aws-lambda/`)

#### Resume Lambda (`resume-lambda/`)
- Processes resume data from DynamoDB
- Generates embeddings using Bedrock
- Indexes to OpenSearch

#### Jobs Lambda (`jobs-lambda/`)
- Processes job data from DynamoDB
- Generates embeddings using Bedrock
- Indexes to OpenSearch

#### Resume-Jobs Matching Lambda (`resume-jobs-matching/`)
- Calculates similarities between resume and job chunks
- Updates DynamoDB with matching results
- Provides comprehensive similarity scores

### 3. Data Processing Scripts (`src/`)
- Various utility scripts for data analysis
- OpenSearch integration helpers
- Similarity calculation utilities

## Environment Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

3. Configure AWS credentials:
```bash
aws configure
```

## Usage

### Generate Resume Data

1. Ensure sample resume files exist in `data/resume/`:
   - ds_sample1.json
   - mle_sample1.json
   - pm_sample1.json

2. Run the generation script:
```bash
python generate_resumes.py
```

3. Generated data will be saved in `data/generated_resumes/`:
   - ds_generated_1.json to ds_generated_30.json
   - mle_generated_1.json to mle_generated_30.json
   - pm_generated_1.json to pm_generated_30.json

### Deploy AWS Lambda Functions

1. Deploy all Lambda functions:
```bash
cd aws-lambda
chmod +x deploy_all.sh
./deploy_all.sh
```

2. Or deploy individually:
```bash
# Resume Lambda
cd aws-lambda/resume-lambda && ./deploy.sh

# Jobs Lambda
cd aws-lambda/jobs-lambda && ./deploy.sh

# Resume-Jobs Matching Lambda
cd aws-lambda/resume-jobs-matching && ./deploy.sh
```

### Run Similarity Matching

1. Execute the matching script:
```bash
python src/resume_jobs_matching.py
```

2. Check results in DynamoDB:
   - `resume-jobs-similarity`: Raw similarity scores
   - `embedding-filtered-resume-test`: Enhanced resume data

## Configuration

### AWS Services
- **DynamoDB Tables**:
  - `benson-haire-parsed_resume`: Source resume data
  - `haire-jobs`: Source job data
  - `resume-jobs-similarity`: Similarity results
  - `embedding-filtered-resume-test`: Enhanced resumes

- **OpenSearch Indices**:
  - `haire-vector-db-resume-chunks-embeddings`: Resume embeddings
  - `haire-vector-db-jobs-chunks-embeddings`: Job embeddings

- **AWS Lambda Functions**:
  - `resume-opensearch-indexing`: Process resume data
  - `jobs-opensearch-indexing`: Process job data
  - `resume-jobs-matching`: Calculate similarities

### Environment Variables
- `OPENAI_API_KEY`: OpenAI API key for content generation
- `AWS_DEFAULT_REGION`: AWS region (default: ap-southeast-1)

## Project Structure

```
cloud_gen_hiring/
├── aws-lambda/                    # AWS Lambda functions
│   ├── resume-lambda/            # Resume processing Lambda
│   ├── jobs-lambda/              # Job processing Lambda
│   ├── resume-jobs-matching/     # Similarity matching Lambda
│   ├── deploy_all.sh             # Deployment script
│   └── README.md                 # Lambda documentation
├── src/                          # Source code and utilities
│   ├── resume_jobs_matching.py   # Similarity matching script
│   ├── analyze_resumes.py        # Resume analysis utilities
│   └── ...                       # Other utility scripts
├── data/                         # Data files
│   ├── resume/                   # Sample resume files
│   ├── generated_resume/         # Generated resume data
│   └── ...                       # Other data files
├── generate_resumes.py           # Resume generation script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Monitoring and Troubleshooting

### CloudWatch Logs
- Each Lambda function has independent CloudWatch Log Group
- Check logs for execution status and errors

### Common Issues
1. **Timeout Errors**: Increase Lambda timeout or memory
2. **Permission Errors**: Check IAM role permissions
3. **OpenSearch Errors**: Verify collection capacity and permissions
4. **API Key Errors**: Ensure OpenAI API key is properly configured

## Security Considerations

1. **API Keys**: Store sensitive keys as environment variables
2. **IAM Permissions**: Follow principle of least privilege
3. **Data Privacy**: Ensure no personal information is exposed
4. **VPC Configuration**: Consider placing Lambda in VPC for enhanced security

## Performance Optimization

1. **Memory Configuration**: Adjust based on data volume
2. **Timeout Settings**: Optimize for processing requirements
3. **Batch Processing**: Consider processing multiple records
4. **Caching**: Implement caching for frequently accessed data

## Contributing

1. Follow the existing code structure
2. Add appropriate documentation
3. Test thoroughly before deployment
4. Update README files for any new features

## License

This project is for internal use only. Please ensure compliance with all applicable data protection and privacy regulations. 