import requests
import json
import time
import os
from fake_useragent import UserAgent
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup

class ResumeScraperPDA:
    def __init__(self):
        self.base_url = "https://pda.104.com.tw/api/resumes"
        self.headers = {
            'User-Agent': UserAgent().random,
            'Accept': 'application/json, text/plain, */*',
        }
        self.output_dir = '../data/resume'
        os.makedirs(self.output_dir, exist_ok=True)
        
    def get_search_results(self, keyword, page=1):
        search_url = f"https://pda.104.com.tw/api/resumes/search"
        params = {
            'keyword': keyword,
            'page': page,
            'sortBy': 'lastUpdateDate',
            'order': 'desc'
        }
        
        response = requests.get(search_url, headers=self.headers, params=params)
        return response.json()

    def get_resume_detail(self, resume_id):
        detail_url = f"{self.base_url}/profiles/{resume_id}"
        response = requests.get(detail_url, headers=self.headers)
        return response.json()

    def save_resume(self, resume_data, index):
        output_file = os.path.join(self.output_dir, f'mle-resume{str(index).zfill(3)}.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({'data': resume_data}, f, ensure_ascii=False, indent=2)

    def scrape_resumes(self, keywords=['machine learning', 'data science'], max_pages=5):
        resume_count = 0
        
        for keyword in keywords:
            print(f"\nSearching resumes for keyword: {keyword}")
            
            for page in range(1, max_pages + 1):
                search_results = self.get_search_results(keyword, page)
                
                if not search_results.get('data', {}).get('list'):
                    break
                
                for resume in tqdm(search_results['data']['list'], desc=f"Page {page}"):
                    try:
                        resume_id = resume['resumeId']
                        resume_detail = self.get_resume_detail(resume_id)
                        
                        # Check if the resume contains relevant keywords
                        resume_text = json.dumps(resume_detail, ensure_ascii=False).lower()
                        if any(kw.lower() in resume_text for kw in keywords):
                            self.save_resume(resume_detail, resume_count)
                            resume_count += 1
                        
                        # Be nice to the server
                        time.sleep(1)
                        
                    except Exception as e:
                        print(f"Error processing resume {resume_id}: {str(e)}")
                
                time.sleep(2)  # Pause between pages

if __name__ == "__main__":
    scraper = ResumeScraperPDA()
    keywords = ['machine learning', 'data science', 'artificial intelligence', 'deep learning']
    scraper.scrape_resumes(keywords=keywords, max_pages=3) 