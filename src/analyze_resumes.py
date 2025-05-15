import json
import os
import pandas as pd
from collections import Counter

def analyze_resumes(resume_dir='../data/resume'):
    all_skills = []
    resume_data = []
    
    for filename in os.listdir(resume_dir):
        if filename.endswith('.json'):
            with open(os.path.join(resume_dir, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Extract relevant information
                resume_info = {
                    'filename': filename,
                    'name': data['data'].get('item', {}).get('user', {}).get('name', ''),
                    'skills': data['data'].get('item', {}).get('user', {}).get('skill_list', []),
                    'education': data['data'].get('item', {}).get('user', {}).get('graduated_from_school', ''),
                    'job_title': data['data'].get('item', {}).get('user', {}).get('most_recent_work_experience', {}).get('title', '')
                }
                
                all_skills.extend(resume_info['skills'])
                resume_data.append(resume_info)
    
    # Create summary DataFrame
    df = pd.DataFrame(resume_data)
    
    # Analyze skills frequency
    skills_freq = Counter(all_skills)
    
    print("\nMost Common Skills:")
    for skill, count in skills_freq.most_common(10):
        print(f"{skill}: {count}")
    
    print("\nResume Summary:")
    print(df[['name', 'education', 'job_title']].to_string())

if __name__ == "__main__":
    analyze_resumes() 