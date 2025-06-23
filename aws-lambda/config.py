# Vector Indexing Configuration
# 集中管理所有配置参数

# DynamoDB配置
DYNAMODB_TABLE = 'benson-haire-parsed_resume'

# OpenSearch Serverless配置
OPENSEARCH_COLLECTION = 'haire-vector-db'
OPENSEARCH_COLLECTION_ENDPOINT = 'https://c3qceibouiy9tqnj94d6.ap-southeast-1.aoss.amazonaws.com'
OPENSEARCH_COLLECTION_ARN = 'arn:aws:aoss:ap-southeast-1:570851831916:collection/c3qceibouiy9tqnj94d6'
OPENSEARCH_INDEX = 'haire-vector-db-resume-chunks-embeddings'

# 文本处理配置
CHUNK_SIZE = 32  # 文本分块大小

# Bedrock配置
BEDROCK_MODEL_ID = 'cohere.embed-multilingual-v3'

# 处理配置
BATCH_SIZE = 100  # 每处理多少个简历刷新一次索引
MAX_RETRIES = 3   # 最大重试次数

# 日志配置
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR

# 可选：自定义AWS区域（如果环境变量未设置）
# AWS_REGION = 'us-east-1'

# 可选：自定义AWS配置文件
# AWS_PROFILE = 'default' 