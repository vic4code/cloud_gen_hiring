// Mock data based on project's actual DynamoDB/CSV data

const MOCK_TEAMS = [
  {
    id: "TECH-FE-DEV",
    team_name: "前端開發組",
    department: "技術部",
    dept_code: "FE",
    company: "科技創新公司",
    company_code: "TECH",
    team_code: "DEV",
    category: "技術開發",
    description: "負責公司所有前端應用程式的開發與維護"
  },
  {
    id: "CFU-DATAAI-AI",
    team_name: "人工智慧科",
    department: "數據暨人工智慧發展部",
    dept_code: "DATAAI",
    company: "國泰金控",
    company_code: "CFU",
    team_code: "AI",
    category: "AI 研發",
    description: "掌握最新的人工智慧科技發展、加速集團 AI 應用"
  },
  {
    id: "CFU-DATAAI-DE",
    team_name: "資料工程科",
    department: "數據暨人工智慧發展部",
    dept_code: "DATAAI",
    company: "國泰金控",
    company_code: "CFU",
    team_code: "DE",
    category: "資料工程",
    description: "負責集團數據基礎架構的建設與維護"
  },
  {
    id: "TECH-BE-DEV",
    team_name: "後端開發組",
    department: "技術部",
    dept_code: "BE",
    company: "科技創新公司",
    company_code: "TECH",
    team_code: "DEV",
    category: "技術開發",
    description: "負責後端 API 與微服務系統的開發維護"
  },
  {
    id: "CXI-DATAAI-CT",
    team_name: "AI 創新實驗室",
    department: "數據暨人工智慧發展部",
    dept_code: "DATAAI",
    company: "國泰人壽",
    company_code: "CXI",
    team_code: "CT",
    category: "AI 研發",
    description: "專注於 AI 新技術的實驗與創新應用探索"
  },
  {
    id: "TECH-QA-TEST",
    team_name: "品質保證組",
    department: "技術部",
    dept_code: "QA",
    company: "科技創新公司",
    company_code: "TECH",
    team_code: "TEST",
    category: "品質保證",
    description: "負責產品品質測試與自動化測試框架開發"
  }
];

const MOCK_JOBS = [
  {
    job_id: "CFU-DATAAI-AI-5cbcaa38",
    job_title: "資料科學分析師 Data Scientist",
    company: "國泰金控",
    department: "數據暨人工智慧發展部",
    team_name: "人工智慧科",
    location: "臺北市 信義區",
    employment_type: "全職",
    salary_min: 40000,
    salary_max: null,
    status: "active",
    required_skills: ["軟體程式設計", "數據分析與管理", "演算法", "機器學習", "深度學習", "Python", "scikit-learn", "PyTorch"],
    min_experience_years: 1,
    education_required: ""
  },
  {
    job_id: "CFU-DATAAI-AI-bb2b5035",
    job_title: "資料科學家(測試職缺解析)",
    company: "國泰金控",
    department: "數據暨人工智慧發展部",
    team_name: "人工智慧科",
    location: "台北市信義區",
    employment_type: "全職",
    salary_min: 65000,
    salary_max: 78000,
    status: "active",
    required_skills: ["機器學習", "深度學習", "Python", "scikit-learn", "PyTorch", "資料科學"],
    min_experience_years: 5,
    education_required: "碩士以上"
  },
  {
    job_id: "TECH-FE-DEV-830cea2a",
    job_title: "前端工程師",
    company: "科技創新公司",
    department: "技術部",
    team_name: "前端開發組",
    location: "台北市",
    employment_type: "全職",
    salary_min: 60000,
    salary_max: 90000,
    status: "active",
    required_skills: ["React", "JavaScript", "CSS"],
    min_experience_years: 2,
    education_required: "大學以上"
  },
  {
    job_id: "TECH-FE-DEV-daec5eb7",
    job_title: "產品經理",
    company: "科技創新公司",
    department: "技術部",
    team_name: "前端開發組",
    location: "台北市",
    employment_type: "全職",
    salary_min: 70000,
    salary_max: 120000,
    status: "active",
    required_skills: ["產品管理", "數據分析", "專案管理"],
    min_experience_years: 3,
    education_required: "大學以上"
  },
  {
    job_id: "TECH-FE-DEV-0f9e71c0",
    job_title: "UI/UX 設計師",
    company: "科技創新公司",
    department: "技術部",
    team_name: "前端開發組",
    location: "台北市",
    employment_type: "全職",
    salary_min: 50000,
    salary_max: 80000,
    status: "active",
    required_skills: ["Figma", "Adobe Creative Suite", "用戶體驗設計"],
    min_experience_years: 1,
    education_required: "大學以上"
  }
];

const MOCK_CANDIDATES = {
  "CFU-DATAAI-AI-5cbcaa38": [
    {
      id: "darren-wu-resume",
      name: "Darren Wu",
      title: "Data Scientist",
      email: "darren.wu@gmail.com",
      phone: "0912-345-678",
      skills: ["Machine Learning", "Deep Learning", "Python", "TensorFlow", "PyTorch", "SQL", "Data Analysis", "NLP"],
      experience: [
        { company: "台灣大哥大", role: "資深資料科學家", duration: "2021/03 - 至今", months: 36 },
        { company: "國泰世華銀行", role: "資料分析師", duration: "2018/06 - 2021/02", months: 33 }
      ],
      education: "國立臺灣大學 資訊工程學系 碩士",
      score: 92,
      reason: "該候選人具備豐富的機器學習與深度學習實務經驗，熟悉 Python 生態系統，且有金融業相關經驗，與國泰金控 AI 團隊的技術需求高度吻合。具備從研究到落地的完整能力。"
    },
    {
      id: "lin-yichen-resume",
      name: "林怡辰",
      title: "Machine Learning Engineer",
      email: "yichen.lin@outlook.com",
      phone: "0923-456-789",
      skills: ["Python", "scikit-learn", "PyTorch", "Docker", "AWS", "MLOps", "Computer Vision"],
      experience: [
        { company: "Appier", role: "機器學習工程師", duration: "2020/08 - 至今", months: 42 },
        { company: "工業技術研究院", role: "AI 研究助理", duration: "2018/09 - 2020/07", months: 22 }
      ],
      education: "國立清華大學 統計學系 碩士",
      score: 87,
      reason: "擁有扎實的機器學習工程經驗及 MLOps 實務，熟悉雲端部署和模型服務化，對團隊正在發展中的技術應用如電腦視覺有直接相關經驗。"
    },
    {
      id: "zhang-xiaoming-resume",
      name: "張小明",
      title: "資料科學應屆畢業生",
      email: "xiaoming.zhang@example.com",
      phone: "0987-654-321",
      skills: ["Python", "SQL", "Tableau", "Power BI", "R", "TensorFlow", "NumPy", "Pandas", "Machine Learning", "Statistics"],
      experience: [
        { company: "智聯科技有限公司", role: "數據分析實習生", duration: "2023/09 - 2023/12", months: 3 },
        { company: "圓圓科技有限公司", role: "資料科學實習生", duration: "2023/07 - 2023/08", months: 2 }
      ],
      education: "國防醫學院 資料科學 學士",
      score: 65,
      reason: "雖然為應屆畢業生且實務經驗較少，但具備良好的資料科學基礎知識，熟悉機器學習和數據視覺化工具，有潛力在團隊指導下快速成長。"
    },
    {
      id: "chen-meihui-resume",
      name: "美惠 陳",
      title: "前端開發實習生",
      email: "meihui.chen@outlook.com",
      phone: "0934-567-890",
      skills: ["JavaScript", "React", "HTML5", "CSS3", "Git", "Python", "MySQL", "Adobe XD"],
      experience: [
        { company: "新創科技公司", role: "前端開發實習生", duration: "2024/01 - 2024/06", months: 6 }
      ],
      education: "國立交通大學 資訊管理學系 學士",
      score: 45,
      reason: "教育背景符合職缺要求，但主要技能偏向前端開發，與資料科學分析師的核心需求有較大落差，建議考慮其他更匹配的職缺。"
    }
  ],
  "CFU-DATAAI-AI-bb2b5035": [
    {
      id: "wang-jiawei-resume",
      name: "王嘉偉",
      title: "Senior Data Scientist",
      email: "jiawei.wang@gmail.com",
      phone: "0945-678-901",
      skills: ["Machine Learning", "Deep Learning", "Python", "PyTorch", "MLOps", "AWS", "Databricks", "RAG", "Computer Vision"],
      experience: [
        { company: "Google Taiwan", role: "資深資料科學家", duration: "2019/01 - 至今", months: 60 },
        { company: "Microsoft", role: "資料科學家", duration: "2016/03 - 2018/12", months: 34 }
      ],
      education: "國立臺灣大學 資訊工程學系 博士",
      score: 95,
      reason: "具備超過 7 年資料科學經驗，在頂級科技公司任職，精通機器學習全技術棧，且具備 MLOps 和雲端平台經驗，完美匹配資深資料科學家的職缺需求。"
    },
    {
      id: "huang-yuru-resume",
      name: "黃郁如",
      title: "AI Research Scientist",
      email: "yuru.huang@ntu.edu.tw",
      phone: "0956-789-012",
      skills: ["Deep Learning", "PyTorch", "NLP", "Federated Learning", "Responsible AI", "Python", "scikit-learn"],
      experience: [
        { company: "中央研究院", role: "AI 研究科學家", duration: "2018/02 - 至今", months: 72 },
        { company: "國立臺灣大學", role: "博士後研究員", duration: "2016/09 - 2018/01", months: 17 }
      ],
      education: "國立臺灣大學 電機工程學系 博士",
      score: 88,
      reason: "在學術研究領域有深厚積累，特別在聯邦學習和負責任 AI 方面有專長，與職缺要求的研究方向高度吻合，能為團隊帶來前沿研究視角。"
    }
  ],
  "TECH-FE-DEV-830cea2a": [
    {
      id: "chen-meihui-resume",
      name: "美惠 陳",
      title: "前端開發實習生",
      email: "meihui.chen@outlook.com",
      phone: "0934-567-890",
      skills: ["JavaScript", "React", "HTML5", "CSS3", "Git", "Python", "MySQL", "Adobe XD"],
      experience: [
        { company: "新創科技公司", role: "前端開發實習生", duration: "2024/01 - 2024/06", months: 6 }
      ],
      education: "國立交通大學 資訊管理學系 學士",
      score: 85,
      reason: "雖然經驗偏初階，但技能組合與前端工程師職缺高度匹配，熟悉 React、JavaScript 等核心技術，有成長潛力。"
    }
  ],
  "TECH-FE-DEV-daec5eb7": [
    {
      id: "li-mingzhe-resume",
      name: "李明哲",
      title: "Product Manager",
      email: "mingzhe.li@gmail.com",
      phone: "0967-890-123",
      skills: ["產品管理", "數據分析", "專案管理", "Agile", "JIRA", "SQL", "Figma"],
      experience: [
        { company: "LINE Taiwan", role: "產品經理", duration: "2020/05 - 至今", months: 48 },
        { company: "PChome", role: "助理產品經理", duration: "2017/08 - 2020/04", months: 33 }
      ],
      education: "國立政治大學 企業管理學系 碩士",
      score: 90,
      reason: "具備豐富的產品管理經驗，在知名科技公司任職超過 6 年，擅長數據驅動的產品決策，與職缺需求高度匹配。"
    }
  ]
};

const MOCK_RESUMES = [
  {
    id: "resume-001",
    name: "Darren Wu",
    email: "darren.wu@gmail.com",
    title: "資深資料科學家",
    skills: ["Machine Learning", "Deep Learning", "Python", "TensorFlow", "PyTorch", "SQL", "NLP"],
    education: "國立臺灣大學 資訊工程學系 碩士",
    source: "upload",
    status: "parsed",
    upload_date: "2026/02/28",
    is_recent: true
  },
  {
    id: "resume-002",
    name: "林怡辰",
    email: "yichen.lin@outlook.com",
    title: "機器學習工程師",
    skills: ["Python", "scikit-learn", "PyTorch", "Docker", "AWS", "MLOps"],
    education: "國立清華大學 統計學系 碩士",
    source: "email",
    status: "parsed",
    upload_date: "2026/02/27",
    is_recent: true
  },
  {
    id: "resume-003",
    name: "張小明",
    email: "xiaoming.zhang@example.com",
    title: "資料科學應屆畢業生",
    skills: ["Python", "SQL", "Tableau", "Power BI", "R", "TensorFlow"],
    education: "國防醫學院 資料科學 學士",
    source: "website",
    status: "parsed",
    upload_date: "2026/02/25",
    is_recent: true
  },
  {
    id: "resume-004",
    name: "美惠 陳",
    email: "meihui.chen@outlook.com",
    title: "前端開發實習生",
    skills: ["JavaScript", "React", "HTML5", "CSS3", "Git", "Python"],
    education: "國立交通大學 資訊管理學系 學士",
    source: "referral",
    status: "parsed",
    upload_date: "2026/02/24",
    is_recent: false
  },
  {
    id: "resume-005",
    name: "王嘉偉",
    email: "jiawei.wang@gmail.com",
    title: "Senior Data Scientist",
    skills: ["Machine Learning", "Deep Learning", "Python", "PyTorch", "MLOps", "AWS", "RAG"],
    education: "國立臺灣大學 資訊工程學系 博士",
    source: "upload",
    status: "parsed",
    upload_date: "2026/02/22",
    is_recent: false
  },
  {
    id: "resume-006",
    name: "黃郁如",
    email: "yuru.huang@ntu.edu.tw",
    title: "AI Research Scientist",
    skills: ["Deep Learning", "PyTorch", "NLP", "Federated Learning", "Responsible AI"],
    education: "國立臺灣大學 電機工程學系 博士",
    source: "email",
    status: "parsed",
    upload_date: "2026/02/20",
    is_recent: false
  },
  {
    id: "resume-007",
    name: "李明哲",
    email: "mingzhe.li@gmail.com",
    title: "Product Manager",
    skills: ["產品管理", "數據分析", "專案管理", "Agile", "JIRA", "SQL"],
    education: "國立政治大學 企業管理學系 碩士",
    source: "website",
    status: "parsed",
    upload_date: "2026/02/18",
    is_recent: false
  },
  {
    id: "resume-008",
    name: "陳建宏",
    email: "jianhong.chen@yahoo.com",
    title: "後端工程師",
    skills: ["Java", "Spring Boot", "PostgreSQL", "Docker", "Kubernetes", "AWS"],
    education: "國立成功大學 資訊工程學系 碩士",
    source: "upload",
    status: "pending",
    upload_date: "2026/03/01",
    is_recent: true
  },
  {
    id: "resume-009",
    name: "周雅婷",
    email: "yating.zhou@gmail.com",
    title: "UI/UX Designer",
    skills: ["Figma", "Adobe XD", "Sketch", "用戶研究", "Prototyping"],
    education: "實踐大學 工業產品設計學系 學士",
    source: "referral",
    status: "parsed",
    upload_date: "2026/02/15",
    is_recent: false
  },
  {
    id: "resume-010",
    name: "劉志偉",
    email: "zhiwei.liu@hotmail.com",
    title: "DevOps Engineer",
    skills: ["AWS", "Terraform", "Docker", "Kubernetes", "CI/CD", "Linux"],
    education: "國立中央大學 資訊工程學系 學士",
    source: "website",
    status: "parsed",
    upload_date: "2026/02/12",
    is_recent: false
  },
  {
    id: "resume-011",
    name: "蔡佳琪",
    email: "jiaqi.tsai@gmail.com",
    title: "Data Analyst",
    skills: ["SQL", "Python", "Tableau", "Excel", "統計分析"],
    education: "國立臺灣師範大學 數學系 學士",
    source: "email",
    status: "pending",
    upload_date: "2026/03/02",
    is_recent: true
  },
  {
    id: "resume-012",
    name: "吳承翰",
    email: "chenghan.wu@example.com",
    title: "Full Stack Developer",
    skills: ["React", "Node.js", "TypeScript", "MongoDB", "GraphQL"],
    education: "國立陽明交通大學 資訊科學與工程研究所 碩士",
    source: "upload",
    status: "failed",
    upload_date: "2026/03/03",
    is_recent: true
  }
];

const MOCK_STATS = {
  teams: MOCK_TEAMS.length,
  activeJobs: MOCK_JOBS.filter(j => j.status === "active").length,
  resumes: 156,
  matches: 43
};
