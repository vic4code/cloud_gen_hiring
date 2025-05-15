# 履歷資料生成器

這個專案用於生成三種不同類型（DS、MLE、PM）的履歷資料，每種類型生成 30 份隨機資料。

## 環境設置

1. 安裝依賴：
```bash
pip install -r requirements.txt
```

2. 設置 OpenAI API key：
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## 使用方法

1. 確保 `data/resume` 目錄下有範例履歷檔案：
   - ds_sample1.json
   - mle_sample1.json
   - pm_sample1.json

2. 運行腳本：
```bash
python generate_resumes.py
```

3. 生成的履歷資料將保存在 `data/generated_resumes` 目錄下，格式為：
   - ds_generated_1.json 到 ds_generated_30.json
   - mle_generated_1.json 到 mle_generated_30.json
   - pm_generated_1.json 到 pm_generated_30.json

## 注意事項

1. 需要有效的 OpenAI API key
2. 生成的履歷資料會保持原始 schema 結構
3. 所有生成的資料都是中文內容
4. 不會包含任何個人隱私資訊

## Project Structure 