# Resume Data Generator

This project is used to generate three different types of resume data (DS, MLE, PM), with 30 random samples for each type.

## Environment Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

1. Ensure there are sample resume files in the `data/resume` directory:
   - ds_sample1.json
   - mle_sample1.json
   - pm_sample1.json

2. Run the script:
```bash
python generate_resumes.py
```

3. Generated resume data will be saved in the `data/generated_resumes` directory with the following format:
   - ds_generated_1.json to ds_generated_30.json
   - mle_generated_1.json to mle_generated_30.json
   - pm_generated_1.json to pm_generated_30.json

## Notes

1. A valid OpenAI API key is required
2. Generated resume data will maintain the original schema structure
3. All generated content will be in Chinese
4. No personal privacy information will be included

## Project Structure 