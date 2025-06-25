# AWS Lambda Functions for OpenSearch Indexing

這個目錄包含兩個獨立的 AWS Lambda 函數，用於將 DynamoDB 中的數據處理並索引到 OpenSearch 中。

## 架構概覽

```
aws-lambda/
├── resume-lambda/          # 處理簡歷數據的 Lambda
│   ├── resume_to_opensearch.py
│   ├── requirements.txt
│   ├── deploy.sh
│   └── README.md
├── jobs-lambda/            # 處理職位數據的 Lambda
│   ├── jobs_to_opensearch.py
│   ├── requirements.txt
│   ├── deploy.sh
│   └── README.md
├── deploy_all.sh           # 同時部署兩個 Lambda
└── README.md               # 本文件
```

## Lambda 函數說明

### 1. Resume Lambda (`resume-lambda/`)
- **功能**: 處理簡歷數據並生成嵌入向量
- **數據源**: DynamoDB 表 `benson-haire-parsed_resume`
- **目標索引**: `haire-vector-db-resume-chunks-embeddings`
- **觸發方式**: DynamoDB Streams

### 2. Jobs Lambda (`jobs-lambda/`)
- **功能**: 處理職位數據並生成嵌入向量
- **數據源**: DynamoDB 表 `haire-jobs`
- **目標索引**: `haire-vector-db-jobs-chunks-embeddings`
- **觸發方式**: DynamoDB Streams

## 快速部署

### 部署所有 Lambda 函數

```bash
# 給部署腳本執行權限
chmod +x deploy_all.sh

# 執行部署
./deploy_all.sh
```

### 單獨部署

```bash
# 部署 Resume Lambda
cd resume-lambda
chmod +x deploy.sh
./deploy.sh

# 部署 Jobs Lambda
cd ../jobs-lambda
chmod +x deploy.sh
./deploy.sh
```

## AWS 配置步驟

### 1. 創建 Lambda 函數

在 AWS Lambda Console 中創建兩個函數：

#### Resume Lambda
- **函數名稱**: `resume-opensearch-indexing`
- **Runtime**: Python 3.9+
- **Handler**: `resume_to_opensearch.lambda_handler`
- **超時**: 15 分鐘 (900 秒)
- **內存**: 1024 MB 或更高

#### Jobs Lambda
- **函數名稱**: `jobs-opensearch-indexing`
- **Runtime**: Python 3.9+
- **Handler**: `jobs_to_opensearch.lambda_handler`
- **超時**: 15 分鐘 (900 秒)
- **內存**: 1024 MB 或更高

### 2. 配置 DynamoDB Streams

#### 為 `benson-haire-parsed_resume` 表啟用 Streams
1. 在 DynamoDB Console 中選擇表
2. 點擊 "Exports and streams" 標籤
3. 在 "DynamoDB stream details" 部分點擊 "Enable stream"
4. 選擇 "New and old images"
5. 點擊 "Enable"

#### 為 `haire-jobs` 表啟用 Streams
1. 重複上述步驟
2. 確保兩個表都有獨立的 Stream ARN

### 3. 配置 Lambda 觸發器

#### Resume Lambda 觸發器
1. 在 Lambda 函數頁面點擊 "Add trigger"
2. 選擇 "DynamoDB"
3. 選擇 `benson-haire-parsed_resume` 表的 Stream ARN
4. 設置批處理大小為 1
5. 點擊 "Add"

#### Jobs Lambda 觸發器
1. 重複上述步驟
2. 選擇 `haire-jobs` 表的 Stream ARN

### 4. IAM 權限配置

為每個 Lambda 執行角色添加以下權限：

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
            "Resource": [
                "arn:aws:dynamodb:*:*:table/benson-haire-parsed_resume",
                "arn:aws:dynamodb:*:*:table/haire-jobs"
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
        }
    ]
}
```

## 監控和故障排除

### CloudWatch Logs
- 每個 Lambda 函數都有獨立的 CloudWatch Log Group
- 查看日誌來監控執行情況和錯誤

### 常見問題
1. **超時錯誤**: 增加 Lambda 超時時間或內存
2. **權限錯誤**: 檢查 IAM 角色權限
3. **OpenSearch 錯誤**: 檢查 OpenSearch 集合容量和權限

## 成本優化

1. **內存配置**: 根據數據量調整內存設置
2. **超時設置**: 避免不必要的長時間運行
3. **批處理**: 考慮批量處理多個記錄

## 安全注意事項

1. **最小權限原則**: 只授予必要的 IAM 權限
2. **環境變數**: 敏感配置使用環境變數
3. **VPC 配置**: 考慮將 Lambda 放在 VPC 中以增強安全性
