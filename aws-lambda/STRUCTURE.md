# AWS Lambda 目錄結構

## 清理後的目錄結構

```
aws-lambda/
├── deploy_all.sh                    # 同時部署兩個 Lambda 的腳本
├── README.md                        # 總體說明文件
├── jobs-lambda/                     # 處理職位數據的 Lambda
│   ├── jobs_to_opensearch.py        # Lambda 函數代碼
│   ├── requirements.txt             # Python 依賴
│   ├── deploy.sh                    # 單獨部署腳本
│   ├── README.md                    # 詳細說明文件
│   └── jobs_lambda_deployment.zip   # 部署包 (16MB)
└── resume-lambda/                   # 處理簡歷數據的 Lambda
    ├── resume_to_opensearch.py      # Lambda 函數代碼
    ├── requirements.txt             # Python 依賴
    ├── deploy.sh                    # 單獨部署腳本
    ├── README.md                    # 詳細說明文件
    └── resume_lambda_deployment.zip # 部署包 (16MB)
```

## 文件說明

### 根目錄文件
- `deploy_all.sh`: 一鍵部署兩個 Lambda 函數
- `README.md`: 總體架構和部署指南

### Lambda 目錄文件
每個 Lambda 目錄包含：
- `*_to_opensearch.py`: Lambda 函數主代碼
- `requirements.txt`: Python 依賴包
- `deploy.sh`: 單獨部署腳本
- `README.md`: 詳細配置說明
- `*_lambda_deployment.zip`: 完整的部署包

## 使用方式

### 快速部署（推薦）
```bash
chmod +x deploy_all.sh
./deploy_all.sh
```

### 單獨部署
```bash
# 部署 Resume Lambda
cd resume-lambda && ./deploy.sh

# 部署 Jobs Lambda
cd jobs-lambda && ./deploy.sh
```

## 清理說明

已移除的文件：
- 根目錄的舊文件（已移至子目錄）
- 部署過程中的臨時目錄 `lambda_deployment/`
- 重複的配置文件

保留的文件：
- 所有必要的源代碼和配置文件
- 完整的部署包
- 詳細的文檔說明
