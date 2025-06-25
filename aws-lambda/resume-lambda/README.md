# Resume to OpenSearch Lambda Function

這個 AWS Lambda 函數用於將 DynamoDB 中的簡歷數據處理並索引到 OpenSearch 中。

## 功能

- 從 DynamoDB 表 `benson-haire-parsed_resume` 讀取簡歷數據
- 提取專業經驗描述
- 將文本分塊並使用 Bedrock 生成嵌入向量
- 將嵌入向量寫入 OpenSearch 索引 `haire-vector-db-resume-chunks-embeddings`

## 部署步驟

### 1. 準備部署包

```bash
# 給部署腳本執行權限
chmod +x deploy.sh

# 執行部署腳本
./deploy.sh
```

### 2. AWS Lambda 配置

1. 在 AWS Lambda Console 中創建新函數或更新現有函數
2. 上傳生成的 `resume_lambda_deployment.zip`
3. 設置以下配置：
   - **Handler**: `resume_to_opensearch.lambda_handler`
   - **Runtime**: Python 3.9 或更高版本
   - **Timeout**: 15 分鐘 (900 秒)
   - **Memory**: 1024 MB 或更高

### 3. IAM 權限

Lambda 執行角色需要以下權限：

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:Scan"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/benson-haire-parsed_resume"
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

### 4. DynamoDB Streams 配置

1. 在 DynamoDB Console 中啟用 `benson-haire-parsed_resume` 表的 Streams
2. 設置 Stream 類型為 "New and old images"
3. 在 Lambda Console 中添加 DynamoDB Streams 觸發器
4. 選擇剛創建的 Stream ARN

### 5. 環境變數 (可選)

如果需要自定義配置，可以設置以下環境變數：

- `CHUNK_SIZE`: 文本分塊大小 (預設: 256)
- `BEDROCK_MODEL_ID`: Bedrock 模型 ID (預設: cohere.embed-multilingual-v3)
- `RESUME_TABLE`: DynamoDB 表名 (預設: benson-haire-parsed_resume)

## 執行

函數可以通過以下方式觸發：

1. **DynamoDB Streams**: 當 benson-haire-parsed_resume 表有更新時自動觸發
2. **手動觸發**: 在 Lambda Console 中點擊 "Test"
3. **API Gateway**: 通過 HTTP 請求觸發
4. **EventBridge**: 按時間表觸發

## 輸出

函數成功執行後會返回：

```json
{
    "statusCode": 200,
    "body": {
        "message": "Successfully processed X resumes and created Y chunks",
        "processed_items": X,
        "total_chunks": Y
    }
}
```

## 監控

- 查看 CloudWatch Logs 來監控執行情況
- 函數會記錄處理進度和錯誤信息
- 每處理 10 個項目會記錄一次進度

## 注意事項

1. 函數會清空現有的 OpenSearch 索引，請確保這是預期行為
2. 處理大量數據時可能需要調整 Lambda 的超時和內存設置
3. 確保 OpenSearch 集合有足夠的容量來存儲所有嵌入向量
4. 此函數與 jobs-lambda 獨立運行，不會互相影響
