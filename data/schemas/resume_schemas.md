# Resume Schema Documentation

## DS Resume Schemas

### Common Schema

This schema represents the common structure across all samples:

```json
{
  "type": "object",
  "properties": {
    "education": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "institution": {
                "type": "str",
                "example": "University of Minnesota"
              },
              "degree": {
                "type": "str",
                "example": "Master's Degree"
              },
              "field": {
                "type": "str",
                "example": "Business Analytics"
              },
              "duration": {
                "type": "str",
                "example": "2023/06~2024/05"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "institution": {
                "type": "str",
                "example": "國立清華大學 (National Tsing Hua University)"
              },
              "degree": {
                "type": "str",
                "example": "Bachelor's Degree"
              },
              "field": {
                "type": "str",
                "example": "科技管理學院學士班 (College of Technology Management, Bachelor's Program)"
              },
              "duration": {
                "type": "str",
                "example": "2019/09~2023/06"
              }
            }
          }
        ]
      }
    },
    "title": {
      "type": "str",
      "example": "Data Science Consultant"
    },
    "tools": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "str",
            "example": "Python"
          },
          {
            "type": "str",
            "example": "R"
          },
          {
            "type": "str",
            "example": "SQL"
          },
          {
            "type": "str",
            "example": "Spark"
          },
          {
            "type": "str",
            "example": "Looker Studio"
          },
          {
            "type": "str",
            "example": "Tableau"
          },
          {
            "type": "str",
            "example": "Power BI"
          }
        ]
      }
    },
    "company": {
      "type": "str",
      "example": "Carlson Analytics Lab"
    },
    "about_chinese": {
      "type": "str",
      "example": "Hello, I am Yvonne! Great to meet you! 我熱愛用數據洞見故事！畢業於清華大學科技管理學院學士班 (專長數據科學 + 管理學) 及美國明尼蘇達大學商業分析碩士 (Master of Science in Business Analytics)，我擁有扎實的統計知識與資料分析能力。在美讀碩期間於 Carlson Analytics Lab擔任數據科學顧問，與三家當地企業合作，運用進階數據分析方法解決商業問題。期待繼續用我的靈敏思維與創新，為我未來的公司提供有價值的決策分析，創造數據影響力！"
    },
    "profile": {
      "type": "object",
      "properties": {
        "awards": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "any"
              },
              {
                "type": "any"
              },
              {
                "type": "any"
              },
              {
                "type": "any"
              }
            ]
          }
        },
        "languages": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "Chinese"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "zh"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "5"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "English"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "en"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "4"
                  }
                }
              },
              {
                "type": "any"
              },
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "Chinese"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "zh"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "5"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "English"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "en"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "4"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "Chinese"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "zh"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "5"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "English"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "en"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "3"
                  }
                }
              }
            ]
          }
        },
        "references": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "any"
              },
              {
                "type": "any"
              },
              {
                "type": "any"
              },
              {
                "type": "any"
              }
            ]
          }
        },
        "educations": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2012"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2013"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "Tilburg University"
                  },
                  "description": {
                    "type": "str",
                    "example": "Master of Science | Econometrics and Mathematical Economics | Tilburg City, the Netherlands (Sep 2012 - Aug 2013)"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2007"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2012"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "National Taipei University"
                  },
                  "description": {
                    "type": "str",
                    "example": "Bachelor | Department of Statistics | New Taipei City, Taiwan (Sep 2007 - Jan 2012)"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2009"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2010"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "University of Innsbruck (Austria) SOWI"
                  },
                  "description": {
                    "type": "str",
                    "example": "One-year exchange student | 2009/09 - 2010/09"
                  }
                }
              },
              {
                "type": "any"
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2018"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2020"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "Hanze University of Applied Sciences / Vilnius University"
                  },
                  "description": {
                    "type": "str",
                    "example": "雙聯碩士 - 國際溝通碩士學程"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2011"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2015"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "Tamkang University"
                  },
                  "description": {
                    "type": "str",
                    "example": "英文系學士"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2014"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2016"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "國立交通大學 統計學研究所"
                  },
                  "description": {
                    "type": "str",
                    "example": "碩士畢業"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2009"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2014"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "國立中正大學 數學系"
                  },
                  "description": {
                    "type": "str",
                    "example": "大學畢業"
                  }
                }
              }
            ]
          }
        },
        "professional_experiences": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "Data Analyst, Assistant Manager"
                  },
                  {
                    "type": "str",
                    "example": "Assistant Manager"
                  },
                  {
                    "type": "str",
                    "example": "Data Analytic Specialist"
                  },
                  {
                    "type": "str",
                    "example": "Event Planning and Coordinator"
                  },
                  {
                    "type": "str",
                    "example": "Business Analysis"
                  },
                  {
                    "type": "str",
                    "example": "Project Manager"
                  },
                  {
                    "type": "str",
                    "example": "Digital Marketing Specialist"
                  },
                  {
                    "type": "str",
                    "example": "市場行銷實習生"
                  },
                  {
                    "type": "str",
                    "example": "數據分析師"
                  },
                  {
                    "type": "str",
                    "example": "資料工程師"
                  },
                  {
                    "type": "str",
                    "example": "雲端解決方案工程師"
                  },
                  {
                    "type": "str",
                    "example": "數據工程師"
                  },
                  {
                    "type": "str",
                    "example": "數位行銷企劃專員"
                  },
                  {
                    "type": "str",
                    "example": "data scientist"
                  },
                  {
                    "type": "str",
                    "example": "大數據分析應用管理師"
                  },
                  {
                    "type": "str",
                    "example": "高級工程師"
                  }
                ]
              },
              "company": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "Morrison Express"
                  },
                  {
                    "type": "str",
                    "example": "Zuellig Pharma Digital and Data"
                  },
                  {
                    "type": "str",
                    "example": "Zuellig Pharma Digital and Data"
                  },
                  {
                    "type": "str",
                    "example": "Yong-He Church NPO"
                  },
                  {
                    "type": "str",
                    "example": "CitiBank"
                  },
                  {
                    "type": "str",
                    "example": "SUPERMEDIA 超人氣新媒體股份有限公司"
                  },
                  {
                    "type": "str",
                    "example": "貝殼放大 Backer-Founder"
                  },
                  {
                    "type": "str",
                    "example": "羅傑斯人工智能股份有限公司"
                  },
                  {
                    "type": "str",
                    "example": "CommonWealth Magazine 天下雜誌"
                  },
                  {
                    "type": "str",
                    "example": "AccuHit 愛酷智能科技"
                  },
                  {
                    "type": "str",
                    "example": "Dynasafe 動力安全資訊"
                  },
                  {
                    "type": "str",
                    "example": "DV Biomed 麗彤生醫"
                  },
                  {
                    "type": "str",
                    "example": "Interwaters Pte. Ltd"
                  },
                  {
                    "type": "str",
                    "example": "宏碁股份有限公司"
                  },
                  {
                    "type": "str",
                    "example": "擎雷防偽科技股份有限公司"
                  },
                  {
                    "type": "str",
                    "example": "旺宏電子"
                  }
                ]
              },
              "start_date": {
                "type": "object",
                "properties": {
                  "month": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "8"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "4"
                      },
                      {
                        "type": "int",
                        "example": "12"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "6"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "6"
                      },
                      {
                        "type": "int",
                        "example": "7"
                      },
                      {
                        "type": "int",
                        "example": "4"
                      },
                      {
                        "type": "int",
                        "example": "11"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "7"
                      }
                    ]
                  },
                  "year": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "2023"
                      },
                      {
                        "type": "int",
                        "example": "2021"
                      },
                      {
                        "type": "int",
                        "example": "2019"
                      },
                      {
                        "type": "int",
                        "example": "2016"
                      },
                      {
                        "type": "int",
                        "example": "2013"
                      },
                      {
                        "type": "int",
                        "example": "2024"
                      },
                      {
                        "type": "int",
                        "example": "2023"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2023"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2021"
                      },
                      {
                        "type": "int",
                        "example": "2020"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2020"
                      },
                      {
                        "type": "int",
                        "example": "2016"
                      }
                    ]
                  }
                }
              },
              "end_date": {
                "type": "object",
                "properties": {
                  "month": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "0"
                      },
                      {
                        "type": "int",
                        "example": "12"
                      },
                      {
                        "type": "int",
                        "example": "7"
                      },
                      {
                        "type": "int",
                        "example": "9"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "12"
                      },
                      {
                        "type": "int",
                        "example": "5"
                      },
                      {
                        "type": "int",
                        "example": "6"
                      },
                      {
                        "type": "int",
                        "example": "7"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "5"
                      },
                      {
                        "type": "int",
                        "example": "10"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "10"
                      }
                    ]
                  },
                  "year": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "0"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2021"
                      },
                      {
                        "type": "int",
                        "example": "2018"
                      },
                      {
                        "type": "int",
                        "example": "2016"
                      },
                      {
                        "type": "int",
                        "example": "2024"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2025"
                      },
                      {
                        "type": "int",
                        "example": "2023"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2021"
                      },
                      {
                        "type": "int",
                        "example": "2023"
                      },
                      {
                        "type": "int",
                        "example": "2022"
                      },
                      {
                        "type": "int",
                        "example": "2019"
                      }
                    ]
                  }
                }
              },
              "location": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "New Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Singapore"
                  },
                  {
                    "type": "str",
                    "example": "Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taiwan"
                  },
                  {
                    "type": "str",
                    "example": "Taiwan"
                  }
                ]
              },
              "description": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "02/01/2023 - present\n\nProject Management / Product Leadership: Spearhead the development of MUSE, an internal reporting product delivering up-to-date financial, sales and operational performance insights through interactive dashboards using agile approach.\n\nStrategic Data Architecture: Design and implement new ETL flows leveraging LakeHouse structure to establish a Single Source Of Truth with prioritized report features, improving data accuracy by 12%.\n\nComplex Data Management: Oversee the migration of 6+ million records and integration of 400+ business logics, ensuring seamless transitions with minimal disruption to business operations.\n\nCross-functional Collaboration: Act as a bridge between end users (20+ across F&A/Sales/Product/Operation) and product team (Data/EA/BI).\n\nOperational Efficiency: Establish process flows and implemented user request platform via Jira Service Management tool, cutting BI admin workload by 70%. Establish centralized platform, boosting BI report efficiency by 60%."
                  },
                  {
                    "type": "str",
                    "example": "01/08/2021 - 31/12/2022\n\nBusiness Development\nStrengthened key account monitor mechanism and proactively collaborated with regional stakeholders to achieve country target at 129% and increased subscribed project number by 132%.\nRedesigned pricing scheme for TW country, increased annual subscription price by 9% and prolonged clients' subscription period by 160%.\n\nData Analytics\nCustomer end-to-end support, from data visualization product all hands to new solution selling.\nConducted sales analysis and presented to valued clients, successfully increased the awareness of company's data capability among the industry and strengthened client engagement.\nDeveloped commercial indicator and visualize business metrics to monitor country growth, generated monthly management report for C-level and higher management team for strategic decision support."
                  },
                  {
                    "type": "str",
                    "example": "25/02/2019 - 01/08/2021\n\nCustomer Insight Analysis\nDesigned, developed, and demonstrated data-driven dashboards, aiming for a better understanding of customer behaviors and consumption patterns to explore business opportunities.\nBuilt and visualized the first interactive dashboard for medical programs to optimize patient stickiness.\n\nKey Accounts Management\nServed as primary data analytic consultant of top 6 key clients; initiated acquisition and retention communications; aligned local stakeholders with the SG regional office.\nPlanned and coordinated the first company webinar of Impact from Covid-19 in the Taiwan healthcare market; served as the Taiwan consultant; collaborated with the regional and local teams to investigate the pandemic impact to the healthcare industry and provide follow-up advice.\n\nAutomation Process\nInnovated ways to streamline business process and improve productivity, reducing 50% manual labor time and cost; developed automated process using Python with SAP data and external data sources."
                  },
                  {
                    "type": "str",
                    "example": "01/04/2016 - 31/08/2018\n\nEvent Planner\nLed 2 teams of 6 students to organize youth camps on a semi-annual basis, including campaign promotion, social media advertising, volunteer's training. Hosted over 10 events.\n\nLife Education Teacher and Mentoring\nDelivered over 50 speeches/lectures in public, reached over 600 audience.\nVolunteered for teaching in 2 schools every week. More than 120 students were benefited and responded over 90% satisfaction.\nProvided one-on-one mentoring to 20+ students and help them succeed in life, relationship, family, performance acceptives."
                  },
                  {
                    "type": "str",
                    "example": "01/12/2013 - 04/02/2016\n\nTaiwan Consultant of Global Reporting Cube Project\nCollaborated with the global team members to reconcile definition differences.\nSupervised India team to re-organize programming flow. Completed UAT within 3 months and conducted follow-on maintenance.\nProvided consultation on Taiwan data warehouse and product profile with the global team.\n\nConsultant of Back-End System for New Product Launch\nBuilt system mapping code per Business request and validated the effectiveness.\nConducted UAT tests and inquiry of ad-hoc reporting.\n\nCampaign Leads Generation and Management\nGenerated over 50+ campaign leads for financial products and tracked the effectiveness of leads.\nConducted customer fulfillment to increase customer loyalty. On average, reach the 95% completion rate of fulfillment.\nAnalyzed customer data, consumption patterns to optimize customer segmentation.\n\nAd-Hoc Requests Organizer\nOrganized and optimized 30+ back-end regular requests and delivered to various departments (ex. compliance, business, branches, anti-money laundry...).\nStreamlined the reporting process through tuning SAS/SQL script and automated reporting process."
                  },
                  {
                    "type": "str",
                    "example": "➤ 與一卡通官方共同打造「潮客 Chicreate」D2C 購物平台，負責平台從 0 到 1 的架構設計：包含物流串接、成本結構、UI/UX、視覺企劃與購物流程優化，並於上線後規劃曝光與 Meta ADs，成功於三個月突破 1000+ 會員數，並達 100+K GMV。\n➤ 作為平台企劃操盤 Kurt Wu 聯名廣告專案，主導內容企劃、文案呈現，並與社群、設計師協作曝光計畫，透過集資方式，成功將預熱人潮在三週內轉化成 600+ 銷售，ROAS 達 3。\n➤ 作為平台企畫與 13+ 組品牌合作進行日常進銷貨，並於季節時提出相關行銷企劃，擴增商品數量至 1,000+。\n➤ 自主使用 ChatGPT + GAS 建立內部工具（如打包工具），簡化資料產出與跨部門協作，提升團隊效率 50%。責"
                  },
                  {
                    "type": "str",
                    "example": "➤ 作為數位行銷專員，透過迭代與內容優化，優化 CRM 數據策略（LINE@ & EDM），提升 GMV 228%、活躍用戶 137%。\n\n➤ 使用 GA4＋Metabse 追蹤消費者購物流程，提升漏斗轉換效率並協助決策。\n\n➤ 推動 Chatbot 與腳本優化，避免游離狀況發生，用以降使用的障礙，成功帶動 UX 改善與活躍使用者成長。低消費者\n\n➤ 負責全站大型活動（如雙 12、Wabay Good Days）整合規劃，協調設計、PM、廣告團隊。"
                  },
                  {
                    "type": "str",
                    "example": "➤優化 eBay 商店 SEO 與廣告策略，提升自然流量 330%、廣告導入 300%。➤實機拍攝並透過 PR 製作 8 支產品介紹與教學影片，支援業務推廣與使用者教育。\n\n➤協調設計與翻譯團隊，製作中英雙語手冊與行銷型錄；負責供應商溝通與預算管理。\n\n➤建立品牌初期官網與社群（WIX + Facebook / Twitter /LinkedIn），導入 SEO 與 GA，規劃內容並追蹤受眾輪廓。\n\n➤撰寫 SOP 手冊與 6 支內部教學影片，協助團隊內部與用戶教育流程。"
                  },
                  {
                    "type": "str",
                    "example": "維護 Data Lake，建置 Data Pipeline，及建立數據產品，包括 : Dashboard、推薦系統、LLM 應用產品\n\n使用 Python、R 和 Airflow 建置易擴展的Data Pipeline\n管理 GCP Data Lake 基礎架構，整合 BigQuery 和 Cloud Storage，提升查詢效能\n與各BU溝通數據需求，開發互動式 Looker Studio Dashboard，支持數據驅動決策\n重構文章推商品推薦系統，加入Search Console 推薦邏輯，提升轉換率 115%\n在 6 個月內建立 2 個 LLM 應用 PoC，使用 Python、LangChain 和 Gemini Pro（Vertex AI）開發文章標題生成 (Flask + Line Chatbot + ngrok)及Email 主旨生成 (Streamlit + Azure DevOps & Cloud Run for CI/CD)，提升行銷效率，供超過 10 位內部行銷人員使用"
                  },
                  {
                    "type": "str",
                    "example": "為公司產品 CDP 的儀表板及標籤系統，開發建置標準化的 Data Pipeline，服務超過15間客戶\n\n使用 Python、Bash 和 SQL 自動化 ETL 處理流程，減少 25% 的數據處理時間\n設計並優化 MySQL 與 MongoDB 的資料模型與結構，提升查詢效能\n建立客製化標籤系統，增強客戶分群和行銷活動的精準度\n與產品團隊密切協作，包括：UIUX、前端/後端、及 PM，確保數據策略與業務目標一致"
                  },
                  {
                    "type": "str",
                    "example": "使用 Oracle Cloud Infrastructure (OCI) 進行售前規劃 (Pre-sales)，專注於雲端數據解決方案，包括 Oracle Autonomous Database、Oracle Analytics Cloud (OAC) 及 Oracle APEX\n\n完成超過5場的簡報及技術 Demo，讓潛在客戶更了解 OCI 數據產品的功能與優勢\n協助設計並執行概念驗證 (PoC)專案，服務客戶包含 BenQ、永豐餘及 Acer 等，達成 60% 的 PoC 轉為完整部署的轉換率\n與銷售團隊和 Oracle 產品團隊合作，客製化解決方案，提升客戶滿意度"
                  },
                  {
                    "type": "str",
                    "example": "協助企業數位轉型，成功將資料從地端資料庫遷移上雲，建立數據中台\n\n透過 SQL、ETL 工具和 Python API，自動化來自 CRM、ERP、網站、LINE、SMS 等超過 10 種資料來源的數據擷取流程，縮短處理時間、提升準確性，每月節省超過 40 小時工時\n優化 Oracle Autonomous Database 的效能，支援 Oracle Analytics Cloud 上的數據儀表板\n為行銷團隊撈取需求名單並製作 BI 報表，透過精準策略提升 15% 的轉換率\n主導 Oracle Cloud Infrastructure (OCI) 上的 SMS 自動化專案，為超過 100 萬名會員發送事件觸發的簡訊，並建立即時儀表板以監控 API 使用量和成本"
                  },
                  {
                    "type": "str",
                    "example": "成功地從零開始替公司建立數位行銷，包括公司網站及各類數位行銷渠道，如 SEM(Google Ads)、SEO、社群網站 (Facebook ads/ LinkedIn ads)、及 B2B 平台 (Alibaba）\n- Google Ads 成果：執行超過80個關鍵字搜尋廣告，CPA 13.89 新加坡幣\n- Facebook Ads 成果：一個月內產生138個轉換，CPA 11.49 新加坡幣\n- SEO 成果：玻璃瓶產品關鍵字在新加坡搜尋排名前五"
                  },
                  {
                    "type": "str",
                    "example": "建立及優化出貨量預測系統\n利用混合模型提高出貨量預測的精確度，種卻率約提高5%\n引入自動化系統以調整模型參數，以優化預測效果\n創建視覺化工具，以協助數據可視化和解釋\n開發自動化系統以進行庫存分配\n與使用者溝通，以制定合適的分配規則\n精簡系統使用，實現一鍵分配的操作方式\n旨在大幅提升使用者效能，並節省人力成本，預估可節省80%的分配時間\n開發圖像文件識別系統\n創建系統，以自動識別紙本商業發票和合約\n實現快速數位化所需文件資訊，並提供客製化設置\n大幅減少文件處理中的人工錯誤\n\nEnhance the Shipment Forecasting System\n\nLeverage Hybrid Models for Enhanced Accuracy\nUtilize hybrid models to increase the accuracy of shipment forecasts, aiming for an approximate 5% improvement.\nImplement an Automated Model Parameter Adjustment System\nIntegrate an automated system for adjusting model parameters to optimize forecasting results.\nDevelop Visual Tools\nCreate visual tools to facilitate data interpretation and decision-making.\nEstablish an Automated Inventory Allocation System\nDefine Allocation Rules through User Communication\nEngage with users to define and establish appropriate allocation rules.\nSimplify System Usage with One-Click Allocation\nStreamline system usage to allow for one-click allocation processes.\nEnhance User Efficiency and Reduce Labor Costs\nAchieve significant efficiency gains, with an estimated 80% reduction in allocated time, leading to substantial labor cost savings.\n\n#Machine Learning #Python #Data Modeling #Github #MySQL #AWS"
                  },
                  {
                    "type": "str",
                    "example": "大規模假貨事件的數據分析\n分析假貨在不同地區的分佈\n研究假貨查詢的時間模式和特徵\n追溯假貨的來源和供應鏈\n估算市場上存在的假貨數量\n特定客戶市場銷售狀況分析\n比較不同年份的銷售情況\n分析銷售區域的分佈和變化\n研究經銷商貨物的流向情況\n假貨鑑定模式的維護與更新\n評估現有模型存在的不足之處\n更新模型的特徵並進行重新建模\n業務數據工具開發\n開發客戶庫存水準和查詢率的記錄表\n建立自動化系統，用於預測假貨銷售曲線\n\nData Analysis of Large-Scale Counterfeit Goods Incidents\n\nAnalyzing the Geographic Distribution of Counterfeit Goods\nExamining the distribution of counterfeit goods across various regions.\nInvestigating Time Patterns and Characteristics in Counterfeit Goods Queries\nExploring the time-related patterns and distinctive features in counterfeit goods queries.\nTracing the Origins and Supply Chain of Counterfeit Goods\nTracing back the sources and supply chain of counterfeit goods.\nEstimating the Quantity of Counterfeit Goods in the Market\nCalculating the approximate quantity of counterfeit goods present in the market\n\nAnalysis of Market Sales Performance for Specific Customers\n\nComparative Analysis of Sales Across Different Years\nEvaluating and comparing sales performance across various years.\nExamination of Sales Region Distribution and Variations\nAnalyzing the distribution and changes in\n\n#Python #MySQL #Tableau #Microsoft Office"
                  },
                  {
                    "type": "str",
                    "example": "資料分析\n分析晶圓生產資料,協助產線進行品質改善(良率平均約提升5%~10%)\n視覺化分析結果並提出改善建議\n系統管理\n管理自動參數調整系統與製程規範管理系統\n協助產品上線與基本系統障礙排除\n協助規劃系統改善\n專案管理\n新產品基礎背景知識了解\n與產線協調進行實驗\n統計模型建立\n與產線協調統計模型驗證工作\n與自動化工程師協調新產品自動化系統上線\n新產品自動化系統上線後持續跟進品質改善狀況\n\nData Analysis\n\nAnalyze wafer production data and assist production lines in quality improvement (The yield rate is increased by about 5% to 10% on average)\nVisually analyze results and make suggestions for improvement\n\nSystem Management\n\nManage automatic parameter adjustment system and process specification management system\nAssist in product launch and troubleshooting of system obstacles\nAssist in planning system improvements\n\nProject Management\n\nBasic background knowledge of new products\nCoordinate with production line for experiments\n\nStatistical model building\n\nCoordinate statistical model validation work with production line\nCoordinate with automation engineers for new product automation system launch\nFollow up on quality improvement after new product automation system launch\n\n#調查樣本統計分析 #提案與簡報技巧 #Quality Control #Matlab #Oracle #R"
                  }
                ]
              },
              "is_current": {
                "oneOf": [
                  {
                    "type": "bool",
                    "example": "True"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "True"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "True"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "True"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  },
                  {
                    "type": "bool",
                    "example": "False"
                  }
                ]
              },
              "duration_in_months": {
                "oneOf": [
                  {
                    "type": "int",
                    "example": "3"
                  },
                  {
                    "type": "int",
                    "example": "16"
                  },
                  {
                    "type": "int",
                    "example": "29"
                  },
                  {
                    "type": "int",
                    "example": "29"
                  },
                  {
                    "type": "int",
                    "example": "27"
                  },
                  {
                    "type": "NoneType",
                    "example": "None"
                  },
                  {
                    "type": "int",
                    "example": "9"
                  },
                  {
                    "type": "int",
                    "example": "10"
                  },
                  {
                    "type": "int",
                    "example": "23"
                  },
                  {
                    "type": "int",
                    "example": "12"
                  },
                  {
                    "type": "int",
                    "example": "4"
                  },
                  {
                    "type": "int",
                    "example": "5"
                  },
                  {
                    "type": "int",
                    "example": "15"
                  },
                  {
                    "type": "int",
                    "example": "19"
                  },
                  {
                    "type": "int",
                    "example": "23"
                  },
                  {
                    "type": "int",
                    "example": "39"
                  }
                ]
              }
            }
          }
        },
        "trainings_and_certifications": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "int",
                    "example": "0"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "ETS (TOEIC / TOEFL)"
                  },
                  "description": {
                    "type": "str",
                    "example": "TOEIC 880 / TOEFL 95"
                  }
                }
              },
              {
                "type": "any"
              },
              {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "int",
                    "example": "2021"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "資策會"
                  },
                  "description": {
                    "type": "str",
                    "example": "BIG DATA 巨量資料分析就業養成班"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "int",
                    "example": "2023"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "AWS"
                  },
                  "description": {
                    "type": "str",
                    "example": "Course : Architecting on AWS 2023/03~2023/03 Architecting on AWS"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "int",
                    "example": "2023"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "AWS"
                  },
                  "description": {
                    "type": "str",
                    "example": "Course : Practical Data Science with Amazon SageMaker 2023/09~2023/09 Practical Data Science with Amazon SageMaker"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "int",
                    "example": "2023"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "AWS"
                  },
                  "description": {
                    "type": "str",
                    "example": "Course : Building Batch Analytics Solutions on AWS 2023/09~2023/09 Building Batch Analytics Solutions on AWS"
                  }
                }
              }
            ]
          }
        },
        "basics": {
          "type": "object",
          "properties": {
            "urls": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "http://www.linkedin.com/in/yunpingkuo"
                  },
                  {
                    "type": "str",
                    "example": "https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=yun-ping-kuo"
                  },
                  {
                    "type": "str",
                    "example": "https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=a9634578"
                  },
                  {
                    "type": "str",
                    "example": "http://www.linkedin.com/in/yuhsuenliu"
                  },
                  {
                    "type": "str",
                    "example": "https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=yu-hsuen-liu"
                  },
                  {
                    "type": "any"
                  }
                ]
              }
            },
            "profession": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "Data Analyst / Business Intelligence Analyst / Business Development"
                },
                {
                  "type": "str",
                  "example": "產品行銷人"
                },
                {
                  "type": "str",
                  "example": "Data Engineer & Analyst"
                },
                {
                  "type": "str",
                  "example": "data scientist"
                }
              ]
            },
            "summary": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "I am an experienced data analyst across financial, healthcare, and logistic industry over 8+ years. A fast learner, self-motivated, and passionate about progress and challenges. Reliable, adaptable, and willing to go the extra mile.\n\n--- Chinese Summary ---\n我擁有六年於金融業及醫療物流產業實務經驗之資料分析師。\n以下是三個與同業相比獨特之專業優勢：\n(1) 豐富跨國溝通協作經歷、英文能力優\n(2) 擁有業務經驗，善於從客戶的角度換位思考並成為客戶與資料工程之間的橋樑\n(3) 豐富簡報經驗，與高階經理人合作經驗。"
                },
                {
                  "type": "str",
                  "example": "我是數據與目標導向的產品行銷人。曾於 4 人團隊，主導從 0 到 1 跨部門、跨公司與UIUX、RD 及外部團隊打造電商平台「潮客 Chicreate」。\n\n我也熟悉 CRM 策略、GA4／Metabase 數據分析、A/B Test，曾透過迭代與內容優化，提升 GMV 228%、使用者活躍率 137%。\n\n我擅長數據分析與策略規劃，將產品價值轉化為具行動力的訊息，有效向市場推動產品，期待能加入開放的產品導向團隊，持續發揮「內容策略 × 數據分析 × 創意發展」的價值。"
                },
                {
                  "type": "str",
                  "example": "✔ 擁有 3 年以上的數據工程與分析經驗，專長建構數據管道與雲端服務\n✔ 有豐富的數據產品開發成果，包含儀表板、推薦系統和LLM 落地應用\n✔ 荷蘭、立陶宛國際溝通雙碩士 + 2年新加坡數位行銷經驗\n✔ 具備高度適應力、跨文化視野及持續學習的精神"
                },
                {
                  "type": "str",
                  "example": "我是一個不像工程師的工程師，比起開發程式/建立模型/數據分析，其實我覺得我更擅長和人溝通與合作，如果能作為一個主管或領導者，或許更能夠發揮出我更多的價值。\n超過五年的工作經驗 能夠獨立作業 更善於團隊合作 擅長溝通合作 具備領導力 良好的適應力 具備資料分析與模型建立的深厚經驗 勇於挑戰\n\n---\n\n專案作品\n\nQuality control system improvement project 2019/01~2019/06\nImport multi-dimensional monitoring methods\nDesign new quality monitoring indicators\nDesign new diagrams and interfaces\n\nprocess improvement plan 2017/01~2019/01\nEvaluate manufacturing quality\nFind key factors that can be improved\nEstablish Run to Run model to assist quality improvement\n\nCounterfeit judgment model improvement plan 2021/01~2021/08\nInformation available from the Exploration Company Database\nFind valuable features\nImprove model structure\n\nImproving shipment forecasting models 2022/03~2022/12\nMixed use of multiple models\nAutomatically update model parameters\nForecast accuracy improved by 5~10%\n\nCourse : Architecting on AWS 2023/03~2023/03 Architecting on AWS\nCourse : Practical Data Science with Amazon SageMaker 2023/09~2023/09 Practical Data Science with Amazon SageMaker\nCourse : Building Batch Analytics Solutions on AWS 2023/09~2023/09 Building Batch Analytics Solutions on AWS\n\nEstablish an automatic inventory allocation system 2023/01~2023/07\nCommunicate assignment terms to users\nBuild user-friendly automated systems\nSave 80% of manual allocation time\n\nCounterfeit Source Tracking Program 2020/08~2020/12\nFake goods distribution analysis\nException query analysis\nSuccessfully obtained source information of counterfeit goods"
                }
              ]
            },
            "gender": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "female"
                },
                {
                  "type": "str",
                  "example": ""
                },
                {
                  "type": "str",
                  "example": "male"
                },
                {
                  "type": "str",
                  "example": "male"
                }
              ]
            },
            "has_driving_license": {
              "oneOf": [
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                }
              ]
            },
            "emails": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "cloudping423@gmail.com"
                  },
                  {
                    "type": "any"
                  },
                  {
                    "type": "str",
                    "example": "peter19930419@gmail.com"
                  },
                  {
                    "type": "str",
                    "example": "example@example.com"
                  }
                ]
              }
            },
            "first_name": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "Yun-Ping (Rhea)"
                },
                {
                  "type": "str",
                  "example": "琨育"
                },
                {
                  "type": "str",
                  "example": "Yu Hsuen"
                },
                {
                  "type": "str",
                  "example": "俊詠"
                }
              ]
            },
            "last_name": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "Kuo (郭)"
                },
                {
                  "type": "str",
                  "example": "邱"
                },
                {
                  "type": "str",
                  "example": "Liu"
                },
                {
                  "type": "str",
                  "example": "陳"
                }
              ]
            },
            "phone_numbers": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "+886-961-016-034"
                  },
                  {
                    "type": "any"
                  },
                  {
                    "type": "str",
                    "example": "0955136095"
                  },
                  {
                    "type": "any"
                  }
                ]
              }
            },
            "skills": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "SQL"
                  },
                  {
                    "type": "str",
                    "example": "Python"
                  },
                  {
                    "type": "str",
                    "example": "SAS"
                  },
                  {
                    "type": "str",
                    "example": "SPSS"
                  },
                  {
                    "type": "str",
                    "example": "Tableau"
                  },
                  {
                    "type": "str",
                    "example": "Teradata"
                  },
                  {
                    "type": "str",
                    "example": "SAP HANA"
                  },
                  {
                    "type": "str",
                    "example": "Microsoft Excel (Pivot)"
                  },
                  {
                    "type": "str",
                    "example": "PowerPoint"
                  },
                  {
                    "type": "str",
                    "example": "Word"
                  },
                  {
                    "type": "str",
                    "example": "Project Management"
                  },
                  {
                    "type": "str",
                    "example": "Communication"
                  },
                  {
                    "type": "str",
                    "example": "Cross-team collaboration"
                  },
                  {
                    "type": "str",
                    "example": "Solution selling"
                  },
                  {
                    "type": "str",
                    "example": "Presentation"
                  },
                  {
                    "type": "str",
                    "example": "Agile work style"
                  },
                  {
                    "type": "str",
                    "example": "數據分析"
                  },
                  {
                    "type": "str",
                    "example": "CRM 策略"
                  },
                  {
                    "type": "str",
                    "example": "GA4"
                  },
                  {
                    "type": "str",
                    "example": "Metabase"
                  },
                  {
                    "type": "str",
                    "example": "A/B Test"
                  },
                  {
                    "type": "str",
                    "example": "ChatGPT"
                  },
                  {
                    "type": "str",
                    "example": "Google Apps Script"
                  },
                  {
                    "type": "str",
                    "example": "SEO"
                  },
                  {
                    "type": "str",
                    "example": "廣告企劃"
                  },
                  {
                    "type": "str",
                    "example": "UX 優化"
                  },
                  {
                    "type": "str",
                    "example": "Python"
                  },
                  {
                    "type": "str",
                    "example": "SQL"
                  },
                  {
                    "type": "str",
                    "example": "R"
                  },
                  {
                    "type": "str",
                    "example": "Airflow"
                  },
                  {
                    "type": "str",
                    "example": "Docker"
                  },
                  {
                    "type": "str",
                    "example": "Linux"
                  },
                  {
                    "type": "str",
                    "example": "MySQL"
                  },
                  {
                    "type": "str",
                    "example": "Oracle"
                  },
                  {
                    "type": "str",
                    "example": "MongoDB"
                  },
                  {
                    "type": "str",
                    "example": "Looker Studio"
                  },
                  {
                    "type": "str",
                    "example": "BigQuery"
                  },
                  {
                    "type": "str",
                    "example": "Cloud Storage"
                  },
                  {
                    "type": "str",
                    "example": "Cloud Run"
                  },
                  {
                    "type": "str",
                    "example": "LangChain"
                  },
                  {
                    "type": "str",
                    "example": "Vertex AI"
                  },
                  {
                    "type": "str",
                    "example": "Machine Learning & Deep Learning Applications"
                  },
                  {
                    "type": "str",
                    "example": "Mathematical and Statistical Model Applications"
                  },
                  {
                    "type": "str",
                    "example": "Office software applications and project management"
                  },
                  {
                    "type": "str",
                    "example": "Python"
                  },
                  {
                    "type": "str",
                    "example": "MySQL"
                  },
                  {
                    "type": "str",
                    "example": "Tableau"
                  },
                  {
                    "type": "str",
                    "example": "Microsoft Office"
                  },
                  {
                    "type": "str",
                    "example": "Matlab"
                  },
                  {
                    "type": "str",
                    "example": "Oracle"
                  },
                  {
                    "type": "str",
                    "example": "R"
                  },
                  {
                    "type": "str",
                    "example": "Github"
                  },
                  {
                    "type": "str",
                    "example": "AWS"
                  }
                ]
              }
            },
            "date_of_birth": {
              "type": "object",
              "properties": {
                "month": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "0"
                    },
                    {
                      "type": "int",
                      "example": "4"
                    },
                    {
                      "type": "int",
                      "example": "0"
                    }
                  ]
                },
                "day": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "0"
                    },
                    {
                      "type": "int",
                      "example": "19"
                    },
                    {
                      "type": "int",
                      "example": "0"
                    }
                  ]
                },
                "year": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "0"
                    },
                    {
                      "type": "int",
                      "example": "1993"
                    },
                    {
                      "type": "int",
                      "example": "0"
                    }
                  ]
                }
              }
            },
            "address": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "6F., No. 8-8, Jieyun Rd., Zhonghe Dist., New Taipei City, Taiwan"
                },
                {
                  "type": "str",
                  "example": "Taipei City, Taiwan"
                },
                {
                  "type": "str",
                  "example": "新北市, 台灣"
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "total_experience_in_years": {
              "oneOf": [
                {
                  "type": "int",
                  "example": "8"
                },
                {
                  "type": "int",
                  "example": "3"
                },
                {
                  "type": "int",
                  "example": "4"
                },
                {
                  "type": "int",
                  "example": "6"
                }
              ]
            }
          }
        }
      }
    },
    "location": {
      "type": "str",
      "example": "University of Minnesota"
    },
    "name": {
      "type": "str",
      "example": "張為淳"
    },
    "about_english": {
      "type": "str",
      "example": "I love telling insightful stories behind data! With a strong academic background in Statistics and Data Science, my proficiency spans Statistical Analysis and Modeling, Machine Learning, Predictive Analytics, Exploratory Data Analysis, and Data Visualization. Graduating from MS Business Analytics at UMN Carlson, I’m focusing on applying advanced data analytics techniques to address complex business problems, bringing innovation and impact to my future role!"
    },
    "skills": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "str",
            "example": "數據科學"
          },
          {
            "type": "str",
            "example": "數據分析"
          },
          {
            "type": "str",
            "example": "團隊合作"
          },
          {
            "type": "str",
            "example": "創意思考"
          },
          {
            "type": "str",
            "example": "勇於挑戰"
          }
        ]
      }
    },
    "links_text": {
      "type": "str",
      "example": "GitHuband LinkedIn (Note: The specific URLs were not directly available as distinct links in the page snapshot text.)"
    },
    "techniques": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "str",
            "example": "統計推論與建模 (Statistical Inference and Modeling)"
          },
          {
            "type": "str",
            "example": "機器學習 (Machine Learning)"
          },
          {
            "type": "str",
            "example": "預測分析 (Predictive Analytics)"
          },
          {
            "type": "str",
            "example": "探索性資料分析 (Exploratory Data Analysis, EDA)"
          },
          {
            "type": "str",
            "example": "資料視覺化 (Data Visualization)"
          }
        ]
      }
    },
    "work_experience": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "role": {
                "type": "str",
                "example": "Data Science Consultant"
              },
              "company": {
                "type": "str",
                "example": "Carlson Analytics Lab"
              },
              "duration": {
                "type": "str",
                "example": "2024/01~2024/04"
              },
              "details": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "Conducted time series analysis in ARIMA model with Python and SQL in BigQuery on 400K+ e-commerce data, visualizing in Looker in Google Cloud Platform (GCP) for inventory analysis. Project link (Note: The specific URL was not directly available as a distinct link in the page snapshot text.)"
                    },
                    {
                      "type": "str",
                      "example": "Conducted statistical analysis and data engineering with Python, PySpark, and Spark SQL in Azure Databricks on 80K+ airline data and visualized flight inefficiency in Power BI, reducing processing time by 30%"
                    },
                    {
                      "type": "str",
                      "example": "Defined metrics and conducted logistic regression with Python"
                    }
                  ]
                }
              },
              "tags": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "#機器學習 (Machine Learning)"
                    },
                    {
                      "type": "str",
                      "example": "#深度學習 (Deep Learning)"
                    },
                    {
                      "type": "str",
                      "example": "#強化學習 (Reinforcement Learning)"
                    },
                    {
                      "type": "str",
                      "example": "#統計分析 (Statistical Analysis)"
                    },
                    {
                      "type": "str",
                      "example": "#預測建模 (Predictive Modeling)"
                    },
                    {
                      "type": "str",
                      "example": "#大數據 (Big Data)"
                    }
                  ]
                }
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "role": {
                "type": "str",
                "example": "Data Analytics Consultant"
              },
              "company": {
                "type": "str",
                "example": "Carlson Analytics Lab"
              },
              "duration": {
                "type": "str",
                "example": "2023/07~2024/01"
              },
              "details": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "Conducted statistical hypothesis testing and Principal Component Analysis (PCA) in R on household saving dataset across eight years, using Analysis of Variance (ANOVA) to determine model with better interpretability"
                    },
                    {
                      "type": "str",
                      "example": "Conducted hierarchical clustering analysis in R to identify underlying customer segmentation on wholesale company data, visualizing cluster features in Principal Component Analysis plot to clarify customer attributes"
                    },
                    {
                      "type": "str",
                      "example": "Achieved 97% accuracy in detecting spam emails using Support Vector Machine (SVM) with Python scikit-learn, performing nested cross-validation to select optimized model for future prediction"
                    },
                    {
                      "type": "str",
                      "example": "Conducted sentiment analysis in Natural Language Processing (NLP) by web-crawling 3K+ editorial articles using Python Beautiful Soup, training model with Word2Vec to generate polarity and subjectivity scores"
                    }
                  ]
                }
              },
              "tags": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "#資料建模 (Data Modeling)"
                    },
                    {
                      "type": "str",
                      "example": "#資料分析 (Data Analytics)"
                    },
                    {
                      "type": "str",
                      "example": "#統計分析 (Statistical Analysis)"
                    },
                    {
                      "type": "str",
                      "example": "#特徵工程 (Feature Engineering)"
                    },
                    {
                      "type": "str",
                      "example": "#統計推論 (Statistical Inference)"
                    },
                    {
                      "type": "str",
                      "example": "#探索性資料分析 (Exploratory Data Analysis)"
                    }
                  ]
                }
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "role": {
                "type": "str",
                "example": "資料分析師 (Data Analyst)"
              },
              "company": {
                "type": "str",
                "example": "SonicBalloon (清華創新育成中心及創業車庫團隊)"
              },
              "duration": {
                "type": "str",
                "example": "2021/07~2022/07"
              },
              "details": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "Spearheaded quantitative analysis and qualitative analysis to identify main competitors, visualizing market values of medical device over six years in Tableau and enhancing market share estimation for the next five years"
                    },
                    {
                      "type": "str",
                      "example": "Presented year-over-year device usage volume across eight years in the U.S. using PivotTable in Microsoft Excel to enhance market value estimation, showcasing product potential and securing startup sponsorship"
                    },
                    {
                      "type": "str",
                      "example": "Increasing teamwork efficiency by 20% through managing stakeholder expectations and providing business insights to foster collaboration and communication between the internal technical team and external consultants"
                    },
                    {
                      "type": "str",
                      "example": "Oversaw weekly meetings by orchestrating information integration and driving goal-oriented collaboration"
                    }
                  ]
                }
              },
              "tags": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "#Excel"
                    },
                    {
                      "type": "str",
                      "example": "#PowerPoint"
                    },
                    {
                      "type": "str",
                      "example": "#數據分析"
                    },
                    {
                      "type": "str",
                      "example": "#市場調查資料分析與報告撰寫"
                    },
                    {
                      "type": "str",
                      "example": "#統計分析"
                    },
                    {
                      "type": "str",
                      "example": "#領導能力"
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    }
  }
}
```

### Sample-specific Schemas

#### ds_sample1.json

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "type": "object",
      "properties": {
        "basics": {
          "type": "object",
          "properties": {
            "first_name": {
              "type": "str",
              "example": "Yun-Ping (Rhea)"
            },
            "last_name": {
              "type": "str",
              "example": "Kuo (郭)"
            },
            "gender": {
              "type": "str",
              "example": "female"
            },
            "emails": {
              "type": "array",
              "items": {
                "type": "str",
                "example": "cloudping423@gmail.com"
              }
            },
            "urls": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "http://www.linkedin.com/in/yunpingkuo"
                  },
                  {
                    "type": "str",
                    "example": "https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=yun-ping-kuo"
                  }
                ]
              }
            },
            "phone_numbers": {
              "type": "array",
              "items": {
                "type": "str",
                "example": "+886-961-016-034"
              }
            },
            "date_of_birth": {
              "type": "object",
              "properties": {
                "year": {
                  "type": "int",
                  "example": "0"
                },
                "month": {
                  "type": "int",
                  "example": "0"
                },
                "day": {
                  "type": "int",
                  "example": "0"
                }
              }
            },
            "address": {
              "type": "str",
              "example": "6F., No. 8-8, Jieyun Rd., Zhonghe Dist., New Taipei City, Taiwan"
            },
            "total_experience_in_years": {
              "type": "int",
              "example": "8"
            },
            "profession": {
              "type": "str",
              "example": "Data Analyst / Business Intelligence Analyst / Business Development"
            },
            "summary": {
              "type": "str",
              "example": "I am an experienced data analyst across financial, healthcare, and logistic industry over 8+ years. A fast learner, self-motivated, and passionate about progress and challenges. Reliable, adaptable, and willing to go the extra mile.\n\n--- Chinese Summary ---\n我擁有六年於金融業及醫療物流產業實務經驗之資料分析師。\n以下是三個與同業相比獨特之專業優勢：\n(1) 豐富跨國溝通協作經歷、英文能力優\n(2) 擁有業務經驗，善於從客戶的角度換位思考並成為客戶與資料工程之間的橋樑\n(3) 豐富簡報經驗，與高階經理人合作經驗。"
            },
            "skills": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "SQL"
                  },
                  {
                    "type": "str",
                    "example": "Python"
                  },
                  {
                    "type": "str",
                    "example": "SAS"
                  },
                  {
                    "type": "str",
                    "example": "SPSS"
                  },
                  {
                    "type": "str",
                    "example": "Tableau"
                  },
                  {
                    "type": "str",
                    "example": "Teradata"
                  },
                  {
                    "type": "str",
                    "example": "SAP HANA"
                  },
                  {
                    "type": "str",
                    "example": "Microsoft Excel (Pivot)"
                  },
                  {
                    "type": "str",
                    "example": "PowerPoint"
                  },
                  {
                    "type": "str",
                    "example": "Word"
                  },
                  {
                    "type": "str",
                    "example": "Project Management"
                  },
                  {
                    "type": "str",
                    "example": "Communication"
                  },
                  {
                    "type": "str",
                    "example": "Cross-team collaboration"
                  },
                  {
                    "type": "str",
                    "example": "Solution selling"
                  },
                  {
                    "type": "str",
                    "example": "Presentation"
                  },
                  {
                    "type": "str",
                    "example": "Agile work style"
                  }
                ]
              }
            },
            "has_driving_license": {
              "type": "bool",
              "example": "False"
            }
          }
        },
        "languages": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "Chinese"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "zh"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "5"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "English"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "en"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "4"
                  }
                }
              }
            ]
          }
        },
        "educations": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2012"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2013"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "Tilburg University"
                  },
                  "description": {
                    "type": "str",
                    "example": "Master of Science | Econometrics and Mathematical Economics | Tilburg City, the Netherlands (Sep 2012 - Aug 2013)"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2007"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2012"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "National Taipei University"
                  },
                  "description": {
                    "type": "str",
                    "example": "Bachelor | Department of Statistics | New Taipei City, Taiwan (Sep 2007 - Jan 2012)"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2009"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2010"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "University of Innsbruck (Austria) SOWI"
                  },
                  "description": {
                    "type": "str",
                    "example": "One-year exchange student | 2009/09 - 2010/09"
                  }
                }
              }
            ]
          }
        },
        "trainings_and_certifications": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "year": {
                "type": "int",
                "example": "0"
              },
              "issuing_organization": {
                "type": "str",
                "example": "ETS (TOEIC / TOEFL)"
              },
              "description": {
                "type": "str",
                "example": "TOEIC 880 / TOEFL 95"
              }
            }
          }
        },
        "professional_experiences": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2023"
                      },
                      "month": {
                        "type": "int",
                        "example": "1"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "True"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "0"
                      },
                      "month": {
                        "type": "int",
                        "example": "0"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "3"
                  },
                  "company": {
                    "type": "str",
                    "example": "Morrison Express"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "Data Analyst, Assistant Manager"
                  },
                  "description": {
                    "type": "str",
                    "example": "02/01/2023 - present\n\nProject Management / Product Leadership: Spearhead the development of MUSE, an internal reporting product delivering up-to-date financial, sales and operational performance insights through interactive dashboards using agile approach.\n\nStrategic Data Architecture: Design and implement new ETL flows leveraging LakeHouse structure to establish a Single Source Of Truth with prioritized report features, improving data accuracy by 12%.\n\nComplex Data Management: Oversee the migration of 6+ million records and integration of 400+ business logics, ensuring seamless transitions with minimal disruption to business operations.\n\nCross-functional Collaboration: Act as a bridge between end users (20+ across F&A/Sales/Product/Operation) and product team (Data/EA/BI).\n\nOperational Efficiency: Establish process flows and implemented user request platform via Jira Service Management tool, cutting BI admin workload by 70%. Establish centralized platform, boosting BI report efficiency by 60%."
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2021"
                      },
                      "month": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "12"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "16"
                  },
                  "company": {
                    "type": "str",
                    "example": "Zuellig Pharma Digital and Data"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "Assistant Manager"
                  },
                  "description": {
                    "type": "str",
                    "example": "01/08/2021 - 31/12/2022\n\nBusiness Development\nStrengthened key account monitor mechanism and proactively collaborated with regional stakeholders to achieve country target at 129% and increased subscribed project number by 132%.\nRedesigned pricing scheme for TW country, increased annual subscription price by 9% and prolonged clients' subscription period by 160%.\n\nData Analytics\nCustomer end-to-end support, from data visualization product all hands to new solution selling.\nConducted sales analysis and presented to valued clients, successfully increased the awareness of company's data capability among the industry and strengthened client engagement.\nDeveloped commercial indicator and visualize business metrics to monitor country growth, generated monthly management report for C-level and higher management team for strategic decision support."
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2019"
                      },
                      "month": {
                        "type": "int",
                        "example": "2"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2021"
                      },
                      "month": {
                        "type": "int",
                        "example": "7"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "29"
                  },
                  "company": {
                    "type": "str",
                    "example": "Zuellig Pharma Digital and Data"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "Data Analytic Specialist"
                  },
                  "description": {
                    "type": "str",
                    "example": "25/02/2019 - 01/08/2021\n\nCustomer Insight Analysis\nDesigned, developed, and demonstrated data-driven dashboards, aiming for a better understanding of customer behaviors and consumption patterns to explore business opportunities.\nBuilt and visualized the first interactive dashboard for medical programs to optimize patient stickiness.\n\nKey Accounts Management\nServed as primary data analytic consultant of top 6 key clients; initiated acquisition and retention communications; aligned local stakeholders with the SG regional office.\nPlanned and coordinated the first company webinar of Impact from Covid-19 in the Taiwan healthcare market; served as the Taiwan consultant; collaborated with the regional and local teams to investigate the pandemic impact to the healthcare industry and provide follow-up advice.\n\nAutomation Process\nInnovated ways to streamline business process and improve productivity, reducing 50% manual labor time and cost; developed automated process using Python with SAP data and external data sources."
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2016"
                      },
                      "month": {
                        "type": "int",
                        "example": "4"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2018"
                      },
                      "month": {
                        "type": "int",
                        "example": "9"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "29"
                  },
                  "company": {
                    "type": "str",
                    "example": "Yong-He Church NPO"
                  },
                  "location": {
                    "type": "str",
                    "example": "New Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "Event Planning and Coordinator"
                  },
                  "description": {
                    "type": "str",
                    "example": "01/04/2016 - 31/08/2018\n\nEvent Planner\nLed 2 teams of 6 students to organize youth camps on a semi-annual basis, including campaign promotion, social media advertising, volunteer's training. Hosted over 10 events.\n\nLife Education Teacher and Mentoring\nDelivered over 50 speeches/lectures in public, reached over 600 audience.\nVolunteered for teaching in 2 schools every week. More than 120 students were benefited and responded over 90% satisfaction.\nProvided one-on-one mentoring to 20+ students and help them succeed in life, relationship, family, performance acceptives."
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2013"
                      },
                      "month": {
                        "type": "int",
                        "example": "12"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2016"
                      },
                      "month": {
                        "type": "int",
                        "example": "3"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "27"
                  },
                  "company": {
                    "type": "str",
                    "example": "CitiBank"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "Business Analysis"
                  },
                  "description": {
                    "type": "str",
                    "example": "01/12/2013 - 04/02/2016\n\nTaiwan Consultant of Global Reporting Cube Project\nCollaborated with the global team members to reconcile definition differences.\nSupervised India team to re-organize programming flow. Completed UAT within 3 months and conducted follow-on maintenance.\nProvided consultation on Taiwan data warehouse and product profile with the global team.\n\nConsultant of Back-End System for New Product Launch\nBuilt system mapping code per Business request and validated the effectiveness.\nConducted UAT tests and inquiry of ad-hoc reporting.\n\nCampaign Leads Generation and Management\nGenerated over 50+ campaign leads for financial products and tracked the effectiveness of leads.\nConducted customer fulfillment to increase customer loyalty. On average, reach the 95% completion rate of fulfillment.\nAnalyzed customer data, consumption patterns to optimize customer segmentation.\n\nAd-Hoc Requests Organizer\nOrganized and optimized 30+ back-end regular requests and delivered to various departments (ex. compliance, business, branches, anti-money laundry...).\nStreamlined the reporting process through tuning SAS/SQL script and automated reporting process."
                  }
                }
              }
            ]
          }
        },
        "awards": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "references": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

#### ds_sample5.json

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "type": "object",
      "properties": {
        "basics": {
          "type": "object",
          "properties": {
            "first_name": {
              "type": "str",
              "example": "琨育"
            },
            "last_name": {
              "type": "str",
              "example": "邱"
            },
            "gender": {
              "type": "str",
              "example": ""
            },
            "emails": {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            "urls": {
              "type": "array",
              "items": {
                "type": "str",
                "example": "https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=a9634578"
              }
            },
            "phone_numbers": {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            "date_of_birth": {
              "type": "object",
              "properties": {}
            },
            "address": {
              "type": "str",
              "example": "Taipei City, Taiwan"
            },
            "total_experience_in_years": {
              "type": "int",
              "example": "3"
            },
            "profession": {
              "type": "str",
              "example": "產品行銷人"
            },
            "summary": {
              "type": "str",
              "example": "我是數據與目標導向的產品行銷人。曾於 4 人團隊，主導從 0 到 1 跨部門、跨公司與UIUX、RD 及外部團隊打造電商平台「潮客 Chicreate」。\n\n我也熟悉 CRM 策略、GA4／Metabase 數據分析、A/B Test，曾透過迭代與內容優化，提升 GMV 228%、使用者活躍率 137%。\n\n我擅長數據分析與策略規劃，將產品價值轉化為具行動力的訊息，有效向市場推動產品，期待能加入開放的產品導向團隊，持續發揮「內容策略 × 數據分析 × 創意發展」的價值。"
            },
            "skills": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "數據分析"
                  },
                  {
                    "type": "str",
                    "example": "CRM 策略"
                  },
                  {
                    "type": "str",
                    "example": "GA4"
                  },
                  {
                    "type": "str",
                    "example": "Metabase"
                  },
                  {
                    "type": "str",
                    "example": "A/B Test"
                  },
                  {
                    "type": "str",
                    "example": "ChatGPT"
                  },
                  {
                    "type": "str",
                    "example": "Google Apps Script"
                  },
                  {
                    "type": "str",
                    "example": "SEO"
                  },
                  {
                    "type": "str",
                    "example": "廣告企劃"
                  },
                  {
                    "type": "str",
                    "example": "UX 優化"
                  }
                ]
              }
            },
            "has_driving_license": {
              "type": "bool",
              "example": "False"
            }
          }
        },
        "languages": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "educations": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "trainings_and_certifications": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "professional_experiences": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2024"
                      },
                      "month": {
                        "type": "int",
                        "example": "2"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "True"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {}
                  },
                  "duration_in_months": {
                    "type": "NoneType",
                    "example": "None"
                  },
                  "company": {
                    "type": "str",
                    "example": "SUPERMEDIA 超人氣新媒體股份有限公司"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "Project Manager"
                  },
                  "description": {
                    "type": "str",
                    "example": "➤ 與一卡通官方共同打造「潮客 Chicreate」D2C 購物平台，負責平台從 0 到 1 的架構設計：包含物流串接、成本結構、UI/UX、視覺企劃與購物流程優化，並於上線後規劃曝光與 Meta ADs，成功於三個月突破 1000+ 會員數，並達 100+K GMV。\n➤ 作為平台企劃操盤 Kurt Wu 聯名廣告專案，主導內容企劃、文案呈現，並與社群、設計師協作曝光計畫，透過集資方式，成功將預熱人潮在三週內轉化成 600+ 銷售，ROAS 達 3。\n➤ 作為平台企畫與 13+ 組品牌合作進行日常進銷貨，並於季節時提出相關行銷企劃，擴增商品數量至 1,000+。\n➤ 自主使用 ChatGPT + GAS 建立內部工具（如打包工具），簡化資料產出與跨部門協作，提升團隊效率 50%。責"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2023"
                      },
                      "month": {
                        "type": "int",
                        "example": "6"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2024"
                      },
                      "month": {
                        "type": "int",
                        "example": "2"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "9"
                  },
                  "company": {
                    "type": "str",
                    "example": "貝殼放大 Backer-Founder"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "Digital Marketing Specialist"
                  },
                  "description": {
                    "type": "str",
                    "example": "➤ 作為數位行銷專員，透過迭代與內容優化，優化 CRM 數據策略（LINE@ & EDM），提升 GMV 228%、活躍用戶 137%。\n\n➤ 使用 GA4＋Metabse 追蹤消費者購物流程，提升漏斗轉換效率並協助決策。\n\n➤ 推動 Chatbot 與腳本優化，避免游離狀況發生，用以降使用的障礙，成功帶動 UX 改善與活躍使用者成長。低消費者\n\n➤ 負責全站大型活動（如雙 12、Wabay Good Days）整合規劃，協調設計、PM、廣告團隊。"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "3"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "12"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "10"
                  },
                  "company": {
                    "type": "str",
                    "example": "羅傑斯人工智能股份有限公司"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "市場行銷實習生"
                  },
                  "description": {
                    "type": "str",
                    "example": "➤優化 eBay 商店 SEO 與廣告策略，提升自然流量 330%、廣告導入 300%。➤實機拍攝並透過 PR 製作 8 支產品介紹與教學影片，支援業務推廣與使用者教育。\n\n➤協調設計與翻譯團隊，製作中英雙語手冊與行銷型錄；負責供應商溝通與預算管理。\n\n➤建立品牌初期官網與社群（WIX + Facebook / Twitter /LinkedIn），導入 SEO 與 GA，規劃內容並追蹤受眾輪廓。\n\n➤撰寫 SOP 手冊與 6 支內部教學影片，協助團隊內部與用戶教育流程。"
                  }
                }
              }
            ]
          }
        },
        "awards": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "references": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

#### ds_sample4.json

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "type": "object",
      "properties": {
        "basics": {
          "type": "object",
          "properties": {
            "first_name": {
              "type": "str",
              "example": "Yu Hsuen"
            },
            "last_name": {
              "type": "str",
              "example": "Liu"
            },
            "gender": {
              "type": "str",
              "example": "male"
            },
            "emails": {
              "type": "array",
              "items": {
                "type": "str",
                "example": "peter19930419@gmail.com"
              }
            },
            "urls": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "http://www.linkedin.com/in/yuhsuenliu"
                  },
                  {
                    "type": "str",
                    "example": "https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=yu-hsuen-liu"
                  }
                ]
              }
            },
            "phone_numbers": {
              "type": "array",
              "items": {
                "type": "str",
                "example": "0955136095"
              }
            },
            "date_of_birth": {
              "type": "object",
              "properties": {
                "year": {
                  "type": "int",
                  "example": "1993"
                },
                "month": {
                  "type": "int",
                  "example": "4"
                },
                "day": {
                  "type": "int",
                  "example": "19"
                }
              }
            },
            "address": {
              "type": "str",
              "example": "新北市, 台灣"
            },
            "total_experience_in_years": {
              "type": "int",
              "example": "4"
            },
            "profession": {
              "type": "str",
              "example": "Data Engineer & Analyst"
            },
            "summary": {
              "type": "str",
              "example": "✔ 擁有 3 年以上的數據工程與分析經驗，專長建構數據管道與雲端服務\n✔ 有豐富的數據產品開發成果，包含儀表板、推薦系統和LLM 落地應用\n✔ 荷蘭、立陶宛國際溝通雙碩士 + 2年新加坡數位行銷經驗\n✔ 具備高度適應力、跨文化視野及持續學習的精神"
            },
            "skills": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "Python"
                  },
                  {
                    "type": "str",
                    "example": "SQL"
                  },
                  {
                    "type": "str",
                    "example": "R"
                  },
                  {
                    "type": "str",
                    "example": "Airflow"
                  },
                  {
                    "type": "str",
                    "example": "Docker"
                  },
                  {
                    "type": "str",
                    "example": "Linux"
                  },
                  {
                    "type": "str",
                    "example": "MySQL"
                  },
                  {
                    "type": "str",
                    "example": "Oracle"
                  },
                  {
                    "type": "str",
                    "example": "MongoDB"
                  },
                  {
                    "type": "str",
                    "example": "Looker Studio"
                  },
                  {
                    "type": "str",
                    "example": "BigQuery"
                  },
                  {
                    "type": "str",
                    "example": "Cloud Storage"
                  },
                  {
                    "type": "str",
                    "example": "Cloud Run"
                  },
                  {
                    "type": "str",
                    "example": "LangChain"
                  },
                  {
                    "type": "str",
                    "example": "Vertex AI"
                  }
                ]
              }
            },
            "has_driving_license": {
              "type": "bool",
              "example": "False"
            }
          }
        },
        "languages": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "Chinese"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "zh"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "5"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "English"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "en"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "4"
                  }
                }
              }
            ]
          }
        },
        "educations": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2018"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2020"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "Hanze University of Applied Sciences / Vilnius University"
                  },
                  "description": {
                    "type": "str",
                    "example": "雙聯碩士 - 國際溝通碩士學程"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2011"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2015"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "Tamkang University"
                  },
                  "description": {
                    "type": "str",
                    "example": "英文系學士"
                  }
                }
              }
            ]
          }
        },
        "trainings_and_certifications": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "year": {
                "type": "int",
                "example": "2021"
              },
              "issuing_organization": {
                "type": "str",
                "example": "資策會"
              },
              "description": {
                "type": "str",
                "example": "BIG DATA 巨量資料分析就業養成班"
              }
            }
          }
        },
        "professional_experiences": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2023"
                      },
                      "month": {
                        "type": "int",
                        "example": "6"
                      }
                    }
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2025"
                      },
                      "month": {
                        "type": "int",
                        "example": "5"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "True"
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "23"
                  },
                  "company": {
                    "type": "str",
                    "example": "CommonWealth Magazine 天下雜誌"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "數據分析師"
                  },
                  "description": {
                    "type": "str",
                    "example": "維護 Data Lake，建置 Data Pipeline，及建立數據產品，包括 : Dashboard、推薦系統、LLM 應用產品\n\n使用 Python、R 和 Airflow 建置易擴展的Data Pipeline\n管理 GCP Data Lake 基礎架構，整合 BigQuery 和 Cloud Storage，提升查詢效能\n與各BU溝通數據需求，開發互動式 Looker Studio Dashboard，支持數據驅動決策\n重構文章推商品推薦系統，加入Search Console 推薦邏輯，提升轉換率 115%\n在 6 個月內建立 2 個 LLM 應用 PoC，使用 Python、LangChain 和 Gemini Pro（Vertex AI）開發文章標題生成 (Flask + Line Chatbot + ngrok)及Email 主旨生成 (Streamlit + Azure DevOps & Cloud Run for CI/CD)，提升行銷效率，供超過 10 位內部行銷人員使用"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "7"
                      }
                    }
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2023"
                      },
                      "month": {
                        "type": "int",
                        "example": "6"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "12"
                  },
                  "company": {
                    "type": "str",
                    "example": "AccuHit 愛酷智能科技"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "資料工程師"
                  },
                  "description": {
                    "type": "str",
                    "example": "為公司產品 CDP 的儀表板及標籤系統，開發建置標準化的 Data Pipeline，服務超過15間客戶\n\n使用 Python、Bash 和 SQL 自動化 ETL 處理流程，減少 25% 的數據處理時間\n設計並優化 MySQL 與 MongoDB 的資料模型與結構，提升查詢效能\n建立客製化標籤系統，增強客戶分群和行銷活動的精準度\n與產品團隊密切協作，包括：UIUX、前端/後端、及 PM，確保數據策略與業務目標一致"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "4"
                      }
                    }
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "7"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "4"
                  },
                  "company": {
                    "type": "str",
                    "example": "Dynasafe 動力安全資訊"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "雲端解決方案工程師"
                  },
                  "description": {
                    "type": "str",
                    "example": "使用 Oracle Cloud Infrastructure (OCI) 進行售前規劃 (Pre-sales)，專注於雲端數據解決方案，包括 Oracle Autonomous Database、Oracle Analytics Cloud (OAC) 及 Oracle APEX\n\n完成超過5場的簡報及技術 Demo，讓潛在客戶更了解 OCI 數據產品的功能與優勢\n協助設計並執行概念驗證 (PoC)專案，服務客戶包含 BenQ、永豐餘及 Acer 等，達成 60% 的 PoC 轉為完整部署的轉換率\n與銷售團隊和 Oracle 產品團隊合作，客製化解決方案，提升客戶滿意度"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2021"
                      },
                      "month": {
                        "type": "int",
                        "example": "11"
                      }
                    }
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "3"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "5"
                  },
                  "company": {
                    "type": "str",
                    "example": "DV Biomed 麗彤生醫"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taipei, Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "數據工程師"
                  },
                  "description": {
                    "type": "str",
                    "example": "協助企業數位轉型，成功將資料從地端資料庫遷移上雲，建立數據中台\n\n透過 SQL、ETL 工具和 Python API，自動化來自 CRM、ERP、網站、LINE、SMS 等超過 10 種資料來源的數據擷取流程，縮短處理時間、提升準確性，每月節省超過 40 小時工時\n優化 Oracle Autonomous Database 的效能，支援 Oracle Analytics Cloud 上的數據儀表板\n為行銷團隊撈取需求名單並製作 BI 報表，透過精準策略提升 15% 的轉換率\n主導 Oracle Cloud Infrastructure (OCI) 上的 SMS 自動化專案，為超過 100 萬名會員發送事件觸發的簡訊，並建立即時儀表板以監控 API 使用量和成本"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2020"
                      },
                      "month": {
                        "type": "int",
                        "example": "3"
                      }
                    }
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2021"
                      },
                      "month": {
                        "type": "int",
                        "example": "5"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "15"
                  },
                  "company": {
                    "type": "str",
                    "example": "Interwaters Pte. Ltd"
                  },
                  "location": {
                    "type": "str",
                    "example": "Singapore"
                  },
                  "title": {
                    "type": "str",
                    "example": "數位行銷企劃專員"
                  },
                  "description": {
                    "type": "str",
                    "example": "成功地從零開始替公司建立數位行銷，包括公司網站及各類數位行銷渠道，如 SEM(Google Ads)、SEO、社群網站 (Facebook ads/ LinkedIn ads)、及 B2B 平台 (Alibaba）\n- Google Ads 成果：執行超過80個關鍵字搜尋廣告，CPA 13.89 新加坡幣\n- Facebook Ads 成果：一個月內產生138個轉換，CPA 11.49 新加坡幣\n- SEO 成果：玻璃瓶產品關鍵字在新加坡搜尋排名前五"
                  }
                }
              }
            ]
          }
        },
        "awards": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "references": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

#### ds_sample3.json

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "type": "object",
      "properties": {
        "basics": {
          "type": "object",
          "properties": {
            "first_name": {
              "type": "str",
              "example": "俊詠"
            },
            "last_name": {
              "type": "str",
              "example": "陳"
            },
            "gender": {
              "type": "str",
              "example": "male"
            },
            "emails": {
              "type": "array",
              "items": {
                "type": "str",
                "example": "example@example.com"
              }
            },
            "urls": {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            "phone_numbers": {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            "date_of_birth": {
              "type": "object",
              "properties": {
                "year": {
                  "type": "int",
                  "example": "0"
                },
                "month": {
                  "type": "int",
                  "example": "0"
                },
                "day": {
                  "type": "int",
                  "example": "0"
                }
              }
            },
            "address": {
              "type": "str",
              "example": ""
            },
            "total_experience_in_years": {
              "type": "int",
              "example": "6"
            },
            "profession": {
              "type": "str",
              "example": "data scientist"
            },
            "summary": {
              "type": "str",
              "example": "我是一個不像工程師的工程師，比起開發程式/建立模型/數據分析，其實我覺得我更擅長和人溝通與合作，如果能作為一個主管或領導者，或許更能夠發揮出我更多的價值。\n超過五年的工作經驗 能夠獨立作業 更善於團隊合作 擅長溝通合作 具備領導力 良好的適應力 具備資料分析與模型建立的深厚經驗 勇於挑戰\n\n---\n\n專案作品\n\nQuality control system improvement project 2019/01~2019/06\nImport multi-dimensional monitoring methods\nDesign new quality monitoring indicators\nDesign new diagrams and interfaces\n\nprocess improvement plan 2017/01~2019/01\nEvaluate manufacturing quality\nFind key factors that can be improved\nEstablish Run to Run model to assist quality improvement\n\nCounterfeit judgment model improvement plan 2021/01~2021/08\nInformation available from the Exploration Company Database\nFind valuable features\nImprove model structure\n\nImproving shipment forecasting models 2022/03~2022/12\nMixed use of multiple models\nAutomatically update model parameters\nForecast accuracy improved by 5~10%\n\nCourse : Architecting on AWS 2023/03~2023/03 Architecting on AWS\nCourse : Practical Data Science with Amazon SageMaker 2023/09~2023/09 Practical Data Science with Amazon SageMaker\nCourse : Building Batch Analytics Solutions on AWS 2023/09~2023/09 Building Batch Analytics Solutions on AWS\n\nEstablish an automatic inventory allocation system 2023/01~2023/07\nCommunicate assignment terms to users\nBuild user-friendly automated systems\nSave 80% of manual allocation time\n\nCounterfeit Source Tracking Program 2020/08~2020/12\nFake goods distribution analysis\nException query analysis\nSuccessfully obtained source information of counterfeit goods"
            },
            "skills": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "Machine Learning & Deep Learning Applications"
                  },
                  {
                    "type": "str",
                    "example": "Mathematical and Statistical Model Applications"
                  },
                  {
                    "type": "str",
                    "example": "Office software applications and project management"
                  },
                  {
                    "type": "str",
                    "example": "Python"
                  },
                  {
                    "type": "str",
                    "example": "MySQL"
                  },
                  {
                    "type": "str",
                    "example": "Tableau"
                  },
                  {
                    "type": "str",
                    "example": "Microsoft Office"
                  },
                  {
                    "type": "str",
                    "example": "Matlab"
                  },
                  {
                    "type": "str",
                    "example": "Oracle"
                  },
                  {
                    "type": "str",
                    "example": "R"
                  },
                  {
                    "type": "str",
                    "example": "Github"
                  },
                  {
                    "type": "str",
                    "example": "AWS"
                  }
                ]
              }
            },
            "has_driving_license": {
              "type": "bool",
              "example": "False"
            }
          }
        },
        "languages": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "Chinese"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "zh"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "5"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "str",
                    "example": "English"
                  },
                  "iso_code": {
                    "type": "str",
                    "example": "en"
                  },
                  "fluency": {
                    "type": "int",
                    "example": "3"
                  }
                }
              }
            ]
          }
        },
        "educations": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2014"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2016"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "國立交通大學 統計學研究所"
                  },
                  "description": {
                    "type": "str",
                    "example": "碩士畢業"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_year": {
                    "type": "int",
                    "example": "2009"
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_year": {
                    "type": "int",
                    "example": "2014"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "國立中正大學 數學系"
                  },
                  "description": {
                    "type": "str",
                    "example": "大學畢業"
                  }
                }
              }
            ]
          }
        },
        "trainings_and_certifications": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "int",
                    "example": "2023"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "AWS"
                  },
                  "description": {
                    "type": "str",
                    "example": "Course : Architecting on AWS 2023/03~2023/03 Architecting on AWS"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "int",
                    "example": "2023"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "AWS"
                  },
                  "description": {
                    "type": "str",
                    "example": "Course : Practical Data Science with Amazon SageMaker 2023/09~2023/09 Practical Data Science with Amazon SageMaker"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "year": {
                    "type": "int",
                    "example": "2023"
                  },
                  "issuing_organization": {
                    "type": "str",
                    "example": "AWS"
                  },
                  "description": {
                    "type": "str",
                    "example": "Course : Building Batch Analytics Solutions on AWS 2023/09~2023/09 Building Batch Analytics Solutions on AWS"
                  }
                }
              }
            ]
          }
        },
        "professional_experiences": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "3"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "True"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2023"
                      },
                      "month": {
                        "type": "int",
                        "example": "10"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "19"
                  },
                  "company": {
                    "type": "str",
                    "example": "宏碁股份有限公司"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "data scientist"
                  },
                  "description": {
                    "type": "str",
                    "example": "建立及優化出貨量預測系統\n利用混合模型提高出貨量預測的精確度，種卻率約提高5%\n引入自動化系統以調整模型參數，以優化預測效果\n創建視覺化工具，以協助數據可視化和解釋\n開發自動化系統以進行庫存分配\n與使用者溝通，以制定合適的分配規則\n精簡系統使用，實現一鍵分配的操作方式\n旨在大幅提升使用者效能，並節省人力成本，預估可節省80%的分配時間\n開發圖像文件識別系統\n創建系統，以自動識別紙本商業發票和合約\n實現快速數位化所需文件資訊，並提供客製化設置\n大幅減少文件處理中的人工錯誤\n\nEnhance the Shipment Forecasting System\n\nLeverage Hybrid Models for Enhanced Accuracy\nUtilize hybrid models to increase the accuracy of shipment forecasts, aiming for an approximate 5% improvement.\nImplement an Automated Model Parameter Adjustment System\nIntegrate an automated system for adjusting model parameters to optimize forecasting results.\nDevelop Visual Tools\nCreate visual tools to facilitate data interpretation and decision-making.\nEstablish an Automated Inventory Allocation System\nDefine Allocation Rules through User Communication\nEngage with users to define and establish appropriate allocation rules.\nSimplify System Usage with One-Click Allocation\nStreamline system usage to allow for one-click allocation processes.\nEnhance User Efficiency and Reduce Labor Costs\nAchieve significant efficiency gains, with an estimated 80% reduction in allocated time, leading to substantial labor cost savings.\n\n#Machine Learning #Python #Data Modeling #Github #MySQL #AWS"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2020"
                      },
                      "month": {
                        "type": "int",
                        "example": "3"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2022"
                      },
                      "month": {
                        "type": "int",
                        "example": "2"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "23"
                  },
                  "company": {
                    "type": "str",
                    "example": "擎雷防偽科技股份有限公司"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "大數據分析應用管理師"
                  },
                  "description": {
                    "type": "str",
                    "example": "大規模假貨事件的數據分析\n分析假貨在不同地區的分佈\n研究假貨查詢的時間模式和特徵\n追溯假貨的來源和供應鏈\n估算市場上存在的假貨數量\n特定客戶市場銷售狀況分析\n比較不同年份的銷售情況\n分析銷售區域的分佈和變化\n研究經銷商貨物的流向情況\n假貨鑑定模式的維護與更新\n評估現有模型存在的不足之處\n更新模型的特徵並進行重新建模\n業務數據工具開發\n開發客戶庫存水準和查詢率的記錄表\n建立自動化系統，用於預測假貨銷售曲線\n\nData Analysis of Large-Scale Counterfeit Goods Incidents\n\nAnalyzing the Geographic Distribution of Counterfeit Goods\nExamining the distribution of counterfeit goods across various regions.\nInvestigating Time Patterns and Characteristics in Counterfeit Goods Queries\nExploring the time-related patterns and distinctive features in counterfeit goods queries.\nTracing the Origins and Supply Chain of Counterfeit Goods\nTracing back the sources and supply chain of counterfeit goods.\nEstimating the Quantity of Counterfeit Goods in the Market\nCalculating the approximate quantity of counterfeit goods present in the market\n\nAnalysis of Market Sales Performance for Specific Customers\n\nComparative Analysis of Sales Across Different Years\nEvaluating and comparing sales performance across various years.\nExamination of Sales Region Distribution and Variations\nAnalyzing the distribution and changes in\n\n#Python #MySQL #Tableau #Microsoft Office"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "start_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2016"
                      },
                      "month": {
                        "type": "int",
                        "example": "7"
                      }
                    }
                  },
                  "is_current": {
                    "type": "bool",
                    "example": "False"
                  },
                  "end_date": {
                    "type": "object",
                    "properties": {
                      "year": {
                        "type": "int",
                        "example": "2019"
                      },
                      "month": {
                        "type": "int",
                        "example": "10"
                      }
                    }
                  },
                  "duration_in_months": {
                    "type": "int",
                    "example": "39"
                  },
                  "company": {
                    "type": "str",
                    "example": "旺宏電子"
                  },
                  "location": {
                    "type": "str",
                    "example": "Taiwan"
                  },
                  "title": {
                    "type": "str",
                    "example": "高級工程師"
                  },
                  "description": {
                    "type": "str",
                    "example": "資料分析\n分析晶圓生產資料,協助產線進行品質改善(良率平均約提升5%~10%)\n視覺化分析結果並提出改善建議\n系統管理\n管理自動參數調整系統與製程規範管理系統\n協助產品上線與基本系統障礙排除\n協助規劃系統改善\n專案管理\n新產品基礎背景知識了解\n與產線協調進行實驗\n統計模型建立\n與產線協調統計模型驗證工作\n與自動化工程師協調新產品自動化系統上線\n新產品自動化系統上線後持續跟進品質改善狀況\n\nData Analysis\n\nAnalyze wafer production data and assist production lines in quality improvement (The yield rate is increased by about 5% to 10% on average)\nVisually analyze results and make suggestions for improvement\n\nSystem Management\n\nManage automatic parameter adjustment system and process specification management system\nAssist in product launch and troubleshooting of system obstacles\nAssist in planning system improvements\n\nProject Management\n\nBasic background knowledge of new products\nCoordinate with production line for experiments\n\nStatistical model building\n\nCoordinate statistical model validation work with production line\nCoordinate with automation engineers for new product automation system launch\nFollow up on quality improvement after new product automation system launch\n\n#調查樣本統計分析 #提案與簡報技巧 #Quality Control #Matlab #Oracle #R"
                  }
                }
              }
            ]
          }
        },
        "awards": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "references": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

#### ds_sample2.json

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "str",
      "example": "張為淳"
    },
    "title": {
      "type": "str",
      "example": "Data Science Consultant"
    },
    "company": {
      "type": "str",
      "example": "Carlson Analytics Lab"
    },
    "location": {
      "type": "str",
      "example": "University of Minnesota"
    },
    "about_chinese": {
      "type": "str",
      "example": "Hello, I am Yvonne! Great to meet you! 我熱愛用數據洞見故事！畢業於清華大學科技管理學院學士班 (專長數據科學 + 管理學) 及美國明尼蘇達大學商業分析碩士 (Master of Science in Business Analytics)，我擁有扎實的統計知識與資料分析能力。在美讀碩期間於 Carlson Analytics Lab擔任數據科學顧問，與三家當地企業合作，運用進階數據分析方法解決商業問題。期待繼續用我的靈敏思維與創新，為我未來的公司提供有價值的決策分析，創造數據影響力！"
    },
    "about_english": {
      "type": "str",
      "example": "I love telling insightful stories behind data! With a strong academic background in Statistics and Data Science, my proficiency spans Statistical Analysis and Modeling, Machine Learning, Predictive Analytics, Exploratory Data Analysis, and Data Visualization. Graduating from MS Business Analytics at UMN Carlson, I’m focusing on applying advanced data analytics techniques to address complex business problems, bringing innovation and impact to my future role!"
    },
    "techniques": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "str",
            "example": "統計推論與建模 (Statistical Inference and Modeling)"
          },
          {
            "type": "str",
            "example": "機器學習 (Machine Learning)"
          },
          {
            "type": "str",
            "example": "預測分析 (Predictive Analytics)"
          },
          {
            "type": "str",
            "example": "探索性資料分析 (Exploratory Data Analysis, EDA)"
          },
          {
            "type": "str",
            "example": "資料視覺化 (Data Visualization)"
          }
        ]
      }
    },
    "tools": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "str",
            "example": "Python"
          },
          {
            "type": "str",
            "example": "R"
          },
          {
            "type": "str",
            "example": "SQL"
          },
          {
            "type": "str",
            "example": "Spark"
          },
          {
            "type": "str",
            "example": "Looker Studio"
          },
          {
            "type": "str",
            "example": "Tableau"
          },
          {
            "type": "str",
            "example": "Power BI"
          }
        ]
      }
    },
    "links_text": {
      "type": "str",
      "example": "GitHuband LinkedIn (Note: The specific URLs were not directly available as distinct links in the page snapshot text.)"
    },
    "skills": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "str",
            "example": "數據科學"
          },
          {
            "type": "str",
            "example": "數據分析"
          },
          {
            "type": "str",
            "example": "團隊合作"
          },
          {
            "type": "str",
            "example": "創意思考"
          },
          {
            "type": "str",
            "example": "勇於挑戰"
          }
        ]
      }
    },
    "work_experience": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "role": {
                "type": "str",
                "example": "Data Science Consultant"
              },
              "company": {
                "type": "str",
                "example": "Carlson Analytics Lab"
              },
              "duration": {
                "type": "str",
                "example": "2024/01~2024/04"
              },
              "details": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "Conducted time series analysis in ARIMA model with Python and SQL in BigQuery on 400K+ e-commerce data, visualizing in Looker in Google Cloud Platform (GCP) for inventory analysis. Project link (Note: The specific URL was not directly available as a distinct link in the page snapshot text.)"
                    },
                    {
                      "type": "str",
                      "example": "Conducted statistical analysis and data engineering with Python, PySpark, and Spark SQL in Azure Databricks on 80K+ airline data and visualized flight inefficiency in Power BI, reducing processing time by 30%"
                    },
                    {
                      "type": "str",
                      "example": "Defined metrics and conducted logistic regression with Python"
                    }
                  ]
                }
              },
              "tags": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "#機器學習 (Machine Learning)"
                    },
                    {
                      "type": "str",
                      "example": "#深度學習 (Deep Learning)"
                    },
                    {
                      "type": "str",
                      "example": "#強化學習 (Reinforcement Learning)"
                    },
                    {
                      "type": "str",
                      "example": "#統計分析 (Statistical Analysis)"
                    },
                    {
                      "type": "str",
                      "example": "#預測建模 (Predictive Modeling)"
                    },
                    {
                      "type": "str",
                      "example": "#大數據 (Big Data)"
                    }
                  ]
                }
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "role": {
                "type": "str",
                "example": "Data Analytics Consultant"
              },
              "company": {
                "type": "str",
                "example": "Carlson Analytics Lab"
              },
              "duration": {
                "type": "str",
                "example": "2023/07~2024/01"
              },
              "details": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "Conducted statistical hypothesis testing and Principal Component Analysis (PCA) in R on household saving dataset across eight years, using Analysis of Variance (ANOVA) to determine model with better interpretability"
                    },
                    {
                      "type": "str",
                      "example": "Conducted hierarchical clustering analysis in R to identify underlying customer segmentation on wholesale company data, visualizing cluster features in Principal Component Analysis plot to clarify customer attributes"
                    },
                    {
                      "type": "str",
                      "example": "Achieved 97% accuracy in detecting spam emails using Support Vector Machine (SVM) with Python scikit-learn, performing nested cross-validation to select optimized model for future prediction"
                    },
                    {
                      "type": "str",
                      "example": "Conducted sentiment analysis in Natural Language Processing (NLP) by web-crawling 3K+ editorial articles using Python Beautiful Soup, training model with Word2Vec to generate polarity and subjectivity scores"
                    }
                  ]
                }
              },
              "tags": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "#資料建模 (Data Modeling)"
                    },
                    {
                      "type": "str",
                      "example": "#資料分析 (Data Analytics)"
                    },
                    {
                      "type": "str",
                      "example": "#統計分析 (Statistical Analysis)"
                    },
                    {
                      "type": "str",
                      "example": "#特徵工程 (Feature Engineering)"
                    },
                    {
                      "type": "str",
                      "example": "#統計推論 (Statistical Inference)"
                    },
                    {
                      "type": "str",
                      "example": "#探索性資料分析 (Exploratory Data Analysis)"
                    }
                  ]
                }
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "role": {
                "type": "str",
                "example": "資料分析師 (Data Analyst)"
              },
              "company": {
                "type": "str",
                "example": "SonicBalloon (清華創新育成中心及創業車庫團隊)"
              },
              "duration": {
                "type": "str",
                "example": "2021/07~2022/07"
              },
              "details": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "Spearheaded quantitative analysis and qualitative analysis to identify main competitors, visualizing market values of medical device over six years in Tableau and enhancing market share estimation for the next five years"
                    },
                    {
                      "type": "str",
                      "example": "Presented year-over-year device usage volume across eight years in the U.S. using PivotTable in Microsoft Excel to enhance market value estimation, showcasing product potential and securing startup sponsorship"
                    },
                    {
                      "type": "str",
                      "example": "Increasing teamwork efficiency by 20% through managing stakeholder expectations and providing business insights to foster collaboration and communication between the internal technical team and external consultants"
                    },
                    {
                      "type": "str",
                      "example": "Oversaw weekly meetings by orchestrating information integration and driving goal-oriented collaboration"
                    }
                  ]
                }
              },
              "tags": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "#Excel"
                    },
                    {
                      "type": "str",
                      "example": "#PowerPoint"
                    },
                    {
                      "type": "str",
                      "example": "#數據分析"
                    },
                    {
                      "type": "str",
                      "example": "#市場調查資料分析與報告撰寫"
                    },
                    {
                      "type": "str",
                      "example": "#統計分析"
                    },
                    {
                      "type": "str",
                      "example": "#領導能力"
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    },
    "education": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "institution": {
                "type": "str",
                "example": "University of Minnesota"
              },
              "degree": {
                "type": "str",
                "example": "Master's Degree"
              },
              "field": {
                "type": "str",
                "example": "Business Analytics"
              },
              "duration": {
                "type": "str",
                "example": "2023/06~2024/05"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "institution": {
                "type": "str",
                "example": "國立清華大學 (National Tsing Hua University)"
              },
              "degree": {
                "type": "str",
                "example": "Bachelor's Degree"
              },
              "field": {
                "type": "str",
                "example": "科技管理學院學士班 (College of Technology Management, Bachelor's Program)"
              },
              "duration": {
                "type": "str",
                "example": "2019/09~2023/06"
              }
            }
          }
        ]
      }
    }
  }
}
```

### Field Descriptions

| Field Path | Type | Description |
|------------|------|-------------|
| education[].institution | str | University of Minnesota |
| education[].degree | str | Master's Degree |
| education[].field | str | Business Analytics |
| education[].duration | str | 2023/06~2024/05 |
| education[].institution | str | 國立清華大學 (National Tsing Hua University) |
| education[].degree | str | Bachelor's Degree |
| education[].field | str | 科技管理學院學士班 (College of Technology Management, Bachelor's Program) |
| education[].duration | str | 2019/09~2023/06 |
| title | str | Data Science Consultant |
| tools[] | str | Python |
| tools[] | str | R |
| tools[] | str | SQL |
| tools[] | str | Spark |
| tools[] | str | Looker Studio |
| tools[] | str | Tableau |
| tools[] | str | Power BI |
| company | str | Carlson Analytics Lab |
| about_chinese | str | Hello, I am Yvonne! Great to meet you! 我熱愛用數據洞見故事！畢業於清華大學科技管理學院學士班 (專長數據科學 + 管理學) 及美國明尼蘇達大學商業分析碩士 (Master of Science in Business Analytics)，我擁有扎實的統計知識與資料分析能力。在美讀碩期間於 Carlson Analytics Lab擔任數據科學顧問，與三家當地企業合作，運用進階數據分析方法解決商業問題。期待繼續用我的靈敏思維與創新，為我未來的公司提供有價值的決策分析，創造數據影響力！ |
| profile.awards[] | any |  |
| profile.awards[] | any |  |
| profile.awards[] | any |  |
| profile.awards[] | any |  |
| profile.languages[].name | str | Chinese |
| profile.languages[].iso_code | str | zh |
| profile.languages[].fluency | int | 5 |
| profile.languages[].name | str | English |
| profile.languages[].iso_code | str | en |
| profile.languages[].fluency | int | 4 |
| profile.languages[] | any |  |
| profile.languages[].name | str | Chinese |
| profile.languages[].iso_code | str | zh |
| profile.languages[].fluency | int | 5 |
| profile.languages[].name | str | English |
| profile.languages[].iso_code | str | en |
| profile.languages[].fluency | int | 4 |
| profile.languages[].name | str | Chinese |
| profile.languages[].iso_code | str | zh |
| profile.languages[].fluency | int | 5 |
| profile.languages[].name | str | English |
| profile.languages[].iso_code | str | en |
| profile.languages[].fluency | int | 3 |
| profile.references[] | any |  |
| profile.references[] | any |  |
| profile.references[] | any |  |
| profile.references[] | any |  |
| profile.educations[].start_year | int | 2012 |
| profile.educations[].is_current | bool | False |
| profile.educations[].end_year | int | 2013 |
| profile.educations[].issuing_organization | str | Tilburg University |
| profile.educations[].description | str | Master of Science | Econometrics and Mathematical Economics | Tilburg City, the Netherlands (Sep 2012 - Aug 2013) |
| profile.educations[].start_year | int | 2007 |
| profile.educations[].is_current | bool | False |
| profile.educations[].end_year | int | 2012 |
| profile.educations[].issuing_organization | str | National Taipei University |
| profile.educations[].description | str | Bachelor | Department of Statistics | New Taipei City, Taiwan (Sep 2007 - Jan 2012) |
| profile.educations[].start_year | int | 2009 |
| profile.educations[].is_current | bool | False |
| profile.educations[].end_year | int | 2010 |
| profile.educations[].issuing_organization | str | University of Innsbruck (Austria) SOWI |
| profile.educations[].description | str | One-year exchange student | 2009/09 - 2010/09 |
| profile.educations[] | any |  |
| profile.educations[].start_year | int | 2018 |
| profile.educations[].end_year | int | 2020 |
| profile.educations[].is_current | bool | False |
| profile.educations[].issuing_organization | str | Hanze University of Applied Sciences / Vilnius University |
| profile.educations[].description | str | 雙聯碩士 - 國際溝通碩士學程 |
| profile.educations[].start_year | int | 2011 |
| profile.educations[].end_year | int | 2015 |
| profile.educations[].is_current | bool | False |
| profile.educations[].issuing_organization | str | Tamkang University |
| profile.educations[].description | str | 英文系學士 |
| profile.educations[].start_year | int | 2014 |
| profile.educations[].is_current | bool | False |
| profile.educations[].end_year | int | 2016 |
| profile.educations[].issuing_organization | str | 國立交通大學 統計學研究所 |
| profile.educations[].description | str | 碩士畢業 |
| profile.educations[].start_year | int | 2009 |
| profile.educations[].is_current | bool | False |
| profile.educations[].end_year | int | 2014 |
| profile.educations[].issuing_organization | str | 國立中正大學 數學系 |
| profile.educations[].description | str | 大學畢業 |
| profile.professional_experiences[].title | str | Data Analyst, Assistant Manager |
| profile.professional_experiences[].title | str | Assistant Manager |
| profile.professional_experiences[].title | str | Data Analytic Specialist |
| profile.professional_experiences[].title | str | Event Planning and Coordinator |
| profile.professional_experiences[].title | str | Business Analysis |
| profile.professional_experiences[].title | str | Project Manager |
| profile.professional_experiences[].title | str | Digital Marketing Specialist |
| profile.professional_experiences[].title | str | 市場行銷實習生 |
| profile.professional_experiences[].title | str | 數據分析師 |
| profile.professional_experiences[].title | str | 資料工程師 |
| profile.professional_experiences[].title | str | 雲端解決方案工程師 |
| profile.professional_experiences[].title | str | 數據工程師 |
| profile.professional_experiences[].title | str | 數位行銷企劃專員 |
| profile.professional_experiences[].title | str | data scientist |
| profile.professional_experiences[].title | str | 大數據分析應用管理師 |
| profile.professional_experiences[].title | str | 高級工程師 |
| profile.professional_experiences[].company | str | Morrison Express |
| profile.professional_experiences[].company | str | Zuellig Pharma Digital and Data |
| profile.professional_experiences[].company | str | Zuellig Pharma Digital and Data |
| profile.professional_experiences[].company | str | Yong-He Church NPO |
| profile.professional_experiences[].company | str | CitiBank |
| profile.professional_experiences[].company | str | SUPERMEDIA 超人氣新媒體股份有限公司 |
| profile.professional_experiences[].company | str | 貝殼放大 Backer-Founder |
| profile.professional_experiences[].company | str | 羅傑斯人工智能股份有限公司 |
| profile.professional_experiences[].company | str | CommonWealth Magazine 天下雜誌 |
| profile.professional_experiences[].company | str | AccuHit 愛酷智能科技 |
| profile.professional_experiences[].company | str | Dynasafe 動力安全資訊 |
| profile.professional_experiences[].company | str | DV Biomed 麗彤生醫 |
| profile.professional_experiences[].company | str | Interwaters Pte. Ltd |
| profile.professional_experiences[].company | str | 宏碁股份有限公司 |
| profile.professional_experiences[].company | str | 擎雷防偽科技股份有限公司 |
| profile.professional_experiences[].company | str | 旺宏電子 |
| profile.professional_experiences[].start_date.month | int | 1 |
| profile.professional_experiences[].start_date.month | int | 8 |
| profile.professional_experiences[].start_date.month | int | 2 |
| profile.professional_experiences[].start_date.month | int | 4 |
| profile.professional_experiences[].start_date.month | int | 12 |
| profile.professional_experiences[].start_date.month | int | 2 |
| profile.professional_experiences[].start_date.month | int | 6 |
| profile.professional_experiences[].start_date.month | int | 3 |
| profile.professional_experiences[].start_date.month | int | 6 |
| profile.professional_experiences[].start_date.month | int | 7 |
| profile.professional_experiences[].start_date.month | int | 4 |
| profile.professional_experiences[].start_date.month | int | 11 |
| profile.professional_experiences[].start_date.month | int | 3 |
| profile.professional_experiences[].start_date.month | int | 3 |
| profile.professional_experiences[].start_date.month | int | 3 |
| profile.professional_experiences[].start_date.month | int | 7 |
| profile.professional_experiences[].start_date.year | int | 2023 |
| profile.professional_experiences[].start_date.year | int | 2021 |
| profile.professional_experiences[].start_date.year | int | 2019 |
| profile.professional_experiences[].start_date.year | int | 2016 |
| profile.professional_experiences[].start_date.year | int | 2013 |
| profile.professional_experiences[].start_date.year | int | 2024 |
| profile.professional_experiences[].start_date.year | int | 2023 |
| profile.professional_experiences[].start_date.year | int | 2022 |
| profile.professional_experiences[].start_date.year | int | 2023 |
| profile.professional_experiences[].start_date.year | int | 2022 |
| profile.professional_experiences[].start_date.year | int | 2022 |
| profile.professional_experiences[].start_date.year | int | 2021 |
| profile.professional_experiences[].start_date.year | int | 2020 |
| profile.professional_experiences[].start_date.year | int | 2022 |
| profile.professional_experiences[].start_date.year | int | 2020 |
| profile.professional_experiences[].start_date.year | int | 2016 |
| profile.professional_experiences[].end_date.month | int | 0 |
| profile.professional_experiences[].end_date.month | int | 12 |
| profile.professional_experiences[].end_date.month | int | 7 |
| profile.professional_experiences[].end_date.month | int | 9 |
| profile.professional_experiences[].end_date.month | int | 3 |
| profile.professional_experiences[].end_date.month | int | 2 |
| profile.professional_experiences[].end_date.month | int | 12 |
| profile.professional_experiences[].end_date.month | int | 5 |
| profile.professional_experiences[].end_date.month | int | 6 |
| profile.professional_experiences[].end_date.month | int | 7 |
| profile.professional_experiences[].end_date.month | int | 3 |
| profile.professional_experiences[].end_date.month | int | 5 |
| profile.professional_experiences[].end_date.month | int | 10 |
| profile.professional_experiences[].end_date.month | int | 2 |
| profile.professional_experiences[].end_date.month | int | 10 |
| profile.professional_experiences[].end_date.year | int | 0 |
| profile.professional_experiences[].end_date.year | int | 2022 |
| profile.professional_experiences[].end_date.year | int | 2021 |
| profile.professional_experiences[].end_date.year | int | 2018 |
| profile.professional_experiences[].end_date.year | int | 2016 |
| profile.professional_experiences[].end_date.year | int | 2024 |
| profile.professional_experiences[].end_date.year | int | 2022 |
| profile.professional_experiences[].end_date.year | int | 2025 |
| profile.professional_experiences[].end_date.year | int | 2023 |
| profile.professional_experiences[].end_date.year | int | 2022 |
| profile.professional_experiences[].end_date.year | int | 2022 |
| profile.professional_experiences[].end_date.year | int | 2021 |
| profile.professional_experiences[].end_date.year | int | 2023 |
| profile.professional_experiences[].end_date.year | int | 2022 |
| profile.professional_experiences[].end_date.year | int | 2019 |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | New Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Taipei, Taiwan |
| profile.professional_experiences[].location | str | Singapore |
| profile.professional_experiences[].location | str | Taiwan |
| profile.professional_experiences[].location | str | Taiwan |
| profile.professional_experiences[].location | str | Taiwan |
| profile.professional_experiences[].description | str | 02/01/2023 - present

Project Management / Product Leadership: Spearhead the development of MUSE, an internal reporting product delivering up-to-date financial, sales and operational performance insights through interactive dashboards using agile approach.

Strategic Data Architecture: Design and implement new ETL flows leveraging LakeHouse structure to establish a Single Source Of Truth with prioritized report features, improving data accuracy by 12%.

Complex Data Management: Oversee the migration of 6+ million records and integration of 400+ business logics, ensuring seamless transitions with minimal disruption to business operations.

Cross-functional Collaboration: Act as a bridge between end users (20+ across F&A/Sales/Product/Operation) and product team (Data/EA/BI).

Operational Efficiency: Establish process flows and implemented user request platform via Jira Service Management tool, cutting BI admin workload by 70%. Establish centralized platform, boosting BI report efficiency by 60%. |
| profile.professional_experiences[].description | str | 01/08/2021 - 31/12/2022

Business Development
Strengthened key account monitor mechanism and proactively collaborated with regional stakeholders to achieve country target at 129% and increased subscribed project number by 132%.
Redesigned pricing scheme for TW country, increased annual subscription price by 9% and prolonged clients' subscription period by 160%.

Data Analytics
Customer end-to-end support, from data visualization product all hands to new solution selling.
Conducted sales analysis and presented to valued clients, successfully increased the awareness of company's data capability among the industry and strengthened client engagement.
Developed commercial indicator and visualize business metrics to monitor country growth, generated monthly management report for C-level and higher management team for strategic decision support. |
| profile.professional_experiences[].description | str | 25/02/2019 - 01/08/2021

Customer Insight Analysis
Designed, developed, and demonstrated data-driven dashboards, aiming for a better understanding of customer behaviors and consumption patterns to explore business opportunities.
Built and visualized the first interactive dashboard for medical programs to optimize patient stickiness.

Key Accounts Management
Served as primary data analytic consultant of top 6 key clients; initiated acquisition and retention communications; aligned local stakeholders with the SG regional office.
Planned and coordinated the first company webinar of Impact from Covid-19 in the Taiwan healthcare market; served as the Taiwan consultant; collaborated with the regional and local teams to investigate the pandemic impact to the healthcare industry and provide follow-up advice.

Automation Process
Innovated ways to streamline business process and improve productivity, reducing 50% manual labor time and cost; developed automated process using Python with SAP data and external data sources. |
| profile.professional_experiences[].description | str | 01/04/2016 - 31/08/2018

Event Planner
Led 2 teams of 6 students to organize youth camps on a semi-annual basis, including campaign promotion, social media advertising, volunteer's training. Hosted over 10 events.

Life Education Teacher and Mentoring
Delivered over 50 speeches/lectures in public, reached over 600 audience.
Volunteered for teaching in 2 schools every week. More than 120 students were benefited and responded over 90% satisfaction.
Provided one-on-one mentoring to 20+ students and help them succeed in life, relationship, family, performance acceptives. |
| profile.professional_experiences[].description | str | 01/12/2013 - 04/02/2016

Taiwan Consultant of Global Reporting Cube Project
Collaborated with the global team members to reconcile definition differences.
Supervised India team to re-organize programming flow. Completed UAT within 3 months and conducted follow-on maintenance.
Provided consultation on Taiwan data warehouse and product profile with the global team.

Consultant of Back-End System for New Product Launch
Built system mapping code per Business request and validated the effectiveness.
Conducted UAT tests and inquiry of ad-hoc reporting.

Campaign Leads Generation and Management
Generated over 50+ campaign leads for financial products and tracked the effectiveness of leads.
Conducted customer fulfillment to increase customer loyalty. On average, reach the 95% completion rate of fulfillment.
Analyzed customer data, consumption patterns to optimize customer segmentation.

Ad-Hoc Requests Organizer
Organized and optimized 30+ back-end regular requests and delivered to various departments (ex. compliance, business, branches, anti-money laundry...).
Streamlined the reporting process through tuning SAS/SQL script and automated reporting process. |
| profile.professional_experiences[].description | str | ➤ 與一卡通官方共同打造「潮客 Chicreate」D2C 購物平台，負責平台從 0 到 1 的架構設計：包含物流串接、成本結構、UI/UX、視覺企劃與購物流程優化，並於上線後規劃曝光與 Meta ADs，成功於三個月突破 1000+ 會員數，並達 100+K GMV。
➤ 作為平台企劃操盤 Kurt Wu 聯名廣告專案，主導內容企劃、文案呈現，並與社群、設計師協作曝光計畫，透過集資方式，成功將預熱人潮在三週內轉化成 600+ 銷售，ROAS 達 3。
➤ 作為平台企畫與 13+ 組品牌合作進行日常進銷貨，並於季節時提出相關行銷企劃，擴增商品數量至 1,000+。
➤ 自主使用 ChatGPT + GAS 建立內部工具（如打包工具），簡化資料產出與跨部門協作，提升團隊效率 50%。責 |
| profile.professional_experiences[].description | str | ➤ 作為數位行銷專員，透過迭代與內容優化，優化 CRM 數據策略（LINE@ & EDM），提升 GMV 228%、活躍用戶 137%。

➤ 使用 GA4＋Metabse 追蹤消費者購物流程，提升漏斗轉換效率並協助決策。

➤ 推動 Chatbot 與腳本優化，避免游離狀況發生，用以降使用的障礙，成功帶動 UX 改善與活躍使用者成長。低消費者

➤ 負責全站大型活動（如雙 12、Wabay Good Days）整合規劃，協調設計、PM、廣告團隊。 |
| profile.professional_experiences[].description | str | ➤優化 eBay 商店 SEO 與廣告策略，提升自然流量 330%、廣告導入 300%。➤實機拍攝並透過 PR 製作 8 支產品介紹與教學影片，支援業務推廣與使用者教育。

➤協調設計與翻譯團隊，製作中英雙語手冊與行銷型錄；負責供應商溝通與預算管理。

➤建立品牌初期官網與社群（WIX + Facebook / Twitter /LinkedIn），導入 SEO 與 GA，規劃內容並追蹤受眾輪廓。

➤撰寫 SOP 手冊與 6 支內部教學影片，協助團隊內部與用戶教育流程。 |
| profile.professional_experiences[].description | str | 維護 Data Lake，建置 Data Pipeline，及建立數據產品，包括 : Dashboard、推薦系統、LLM 應用產品

使用 Python、R 和 Airflow 建置易擴展的Data Pipeline
管理 GCP Data Lake 基礎架構，整合 BigQuery 和 Cloud Storage，提升查詢效能
與各BU溝通數據需求，開發互動式 Looker Studio Dashboard，支持數據驅動決策
重構文章推商品推薦系統，加入Search Console 推薦邏輯，提升轉換率 115%
在 6 個月內建立 2 個 LLM 應用 PoC，使用 Python、LangChain 和 Gemini Pro（Vertex AI）開發文章標題生成 (Flask + Line Chatbot + ngrok)及Email 主旨生成 (Streamlit + Azure DevOps & Cloud Run for CI/CD)，提升行銷效率，供超過 10 位內部行銷人員使用 |
| profile.professional_experiences[].description | str | 為公司產品 CDP 的儀表板及標籤系統，開發建置標準化的 Data Pipeline，服務超過15間客戶

使用 Python、Bash 和 SQL 自動化 ETL 處理流程，減少 25% 的數據處理時間
設計並優化 MySQL 與 MongoDB 的資料模型與結構，提升查詢效能
建立客製化標籤系統，增強客戶分群和行銷活動的精準度
與產品團隊密切協作，包括：UIUX、前端/後端、及 PM，確保數據策略與業務目標一致 |
| profile.professional_experiences[].description | str | 使用 Oracle Cloud Infrastructure (OCI) 進行售前規劃 (Pre-sales)，專注於雲端數據解決方案，包括 Oracle Autonomous Database、Oracle Analytics Cloud (OAC) 及 Oracle APEX

完成超過5場的簡報及技術 Demo，讓潛在客戶更了解 OCI 數據產品的功能與優勢
協助設計並執行概念驗證 (PoC)專案，服務客戶包含 BenQ、永豐餘及 Acer 等，達成 60% 的 PoC 轉為完整部署的轉換率
與銷售團隊和 Oracle 產品團隊合作，客製化解決方案，提升客戶滿意度 |
| profile.professional_experiences[].description | str | 協助企業數位轉型，成功將資料從地端資料庫遷移上雲，建立數據中台

透過 SQL、ETL 工具和 Python API，自動化來自 CRM、ERP、網站、LINE、SMS 等超過 10 種資料來源的數據擷取流程，縮短處理時間、提升準確性，每月節省超過 40 小時工時
優化 Oracle Autonomous Database 的效能，支援 Oracle Analytics Cloud 上的數據儀表板
為行銷團隊撈取需求名單並製作 BI 報表，透過精準策略提升 15% 的轉換率
主導 Oracle Cloud Infrastructure (OCI) 上的 SMS 自動化專案，為超過 100 萬名會員發送事件觸發的簡訊，並建立即時儀表板以監控 API 使用量和成本 |
| profile.professional_experiences[].description | str | 成功地從零開始替公司建立數位行銷，包括公司網站及各類數位行銷渠道，如 SEM(Google Ads)、SEO、社群網站 (Facebook ads/ LinkedIn ads)、及 B2B 平台 (Alibaba）
- Google Ads 成果：執行超過80個關鍵字搜尋廣告，CPA 13.89 新加坡幣
- Facebook Ads 成果：一個月內產生138個轉換，CPA 11.49 新加坡幣
- SEO 成果：玻璃瓶產品關鍵字在新加坡搜尋排名前五 |
| profile.professional_experiences[].description | str | 建立及優化出貨量預測系統
利用混合模型提高出貨量預測的精確度，種卻率約提高5%
引入自動化系統以調整模型參數，以優化預測效果
創建視覺化工具，以協助數據可視化和解釋
開發自動化系統以進行庫存分配
與使用者溝通，以制定合適的分配規則
精簡系統使用，實現一鍵分配的操作方式
旨在大幅提升使用者效能，並節省人力成本，預估可節省80%的分配時間
開發圖像文件識別系統
創建系統，以自動識別紙本商業發票和合約
實現快速數位化所需文件資訊，並提供客製化設置
大幅減少文件處理中的人工錯誤

Enhance the Shipment Forecasting System

Leverage Hybrid Models for Enhanced Accuracy
Utilize hybrid models to increase the accuracy of shipment forecasts, aiming for an approximate 5% improvement.
Implement an Automated Model Parameter Adjustment System
Integrate an automated system for adjusting model parameters to optimize forecasting results.
Develop Visual Tools
Create visual tools to facilitate data interpretation and decision-making.
Establish an Automated Inventory Allocation System
Define Allocation Rules through User Communication
Engage with users to define and establish appropriate allocation rules.
Simplify System Usage with One-Click Allocation
Streamline system usage to allow for one-click allocation processes.
Enhance User Efficiency and Reduce Labor Costs
Achieve significant efficiency gains, with an estimated 80% reduction in allocated time, leading to substantial labor cost savings.

#Machine Learning #Python #Data Modeling #Github #MySQL #AWS |
| profile.professional_experiences[].description | str | 大規模假貨事件的數據分析
分析假貨在不同地區的分佈
研究假貨查詢的時間模式和特徵
追溯假貨的來源和供應鏈
估算市場上存在的假貨數量
特定客戶市場銷售狀況分析
比較不同年份的銷售情況
分析銷售區域的分佈和變化
研究經銷商貨物的流向情況
假貨鑑定模式的維護與更新
評估現有模型存在的不足之處
更新模型的特徵並進行重新建模
業務數據工具開發
開發客戶庫存水準和查詢率的記錄表
建立自動化系統，用於預測假貨銷售曲線

Data Analysis of Large-Scale Counterfeit Goods Incidents

Analyzing the Geographic Distribution of Counterfeit Goods
Examining the distribution of counterfeit goods across various regions.
Investigating Time Patterns and Characteristics in Counterfeit Goods Queries
Exploring the time-related patterns and distinctive features in counterfeit goods queries.
Tracing the Origins and Supply Chain of Counterfeit Goods
Tracing back the sources and supply chain of counterfeit goods.
Estimating the Quantity of Counterfeit Goods in the Market
Calculating the approximate quantity of counterfeit goods present in the market

Analysis of Market Sales Performance for Specific Customers

Comparative Analysis of Sales Across Different Years
Evaluating and comparing sales performance across various years.
Examination of Sales Region Distribution and Variations
Analyzing the distribution and changes in

#Python #MySQL #Tableau #Microsoft Office |
| profile.professional_experiences[].description | str | 資料分析
分析晶圓生產資料,協助產線進行品質改善(良率平均約提升5%~10%)
視覺化分析結果並提出改善建議
系統管理
管理自動參數調整系統與製程規範管理系統
協助產品上線與基本系統障礙排除
協助規劃系統改善
專案管理
新產品基礎背景知識了解
與產線協調進行實驗
統計模型建立
與產線協調統計模型驗證工作
與自動化工程師協調新產品自動化系統上線
新產品自動化系統上線後持續跟進品質改善狀況

Data Analysis

Analyze wafer production data and assist production lines in quality improvement (The yield rate is increased by about 5% to 10% on average)
Visually analyze results and make suggestions for improvement

System Management

Manage automatic parameter adjustment system and process specification management system
Assist in product launch and troubleshooting of system obstacles
Assist in planning system improvements

Project Management

Basic background knowledge of new products
Coordinate with production line for experiments

Statistical model building

Coordinate statistical model validation work with production line
Coordinate with automation engineers for new product automation system launch
Follow up on quality improvement after new product automation system launch

#調查樣本統計分析 #提案與簡報技巧 #Quality Control #Matlab #Oracle #R |
| profile.professional_experiences[].is_current | bool | True |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | True |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | True |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | True |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].is_current | bool | False |
| profile.professional_experiences[].duration_in_months | int | 3 |
| profile.professional_experiences[].duration_in_months | int | 16 |
| profile.professional_experiences[].duration_in_months | int | 29 |
| profile.professional_experiences[].duration_in_months | int | 29 |
| profile.professional_experiences[].duration_in_months | int | 27 |
| profile.professional_experiences[].duration_in_months | NoneType | None |
| profile.professional_experiences[].duration_in_months | int | 9 |
| profile.professional_experiences[].duration_in_months | int | 10 |
| profile.professional_experiences[].duration_in_months | int | 23 |
| profile.professional_experiences[].duration_in_months | int | 12 |
| profile.professional_experiences[].duration_in_months | int | 4 |
| profile.professional_experiences[].duration_in_months | int | 5 |
| profile.professional_experiences[].duration_in_months | int | 15 |
| profile.professional_experiences[].duration_in_months | int | 19 |
| profile.professional_experiences[].duration_in_months | int | 23 |
| profile.professional_experiences[].duration_in_months | int | 39 |
| profile.trainings_and_certifications[].year | int | 0 |
| profile.trainings_and_certifications[].issuing_organization | str | ETS (TOEIC / TOEFL) |
| profile.trainings_and_certifications[].description | str | TOEIC 880 / TOEFL 95 |
| profile.trainings_and_certifications[] | any |  |
| profile.trainings_and_certifications[].year | int | 2021 |
| profile.trainings_and_certifications[].issuing_organization | str | 資策會 |
| profile.trainings_and_certifications[].description | str | BIG DATA 巨量資料分析就業養成班 |
| profile.trainings_and_certifications[].year | int | 2023 |
| profile.trainings_and_certifications[].issuing_organization | str | AWS |
| profile.trainings_and_certifications[].description | str | Course : Architecting on AWS 2023/03~2023/03 Architecting on AWS |
| profile.trainings_and_certifications[].year | int | 2023 |
| profile.trainings_and_certifications[].issuing_organization | str | AWS |
| profile.trainings_and_certifications[].description | str | Course : Practical Data Science with Amazon SageMaker 2023/09~2023/09 Practical Data Science with Amazon SageMaker |
| profile.trainings_and_certifications[].year | int | 2023 |
| profile.trainings_and_certifications[].issuing_organization | str | AWS |
| profile.trainings_and_certifications[].description | str | Course : Building Batch Analytics Solutions on AWS 2023/09~2023/09 Building Batch Analytics Solutions on AWS |
| profile.basics.urls[] | str | http://www.linkedin.com/in/yunpingkuo |
| profile.basics.urls[] | str | https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=yun-ping-kuo |
| profile.basics.urls[] | str | https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=a9634578 |
| profile.basics.urls[] | str | http://www.linkedin.com/in/yuhsuenliu |
| profile.basics.urls[] | str | https://www.cake.me/?ref=resume_web&utm_source=resume&utm_medium=web&utm_content=yu-hsuen-liu |
| profile.basics.urls[] | any |  |
| profile.basics.profession | str | Data Analyst / Business Intelligence Analyst / Business Development |
| profile.basics.profession | str | 產品行銷人 |
| profile.basics.profession | str | Data Engineer & Analyst |
| profile.basics.profession | str | data scientist |
| profile.basics.summary | str | I am an experienced data analyst across financial, healthcare, and logistic industry over 8+ years. A fast learner, self-motivated, and passionate about progress and challenges. Reliable, adaptable, and willing to go the extra mile.

--- Chinese Summary ---
我擁有六年於金融業及醫療物流產業實務經驗之資料分析師。
以下是三個與同業相比獨特之專業優勢：
(1) 豐富跨國溝通協作經歷、英文能力優
(2) 擁有業務經驗，善於從客戶的角度換位思考並成為客戶與資料工程之間的橋樑
(3) 豐富簡報經驗，與高階經理人合作經驗。 |
| profile.basics.summary | str | 我是數據與目標導向的產品行銷人。曾於 4 人團隊，主導從 0 到 1 跨部門、跨公司與UIUX、RD 及外部團隊打造電商平台「潮客 Chicreate」。

我也熟悉 CRM 策略、GA4／Metabase 數據分析、A/B Test，曾透過迭代與內容優化，提升 GMV 228%、使用者活躍率 137%。

我擅長數據分析與策略規劃，將產品價值轉化為具行動力的訊息，有效向市場推動產品，期待能加入開放的產品導向團隊，持續發揮「內容策略 × 數據分析 × 創意發展」的價值。 |
| profile.basics.summary | str | ✔ 擁有 3 年以上的數據工程與分析經驗，專長建構數據管道與雲端服務
✔ 有豐富的數據產品開發成果，包含儀表板、推薦系統和LLM 落地應用
✔ 荷蘭、立陶宛國際溝通雙碩士 + 2年新加坡數位行銷經驗
✔ 具備高度適應力、跨文化視野及持續學習的精神 |
| profile.basics.summary | str | 我是一個不像工程師的工程師，比起開發程式/建立模型/數據分析，其實我覺得我更擅長和人溝通與合作，如果能作為一個主管或領導者，或許更能夠發揮出我更多的價值。
超過五年的工作經驗 能夠獨立作業 更善於團隊合作 擅長溝通合作 具備領導力 良好的適應力 具備資料分析與模型建立的深厚經驗 勇於挑戰

---

專案作品

Quality control system improvement project 2019/01~2019/06
Import multi-dimensional monitoring methods
Design new quality monitoring indicators
Design new diagrams and interfaces

process improvement plan 2017/01~2019/01
Evaluate manufacturing quality
Find key factors that can be improved
Establish Run to Run model to assist quality improvement

Counterfeit judgment model improvement plan 2021/01~2021/08
Information available from the Exploration Company Database
Find valuable features
Improve model structure

Improving shipment forecasting models 2022/03~2022/12
Mixed use of multiple models
Automatically update model parameters
Forecast accuracy improved by 5~10%

Course : Architecting on AWS 2023/03~2023/03 Architecting on AWS
Course : Practical Data Science with Amazon SageMaker 2023/09~2023/09 Practical Data Science with Amazon SageMaker
Course : Building Batch Analytics Solutions on AWS 2023/09~2023/09 Building Batch Analytics Solutions on AWS

Establish an automatic inventory allocation system 2023/01~2023/07
Communicate assignment terms to users
Build user-friendly automated systems
Save 80% of manual allocation time

Counterfeit Source Tracking Program 2020/08~2020/12
Fake goods distribution analysis
Exception query analysis
Successfully obtained source information of counterfeit goods |
| profile.basics.gender | str | female |
| profile.basics.gender | str |  |
| profile.basics.gender | str | male |
| profile.basics.gender | str | male |
| profile.basics.has_driving_license | bool | False |
| profile.basics.has_driving_license | bool | False |
| profile.basics.has_driving_license | bool | False |
| profile.basics.has_driving_license | bool | False |
| profile.basics.emails[] | str | cloudping423@gmail.com |
| profile.basics.emails[] | any |  |
| profile.basics.emails[] | str | peter19930419@gmail.com |
| profile.basics.emails[] | str | example@example.com |
| profile.basics.first_name | str | Yun-Ping (Rhea) |
| profile.basics.first_name | str | 琨育 |
| profile.basics.first_name | str | Yu Hsuen |
| profile.basics.first_name | str | 俊詠 |
| profile.basics.last_name | str | Kuo (郭) |
| profile.basics.last_name | str | 邱 |
| profile.basics.last_name | str | Liu |
| profile.basics.last_name | str | 陳 |
| profile.basics.phone_numbers[] | str | +886-961-016-034 |
| profile.basics.phone_numbers[] | any |  |
| profile.basics.phone_numbers[] | str | 0955136095 |
| profile.basics.phone_numbers[] | any |  |
| profile.basics.skills[] | str | SQL |
| profile.basics.skills[] | str | Python |
| profile.basics.skills[] | str | SAS |
| profile.basics.skills[] | str | SPSS |
| profile.basics.skills[] | str | Tableau |
| profile.basics.skills[] | str | Teradata |
| profile.basics.skills[] | str | SAP HANA |
| profile.basics.skills[] | str | Microsoft Excel (Pivot) |
| profile.basics.skills[] | str | PowerPoint |
| profile.basics.skills[] | str | Word |
| profile.basics.skills[] | str | Project Management |
| profile.basics.skills[] | str | Communication |
| profile.basics.skills[] | str | Cross-team collaboration |
| profile.basics.skills[] | str | Solution selling |
| profile.basics.skills[] | str | Presentation |
| profile.basics.skills[] | str | Agile work style |
| profile.basics.skills[] | str | 數據分析 |
| profile.basics.skills[] | str | CRM 策略 |
| profile.basics.skills[] | str | GA4 |
| profile.basics.skills[] | str | Metabase |
| profile.basics.skills[] | str | A/B Test |
| profile.basics.skills[] | str | ChatGPT |
| profile.basics.skills[] | str | Google Apps Script |
| profile.basics.skills[] | str | SEO |
| profile.basics.skills[] | str | 廣告企劃 |
| profile.basics.skills[] | str | UX 優化 |
| profile.basics.skills[] | str | Python |
| profile.basics.skills[] | str | SQL |
| profile.basics.skills[] | str | R |
| profile.basics.skills[] | str | Airflow |
| profile.basics.skills[] | str | Docker |
| profile.basics.skills[] | str | Linux |
| profile.basics.skills[] | str | MySQL |
| profile.basics.skills[] | str | Oracle |
| profile.basics.skills[] | str | MongoDB |
| profile.basics.skills[] | str | Looker Studio |
| profile.basics.skills[] | str | BigQuery |
| profile.basics.skills[] | str | Cloud Storage |
| profile.basics.skills[] | str | Cloud Run |
| profile.basics.skills[] | str | LangChain |
| profile.basics.skills[] | str | Vertex AI |
| profile.basics.skills[] | str | Machine Learning & Deep Learning Applications |
| profile.basics.skills[] | str | Mathematical and Statistical Model Applications |
| profile.basics.skills[] | str | Office software applications and project management |
| profile.basics.skills[] | str | Python |
| profile.basics.skills[] | str | MySQL |
| profile.basics.skills[] | str | Tableau |
| profile.basics.skills[] | str | Microsoft Office |
| profile.basics.skills[] | str | Matlab |
| profile.basics.skills[] | str | Oracle |
| profile.basics.skills[] | str | R |
| profile.basics.skills[] | str | Github |
| profile.basics.skills[] | str | AWS |
| profile.basics.date_of_birth.month | int | 0 |
| profile.basics.date_of_birth.month | int | 4 |
| profile.basics.date_of_birth.month | int | 0 |
| profile.basics.date_of_birth.day | int | 0 |
| profile.basics.date_of_birth.day | int | 19 |
| profile.basics.date_of_birth.day | int | 0 |
| profile.basics.date_of_birth.year | int | 0 |
| profile.basics.date_of_birth.year | int | 1993 |
| profile.basics.date_of_birth.year | int | 0 |
| profile.basics.address | str | 6F., No. 8-8, Jieyun Rd., Zhonghe Dist., New Taipei City, Taiwan |
| profile.basics.address | str | Taipei City, Taiwan |
| profile.basics.address | str | 新北市, 台灣 |
| profile.basics.address | str |  |
| profile.basics.total_experience_in_years | int | 8 |
| profile.basics.total_experience_in_years | int | 3 |
| profile.basics.total_experience_in_years | int | 4 |
| profile.basics.total_experience_in_years | int | 6 |
| location | str | University of Minnesota |
| name | str | 張為淳 |
| about_english | str | I love telling insightful stories behind data! With a strong academic background in Statistics and Data Science, my proficiency spans Statistical Analysis and Modeling, Machine Learning, Predictive Analytics, Exploratory Data Analysis, and Data Visualization. Graduating from MS Business Analytics at UMN Carlson, I’m focusing on applying advanced data analytics techniques to address complex business problems, bringing innovation and impact to my future role! |
| skills[] | str | 數據科學 |
| skills[] | str | 數據分析 |
| skills[] | str | 團隊合作 |
| skills[] | str | 創意思考 |
| skills[] | str | 勇於挑戰 |
| links_text | str | GitHuband LinkedIn (Note: The specific URLs were not directly available as distinct links in the page snapshot text.) |
| techniques[] | str | 統計推論與建模 (Statistical Inference and Modeling) |
| techniques[] | str | 機器學習 (Machine Learning) |
| techniques[] | str | 預測分析 (Predictive Analytics) |
| techniques[] | str | 探索性資料分析 (Exploratory Data Analysis, EDA) |
| techniques[] | str | 資料視覺化 (Data Visualization) |
| work_experience[].role | str | Data Science Consultant |
| work_experience[].company | str | Carlson Analytics Lab |
| work_experience[].duration | str | 2024/01~2024/04 |
| work_experience[].details[] | str | Conducted time series analysis in ARIMA model with Python and SQL in BigQuery on 400K+ e-commerce data, visualizing in Looker in Google Cloud Platform (GCP) for inventory analysis. Project link (Note: The specific URL was not directly available as a distinct link in the page snapshot text.) |
| work_experience[].details[] | str | Conducted statistical analysis and data engineering with Python, PySpark, and Spark SQL in Azure Databricks on 80K+ airline data and visualized flight inefficiency in Power BI, reducing processing time by 30% |
| work_experience[].details[] | str | Defined metrics and conducted logistic regression with Python |
| work_experience[].tags[] | str | #機器學習 (Machine Learning) |
| work_experience[].tags[] | str | #深度學習 (Deep Learning) |
| work_experience[].tags[] | str | #強化學習 (Reinforcement Learning) |
| work_experience[].tags[] | str | #統計分析 (Statistical Analysis) |
| work_experience[].tags[] | str | #預測建模 (Predictive Modeling) |
| work_experience[].tags[] | str | #大數據 (Big Data) |
| work_experience[].role | str | Data Analytics Consultant |
| work_experience[].company | str | Carlson Analytics Lab |
| work_experience[].duration | str | 2023/07~2024/01 |
| work_experience[].details[] | str | Conducted statistical hypothesis testing and Principal Component Analysis (PCA) in R on household saving dataset across eight years, using Analysis of Variance (ANOVA) to determine model with better interpretability |
| work_experience[].details[] | str | Conducted hierarchical clustering analysis in R to identify underlying customer segmentation on wholesale company data, visualizing cluster features in Principal Component Analysis plot to clarify customer attributes |
| work_experience[].details[] | str | Achieved 97% accuracy in detecting spam emails using Support Vector Machine (SVM) with Python scikit-learn, performing nested cross-validation to select optimized model for future prediction |
| work_experience[].details[] | str | Conducted sentiment analysis in Natural Language Processing (NLP) by web-crawling 3K+ editorial articles using Python Beautiful Soup, training model with Word2Vec to generate polarity and subjectivity scores |
| work_experience[].tags[] | str | #資料建模 (Data Modeling) |
| work_experience[].tags[] | str | #資料分析 (Data Analytics) |
| work_experience[].tags[] | str | #統計分析 (Statistical Analysis) |
| work_experience[].tags[] | str | #特徵工程 (Feature Engineering) |
| work_experience[].tags[] | str | #統計推論 (Statistical Inference) |
| work_experience[].tags[] | str | #探索性資料分析 (Exploratory Data Analysis) |
| work_experience[].role | str | 資料分析師 (Data Analyst) |
| work_experience[].company | str | SonicBalloon (清華創新育成中心及創業車庫團隊) |
| work_experience[].duration | str | 2021/07~2022/07 |
| work_experience[].details[] | str | Spearheaded quantitative analysis and qualitative analysis to identify main competitors, visualizing market values of medical device over six years in Tableau and enhancing market share estimation for the next five years |
| work_experience[].details[] | str | Presented year-over-year device usage volume across eight years in the U.S. using PivotTable in Microsoft Excel to enhance market value estimation, showcasing product potential and securing startup sponsorship |
| work_experience[].details[] | str | Increasing teamwork efficiency by 20% through managing stakeholder expectations and providing business insights to foster collaboration and communication between the internal technical team and external consultants |
| work_experience[].details[] | str | Oversaw weekly meetings by orchestrating information integration and driving goal-oriented collaboration |
| work_experience[].tags[] | str | #Excel |
| work_experience[].tags[] | str | #PowerPoint |
| work_experience[].tags[] | str | #數據分析 |
| work_experience[].tags[] | str | #市場調查資料分析與報告撰寫 |
| work_experience[].tags[] | str | #統計分析 |
| work_experience[].tags[] | str | #領導能力 |

## MLE Resume Schemas

### Common Schema

This schema represents the common structure across all samples:

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "experience": {
          "type": "object",
          "properties": {
            "experiences": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "duration": {
                    "type": "object",
                    "properties": {
                      "startMonth": {
                        "type": "object",
                        "properties": {
                          "value": {
                            "oneOf": [
                              {
                                "type": "int",
                                "example": "3"
                              },
                              {
                                "type": "int",
                                "example": "9"
                              },
                              {
                                "type": "int",
                                "example": "9"
                              },
                              {
                                "type": "int",
                                "example": "7"
                              },
                              {
                                "type": "int",
                                "example": "7"
                              },
                              {
                                "type": "int",
                                "example": "1"
                              },
                              {
                                "type": "int",
                                "example": "10"
                              }
                            ]
                          },
                          "text": {
                            "oneOf": [
                              {
                                "type": "str",
                                "example": "3"
                              },
                              {
                                "type": "str",
                                "example": "9"
                              },
                              {
                                "type": "str",
                                "example": "9"
                              },
                              {
                                "type": "str",
                                "example": "7"
                              },
                              {
                                "type": "str",
                                "example": "7"
                              },
                              {
                                "type": "str",
                                "example": "1"
                              },
                              {
                                "type": "str",
                                "example": "10"
                              }
                            ]
                          }
                        }
                      },
                      "startYear": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "2023"
                          },
                          {
                            "type": "str",
                            "example": "2022"
                          },
                          {
                            "type": "str",
                            "example": "2021"
                          },
                          {
                            "type": "str",
                            "example": "2018"
                          },
                          {
                            "type": "str",
                            "example": "2022"
                          },
                          {
                            "type": "str",
                            "example": "2022"
                          },
                          {
                            "type": "str",
                            "example": "2019"
                          }
                        ]
                      },
                      "endMonth": {
                        "oneOf": [
                          {
                            "type": "array",
                            "items": {
                              "type": "any"
                            }
                          },
                          {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "1"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "2"
                              },
                              "value": {
                                "type": "int",
                                "example": "2"
                              }
                            }
                          },
                          {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "9"
                              },
                              "value": {
                                "type": "int",
                                "example": "9"
                              }
                            }
                          },
                          {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "12"
                              },
                              "value": {
                                "type": "int",
                                "example": "12"
                              }
                            }
                          },
                          {
                            "type": "array",
                            "items": {
                              "type": "any"
                            }
                          },
                          {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "3"
                              },
                              "value": {
                                "type": "int",
                                "example": "3"
                              }
                            }
                          }
                        ]
                      },
                      "endYear": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": "2023"
                          },
                          {
                            "type": "str",
                            "example": "2022"
                          },
                          {
                            "type": "str",
                            "example": "2018"
                          },
                          {
                            "type": "str",
                            "example": "2022"
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": "2021"
                          }
                        ]
                      }
                    }
                  },
                  "jobName": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "工程師"
                      },
                      {
                        "type": "str",
                        "example": "AI 智慧應用開發實戰養成班"
                      },
                      {
                        "type": "str",
                        "example": "台積電計畫研究生"
                      },
                      {
                        "type": "str",
                        "example": "實習生"
                      },
                      {
                        "type": "str",
                        "example": "軟體研究部門實習生"
                      },
                      {
                        "type": "str",
                        "example": "吳俊穎教授實驗室研究助理"
                      },
                      {
                        "type": "str",
                        "example": "急診護理師"
                      }
                    ]
                  },
                  "jobType": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "全職"
                          },
                          {
                            "type": "str",
                            "example": "全職"
                          },
                          {
                            "type": "str",
                            "example": "兼職"
                          },
                          {
                            "type": "str",
                            "example": "兼職"
                          },
                          {
                            "type": "str",
                            "example": "兼職"
                          },
                          {
                            "type": "str",
                            "example": "兼職"
                          },
                          {
                            "type": "str",
                            "example": "全職"
                          }
                        ]
                      }
                    }
                  },
                  "salaryVisibility": {
                    "oneOf": [
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      }
                    ]
                  },
                  "companyScale": {
                    "oneOf": [
                      {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "500人以上"
                          },
                          "value": {
                            "type": "int",
                            "example": "4"
                          }
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "500人以上"
                          },
                          "value": {
                            "type": "int",
                            "example": "4"
                          }
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "500人以上"
                          },
                          "value": {
                            "type": "int",
                            "example": "4"
                          }
                        }
                      }
                    ]
                  },
                  "skill": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "顯示器技術"
                            },
                            "value": {
                              "type": "str",
                              "example": "0"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "TFT知識"
                            },
                            "value": {
                              "type": "str",
                              "example": "0"
                            }
                          }
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "護理指導及諮詢"
                            },
                            "value": {
                              "type": "str",
                              "example": "11012010016"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "執行靜脈或肌肉注射相關作業"
                            },
                            "value": {
                              "type": "str",
                              "example": "11012010008"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "預防保護之護理措施"
                            },
                            "value": {
                              "type": "str",
                              "example": "11012010012"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "健康問題之護理評估"
                            },
                            "value": {
                              "type": "str",
                              "example": "11007003010"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "急救甦醒器之使用與維護"
                            },
                            "value": {
                              "type": "str",
                              "example": "11012010020"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "協同專科醫師進行會診或轉診"
                            },
                            "value": {
                              "type": "str",
                              "example": "11012010001"
                            }
                          }
                        }
                      ]
                    }
                  },
                  "stillWork": {
                    "oneOf": [
                      {
                        "type": "bool",
                        "example": "True"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      },
                      {
                        "type": "bool",
                        "example": "True"
                      },
                      {
                        "type": "bool",
                        "example": "False"
                      }
                    ]
                  },
                  "sort": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "4"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      }
                    ]
                  },
                  "logo": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": ""
                      },
                      {
                        "type": "str",
                        "example": "https://static.104.com.tw/b_profile/cust_picture/2476/130000000082476/logo.png?v=20250410150005"
                      },
                      {
                        "type": "str",
                        "example": "https://static.104.com.tw/b_profile/cust_picture/1000/22099131000/logo.gif?v=20220111153850"
                      },
                      {
                        "type": "str",
                        "example": "https://static.104.com.tw/b_profile/cust_picture/8000/84149738000/logo.png?v=20250321110724"
                      },
                      {
                        "type": "str",
                        "example": "https://static.104.com.tw/b_profile/cust_picture/6001/5076416001/logo.gif?v=20241213151351"
                      },
                      {
                        "type": "str",
                        "example": ""
                      },
                      {
                        "type": "str",
                        "example": ""
                      }
                    ]
                  },
                  "jobCat": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "no": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "2007001020"
                            },
                            {
                              "type": "int",
                              "example": "2007001004"
                            },
                            {
                              "type": "int",
                              "example": "2016001013"
                            },
                            {
                              "type": "int",
                              "example": "2008001018"
                            },
                            {
                              "type": "int",
                              "example": "2002001011"
                            },
                            {
                              "type": "int",
                              "example": "2016001013"
                            },
                            {
                              "type": "int",
                              "example": "2015001004"
                            }
                          ]
                        },
                        "des": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "AI工程師"
                            },
                            {
                              "type": "str",
                              "example": "軟體工程師"
                            },
                            {
                              "type": "str",
                              "example": "研究助理"
                            },
                            {
                              "type": "str",
                              "example": "光電工程師"
                            },
                            {
                              "type": "str",
                              "example": "工讀生"
                            },
                            {
                              "type": "str",
                              "example": "研究助理"
                            },
                            {
                              "type": "str",
                              "example": "護理師及護士"
                            }
                          ]
                        }
                      }
                    }
                  },
                  "invoice": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "94096794"
                      },
                      {
                        "type": "int",
                        "example": "24708053"
                      },
                      {
                        "type": "int",
                        "example": "22099131"
                      },
                      {
                        "type": "int",
                        "example": "84149738"
                      },
                      {
                        "type": "int",
                        "example": "5076416"
                      },
                      {
                        "type": "int",
                        "example": "0"
                      },
                      {
                        "type": "int",
                        "example": "29906905"
                      }
                    ]
                  },
                  "workArea": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "no": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "6001001010"
                            },
                            {
                              "type": "int",
                              "example": "6001002004"
                            },
                            {
                              "type": "int",
                              "example": "6001006001"
                            },
                            {
                              "type": "int",
                              "example": "6001006001"
                            },
                            {
                              "type": "int",
                              "example": "6001001004"
                            },
                            {
                              "type": "int",
                              "example": "6001001009"
                            },
                            {
                              "type": "int",
                              "example": "6001001009"
                            }
                          ]
                        },
                        "des": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "台北市內湖區"
                            },
                            {
                              "type": "str",
                              "example": "新北市汐止區"
                            },
                            {
                              "type": "str",
                              "example": "新竹市"
                            },
                            {
                              "type": "str",
                              "example": "新竹市"
                            },
                            {
                              "type": "str",
                              "example": "台北市松山區"
                            },
                            {
                              "type": "str",
                              "example": "台北市北投區"
                            },
                            {
                              "type": "str",
                              "example": "台北市北投區"
                            }
                          ]
                        }
                      }
                    }
                  },
                  "description": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "<p><span style=\"background-color:rgb(255,255,255);color:rgba(0,0,0,0.9);\">Developing Deep Learning Solution : AutoEncoder or LSTM for Engineering including Wind speed or vibration signal analysis so far.</span></p><p><span style=\"background-color:rgb(255,255,255);color:rgba(0,0,0,0.9);\">Good at 1-D Signal Processing (FFT 、wavelet Transform), ready to study 2-D Signal Processing</span></p>"
                      },
                      {
                        "type": "str",
                        "example": "● 負責功能整合成桌面應用及GUI呈現 #Let's Dance 舞蹈辨識系統\n● 使用 threading 平行化技術 達成遊戲同時多工效果\n● 使用 PyQt5 將跳舞遊玩結果以GUI呈現給消費者\n● 500小時學習資料收集、清洗，AI模型訓練，部署模型至雲端，資料視覺化等AI完整應用"
                      },
                      {
                        "type": "str",
                        "example": "● 研究所期間與台積電為期半年的合作計畫\n● 使用 Matlab 對光的傳播進行傅立葉分析，模擬光阻內最小氣泡的位置，以提升元件良率"
                      },
                      {
                        "type": "str",
                        "example": "● 研究所期間參與友達光電的暑期實習計畫\n● 75吋面板正視、側視收光量測\n● 學習產品TFT - LCD原理，反推defect成因並解決"
                      },
                      {
                        "type": "str",
                        "example": "● 此為經濟部工業局「Digitalent」實習計畫 – 「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」 專案\n1. 專案發想、時程規劃安排、論文技術討論\n2.負責與醫院端及產業端合作溝通\n3. 協助臨床數據收集\n4. 協助利用python以機器學習方式建置呼吸音辨識模型"
                      },
                      {
                        "type": "str",
                        "example": "協助臨床研究收案，健保資料庫分析，實驗室相關庶務\n\n● 協助執行科技部計畫 – 「腸道微菌叢對於新冠肺炎疫苗相關免疫反應、副作用、持久性及突破性感染之角色」 \n1. 負責計畫部分臨床收案，需主動找尋受試者、和民眾溝通，與醫院單位協調\n2.進行實驗室血液檢體分析、檢體保存管理、估算使用成本等事務\n\n● 健保資料庫統計分析：\n1. 與醫學中心皮膚科醫師合作進行健康資料流行病學分析，曾處理過慢性腎臟病與類天疱瘡相關性、白斑與視網膜剝離的關聯性、系統性藥物治療的乾癬患者發生心血管疾病的風險、類天皰瘡與各感染疾病之關係等案件。\n2.藉由資料庫分析，處理過2300萬人的大型資料數據。\n\n● 就學期間曾修習相關領域課程：SAS資料分析及應用、資料科學軟體實作、雲端技術及網路服務實務、資料視覺化與視覺分析、進階流行病學研究設計、深度學習於生醫資料分析 、資料探勘，且於在學期間取得公衛師考試的資格。"
                      },
                      {
                        "type": "str",
                        "example": "擔任急診護理師需具備刻苦耐勞的個性、能力上需反應快動作靈敏、與人可以良好溝通。工作內容主要為照顧病人，協助醫師診治，執行護理相關技術，急救處理(ACLS)。"
                      }
                    ]
                  },
                  "companyName": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "神耀科技股份有限公司"
                      },
                      {
                        "type": "str",
                        "example": "緯育股份有限公司"
                      },
                      {
                        "type": "str",
                        "example": "台灣積體電路製造股份有限公司"
                      },
                      {
                        "type": "str",
                        "example": "友達光電股份有限公司"
                      },
                      {
                        "type": "str",
                        "example": "財團法人資訊工業策進會"
                      },
                      {
                        "type": "str",
                        "example": "國立陽明交通大學"
                      },
                      {
                        "type": "str",
                        "example": "臺北榮民總醫院"
                      }
                    ]
                  },
                  "salary": {
                    "type": "object",
                    "properties": {
                      "yearPay": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          }
                        ]
                      },
                      "jobParttimeType": {
                        "type": "object",
                        "properties": {
                          "value": {
                            "oneOf": [
                              {
                                "type": "int",
                                "example": "1"
                              },
                              {
                                "type": "int",
                                "example": "1"
                              },
                              {
                                "type": "int",
                                "example": "1"
                              },
                              {
                                "type": "int",
                                "example": "3"
                              },
                              {
                                "type": "int",
                                "example": "1"
                              },
                              {
                                "type": "int",
                                "example": "1"
                              },
                              {
                                "type": "int",
                                "example": "1"
                              }
                            ]
                          },
                          "text": {
                            "oneOf": [
                              {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              {
                                "type": "str",
                                "example": "平均月薪"
                              },
                              {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              {
                                "type": "str",
                                "example": "平均時薪"
                              }
                            ]
                          }
                        }
                      },
                      "monthPay": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          }
                        ]
                      },
                      "jobParttimePay": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "int",
                            "example": "28000"
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": ""
                          }
                        ]
                      }
                    }
                  },
                  "companyVisibility": {
                    "oneOf": [
                      {
                        "type": "bool",
                        "example": "True"
                      },
                      {
                        "type": "bool",
                        "example": "True"
                      },
                      {
                        "type": "bool",
                        "example": "True"
                      },
                      {
                        "type": "bool",
                        "example": "True"
                      },
                      {
                        "type": "bool",
                        "example": "True"
                      },
                      {
                        "type": "bool",
                        "example": "True"
                      },
                      {
                        "type": "bool",
                        "example": "True"
                      }
                    ]
                  },
                  "custNo": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "0"
                      },
                      {
                        "type": "str",
                        "example": "1a2x6bjqy4"
                      },
                      {
                        "type": "str",
                        "example": "a5h92m0"
                      },
                      {
                        "type": "str",
                        "example": "12nokxe8"
                      },
                      {
                        "type": "str",
                        "example": "2byd7nl"
                      },
                      {
                        "type": "int",
                        "example": "0"
                      },
                      {
                        "type": "str",
                        "example": "dqlsrl4"
                      }
                    ]
                  },
                  "industry": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "no": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1001001001"
                            },
                            {
                              "type": "int",
                              "example": "1001001001"
                            },
                            {
                              "type": "int",
                              "example": "1001006002"
                            },
                            {
                              "type": "int",
                              "example": "1001004002"
                            },
                            {
                              "type": "int",
                              "example": "1001001002"
                            },
                            {
                              "type": "int",
                              "example": "1005001007"
                            },
                            {
                              "type": "int",
                              "example": "1012001001"
                            }
                          ]
                        },
                        "des": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "電腦系統整合服務業"
                            },
                            {
                              "type": "str",
                              "example": "電腦系統整合服務業"
                            },
                            {
                              "type": "str",
                              "example": "半導體製造業"
                            },
                            {
                              "type": "str",
                              "example": "光學器材製造業"
                            },
                            {
                              "type": "str",
                              "example": "電腦軟體服務業"
                            },
                            {
                              "type": "str",
                              "example": "大專校院教育事業"
                            },
                            {
                              "type": "str",
                              "example": "醫院"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "seniority": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "0"
                    },
                    {
                      "type": "int",
                      "example": "1"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "1年(含)以下"
                    },
                    {
                      "type": "str",
                      "example": "1~2年"
                    }
                  ]
                }
              }
            }
          }
        },
        "custom1": {
          "oneOf": [
            {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            {
              "type": "object",
              "properties": {
                "custom": {
                  "type": "object",
                  "properties": {
                    "sort": {
                      "type": "int",
                      "example": "1"
                    },
                    "name": {
                      "type": "str",
                      "example": "經濟部跨域數位人才加速躍升計畫"
                    },
                    "content": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "duration": {
                            "type": "object",
                            "properties": {
                              "startYear": {
                                "type": "str",
                                "example": "2022"
                              },
                              "startMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "7"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "7"
                                  }
                                }
                              },
                              "endYear": {
                                "type": "str",
                                "example": "2022"
                              },
                              "endMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "12"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "12"
                                  }
                                }
                              }
                            }
                          },
                          "isInProgress": {
                            "type": "bool",
                            "example": "False"
                          },
                          "introduction": {
                            "type": "str",
                            "example": "【DIGI+Talent 跨域數位人才加速躍升計畫】\n此跨域計畫為行政院自2017年起推動「數位國家・創新經濟發展方案（簡稱DIGI+）」，入選為2022年智慧聯網類研習生，以「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」為主題，團隊於2022年底成果發表會42組隊伍中獲得第二名佳績。\n\n● 由資訊工業策進會業師指導，與醫院及國內業者合作推行專案\n● 經歷6個月實習，總時數超過240小時的研習及30小時線上課程學習。\n●專案內容涵蓋Python程式設計、智慧聯網、機器學習應用實務、語音辨識、萃取音訊特徵，對音訊進行分析等。"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://www.youtube.com/watch?v=uWeHwZRZI6M&list=PLoQj70ABw1jnRdB-HBAOgFj2Ini6hEp1_&index=6"
                          }
                        }
                      }
                    }
                  }
                },
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "經典風格"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "CustomThemeClassic"
                        }
                      }
                    }
                  }
                },
                "img": {
                  "type": "object",
                  "properties": {
                    "pic": {
                      "type": "int",
                      "example": "1"
                    },
                    "fileId": {
                      "type": "str",
                      "example": "custom_content_img1"
                    },
                    "src": {
                      "type": "str",
                      "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img1?v=1675868589"
                    }
                  }
                },
                "img2": {
                  "type": "object",
                  "properties": {
                    "pic": {
                      "type": "int",
                      "example": "0"
                    },
                    "fileId": {
                      "type": "str",
                      "example": ""
                    },
                    "src": {
                      "type": "str",
                      "example": ""
                    }
                  }
                }
              }
            }
          ]
        },
        "custom2": {
          "oneOf": [
            {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            {
              "type": "object",
              "properties": {
                "custom": {
                  "type": "object",
                  "properties": {
                    "sort": {
                      "type": "int",
                      "example": "2"
                    },
                    "name": {
                      "type": "str",
                      "example": "論文專案"
                    },
                    "content": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "duration": {
                            "type": "object",
                            "properties": {
                              "startYear": {
                                "type": "str",
                                "example": "2022"
                              },
                              "startMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "3"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "3"
                                  }
                                }
                              },
                              "endYear": {
                                "type": "str",
                                "example": "2023"
                              },
                              "endMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "1"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "1"
                                  }
                                }
                              }
                            }
                          },
                          "isInProgress": {
                            "type": "bool",
                            "example": "False"
                          },
                          "introduction": {
                            "type": "str",
                            "example": "【慢性腎臟病與類天皰瘡發生風險之相關性：族群的世代研究】\n● 運用大數據分析慢性腎臟病與類天皰瘡的關聯性之論文\n● 臺灣慢性腎臟病盛行率達11.9%，約200萬人受此疾病所苦\n● 使用2300萬人口的數據資料，處理過數億筆資料的經驗\n● 進行研究族群之人口學特徵描述性統計、計算不同分類人口中的發生率\n● 針對慢性腎臟病與類天皰瘡進行存活分析，觀察10年期間的變化\n●進行不同組間，不同疾病、年齡、性別間的風險比計算、分層分析"
                          },
                          "url": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      }
                    }
                  }
                },
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "經典風格"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "CustomThemeClassic"
                        }
                      }
                    }
                  }
                },
                "img": {
                  "type": "object",
                  "properties": {
                    "pic": {
                      "type": "int",
                      "example": "1"
                    },
                    "fileId": {
                      "type": "str",
                      "example": "custom_content_img2"
                    },
                    "src": {
                      "type": "str",
                      "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img2?v=1675867362"
                    }
                  }
                },
                "img2": {
                  "type": "object",
                  "properties": {
                    "pic": {
                      "type": "int",
                      "example": "0"
                    },
                    "fileId": {
                      "type": "str",
                      "example": ""
                    },
                    "src": {
                      "type": "str",
                      "example": ""
                    }
                  }
                }
              }
            }
          ]
        },
        "profile": {
          "type": "object",
          "properties": {
            "uuid": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "cf3ab3b1-e057-419a-a0f2-747d778f178d"
                },
                {
                  "type": "str",
                  "example": "52bba939-8c84-49b7-9368-cfd355b724ee"
                }
              ]
            },
            "personalLink3Type": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "4"
                    },
                    {
                      "type": "int",
                      "example": "4"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "Facebook"
                    },
                    {
                      "type": "str",
                      "example": "Facebook"
                    }
                  ]
                }
              }
            },
            "signIn": {
              "oneOf": [
                {
                  "type": "bool",
                  "example": "True"
                },
                {
                  "type": "bool",
                  "example": "True"
                }
              ]
            },
            "createdAt": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "2024-02-15 15:26:08"
                },
                {
                  "type": "str",
                  "example": "2023-01-27 20:26:49"
                }
              ]
            },
            "headshotUrl": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/avatar?v=1743305442"
                },
                {
                  "type": "str",
                  "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/avatar?v=1743309994"
                }
              ]
            },
            "imageUrl": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/background_img.jpeg?v=1743305442"
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "isSelf": {
              "oneOf": [
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                }
              ]
            },
            "motto": {
              "oneOf": [
                {
                  "type": "str",
                  "example": ""
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "aboutMe": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "<p><span style=\"color: rgba(0, 0, 0, 0.9); background-color: rgb(255, 255, 255);\">Developing Deep Learning Solution : AutoEncoder or LSTM for Engineering including Wind speed or vibration signal analysis so far.</span></p><p><span style=\"color: rgba(0, 0, 0, 0.9); background-color: rgb(255, 255, 255);\">Good at 1-D Signal Processing (FFT 、wavelet Transform), ready to study 2-D Signal Processing</span></p><p><br /></p><p>Expertise: Good at Optics, <span style=\"background-color: rgb(255, 255, 255); color: rgb(77, 81, 86);\">Electromagnetism.</span></p><p>Self-Improving: learning C++, reviewing Linear Algebra, Electric knowledge after work shift.</p>"
                },
                {
                  "type": "str",
                  "example": "【急診護理師跨領域資料科學，喜歡透過數據說故事】\n我畢業於護理系曾於急診室工作，生醫資訊研究所畢業後具備健保資料庫分析與醫師合作的經驗，擅長利用SAS、R、python進行資料處理及統計分析，也上過機器與深度學習相關課程。熱愛嘗試新事物的人，不畏懼挑戰願意學習，面對問題會努力尋找解決方法，思考背後的原因，喜歡照顧別人，享受學習醫學與電腦科學相關知識，高中開始參加管樂團培養團隊合作及溝通的能力。"
                }
              ]
            },
            "isFollowingMe": {
              "oneOf": [
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                }
              ]
            },
            "followed": {
              "oneOf": [
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                }
              ]
            },
            "followerCount": {
              "oneOf": [
                {
                  "type": "int",
                  "example": "0"
                },
                {
                  "type": "int",
                  "example": "0"
                }
              ]
            },
            "abilities": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "團隊溝通"
                  },
                  {
                    "type": "str",
                    "example": "主動討論"
                  },
                  {
                    "type": "str",
                    "example": "角色適應"
                  },
                  {
                    "type": "str",
                    "example": "自強不息"
                  },
                  {
                    "type": "str",
                    "example": "持續學習"
                  },
                  {
                    "type": "str",
                    "example": "資料處理"
                  },
                  {
                    "type": "str",
                    "example": "SAS統計分析"
                  },
                  {
                    "type": "str",
                    "example": "積極主動"
                  },
                  {
                    "type": "str",
                    "example": "團隊合作"
                  },
                  {
                    "type": "str",
                    "example": "學習力佳"
                  },
                  {
                    "type": "str",
                    "example": "抗壓性高"
                  }
                ]
              }
            },
            "preferJobTitle": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "演算法工程師、軟/韌體工程師、資料科學家、後端工程師、光學(研發)工程師"
                },
                {
                  "type": "str",
                  "example": "數據分析師、資料分析師、數據工程師、統計分析師、資料科學家、SAS programmer、data analyst、data scientist、data engineer"
                }
              ]
            },
            "themeChoose": {
              "type": "object",
              "properties": {
                "selectedTheme": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "oneOf": [
                        {
                          "type": "str",
                          "example": "ProfileThemeClassic"
                        },
                        {
                          "type": "str",
                          "example": "ProfileThemeClassic"
                        }
                      ]
                    },
                    "value": {
                      "oneOf": [
                        {
                          "type": "int",
                          "example": "1"
                        },
                        {
                          "type": "int",
                          "example": "1"
                        }
                      ]
                    },
                    "text": {
                      "oneOf": [
                        {
                          "type": "str",
                          "example": "經典風格"
                        },
                        {
                          "type": "str",
                          "example": "經典風格"
                        }
                      ]
                    }
                  }
                },
                "backgroundColor": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": ""
                    },
                    {
                      "type": "str",
                      "example": ""
                    }
                  ]
                }
              }
            },
            "title": {
              "type": "object",
              "properties": {
                "degreeLevel": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "0"
                    },
                    {
                      "type": "int",
                      "example": "0"
                    }
                  ]
                },
                "jobName": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "AI工程師"
                    },
                    {
                      "type": "str",
                      "example": "研究助理"
                    }
                  ]
                },
                "majorName": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": ""
                    },
                    {
                      "type": "str",
                      "example": "生物醫學資訊研究所"
                    }
                  ]
                },
                "companyName": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "神耀科技股份有限公司"
                    },
                    {
                      "type": "str",
                      "example": "陽明交通大學生物醫學資訊所"
                    }
                  ]
                },
                "schoolName": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": ""
                    },
                    {
                      "type": "str",
                      "example": "國立陽明交通大學"
                    }
                  ]
                },
                "workExperience": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "0"
                    },
                    {
                      "type": "int",
                      "example": "0"
                    }
                  ]
                }
              }
            },
            "personalLink2Url": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "https://www.linkedin.com/in/josh-smith-706891241/"
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "viewCount": {
              "oneOf": [
                {
                  "type": "int",
                  "example": "3424"
                },
                {
                  "type": "int",
                  "example": "1566"
                }
              ]
            },
            "hasBeenRequested": {
              "oneOf": [
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                }
              ]
            },
            "publicStatus": {
              "oneOf": [
                {
                  "type": "int",
                  "example": "1"
                },
                {
                  "type": "int",
                  "example": "1"
                }
              ]
            },
            "key": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "3Cs09h2VRhp"
                },
                {
                  "type": "str",
                  "example": "1ZSUUFKUw0r"
                }
              ]
            },
            "followedCount": {
              "oneOf": [
                {
                  "type": "int",
                  "example": "0"
                },
                {
                  "type": "int",
                  "example": "0"
                }
              ]
            },
            "personalLink1Url": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "https://github.com/joshsmiththenoob"
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "personalLink3Url": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "https://www.facebook.com/profile.php?id=100002502312505"
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "nickname": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "傅騰緯"
                },
                {
                  "type": "str",
                  "example": "陳彥伶"
                }
              ]
            },
            "personalLink1Type": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "8"
                    },
                    {
                      "type": "int",
                      "example": "1"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "Github"
                    },
                    {
                      "type": "str",
                      "example": "個人網站"
                    }
                  ]
                }
              }
            },
            "hasRequestedMe": {
              "oneOf": [
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                }
              ]
            },
            "personalLink2Type": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "1"
                    },
                    {
                      "type": "int",
                      "example": "8"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "個人網站"
                    },
                    {
                      "type": "str",
                      "example": "Github"
                    }
                  ]
                }
              }
            },
            "isFollowed": {
              "oneOf": [
                {
                  "type": "bool",
                  "example": "False"
                },
                {
                  "type": "bool",
                  "example": "False"
                }
              ]
            }
          }
        },
        "skill": {
          "type": "object",
          "properties": {
            "skills": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "sort": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "4"
                      },
                      {
                        "type": "int",
                        "example": "5"
                      },
                      {
                        "type": "int",
                        "example": "6"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "4"
                      },
                      {
                        "type": "int",
                        "example": "5"
                      }
                    ]
                  },
                  "name": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Programming Language"
                      },
                      {
                        "type": "str",
                        "example": "Back-End"
                      },
                      {
                        "type": "str",
                        "example": "DataBase"
                      },
                      {
                        "type": "str",
                        "example": "AI"
                      },
                      {
                        "type": "str",
                        "example": "Engineering"
                      },
                      {
                        "type": "str",
                        "example": "Tools"
                      },
                      {
                        "type": "str",
                        "example": "程式語言"
                      },
                      {
                        "type": "str",
                        "example": "統計軟體"
                      },
                      {
                        "type": "str",
                        "example": "Microsoft Office"
                      },
                      {
                        "type": "str",
                        "example": "數據分析-全民健保資料庫"
                      },
                      {
                        "type": "str",
                        "example": "醫療護理"
                      }
                    ]
                  },
                  "status": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      }
                    ]
                  },
                  "tag": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "軟體程式設計"
                            },
                            "value": {
                              "type": "str",
                              "example": "11009005001"
                            }
                          }
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "Machine Learning"
                            },
                            "value": {
                              "type": "str",
                              "example": "11009005007"
                            }
                          }
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "Git"
                            },
                            "value": {
                              "type": "str",
                              "example": "12001002018"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "SolidWorks"
                            },
                            "value": {
                              "type": "str",
                              "example": "12002003012"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "Python"
                            },
                            "value": {
                              "type": "str",
                              "example": "12001003045"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "軟體程式設計"
                            },
                            "value": {
                              "type": "str",
                              "example": "11009005001"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "軟體工程系統開發"
                            },
                            "value": {
                              "type": "str",
                              "example": "11009002008"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "調查樣本統計分析"
                            },
                            "value": {
                              "type": "str",
                              "example": "11005004007"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "統計軟體操作"
                            },
                            "value": {
                              "type": "str",
                              "example": "11005004004"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "市場調查資料分析與報告撰寫"
                            },
                            "value": {
                              "type": "str",
                              "example": "11005004002"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "SPSS"
                            },
                            "value": {
                              "type": "str",
                              "example": "12003005011"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "SAS"
                            },
                            "value": {
                              "type": "str",
                              "example": "12003005009"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "PowerPoint"
                            },
                            "value": {
                              "type": "str",
                              "example": "12001008012"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "Excel"
                            },
                            "value": {
                              "type": "str",
                              "example": "12001008003"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "Outlook"
                            },
                            "value": {
                              "type": "str",
                              "example": "12001008011"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "文件檔案資料處理、轉換及整合工作"
                            },
                            "value": {
                              "type": "str",
                              "example": "11001005007"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "文書處理╱排版能力"
                            },
                            "value": {
                              "type": "str",
                              "example": "11001005002"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "文件或資料輸入建檔處理"
                            },
                            "value": {
                              "type": "str",
                              "example": "11001005006"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "電話接聽與人員接待事項"
                            },
                            "value": {
                              "type": "str",
                              "example": "11001005005"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "報表彙整與管理"
                            },
                            "value": {
                              "type": "str",
                              "example": "11001005004"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "文件收發與檔案管理"
                            },
                            "value": {
                              "type": "str",
                              "example": "11001005001"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "Word"
                            },
                            "value": {
                              "type": "str",
                              "example": "12001008016"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "SAS"
                            },
                            "value": {
                              "type": "str",
                              "example": "12003005009"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "撰寫研究報告與論文"
                            },
                            "value": {
                              "type": "str",
                              "example": "11017009011"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "健康問題之護理評估"
                            },
                            "value": {
                              "type": "str",
                              "example": "11007003010"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "執行靜脈或肌肉注射相關作業"
                            },
                            "value": {
                              "type": "str",
                              "example": "11012010008"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "預防保護之護理措施"
                            },
                            "value": {
                              "type": "str",
                              "example": "11012010012"
                            }
                          }
                        }
                      ]
                    }
                  },
                  "desc": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "<p>熟悉的程式語言 :</p><p>● Matlab </p><p>● Python</p><p>正在學習的程式語言:</p><p>● C++ </p>"
                      },
                      {
                        "type": "str",
                        "example": "後端網路伺服器架設技能 :\n●  Flask \n●  GCP \n●  AWS\n●  Docker\n●  Selenium \n● RESTful API"
                      },
                      {
                        "type": "str",
                        "example": "擅長使用的DB及查詢語言 : \n●  MySQL \n●  MongoDB"
                      },
                      {
                        "type": "str",
                        "example": "基礎機器學習、深度學習套件使用 :\n●  Scikit-learn\n●  Tensorflow \n●  PyTorch"
                      },
                      {
                        "type": "str",
                        "example": "<p>● Signal Processing : 目前做震動訊號處理(FFT, Hilbert Transform), Wavelet Transform, 朝向2D訊號處理學習中</p><p>● 強項為光學、電磁學</p>"
                      },
                      {
                        "type": "str",
                        "example": "<p>其他工具進行開發管理、資料視覺化或前後端整合</p><p>● Linux作業系統 (熟悉使用Ubuntu)</p><p>● Kafka 串流平台 (IoT資料即時傳輸)</p><p>● Git 版控</p><p>● LineBot</p><p>● Notion</p><p>● HackMD</p><p>● SolidWorks : 基礎3D建模</p><p>● OSLO : 幾何光學設計</p>"
                      },
                      {
                        "type": "str",
                        "example": "Python、R、SQL"
                      },
                      {
                        "type": "str",
                        "example": "SAS、SPSS、Stata"
                      },
                      {
                        "type": "str",
                        "example": "Word、Excel、PowerPoint"
                      },
                      {
                        "type": "str",
                        "example": "公共衛生與流行病學統計，利用資料庫數據分析的方法，探討疾病間的關係\n在學期間協助4篇論文分析:\n1.慢性腎臟病與類天疱瘡發生風險之相關性：族群的世代研究\n2.白斑與視網膜剝離的關聯性：全台灣人口研究調查\n3.接受系統性藥物治療的乾癬患者發生心血管疾病的風險：以臺灣人口研究\n4.類天皰瘡與各感染疾病之關係"
                      },
                      {
                        "type": "str",
                        "example": "醫學統計:熟悉健保資料庫、醫學統計相關應用\n健康照護:熟悉病人照護、護理諮詢指導、護理技術執行\n緊急醫療處理:了解緊急狀況之醫療處置及救護"
                      }
                    ]
                  }
                }
              }
            },
            "themeChoose": {
              "type": "object",
              "properties": {
                "name": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "SkillThemeCard"
                    },
                    {
                      "type": "str",
                      "example": "SkillThemeCard"
                    }
                  ]
                },
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "2"
                    },
                    {
                      "type": "int",
                      "example": "2"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "卡片式"
                    },
                    {
                      "type": "str",
                      "example": "卡片式"
                    }
                  ]
                }
              }
            }
          }
        },
        "custom3": {
          "oneOf": [
            {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            {
              "type": "object",
              "properties": {
                "custom": {
                  "type": "object",
                  "properties": {
                    "sort": {
                      "type": "int",
                      "example": "3"
                    },
                    "name": {
                      "type": "str",
                      "example": "國立陽明交通大學愛杏管弦樂團"
                    },
                    "content": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "duration": {
                            "type": "object",
                            "properties": {
                              "startYear": {
                                "type": "str",
                                "example": "2021"
                              },
                              "startMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "3"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "3"
                                  }
                                }
                              },
                              "endYear": {
                                "type": "str",
                                "example": "2023"
                              },
                              "endMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "2"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "2"
                                  }
                                }
                              }
                            }
                          },
                          "isInProgress": {
                            "type": "bool",
                            "example": "False"
                          },
                          "introduction": {
                            "type": "str",
                            "example": "【克服樂團的困境，協助建立好的風氣】\n2022/10 - 2023/02\n於加入管弦樂團後第二年遭遇團上經費嚴重不足，團員流失嚴重，因此加入幹部團隊，協助樂團行政工作。\n\n●協助招募新團員:協助發布招募團員之文案\n●尋求經費上贊助:透過統計軟體整理歷屆團員聯絡資訊，協助連絡已畢業學長姐\n●協助舉行交大陽明校區巡迴演出活動"
                          },
                          "url": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      }
                    }
                  }
                },
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "經典風格"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "CustomThemeClassic"
                        }
                      }
                    }
                  }
                },
                "img": {
                  "type": "object",
                  "properties": {
                    "pic": {
                      "type": "int",
                      "example": "1"
                    },
                    "fileId": {
                      "type": "str",
                      "example": "custom_content_img3"
                    },
                    "src": {
                      "type": "str",
                      "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img3?v=1675868597"
                    }
                  }
                },
                "img2": {
                  "type": "object",
                  "properties": {
                    "pic": {
                      "type": "int",
                      "example": "0"
                    },
                    "fileId": {
                      "type": "str",
                      "example": ""
                    },
                    "src": {
                      "type": "str",
                      "example": ""
                    }
                  }
                }
              }
            }
          ]
        },
        "structured_data_sets": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "@context": {
                "type": "str",
                "example": "http://schema.org/"
              },
              "@type": {
                "type": "str",
                "example": "Person"
              },
              "name": {
                "type": "str",
                "example": "Chun-Jung Huang"
              },
              "image": {
                "type": "str",
                "example": "https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
              },
              "description": {
                "type": "str",
                "example": "To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success."
              },
              "url": {
                "type": "str",
                "example": "https://www.cake.me/mortis-huang"
              },
              "jobTitle": {
                "type": "str",
                "example": "OPC Chief Engineer"
              },
              "sameAs": {
                "type": "str",
                "example": "https://mortis.tech/"
              }
            }
          }
        },
        "custom6": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "any"
              },
              {
                "type": "any"
              }
            ]
          }
        },
        "jobCondition": {
          "type": "object",
          "properties": {
            "workShift": {
              "oneOf": [
                {
                  "type": "int",
                  "example": "1"
                },
                {
                  "type": "int",
                  "example": "0"
                }
              ]
            },
            "remoteWork": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "1"
                    },
                    {
                      "type": "int",
                      "example": "1"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "對遠端工作有意願"
                    },
                    {
                      "type": "str",
                      "example": "對遠端工作有意願"
                    }
                  ]
                }
              }
            },
            "salaryOfHours": {
              "oneOf": [
                {
                  "type": "str",
                  "example": ""
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "otherTimePeriod": {
              "oneOf": [
                {
                  "type": "str",
                  "example": ""
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "onBoardAfterGetOffer": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "1"
                    },
                    {
                      "type": "int",
                      "example": "0"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "一週"
                    },
                    {
                      "type": "str",
                      "example": "隨時"
                    }
                  ]
                }
              }
            },
            "onBoardDate": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "1"
                    },
                    {
                      "type": "str",
                      "example": "1"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "錄取後"
                    },
                    {
                      "type": "str",
                      "example": "錄取後"
                    }
                  ]
                }
              }
            },
            "jobTimeType": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "value": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      }
                    ]
                  },
                  "text": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "全職工作"
                      },
                      {
                        "type": "str",
                        "example": "全職工作"
                      }
                    ]
                  }
                }
              }
            },
            "preferJobContent": {
              "oneOf": [
                {
                  "type": "str",
                  "example": ""
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            },
            "preferJobIndustry": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "no": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1001001000"
                      },
                      {
                        "type": "int",
                        "example": "1001004000"
                      },
                      {
                        "type": "int",
                        "example": "1004000000"
                      },
                      {
                        "type": "int",
                        "example": "1001000000"
                      },
                      {
                        "type": "int",
                        "example": "1004000000"
                      },
                      {
                        "type": "int",
                        "example": "1012000000"
                      }
                    ]
                  },
                  "des": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "軟體及網路相關業"
                      },
                      {
                        "type": "str",
                        "example": "光電及光學相關業"
                      },
                      {
                        "type": "str",
                        "example": "金融投顧及保險業"
                      },
                      {
                        "type": "str",
                        "example": "電子資訊／軟體／半導體相關業"
                      },
                      {
                        "type": "str",
                        "example": "金融投顧及保險業"
                      },
                      {
                        "type": "str",
                        "example": "醫療保健及環境衛生業"
                      }
                    ]
                  }
                }
              }
            },
            "preferJobType": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "no": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "2008001018"
                      },
                      {
                        "type": "int",
                        "example": "2008001019"
                      },
                      {
                        "type": "int",
                        "example": "2007001012"
                      },
                      {
                        "type": "int",
                        "example": "2007001006"
                      },
                      {
                        "type": "int",
                        "example": "2007001004"
                      },
                      {
                        "type": "int",
                        "example": "2016001007"
                      },
                      {
                        "type": "int",
                        "example": "2004001010"
                      },
                      {
                        "type": "int",
                        "example": "2007002002"
                      },
                      {
                        "type": "int",
                        "example": "2003002008"
                      }
                    ]
                  },
                  "des": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "光電工程師"
                      },
                      {
                        "type": "str",
                        "example": "光學工程師"
                      },
                      {
                        "type": "str",
                        "example": "演算法工程師"
                      },
                      {
                        "type": "str",
                        "example": "Internet程式設計師"
                      },
                      {
                        "type": "str",
                        "example": "軟體工程師"
                      },
                      {
                        "type": "str",
                        "example": "統計學研究員"
                      },
                      {
                        "type": "str",
                        "example": "市場調查／市場分析"
                      },
                      {
                        "type": "str",
                        "example": "資料庫管理人員"
                      },
                      {
                        "type": "str",
                        "example": "統計精算人員"
                      }
                    ]
                  }
                }
              }
            },
            "salary": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "1"
                    },
                    {
                      "type": "int",
                      "example": "1"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "面議"
                    },
                    {
                      "type": "str",
                      "example": "面議"
                    }
                  ]
                }
              }
            },
            "salariesOfYear": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "any"
                  },
                  {
                    "type": "any"
                  }
                ]
              }
            },
            "jobTimePeriod": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "value": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      }
                    ]
                  },
                  "text": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "日班"
                      },
                      {
                        "type": "str",
                        "example": "日班"
                      }
                    ]
                  }
                }
              }
            },
            "preferArea": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "no": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "6001001000"
                      },
                      {
                        "type": "int",
                        "example": "6001002000"
                      },
                      {
                        "type": "int",
                        "example": "6001005000"
                      },
                      {
                        "type": "int",
                        "example": "6001008000"
                      },
                      {
                        "type": "int",
                        "example": "6001014000"
                      },
                      {
                        "type": "int",
                        "example": "6001006000"
                      },
                      {
                        "type": "int",
                        "example": "6001001000"
                      },
                      {
                        "type": "int",
                        "example": "6001002000"
                      },
                      {
                        "type": "int",
                        "example": "6001006000"
                      }
                    ]
                  },
                  "des": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "台北市"
                      },
                      {
                        "type": "str",
                        "example": "新北市"
                      },
                      {
                        "type": "str",
                        "example": "桃園市"
                      },
                      {
                        "type": "str",
                        "example": "台中市"
                      },
                      {
                        "type": "str",
                        "example": "台南市"
                      },
                      {
                        "type": "str",
                        "example": "新竹縣市"
                      },
                      {
                        "type": "str",
                        "example": "台北市"
                      },
                      {
                        "type": "str",
                        "example": "新北市"
                      },
                      {
                        "type": "str",
                        "example": "新竹縣市"
                      }
                    ]
                  }
                }
              }
            },
            "salaryPeriod": {
              "type": "object",
              "properties": {
                "value": {
                  "oneOf": [
                    {
                      "type": "int",
                      "example": "5"
                    },
                    {
                      "type": "int",
                      "example": "5"
                    }
                  ]
                },
                "text": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "月薪"
                    },
                    {
                      "type": "str",
                      "example": "月薪"
                    }
                  ]
                }
              }
            },
            "customOnBoardDate": {
              "type": "object",
              "properties": {
                "date": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "any"
                      },
                      {
                        "type": "any"
                      }
                    ]
                  }
                },
                "month": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "any"
                      },
                      {
                        "type": "any"
                      }
                    ]
                  }
                },
                "year": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": ""
                    },
                    {
                      "type": "str",
                      "example": ""
                    }
                  ]
                }
              }
            },
            "preferJobTitle": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "演算法工程師、軟/韌體工程師、資料科學家、後端工程師、光學(研發)工程師"
                },
                {
                  "type": "str",
                  "example": "數據分析師、資料分析師、數據工程師、統計分析師、資料科學家、SAS programmer、data analyst、data scientist、data engineer"
                }
              ]
            },
            "salaryOfMonth": {
              "type": "object",
              "properties": {
                "unitOfThousand": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "any"
                      },
                      {
                        "type": "any"
                      }
                    ]
                  }
                },
                "unitOfTenThousand": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "any"
                      },
                      {
                        "type": "any"
                      }
                    ]
                  }
                }
              }
            }
          }
        },
        "item": {
          "type": "object",
          "properties": {
            "id": {
              "type": "int",
              "example": "1002587"
            },
            "name": {
              "type": "str",
              "example": "My CakeResume"
            },
            "description": {
              "type": "str",
              "example": "Chun-Jung Huang mortis.huang@gmail.comNational Chiao-Tung University, Ph.D. - Photonics,2015 ~ 2020 Member of The Phi Tau Phi Scholastic Honor Soci..."
            },
            "path": {
              "type": "str",
              "example": "mortis-huang"
            },
            "liked": {
              "type": "bool",
              "example": "False"
            },
            "is_owner": {
              "type": "bool",
              "example": "False"
            },
            "added_to_folder": {
              "type": "bool",
              "example": "False"
            },
            "votes_total": {
              "type": "int",
              "example": "38"
            },
            "lang": {
              "type": "str",
              "example": "en"
            },
            "theme": {
              "type": "str",
              "example": "default"
            },
            "editor_version": {
              "type": "int",
              "example": "0"
            },
            "style": {
              "type": "str",
              "example": "paper"
            },
            "style_config": {
              "type": "object",
              "properties": {}
            },
            "spacing": {
              "type": "str",
              "example": "normal"
            },
            "connected_with_posts": {
              "type": "bool",
              "example": "False"
            },
            "seems_spam": {
              "type": "bool",
              "example": "False"
            },
            "should_confirm_external_links": {
              "type": "bool",
              "example": "False"
            },
            "system_generated": {
              "type": "bool",
              "example": "False"
            },
            "exported_from_profile": {
              "type": "bool",
              "example": "True"
            },
            "body": {
              "type": "str",
              "example": "<div class=\"row snippet-profile-041\"><div class=\"col-sm-8\"><h1><b>Chun-Jung Huang</b></h1><p>mortis.huang@gmail.com</p><p>&nbsp;(+886)-988-728-641</p><p>National Chiao-Tung University, Ph.D. - Photonics,2015 ~ 2020&nbsp;</p><p>Member of The Phi Tau Phi Scholastic Honor Society of the Republic of China.<br></p></div><div class=\"col-sm-4\"><img data-no-retina=\"true\" src=\"https://images.cakeresume.com/XgMVZ/mortis-huang/191caa57-6fe0-4fd6-9b12-a9ce4ebafc0f.png\" style=\"border-radius: 0px;\" loading=\"\"></div></div><div class=\"row snippet-features-001\"><div class=\"col-sm-12\"><div class=\"row\"><div class=\"col-sm-12\"><h1><b>Skills</b></h1></div></div><div class=\"row\" title=\"\"><div class=\"col-sm-12 item\"><hr><p><b>Languages:</b> Python, MatLab, Shell scripting, LabVIEW&nbsp;</p><p><b>Deep Learning:</b> Proficient in CNNs, LLM development, and deployment.&nbsp;</p><p><b>GPU Programming: </b>Python CPU to GPU migration and acceleration optimization.&nbsp;</p><p><b>Developer Tools:</b>&nbsp;Obsidian, Nsight Systems, pdb (python debugger), and Git.\n\n</p></div></div></div></div><div class=\"row snippet-experiences-013\"><div class=\"col-xs-12\"><div class=\"row\"><div class=\"col-xs-12\"><h1><b>Work Experience</b><br></h1></div></div><div class=\"row\" title=\"\"><div class=\"col-xs-2 col-sm-1 item-bullet\"></div><div class=\"col-xs-10 col-sm-11 item\"><h3>TSMC, nPtD/OPC-III Chief Engineer (March 2020 - Now)</h3><p><b>- Advanced CNN Applications:</b>&nbsp;</p><p>Integrated CNNs for enhanced anomaly detection and image processing.<br></p><p><b>- Localization of LLM:</b>&nbsp;</p><p>Customized large language models to meet specific operational needs, enhancing internal AI capabilities.<br></p><p><b>- GPU Acceleration:&nbsp;</b></p><p>Directed the migration of large Python codebases from CPU to GPU, leveraging CuPy API, cp.fuse, and RawKernel to optimize performance and reduce runtime by over 50%.<br></p></div></div><div class=\"row\" title=\"\"><div class=\"col-xs-2 col-sm-1 item-bullet\"></div><div class=\"col-xs-10 col-sm-11 item\"><h3> The University of Tokyo, Foreign Researcher (Oct. 2017 - Sep. 2018)</h3><p>Developed a CNN-based cell image recognition system from scratch, contributing to advancements in biomedical imaging and analysis.<br></p></div></div></div></div><div class=\"row snippet-educations-013 snippet-experiences-013\"><div class=\"col-xs-12\"><div class=\"row\"><div class=\"col-xs-12\"><h1><b>Education</b><br></h1></div></div><div class=\"row\" title=\"\"><div class=\"col-xs-2 col-sm-1 item-bullet\"></div><div class=\"col-xs-10 col-sm-11 item\"><h3><b>National Chiao-Tung University, Ph.D. - Photonics, 2015 ~ 2020</b></h3><p>Development of Intelligent Wearable Near Infrared Spectroscopy</p></div></div><div class=\"row\" title=\"\"><div class=\"col-xs-2 col-sm-1 item-bullet\"></div><div class=\"col-xs-10 col-sm-11 item\"><h3><b>National Chiao-Tung University, Bachelor - Photonics, 2011 ~ 2015</b></h3></div></div></div></div><div class=\"row snippet-paragraphs-001\"><div class=\"col-xs-12\"><h1><b>Main Publications</b></h1><ul><li>Virtual-freezing fluorescence imaging flow cytometry - <b>Nature communications</b>&nbsp;(IF:14.9) - 2020&nbsp;<br></li><li>Intelligent classification of platelet aggregates by agonist type - <b>Elife</b> (IF:8.14) - 2020<br></li><li>Label-free chemical imaging flow cytometry by high-speed multicolor stimulated Raman scattering - <b>PNAS</b> (IF:11.2) - 2019<br></li><li>Functional connectivity during phonemic and semantic verbal fluency test: a multichannel near infrared spectroscopy study -<b> JSTQE&nbsp;</b>(IF:4.5)&nbsp;- 2015<br></li></ul><p></p></div></div>"
            },
            "body_json_v2": {
              "type": "NoneType",
              "example": "None"
            },
            "user": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "str",
                  "example": "Chun-Jung Huang"
                },
                "username": {
                  "type": "str",
                  "example": "mortis-huang"
                },
                "id": {
                  "type": "int",
                  "example": "669487"
                },
                "first_name": {
                  "type": "str",
                  "example": "Chun-Jung"
                },
                "last_name": {
                  "type": "str",
                  "example": "Huang"
                },
                "description": {
                  "type": "str",
                  "example": "To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success."
                },
                "cover_image": {
                  "type": "object",
                  "properties": {
                    "url": {
                      "type": "str",
                      "example": "https://media.cakeresume.com/image/upload/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                    },
                    "small": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/c_crop,h_360,w_720/c_scale,h_180,w_360/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    },
                    "medium": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--Vm8J95tp--/c_fill,h_360,w_720/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    },
                    "large": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--VrSkpH3n--/c_fill,h_500,w_1500/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    },
                    "small_3_1": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--YGPutB6G--/c_fill,f_auto,h_140,w_420/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    },
                    "medium_3_1": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--6GTJ9tLF--/c_fill,f_auto,h_314,w_942/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    }
                  }
                },
                "avatar": {
                  "type": "object",
                  "properties": {
                    "url": {
                      "type": "str",
                      "example": "https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                    },
                    "tiny": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    },
                    "small": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    },
                    "medium": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    },
                    "large": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--9QlfPnJO--/c_fill,g_face,h_300,w_300/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    },
                    "xlarge": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--1eTMbnTr--/c_fill,g_face,h_600,w_600/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    }
                  }
                },
                "avatar_tiny_url": {
                  "type": "str",
                  "example": "https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                },
                "avatar_small_url": {
                  "type": "str",
                  "example": "https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                },
                "avatar_medium_url": {
                  "type": "str",
                  "example": "https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                },
                "has_phone": {
                  "type": "bool",
                  "example": "True"
                },
                "has_email": {
                  "type": "bool",
                  "example": "True"
                },
                "main_public_item_path": {
                  "type": "str",
                  "example": "mortis-huang"
                },
                "main_signed_url_non_hidden_item_path": {
                  "type": "NoneType",
                  "example": "None"
                },
                "posts_count": {
                  "type": "int",
                  "example": "0"
                },
                "published_posts_count": {
                  "type": "int",
                  "example": "0"
                },
                "profile_privacy_level": {
                  "type": "str",
                  "example": "public"
                },
                "online_status": {
                  "type": "str",
                  "example": "offline"
                },
                "recommendee_token": {
                  "type": "str",
                  "example": "56Vxmbj3Wn3YaZMkl0L2GP"
                },
                "public_recommendations_count": {
                  "type": "int",
                  "example": "0"
                },
                "mutual_connections_count": {
                  "type": "bool",
                  "example": "False"
                },
                "unique_impressions_count": {
                  "type": "int",
                  "example": "2380"
                },
                "is_premium": {
                  "type": "bool",
                  "example": "False"
                },
                "no_branding": {
                  "type": "bool",
                  "example": "False"
                },
                "seems_spam": {
                  "type": "bool",
                  "example": "False"
                },
                "desired_job_type": {
                  "type": "str",
                  "example": "full_time"
                },
                "job_search_progress": {
                  "type": "str",
                  "example": "ready_to_interview"
                },
                "current_employment_status": {
                  "type": "str",
                  "example": "employed"
                },
                "is_freelancer": {
                  "type": "str",
                  "example": "part_time_freelancer"
                },
                "work_experience": {
                  "type": "str",
                  "example": "four_six"
                },
                "relevant_work_experience": {
                  "type": "str",
                  "example": "four_six"
                },
                "desired_position": {
                  "type": "str",
                  "example": "AI工程師、機器學習工程師、深度學習工程師、資料科學家、Machine Learning Engineer、Deep Learning Engineer、Data Scientist"
                },
                "role": {
                  "type": "str",
                  "example": "Ph.D."
                },
                "languages": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "English,3"
                      },
                      {
                        "type": "str",
                        "example": "Chinese,4"
                      }
                    ]
                  }
                },
                "remote": {
                  "type": "str",
                  "example": "interested"
                },
                "country": {
                  "type": "str",
                  "example": "TW"
                },
                "city": {
                  "type": "NoneType",
                  "example": "None"
                },
                "city_name": {
                  "type": "NoneType",
                  "example": "None"
                },
                "city_name_en": {
                  "type": "NoneType",
                  "example": "None"
                },
                "google_place_id": {
                  "type": "str",
                  "example": "ChIJoSFawR-waDQR-6m5DFTfH-8"
                },
                "google_place_name": {
                  "type": "str",
                  "example": "Taiwan, 台灣"
                },
                "google_place_name_en": {
                  "type": "str",
                  "example": "Taiwan, 台灣"
                },
                "google_place_country_name_en": {
                  "type": "str",
                  "example": "Taiwan"
                },
                "google_place_region_name_en": {
                  "type": "str",
                  "example": "Taiwan Province"
                },
                "desired_location_google_place_ids": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "ChIJL1cHXAbzbjQRaVScvwTwEec"
                      },
                      {
                        "type": "str",
                        "example": "ChIJLxl_1w9OZzQRRFJmfNR1QvU"
                      },
                      {
                        "type": "str",
                        "example": "ChIJdZOLiiMR2jERxPWrUs9peIg"
                      }
                    ]
                  }
                },
                "desired_location_names": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Taiwan"
                      },
                      {
                        "type": "str",
                        "example": "Japan"
                      },
                      {
                        "type": "str",
                        "example": "Singapore"
                      }
                    ]
                  }
                },
                "desired_location_names_en": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Taiwan"
                      },
                      {
                        "type": "str",
                        "example": "Japan"
                      },
                      {
                        "type": "str",
                        "example": "Singapore"
                      }
                    ]
                  }
                },
                "desired_location_country_names_en": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Taiwan"
                      },
                      {
                        "type": "str",
                        "example": "Japan"
                      },
                      {
                        "type": "str",
                        "example": "Singapore"
                      }
                    ]
                  }
                },
                "desired_location_region_names_en": {
                  "type": "array",
                  "items": {
                    "type": "NoneType",
                    "example": "None"
                  }
                },
                "cr_location": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "str",
                      "example": "ChIJoSFawR-waDQR-6m5DFTfH-8"
                    },
                    "full_name": {
                      "type": "str",
                      "example": "Taiwan, 台灣"
                    },
                    "country": {
                      "type": "str",
                      "example": "Taiwan"
                    },
                    "admin_level_1": {
                      "type": "str",
                      "example": "Taiwan Province"
                    },
                    "locale": {
                      "type": "str",
                      "example": "zh-TW"
                    }
                  }
                },
                "cr_desired_locations": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "str",
                            "example": "ChIJL1cHXAbzbjQRaVScvwTwEec"
                          },
                          "full_name": {
                            "type": "str",
                            "example": "Taiwan"
                          },
                          "country": {
                            "type": "str",
                            "example": "Taiwan"
                          },
                          "admin_level_1": {
                            "type": "NoneType",
                            "example": "None"
                          },
                          "locale": {
                            "type": "str",
                            "example": "en"
                          }
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "str",
                            "example": "ChIJLxl_1w9OZzQRRFJmfNR1QvU"
                          },
                          "full_name": {
                            "type": "str",
                            "example": "Japan"
                          },
                          "country": {
                            "type": "str",
                            "example": "Japan"
                          },
                          "admin_level_1": {
                            "type": "NoneType",
                            "example": "None"
                          },
                          "locale": {
                            "type": "str",
                            "example": "en"
                          }
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "str",
                            "example": "ChIJdZOLiiMR2jERxPWrUs9peIg"
                          },
                          "full_name": {
                            "type": "str",
                            "example": "Singapore"
                          },
                          "country": {
                            "type": "str",
                            "example": "Singapore"
                          },
                          "admin_level_1": {
                            "type": "NoneType",
                            "example": "None"
                          },
                          "locale": {
                            "type": "str",
                            "example": "en"
                          }
                        }
                      }
                    ]
                  }
                },
                "eligible_work_locations": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                },
                "graduated_from_school": {
                  "type": "str",
                  "example": "National Chiao-Tung University"
                },
                "graduated_from_field": {
                  "type": "str",
                  "example": "Ph.D. - Clinical Engineering"
                },
                "skill_list": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Python"
                      },
                      {
                        "type": "str",
                        "example": "GPU"
                      },
                      {
                        "type": "str",
                        "example": "Machine Learning"
                      },
                      {
                        "type": "str",
                        "example": "AI"
                      },
                      {
                        "type": "str",
                        "example": "Linux OS"
                      },
                      {
                        "type": "str",
                        "example": "Automation"
                      },
                      {
                        "type": "str",
                        "example": "GPU Programming HPC"
                      }
                    ]
                  }
                },
                "professions": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "it_machine-learning-engineer"
                      },
                      {
                        "type": "str",
                        "example": "it_python-developer"
                      },
                      {
                        "type": "str",
                        "example": "it_semiconductor-engineering"
                      }
                    ]
                  }
                },
                "industries": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "tech_semiconductor"
                      },
                      {
                        "type": "str",
                        "example": "tech_artificial-intelligence-machine-learning"
                      }
                    ]
                  }
                },
                "headline": {
                  "type": "str",
                  "example": "Ph.D."
                },
                "number_of_management": {
                  "type": "str",
                  "example": "one_five"
                },
                "education_level": {
                  "type": "str",
                  "example": "doctoral"
                },
                "last_seen_at_days_ago_level": {
                  "type": "int",
                  "example": "30"
                },
                "network_profile": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "str",
                      "example": "zbXd"
                    },
                    "avatar": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/v1704774606/eamlf29dbenp1ll63knm.jpg"
                        },
                        "tiny": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--z9cNBI1Q--/c_fill,g_face,h_24,w_24/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        },
                        "small": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--wg4dVaga--/c_fill,g_face,h_60,w_60/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        },
                        "medium": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--1AVroZGi--/c_fill,g_face,h_120,w_120/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        },
                        "large": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--KsOWQeOQ--/c_fill,g_face,h_300,w_300/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        },
                        "xlarge": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--echNo8F4--/c_fill,g_face,h_600,w_600/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        }
                      }
                    },
                    "status": {
                      "type": "str",
                      "example": "published"
                    },
                    "description": {
                      "type": "str",
                      "example": "交大Ph.D.\n台積電OPC\nMachine Learning Solutions"
                    },
                    "identity_types": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "mentor"
                          },
                          {
                            "type": "str",
                            "example": "job_seeker"
                          },
                          {
                            "type": "str",
                            "example": "professional"
                          }
                        ]
                      }
                    },
                    "topics_to_learn": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "job_openings"
                          },
                          {
                            "type": "str",
                            "example": "company_insights"
                          },
                          {
                            "type": "str",
                            "example": "skills_development"
                          }
                        ]
                      }
                    },
                    "topics_to_share": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "company_insights"
                          },
                          {
                            "type": "str",
                            "example": "skills_development"
                          }
                        ]
                      }
                    },
                    "tags": {
                      "type": "array",
                      "items": {
                        "type": "any"
                      }
                    },
                    "badges": {
                      "type": "array",
                      "items": {
                        "type": "any"
                      }
                    },
                    "suspended": {
                      "type": "bool",
                      "example": "False"
                    },
                    "user": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "str",
                          "example": "Chun-Jung Huang"
                        },
                        "username": {
                          "type": "str",
                          "example": "mortis-huang"
                        },
                        "first_name": {
                          "type": "str",
                          "example": "Chun-Jung"
                        },
                        "last_name": {
                          "type": "str",
                          "example": "Huang"
                        },
                        "description": {
                          "type": "str",
                          "example": "To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success."
                        },
                        "cover_image": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                            },
                            "small": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/c_crop,h_360,w_720/c_scale,h_180,w_360/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            },
                            "medium": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--Vm8J95tp--/c_fill,h_360,w_720/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            },
                            "large": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--VrSkpH3n--/c_fill,h_500,w_1500/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            },
                            "small_3_1": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--YGPutB6G--/c_fill,f_auto,h_140,w_420/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            },
                            "medium_3_1": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--6GTJ9tLF--/c_fill,f_auto,h_314,w_942/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            }
                          }
                        },
                        "avatar": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                            },
                            "tiny": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            },
                            "small": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            },
                            "medium": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            },
                            "large": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--9QlfPnJO--/c_fill,g_face,h_300,w_300/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            },
                            "xlarge": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--1eTMbnTr--/c_fill,g_face,h_600,w_600/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            }
                          }
                        },
                        "avatar_tiny_url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        },
                        "avatar_small_url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        },
                        "avatar_medium_url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        },
                        "profile_privacy_level": {
                          "type": "str",
                          "example": "public"
                        },
                        "online_status": {
                          "type": "str",
                          "example": "offline"
                        },
                        "current_job_title": {
                          "type": "str",
                          "example": "OPC Chief Engineer"
                        },
                        "current_company": {
                          "type": "str",
                          "example": "TSMC"
                        },
                        "headline": {
                          "type": "str",
                          "example": "Ph.D."
                        },
                        "is_premium": {
                          "type": "bool",
                          "example": "False"
                        },
                        "status": {
                          "type": "str",
                          "example": "created"
                        }
                      }
                    },
                    "review_application": {
                      "type": "object",
                      "properties": {
                        "precedence": {
                          "type": "int",
                          "example": "-12551"
                        },
                        "status": {
                          "type": "str",
                          "example": "approved"
                        },
                        "reject_reason": {
                          "type": "NoneType",
                          "example": "None"
                        },
                        "reject_details": {
                          "type": "NoneType",
                          "example": "None"
                        }
                      }
                    }
                  }
                },
                "most_recent_work_experience": {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "str",
                      "example": "OPC Chief Engineer"
                    },
                    "currently_work_here": {
                      "type": "bool",
                      "example": "True"
                    },
                    "from_year": {
                      "type": "int",
                      "example": "2020"
                    },
                    "from_month": {
                      "type": "int",
                      "example": "3"
                    },
                    "end_year": {
                      "type": "NoneType",
                      "example": "None"
                    },
                    "end_month": {
                      "type": "NoneType",
                      "example": "None"
                    },
                    "organization": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "str",
                          "example": "TSMC"
                        },
                        "id": {
                          "type": "int",
                          "example": "464650"
                        },
                        "logo": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/v1604585338/pbqvfhcwccdzrdu0tved.png"
                            },
                            "tiny": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--PSVTyqPa--/c_pad,fl_png8,h_60,w_60/v1604585338/pbqvfhcwccdzrdu0tved.png"
                                }
                              }
                            },
                            "thumb": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--o7W3GKLx--/c_pad,fl_png8,h_100,w_100/v1604585338/pbqvfhcwccdzrdu0tved.png"
                                }
                              }
                            },
                            "medium": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--nGEg_GN8--/c_pad,fl_png8,h_200,w_200/v1604585338/pbqvfhcwccdzrdu0tved.png"
                                }
                              }
                            },
                            "large": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "NoneType",
                                  "example": "None"
                                }
                              }
                            },
                            "og_image": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "NoneType",
                                  "example": "None"
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "most_recent_education": {
                  "type": "object",
                  "properties": {
                    "degree_type": {
                      "type": "str",
                      "example": "doctor_of_philosophy_phd"
                    },
                    "majors": {
                      "type": "array",
                      "items": {
                        "type": "str",
                        "example": "Ph.D. - Clinical Engineering"
                      }
                    },
                    "from_year": {
                      "type": "int",
                      "example": "2015"
                    },
                    "end_year": {
                      "type": "int",
                      "example": "2020"
                    },
                    "organization": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "str",
                          "example": "National Chiao-Tung University"
                        },
                        "id": {
                          "type": "int",
                          "example": "464666"
                        },
                        "logo": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/v1604586192/jjunzkeazgfytbttav1t.png"
                            },
                            "tiny": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--7rkjq4Gg--/c_pad,fl_png8,h_60,w_60/v1604586192/jjunzkeazgfytbttav1t.png"
                                }
                              }
                            },
                            "thumb": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--1qBAGmIY--/c_pad,fl_png8,h_100,w_100/v1604586192/jjunzkeazgfytbttav1t.png"
                                }
                              }
                            },
                            "medium": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--7OjsoMvQ--/c_pad,fl_png8,h_200,w_200/v1604586192/jjunzkeazgfytbttav1t.png"
                                }
                              }
                            },
                            "large": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "NoneType",
                                  "example": "None"
                                }
                              }
                            },
                            "og_image": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "NoneType",
                                  "example": "None"
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            },
            "use_signed_url": {
              "type": "bool",
              "example": "False"
            },
            "no_branding": {
              "type": "bool",
              "example": "False"
            },
            "privacy_level": {
              "type": "int",
              "example": "0"
            },
            "signed_or_not_item_url": {
              "type": "str",
              "example": "https://www.cake.me/mortis-huang"
            },
            "metadata": {
              "type": "object",
              "properties": {
                "images": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "src": {
                        "type": "str",
                        "example": "https://images.cakeresume.com/XgMVZ/mortis-huang/191caa57-6fe0-4fd6-9b12-a9ce4ebafc0f.png"
                      },
                      "width": {
                        "type": "int",
                        "example": "564"
                      },
                      "height": {
                        "type": "int",
                        "example": "318"
                      }
                    }
                  }
                }
              }
            },
            "ga_tracking_code": {
              "type": "NoneType",
              "example": "None"
            },
            "has_permission_ga": {
              "type": "bool",
              "example": "False"
            },
            "draft_update_count": {
              "type": "int",
              "example": "429"
            }
          }
        },
        "meta_tags": {
          "type": "object",
          "properties": {
            "title": {
              "type": "str",
              "example": "Chun-Jung Huang"
            },
            "description": {
              "type": "str",
              "example": "To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success."
            },
            "canonical": {
              "type": "str",
              "example": "https://www.cake.me/mortis-huang"
            },
            "og": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "str",
                  "example": "profile"
                },
                "image": {
                  "type": "str",
                  "example": "https://media.cakeresume.com/image/url2png/s--cuUyBM8A--/c_crop,g_north,h_751,w_992/c_fit,g_north,h_606,w_800/b_rgb:F0F2F1,c_lpad,g_south,h_630,w_1200/l_fetch:aHR0cHM6Ly93d3cuY2FrZXJlc3VtZS5jb20vZmF2aWNvbnMvbXN0aWxlLTMxMHgzMTAucG5n/c_scale,w_103/fl_layer_apply,g_north_west,x_0,y_0/fl_png8/https://www.cake.me/mortis-huang%3Fno-page-layout%3Dtrue%26v%3D1/url2png/viewport%3D1480x1800%7Cfullpage%3Dfalse%7Cunique%3D958442"
                }
              }
            },
            "nofollow": {
              "type": "bool",
              "example": "True"
            },
            "noindex": {
              "type": "bool",
              "example": "False"
            },
            "amphtml": {
              "type": "str",
              "example": "https://www.cake.me/mortis-huang.amp"
            }
          }
        },
        "custom4": {
          "oneOf": [
            {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            {
              "type": "object",
              "properties": {
                "custom": {
                  "type": "object",
                  "properties": {
                    "sort": {
                      "type": "int",
                      "example": "4"
                    },
                    "name": {
                      "type": "str",
                      "example": "長庚大學管樂團"
                    },
                    "content": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "duration": {
                            "type": "object",
                            "properties": {
                              "startYear": {
                                "type": "str",
                                "example": "2015"
                              },
                              "startMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "9"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "9"
                                  }
                                }
                              },
                              "endYear": {
                                "type": "str",
                                "example": "2019"
                              },
                              "endMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "6"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "6"
                                  }
                                }
                              }
                            }
                          },
                          "isInProgress": {
                            "type": "bool",
                            "example": "False"
                          },
                          "introduction": {
                            "type": "str",
                            "example": "【創造樂團輝煌時代】\n2016/6-2017/6\n接管幹部時，經歷團上意見紛歧、大家對於比賽想法不同等問題，與團隊一起努力透過溝通，把樂團創經營的更好更有向心力，經費與團員更加充足，且於全國比賽獲得佳績。\n\n●擔任社團幹部:負責藏譜管理、參與會議討論\n●管樂週以及校慶擺攤活動總召:利用中午時間與一般學生宣傳管樂團的特色、安排午餐音樂會、協助甜點販賣，一週為社團賺進2萬元的資金、校慶擺攤一個下午有4千元的業績\n● 參與4年度的全國學生音樂團體比賽:獲得三年學生音樂比賽優等，一年全國賽特優的佳績。"
                          },
                          "url": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      }
                    }
                  }
                },
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "經典風格"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "CustomThemeClassic"
                        }
                      }
                    }
                  }
                },
                "img": {
                  "type": "object",
                  "properties": {
                    "pic": {
                      "type": "int",
                      "example": "1"
                    },
                    "fileId": {
                      "type": "str",
                      "example": "custom_content_img4"
                    },
                    "src": {
                      "type": "str",
                      "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img4?v=1675868603"
                    }
                  }
                },
                "img2": {
                  "type": "object",
                  "properties": {
                    "pic": {
                      "type": "int",
                      "example": "0"
                    },
                    "fileId": {
                      "type": "str",
                      "example": ""
                    },
                    "src": {
                      "type": "str",
                      "example": ""
                    }
                  }
                }
              }
            }
          ]
        },
        "education": {
          "type": "object",
          "properties": {
            "educations": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "duration": {
                    "type": "object",
                    "properties": {
                      "startMonth": {
                        "type": "object",
                        "properties": {
                          "value": {
                            "oneOf": [
                              {
                                "type": "int",
                                "example": "9"
                              },
                              {
                                "type": "int",
                                "example": "9"
                              },
                              {
                                "type": "int",
                                "example": "3"
                              },
                              {
                                "type": "int",
                                "example": "9"
                              }
                            ]
                          },
                          "text": {
                            "oneOf": [
                              {
                                "type": "str",
                                "example": "9"
                              },
                              {
                                "type": "str",
                                "example": "9"
                              },
                              {
                                "type": "str",
                                "example": "3"
                              },
                              {
                                "type": "str",
                                "example": "9"
                              }
                            ]
                          }
                        }
                      },
                      "startYear": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "2017"
                          },
                          {
                            "type": "str",
                            "example": "2013"
                          },
                          {
                            "type": "str",
                            "example": "2021"
                          },
                          {
                            "type": "str",
                            "example": "2015"
                          }
                        ]
                      },
                      "endMonth": {
                        "type": "object",
                        "properties": {
                          "value": {
                            "oneOf": [
                              {
                                "type": "int",
                                "example": "1"
                              },
                              {
                                "type": "int",
                                "example": "6"
                              },
                              {
                                "type": "int",
                                "example": "2"
                              },
                              {
                                "type": "int",
                                "example": "6"
                              }
                            ]
                          },
                          "text": {
                            "oneOf": [
                              {
                                "type": "str",
                                "example": "1"
                              },
                              {
                                "type": "str",
                                "example": "6"
                              },
                              {
                                "type": "str",
                                "example": "2"
                              },
                              {
                                "type": "str",
                                "example": "6"
                              }
                            ]
                          }
                        }
                      },
                      "endYear": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "2022"
                          },
                          {
                            "type": "str",
                            "example": "2017"
                          },
                          {
                            "type": "str",
                            "example": "2023"
                          },
                          {
                            "type": "str",
                            "example": "2019"
                          }
                        ]
                      }
                    }
                  },
                  "highest": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "3"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "3"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "碩士"
                          },
                          {
                            "type": "str",
                            "example": "大學"
                          },
                          {
                            "type": "str",
                            "example": "碩士"
                          },
                          {
                            "type": "str",
                            "example": "大學"
                          }
                        ]
                      }
                    }
                  },
                  "inSchoolStatus": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        }
                      ]
                    }
                  },
                  "schoolId": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "5023000000"
                      },
                      {
                        "type": "int",
                        "example": "5030000000"
                      },
                      {
                        "type": "int",
                        "example": "5180000000"
                      },
                      {
                        "type": "int",
                        "example": "5065000000"
                      }
                    ]
                  },
                  "foreign": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        },
                        {
                          "type": "any"
                        }
                      ]
                    }
                  },
                  "sort": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      }
                    ]
                  },
                  "name": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "國立臺北科技大學"
                      },
                      {
                        "type": "str",
                        "example": "國立聯合大學"
                      },
                      {
                        "type": "str",
                        "example": "國立陽明交通大學"
                      },
                      {
                        "type": "str",
                        "example": "長庚大學"
                      }
                    ]
                  },
                  "departments": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "光電工程系"
                            },
                            {
                              "type": "str",
                              "example": "光電工程學系"
                            },
                            {
                              "type": "str",
                              "example": "生物醫學資訊研究所"
                            },
                            {
                              "type": "str",
                              "example": "護理學系"
                            }
                          ]
                        },
                        "type": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "no": {
                                "oneOf": [
                                  {
                                    "type": "int",
                                    "example": "3011016000"
                                  },
                                  {
                                    "type": "int",
                                    "example": "3011016000"
                                  },
                                  {
                                    "type": "int",
                                    "example": "3009009000"
                                  },
                                  {
                                    "type": "int",
                                    "example": "3009005000"
                                  }
                                ]
                              },
                              "des": {
                                "oneOf": [
                                  {
                                    "type": "str",
                                    "example": "光電工程相關"
                                  },
                                  {
                                    "type": "str",
                                    "example": "光電工程相關"
                                  },
                                  {
                                    "type": "str",
                                    "example": "醫藥工程相關"
                                  },
                                  {
                                    "type": "str",
                                    "example": "護理助產相關"
                                  }
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  },
                  "status": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "畢業"
                          },
                          {
                            "type": "str",
                            "example": "畢業"
                          },
                          {
                            "type": "str",
                            "example": "畢業"
                          },
                          {
                            "type": "str",
                            "example": "畢業"
                          }
                        ]
                      }
                    }
                  },
                  "region": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "7001053000"
                          },
                          {
                            "type": "int",
                            "example": "7001053000"
                          },
                          {
                            "type": "int",
                            "example": "7001053000"
                          },
                          {
                            "type": "int",
                            "example": "7001053000"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "台灣"
                          },
                          {
                            "type": "str",
                            "example": "台灣"
                          },
                          {
                            "type": "str",
                            "example": "台灣"
                          },
                          {
                            "type": "str",
                            "example": "台灣"
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "publicStatus": {
          "oneOf": [
            {
              "type": "int",
              "example": "1"
            },
            {
              "type": "int",
              "example": "1"
            }
          ]
        },
        "project": {
          "oneOf": [
            {
              "type": "object",
              "properties": {
                "projects": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "object",
                        "properties": {
                          "sort": {
                            "type": "int",
                            "example": "1"
                          },
                          "name": {
                            "type": "str",
                            "example": "Let's Dance - 舞蹈評分系統"
                          },
                          "duration": {
                            "type": "object",
                            "properties": {
                              "startYear": {
                                "type": "str",
                                "example": "2022"
                              },
                              "startMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "11"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "11"
                                  }
                                }
                              },
                              "endYear": {
                                "type": "str",
                                "example": "2023"
                              },
                              "endMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "1"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "1"
                                  }
                                }
                              }
                            }
                          },
                          "isInProgress": {
                            "type": "bool",
                            "example": "False"
                          },
                          "introduction": {
                            "type": "str",
                            "example": "疫情下，為了滿足消費者對於室內運動和娛樂的需求，團隊推出了「Let's Dance : 舞蹈評分系統」的桌面應用\n- 專案擔任角色 : GUI呈現\n  ● 系統整合 : 將遊戲中四大功能整合成桌面應用\n  ● threading : 平行化技術實現遊戲多工特性\n  ● PyQt5 :  Qt結合上面兩項任務，創建桌面GUI ， 供使用者更直觀的體驗\n\n- 遊戲其他功能\n  ● 臉部辨識系統 : 以face_recognition人臉辨識模型為基礎製作人臉辨識系統，並與資料庫串接\n  ● 舞蹈評分系統 : Mediapipe 體態辨識模型實現使用者 - 教練 姿勢即時比對系統\n  ● AI 體感操作模型 : Mediapipe+DNN網路 實現使用者以體感操作GUI介面的功能\n  ● 資料庫 : 使用於GCP上建立MySQL資料庫，以記錄玩家個人資訊、歷史分數等相關資料，以GUI顯示分數排名"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://drive.google.com/file/d/1XdSRXETPWzP6Vd9y1L78KHUpwhe4tnCl/view?usp=sharing"
                          },
                          "img": {
                            "type": "object",
                            "properties": {
                              "pic": {
                                "type": "str",
                                "example": "1"
                              },
                              "fileId": {
                                "type": "str",
                                "example": "achievement_img1.jpeg"
                              },
                              "src": {
                                "type": "str",
                                "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img1.jpeg?v=1707981972"
                              }
                            }
                          }
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "sort": {
                            "type": "int",
                            "example": "2"
                          },
                          "name": {
                            "type": "str",
                            "example": "LoLi Nahida"
                          },
                          "duration": {
                            "type": "object",
                            "properties": {
                              "startYear": {
                                "type": "str",
                                "example": "2023"
                              },
                              "startMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "1"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "1"
                                  }
                                }
                              },
                              "endYear": {
                                "type": "str",
                                "example": "2023"
                              },
                              "endMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "2"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "2"
                                  }
                                }
                              }
                            }
                          },
                          "isInProgress": {
                            "type": "bool",
                            "example": "False"
                          },
                          "introduction": {
                            "type": "str",
                            "example": "ChatGPT的流行，已為使用者帶來不少的方便性。\n如果將類似的功能部署至每日必用的LINE上，是否就像你的貼身小助手了呢?\n- 小作品功能 :\n● 撰寫LINEBOT API，並串接OpenAI的Text CompletionAPI，達成接收客戶請求，並以同個話題與客戶回應，進行流利對答。\n● 將LINEBOT功能已兩種方式部署至GCP :\n   ▲ 方法一 VM : 於GCP開啟VM啟用24hr服務，結合Nginx + DNS(from GoDaddy) + Let's Encrypt  產生 憑證(https)的API ， 以供客戶(LINE伺服器端)進行請求。\n   ▲ 方法二 容器化 : 將LINEBOT功能容器化，並部署至GCP CloudRun，即可擁有 DNS + 憑證(https)的 ， 但回應速度較慢 (客戶傳訊息才啟用服務)"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://line.me/R/ti/p/%40965qbkve"
                          },
                          "img": {
                            "type": "object",
                            "properties": {
                              "pic": {
                                "type": "str",
                                "example": "1"
                              },
                              "fileId": {
                                "type": "str",
                                "example": "achievement_img2.jpeg"
                              },
                              "src": {
                                "type": "str",
                                "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img2.jpeg?v=1707981972"
                              }
                            }
                          }
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "sort": {
                            "type": "int",
                            "example": "3"
                          },
                          "name": {
                            "type": "str",
                            "example": "Crawler Training"
                          },
                          "duration": {
                            "type": "object",
                            "properties": {
                              "startYear": {
                                "type": "str",
                                "example": "2023"
                              },
                              "startMonth": {
                                "type": "object",
                                "properties": {
                                  "text": {
                                    "type": "str",
                                    "example": "2"
                                  },
                                  "value": {
                                    "type": "int",
                                    "example": "2"
                                  }
                                }
                              },
                              "endYear": {
                                "type": "str",
                                "example": ""
                              },
                              "endMonth": {
                                "type": "array",
                                "items": {
                                  "type": "any"
                                }
                              }
                            }
                          },
                          "isInProgress": {
                            "type": "bool",
                            "example": "True"
                          },
                          "introduction": {
                            "type": "str",
                            "example": "使用Selenium撰寫爬蟲軟體，以整理出使用者需求的職缺。\n- 欲使用技術 : \n  ● Selenium : 模擬為人操作，訪問網頁並得到資料\n  ● Pandas : 進行資料清洗，並儲存為csv檔案\n  ● MultiProcessing & Threading (計畫中) : 平行化技術分配各個人力抓取不同職缺資訊"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://github.com/joshsmiththenoob/CrawlerTraining"
                          },
                          "img": {
                            "type": "object",
                            "properties": {
                              "pic": {
                                "type": "str",
                                "example": "1"
                              },
                              "fileId": {
                                "type": "str",
                                "example": "achievement_img3.jpeg"
                              },
                              "src": {
                                "type": "str",
                                "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img3.jpeg?v=1707981972"
                              }
                            }
                          }
                        }
                      }
                    ]
                  }
                }
              }
            },
            {
              "type": "array",
              "items": {
                "type": "any"
              }
            }
          ]
        },
        "portfolio": {
          "type": "object",
          "properties": {
            "portfolios": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "sort": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      },
                      {
                        "type": "int",
                        "example": "4"
                      },
                      {
                        "type": "int",
                        "example": "5"
                      },
                      {
                        "type": "int",
                        "example": "6"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "2"
                      },
                      {
                        "type": "int",
                        "example": "3"
                      }
                    ]
                  },
                  "name": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "軟體培訓簡歷表"
                      },
                      {
                        "type": "str",
                        "example": "北科碩士成績"
                      },
                      {
                        "type": "str",
                        "example": "TOEIC"
                      },
                      {
                        "type": "str",
                        "example": "簡歷表"
                      },
                      {
                        "type": "str",
                        "example": "聯合大學成績單"
                      },
                      {
                        "type": "str",
                        "example": "Python-Nvidia Deep Learning Institute-深度學習基礎理論與實踐修課證明"
                      },
                      {
                        "type": "str",
                        "example": "Toeic成績單"
                      },
                      {
                        "type": "str",
                        "example": "跨領域數位人才加速計畫成果發表第二名獎狀"
                      },
                      {
                        "type": "str",
                        "example": "實習結業證書"
                      }
                    ]
                  },
                  "attach": {
                    "type": "object",
                    "properties": {
                      "fileId": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": ""
                          },
                          {
                            "type": "str",
                            "example": "upload1.pdf"
                          },
                          {
                            "type": "str",
                            "example": "upload2.pdf"
                          },
                          {
                            "type": "str",
                            "example": "upload3.pdf"
                          },
                          {
                            "type": "str",
                            "example": "upload4.pdf"
                          },
                          {
                            "type": "str",
                            "example": "upload5.pdf"
                          },
                          {
                            "type": "str",
                            "example": "upload1"
                          },
                          {
                            "type": "str",
                            "example": "upload2"
                          },
                          {
                            "type": "str",
                            "example": "upload3"
                          }
                        ]
                      },
                      "url": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "https://drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload1.pdf"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload2.pdf"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload3.pdf"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload4.pdf"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload5.pdf"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload1"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload2"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload3"
                          }
                        ]
                      },
                      "name": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link"
                          },
                          {
                            "type": "str",
                            "example": "北科碩成績單.pdf"
                          },
                          {
                            "type": "str",
                            "example": "TOIEC1101015.pdf"
                          },
                          {
                            "type": "str",
                            "example": "傅騰緯_簡歷表.pdf"
                          },
                          {
                            "type": "str",
                            "example": "0826_傅騰緯_聯合大學102學年度學士班成績單.pdf"
                          },
                          {
                            "type": "str",
                            "example": "DLI C-FX-01 修课证明 _ Deep Learning Institute.pdf"
                          },
                          {
                            "type": "str",
                            "example": "toeic.png"
                          },
                          {
                            "type": "str",
                            "example": "Adobe Scan Jan 28, 2023-1.pdf"
                          },
                          {
                            "type": "str",
                            "example": "數轉部實習證書.pdf"
                          }
                        ]
                      },
                      "status": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "0"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "2"
                          }
                        ]
                      },
                      "src": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "https://drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail1?v=1707981983"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail2?v=1707981983"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail3?v=1707981983"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail4?v=1707981983"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail5?v=1707981983"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail1?v=1674831901"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail2?v=1674925537"
                          },
                          {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail3?v=1675062025"
                          }
                        ]
                      }
                    }
                  },
                  "attachType": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "2"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "連結"
                          },
                          {
                            "type": "str",
                            "example": "檔案"
                          },
                          {
                            "type": "str",
                            "example": "檔案"
                          },
                          {
                            "type": "str",
                            "example": "檔案"
                          },
                          {
                            "type": "str",
                            "example": "檔案"
                          },
                          {
                            "type": "str",
                            "example": "檔案"
                          },
                          {
                            "type": "str",
                            "example": "檔案"
                          },
                          {
                            "type": "str",
                            "example": "檔案"
                          },
                          {
                            "type": "str",
                            "example": "檔案"
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "bio": {
          "type": "object",
          "properties": {
            "chi": {
              "oneOf": [
                {
                  "type": "str",
                  "example": "● 關於我 :\n\n您好! 我是傅騰緯，北科大光電所主修繞射光學、光資訊處理，研究所期間培養了傅立葉分析以及撰寫程式的能力，目前於商研院進修AI養成實戰班課程。\n在團隊中，我會主動提出想法與組員討論，且和組員討論過程中幫助我以不同的視野、邏輯看待同一件事情，這種教學相長的環境使我受益良多。為了團隊專案的完整性，我主動學習之前沒有碰過的新技能 ─ Qt、Threading，並應用在專案上。\n健身、打籃球、彈吉他的習慣讓我適時的放鬆並重整思路，也隨時保持體力面對挑戰。\n\n● 軟體業進修動機 :\n\n求學期間主修光電工程，研究方向以繞射分析、光學模擬為主，研究所畢業後，發覺特定產業不只需要光學知識，也需擁有Python、影像處理、影像辨識的能力，所以，在尋職的同時，我也找了網路資源學習Python，並開始對程式語言產生興趣，繼而萌生轉換跑道的念頭。在網路上找到了商研院開立的AI實戰養成班，再三思考下，決定全心全力投入四個月AI班課程，提升職場競爭力!\n\n● 進修作品 :\n\n在商研院開立的AI實戰養成班中，不僅學習到了基礎語法、資料探勘、AI模型訓練與部署及資料視覺化等知識外，也提供了專題實作的機會，讓我們可以將課堂上的知識應用在實務上。\n\n所屬團隊負責的專題為「Let's Dance : 舞蹈辨識評分系統」，目的是為了在嚴峻的疫情下，可以滿足消費者室內運動和娛樂的需求，專案技術分為五大項  : 臉部辨識、體感操作AI模型、舞蹈評分系統、資料庫以及GUI設計。\n\n在團隊中，我主要目負責的項目為 GUI設計，任務是將前四大項功能整合成Windows桌面應用，並利用threading平行化技術，達成遊戲多工的效果，最終以圖形介面的方式呈現給使用者。由於時間、人力的關係，目前專案成果為Windows桌面應用，本專案的最終目標是將該應用引入至嵌入式系統(Jetson Nano)，並以體感操作、成本低的特點成為具競爭力的商品 !\n\n● 碩論 - 三種應用於二次光學系統的數值分析方法之實現與比較：\n\n主要利用Matlab架設二次光學系統的模擬環境，並找出在不同環境下均有效、快速的光學模擬方案。\n\n● 經歷的困難及如何解決：\n\nChallenge : \n一個月內快速學習新技術 ─ Qt、threading，如何在專案結束前快速將系統整合，完成該項專案作品?\nHow To Solve: \n查找Qt、threading相關文檔，並參考Stack OverfLow解決相對應問題；重要的是，由於系統整合需要理解大家的功能及原理，所以與團隊溝通很重要。也感謝團隊成員們熱心討論、交流，才讓我得以快速整合！。\n\nChallenge : \n如何在一定的記憶體使用量內有效地模擬顯微鏡光學成像?\nHow To Solve : \n在光學本質上，使用不同種的繞射模擬方法，即可使用最少的記憶體模擬顯微鏡的光學成像，達成演算法優化的效果。\n\n\n● 未來期許：\n將培訓的技能應用在實務上，包括將功能包在Docker並部署至AWS上， 為公司提供商業價值；短期內加強自身軟體知識以及語文能力，期望自己的軟體、訊號處理能力為貴公司創造最大的價值!\n\n"
                },
                {
                  "type": "str",
                  "example": "「不求與人相比，但求超越自己」，這是在我在面對每一個新領域、新工作的價值觀與態度，跨領域經驗使我具備學習能力佳，願意嘗試新事物的特質。\n\n我是陳彥伶，在林口長庚大學護理系度過大學的生涯，畢業後任職臺北榮總急診室護理師一年半，離職後進入陽明交通大學生物醫學資訊所就讀。護理背景使我有良好的觀察與溝通能力，急診室分秒必爭的環境培養出我的抗壓性，資訊統計的背景也讓我對數據有敏感度，能夠察覺不合理之處，可以發現問題，有條不紊的分析可能原因，並且透過現有數據驗證假設與結果。熟悉SAS、R、python等軟體操作，論文以健保資料庫探討慢性腎病與皮膚疾病的關係。曾主動至交大校區上課，學習網路通訊、資料科學等課程。碩班期間也參加「DIGI+Talent 跨域數位人才加速躍升計畫」於資策會實習增加產業經驗，同時完成「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」的專案，從中利用python將睡眠時聲音轉換成數值進行機器學習並預測相關疾病。具備資料前處理、資料視覺化、統計分析的能力，並在學習的過程中發現自身對於數據分析的興趣\n\n「台上十分鐘，台下十年功」身為管樂人有深刻的領悟，從高中開始加入管樂團，重新學習銅管樂器，參與過數次學生團體音樂比賽獲得優等、特優的佳績，練習過程中透過自我要求、自律的每日定時練習彌補樂器演奏上的不足，也樂於分享自己的學習經驗予初學者。同時也主動肩負起團上的行政庶務，安排與各校的交流活動讓團員有更豐富的經驗，加強大家的團隊意識與凝聚力，對團體好的事情，都盡心盡力完成。\n\n經過醫院急診室生死離別的洗禮，培養出「快、狠、準」的做事方法與關懷他人、細心的工作態度，也從研究所習得數理統計、醫學研究、程式設計、電腦科學的相關知識，建立數據分析與解決問題的良好基礎。我抱著虛心求教、認真學習的態度面對每一份工作與挑戰，期待能透過我的能力與經驗協助貴公司快速掌握問題癥結，能有機會進入貴公司，與優秀團隊合作。"
                }
              ]
            },
            "eng": {
              "oneOf": [
                {
                  "type": "str",
                  "example": ""
                },
                {
                  "type": "str",
                  "example": "\"Don't compare yourself with others, but go beyond your own.\" This is my attitude when I face every new field or job. Interdisciplinary experiences have given me the good learning ability and willingness to take risks and try new things.\n\nI am Yen-Ling,Chen. I majored in nursing at Chang Gung University. After graduation,I worked as a nurse in the emergency room of Taipei Veterans General Hospital for one and a half years. Afterward, I was admitted to the Biomedical Information Institute of National Yang Ming Chiao Tung University.\nI have good observation and communication skills and I also perform well under stress from being a nurse in  the emergency room.The background of statistics also makes me sensitive to data. I have the ability to detect unreasonable numbers and analyze hypotheses or problems logically and  methodically.I am familiar with SAS, R, python and I have the ability of data pre-processing, data visualization, and statistical analysis.My dissertation also explored the relationship between chronic kidney disease and skin diseases from the health insurance database.During my master time, I also participated in the “DIGI+Talent Plan” and being an intern in the Institute for Information Industry.The project we implemented was “Applying smart speakers to recognition of sleep breathing sound and home sleep care”.We need to convert the sleeping sound to numerical values for machine learning.\n\n“One minute on the stage needs ten years of practice off stage”. I joined the orchestra in high school and learned how to play the french horn. I have participated in several group music competitions and won excellent results.I was also a self-disciplined player who practiced every day to pursue better performance and was willing to share my learning experience with beginners.At the same time, I took the responsibility to handle the administrative affairs, such as arranging exchange activities with other schools in order to strengthen members’ cohesion and widen our perspective.\n\nI face every job and challenge with a humble and active learning attitude. I am looking forward to helping your company quickly grasp the problem through my ability and experience.Hope to  have the opportunity to enter your company and cooperate with an excellent team."
                }
              ]
            }
          }
        },
        "custom5": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "any"
              },
              {
                "type": "any"
              }
            ]
          }
        },
        "sidebar": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "profile"
                  },
                  {
                    "type": "str",
                    "example": "education"
                  },
                  {
                    "type": "str",
                    "example": "experience"
                  },
                  {
                    "type": "str",
                    "example": "jobCondition"
                  },
                  {
                    "type": "str",
                    "example": "language"
                  },
                  {
                    "type": "str",
                    "example": "skill"
                  },
                  {
                    "type": "str",
                    "example": "certificate"
                  },
                  {
                    "type": "str",
                    "example": "portfolio"
                  },
                  {
                    "type": "str",
                    "example": "bio"
                  },
                  {
                    "type": "str",
                    "example": "project"
                  },
                  {
                    "type": "str",
                    "example": "referrer"
                  },
                  {
                    "type": "str",
                    "example": "profile"
                  },
                  {
                    "type": "str",
                    "example": "education"
                  },
                  {
                    "type": "str",
                    "example": "skill"
                  },
                  {
                    "type": "str",
                    "example": "experience"
                  },
                  {
                    "type": "str",
                    "example": "jobCondition"
                  },
                  {
                    "type": "str",
                    "example": "certificate"
                  },
                  {
                    "type": "str",
                    "example": "language"
                  },
                  {
                    "type": "str",
                    "example": "custom2"
                  },
                  {
                    "type": "str",
                    "example": "custom1"
                  },
                  {
                    "type": "str",
                    "example": "custom3"
                  },
                  {
                    "type": "str",
                    "example": "custom4"
                  },
                  {
                    "type": "str",
                    "example": "bio"
                  },
                  {
                    "type": "str",
                    "example": "portfolio"
                  }
                ]
              }
            }
          }
        },
        "layout": {
          "type": "object",
          "properties": {
            "education": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "EducationThemeList"
                            },
                            {
                              "type": "str",
                              "example": "EducationThemeList"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1"
                            },
                            {
                              "type": "int",
                              "example": "1"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "列表式"
                            },
                            {
                              "type": "str",
                              "example": "列表式"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "experience": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "ExperienceThemeList"
                            },
                            {
                              "type": "str",
                              "example": "ExperienceThemeList"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1"
                            },
                            {
                              "type": "int",
                              "example": "1"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "列表式"
                            },
                            {
                              "type": "str",
                              "example": "列表式"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "jobCondition": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "JobConditionThemeList"
                            },
                            {
                              "type": "str",
                              "example": "JobConditionThemeList"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1"
                            },
                            {
                              "type": "int",
                              "example": "1"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "列表式"
                            },
                            {
                              "type": "str",
                              "example": "列表式"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "profile": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "ProfileThemeClassic"
                            },
                            {
                              "type": "str",
                              "example": "ProfileThemeClassic"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1"
                            },
                            {
                              "type": "int",
                              "example": "1"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "經典風格"
                            },
                            {
                              "type": "str",
                              "example": "經典風格"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "skill": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "SkillThemeCard"
                            },
                            {
                              "type": "str",
                              "example": "SkillThemeCard"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "2"
                            },
                            {
                              "type": "int",
                              "example": "2"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "卡片式"
                            },
                            {
                              "type": "str",
                              "example": "卡片式"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "project": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "ProjectTheme1Column"
                            },
                            {
                              "type": "str",
                              "example": "ProjectTheme1Column"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1"
                            },
                            {
                              "type": "int",
                              "example": "1"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "單欄式"
                            },
                            {
                              "type": "str",
                              "example": "單欄式"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "portfolio": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "PortfolioTheme3Column"
                            },
                            {
                              "type": "str",
                              "example": "PortfolioTheme3Column"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1"
                            },
                            {
                              "type": "int",
                              "example": "1"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "三欄式"
                            },
                            {
                              "type": "str",
                              "example": "三欄式"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "certificate": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "CertificateThemeList"
                            },
                            {
                              "type": "str",
                              "example": "CertificateThemeList"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1"
                            },
                            {
                              "type": "int",
                              "example": "1"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "列表式"
                            },
                            {
                              "type": "str",
                              "example": "列表式"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            },
            "language": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "LanguageThemeList"
                            },
                            {
                              "type": "str",
                              "example": "LanguageThemeList"
                            }
                          ]
                        },
                        "value": {
                          "oneOf": [
                            {
                              "type": "int",
                              "example": "1"
                            },
                            {
                              "type": "int",
                              "example": "1"
                            }
                          ]
                        },
                        "text": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "列表式"
                            },
                            {
                              "type": "str",
                              "example": "列表式"
                            }
                          ]
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "certificate": {
          "type": "object",
          "properties": {
            "certificates": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "no": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "4001001005"
                      },
                      {
                        "type": "int",
                        "example": "4014003003"
                      },
                      {
                        "type": "int",
                        "example": "4014003004"
                      }
                    ]
                  },
                  "des": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "TOEIC (多益測驗)"
                      },
                      {
                        "type": "str",
                        "example": "高考護理師執照"
                      },
                      {
                        "type": "str",
                        "example": "CPR證照"
                      }
                    ]
                  }
                }
              }
            },
            "others": {
              "oneOf": [
                {
                  "type": "str",
                  "example": ""
                },
                {
                  "type": "str",
                  "example": ""
                }
              ]
            }
          }
        },
        "language": {
          "type": "object",
          "properties": {
            "local": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "any"
                  },
                  {
                    "type": "any"
                  }
                ]
              }
            },
            "foreign": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "writing": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "8"
                          },
                          {
                            "type": "int",
                            "example": "8"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "中等"
                          },
                          {
                            "type": "str",
                            "example": "中等"
                          }
                        ]
                      }
                    }
                  },
                  "sort": {
                    "oneOf": [
                      {
                        "type": "int",
                        "example": "1"
                      },
                      {
                        "type": "int",
                        "example": "1"
                      }
                    ]
                  },
                  "speaking": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "8"
                          },
                          {
                            "type": "int",
                            "example": "8"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "中等"
                          },
                          {
                            "type": "str",
                            "example": "中等"
                          }
                        ]
                      }
                    }
                  },
                  "listening": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "8"
                          },
                          {
                            "type": "int",
                            "example": "8"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "中等"
                          },
                          {
                            "type": "str",
                            "example": "中等"
                          }
                        ]
                      }
                    }
                  },
                  "type": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "1"
                          },
                          {
                            "type": "int",
                            "example": "1"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "英文"
                          },
                          {
                            "type": "str",
                            "example": "英文"
                          }
                        ]
                      }
                    }
                  },
                  "certificate": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "title": {
                          "type": "object",
                          "properties": {
                            "value": {
                              "oneOf": [
                                {
                                  "type": "int",
                                  "example": "4001001005"
                                },
                                {
                                  "type": "int",
                                  "example": "4001001005"
                                }
                              ]
                            },
                            "text": {
                              "oneOf": [
                                {
                                  "type": "str",
                                  "example": "TOEIC (多益測驗)"
                                },
                                {
                                  "type": "str",
                                  "example": "TOEIC (多益測驗)"
                                }
                              ]
                            }
                          }
                        },
                        "grade": {
                          "oneOf": [
                            {
                              "type": "str",
                              "example": "720"
                            },
                            {
                              "type": "str",
                              "example": "925"
                            }
                          ]
                        }
                      }
                    }
                  },
                  "reading": {
                    "type": "object",
                    "properties": {
                      "value": {
                        "oneOf": [
                          {
                            "type": "int",
                            "example": "8"
                          },
                          {
                            "type": "int",
                            "example": "8"
                          }
                        ]
                      },
                      "text": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "中等"
                          },
                          {
                            "type": "str",
                            "example": "中等"
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {}
    }
  }
}
```

### Sample-specific Schemas

#### mle_sample1.json

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "sidebar": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "profile"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "education"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "experience"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "jobCondition"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "language"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "skill"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "certificate"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "portfolio"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "bio"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "project"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "referrer"
                  }
                }
              }
            ]
          }
        },
        "jobCondition": {
          "type": "object",
          "properties": {
            "jobTimeType": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "text": {
                    "type": "str",
                    "example": "全職工作"
                  },
                  "value": {
                    "type": "int",
                    "example": "1"
                  }
                }
              }
            },
            "jobTimePeriod": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "text": {
                    "type": "str",
                    "example": "日班"
                  },
                  "value": {
                    "type": "int",
                    "example": "1"
                  }
                }
              }
            },
            "otherTimePeriod": {
              "type": "str",
              "example": ""
            },
            "workShift": {
              "type": "int",
              "example": "1"
            },
            "onBoardAfterGetOffer": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "一週"
                },
                "value": {
                  "type": "int",
                  "example": "1"
                }
              }
            },
            "customOnBoardDate": {
              "type": "object",
              "properties": {
                "year": {
                  "type": "str",
                  "example": ""
                },
                "month": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                },
                "date": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                }
              }
            },
            "onBoardDate": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "錄取後"
                },
                "value": {
                  "type": "str",
                  "example": "1"
                }
              }
            },
            "salary": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "面議"
                },
                "value": {
                  "type": "int",
                  "example": "1"
                }
              }
            },
            "salaryPeriod": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "月薪"
                },
                "value": {
                  "type": "int",
                  "example": "5"
                }
              }
            },
            "salaryOfHours": {
              "type": "str",
              "example": ""
            },
            "salaryOfMonth": {
              "type": "object",
              "properties": {
                "unitOfTenThousand": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                },
                "unitOfThousand": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                }
              }
            },
            "salariesOfYear": {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            "preferJobTitle": {
              "type": "str",
              "example": "演算法工程師、軟/韌體工程師、資料科學家、後端工程師、光學(研發)工程師"
            },
            "preferArea": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001001000"
                      },
                      "des": {
                        "type": "str",
                        "example": "台北市"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001002000"
                      },
                      "des": {
                        "type": "str",
                        "example": "新北市"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001005000"
                      },
                      "des": {
                        "type": "str",
                        "example": "桃園市"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001008000"
                      },
                      "des": {
                        "type": "str",
                        "example": "台中市"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001014000"
                      },
                      "des": {
                        "type": "str",
                        "example": "台南市"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001006000"
                      },
                      "des": {
                        "type": "str",
                        "example": "新竹縣市"
                      }
                    }
                  }
                ]
              }
            },
            "preferJobType": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2008001018"
                      },
                      "des": {
                        "type": "str",
                        "example": "光電工程師"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2008001019"
                      },
                      "des": {
                        "type": "str",
                        "example": "光學工程師"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2007001012"
                      },
                      "des": {
                        "type": "str",
                        "example": "演算法工程師"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2007001006"
                      },
                      "des": {
                        "type": "str",
                        "example": "Internet程式設計師"
                      }
                    }
                  }
                ]
              }
            },
            "preferJobIndustry": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "1001001000"
                      },
                      "des": {
                        "type": "str",
                        "example": "軟體及網路相關業"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "1001004000"
                      },
                      "des": {
                        "type": "str",
                        "example": "光電及光學相關業"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "1004000000"
                      },
                      "des": {
                        "type": "str",
                        "example": "金融投顧及保險業"
                      }
                    }
                  }
                ]
              }
            },
            "preferJobContent": {
              "type": "str",
              "example": ""
            },
            "remoteWork": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "對遠端工作有意願"
                },
                "value": {
                  "type": "int",
                  "example": "1"
                }
              }
            }
          }
        },
        "layout": {
          "type": "object",
          "properties": {
            "profile": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "經典風格"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "ProfileThemeClassic"
                        }
                      }
                    }
                  }
                }
              }
            },
            "skill": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "卡片式"
                        },
                        "value": {
                          "type": "int",
                          "example": "2"
                        },
                        "name": {
                          "type": "str",
                          "example": "SkillThemeCard"
                        }
                      }
                    }
                  }
                }
              }
            },
            "education": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "EducationThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "experience": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "ExperienceThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "jobCondition": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "JobConditionThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "language": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "LanguageThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "certificate": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "CertificateThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "portfolio": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "三欄式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "PortfolioTheme3Column"
                        }
                      }
                    }
                  }
                }
              }
            },
            "project": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "單欄式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "ProjectTheme1Column"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "education": {
          "type": "object",
          "properties": {
            "educations": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "schoolId": {
                        "type": "int",
                        "example": "5023000000"
                      },
                      "name": {
                        "type": "str",
                        "example": "國立臺北科技大學"
                      },
                      "departments": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "光電工程系"
                            },
                            "type": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "no": {
                                    "type": "int",
                                    "example": "3011016000"
                                  },
                                  "des": {
                                    "type": "str",
                                    "example": "光電工程相關"
                                  }
                                }
                              }
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2017"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "9"
                              },
                              "value": {
                                "type": "int",
                                "example": "9"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "1"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          }
                        }
                      },
                      "highest": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "碩士"
                          },
                          "value": {
                            "type": "int",
                            "example": "2"
                          }
                        }
                      },
                      "status": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "畢業"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      },
                      "inSchoolStatus": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "foreign": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "region": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "台灣"
                          },
                          "value": {
                            "type": "int",
                            "example": "7001053000"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "schoolId": {
                        "type": "int",
                        "example": "5030000000"
                      },
                      "name": {
                        "type": "str",
                        "example": "國立聯合大學"
                      },
                      "departments": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "光電工程學系"
                            },
                            "type": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "no": {
                                    "type": "int",
                                    "example": "3011016000"
                                  },
                                  "des": {
                                    "type": "str",
                                    "example": "光電工程相關"
                                  }
                                }
                              }
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2013"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "9"
                              },
                              "value": {
                                "type": "int",
                                "example": "9"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2017"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "6"
                              },
                              "value": {
                                "type": "int",
                                "example": "6"
                              }
                            }
                          }
                        }
                      },
                      "highest": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "大學"
                          },
                          "value": {
                            "type": "int",
                            "example": "3"
                          }
                        }
                      },
                      "status": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "畢業"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      },
                      "inSchoolStatus": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "foreign": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "region": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "台灣"
                          },
                          "value": {
                            "type": "int",
                            "example": "7001053000"
                          }
                        }
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "experience": {
          "type": "object",
          "properties": {
            "seniority": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "1年(含)以下"
                },
                "value": {
                  "type": "int",
                  "example": "0"
                }
              }
            },
            "experiences": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "4"
                      },
                      "companyName": {
                        "type": "str",
                        "example": "神耀科技股份有限公司"
                      },
                      "custNo": {
                        "type": "int",
                        "example": "0"
                      },
                      "invoice": {
                        "type": "int",
                        "example": "94096794"
                      },
                      "logo": {
                        "type": "str",
                        "example": ""
                      },
                      "industry": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "1001001001"
                            },
                            "des": {
                              "type": "str",
                              "example": "電腦系統整合服務業"
                            }
                          }
                        }
                      },
                      "companyScale": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "jobName": {
                        "type": "str",
                        "example": "工程師"
                      },
                      "workArea": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "6001001010"
                            },
                            "des": {
                              "type": "str",
                              "example": "台北市內湖區"
                            }
                          }
                        }
                      },
                      "jobType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "全職"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      },
                      "jobCat": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "2007001020"
                            },
                            "des": {
                              "type": "str",
                              "example": "AI工程師"
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "3"
                              },
                              "value": {
                                "type": "int",
                                "example": "3"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": ""
                          },
                          "endMonth": {
                            "type": "array",
                            "items": {
                              "type": "any"
                            }
                          }
                        }
                      },
                      "description": {
                        "type": "str",
                        "example": "<p><span style=\"background-color:rgb(255,255,255);color:rgba(0,0,0,0.9);\">Developing Deep Learning Solution : AutoEncoder or LSTM for Engineering including Wind speed or vibration signal analysis so far.</span></p><p><span style=\"background-color:rgb(255,255,255);color:rgba(0,0,0,0.9);\">Good at 1-D Signal Processing (FFT 、wavelet Transform), ready to study 2-D Signal Processing</span></p>"
                      },
                      "skill": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "salary": {
                        "type": "object",
                        "properties": {
                          "monthPay": {
                            "type": "str",
                            "example": ""
                          },
                          "yearPay": {
                            "type": "str",
                            "example": ""
                          },
                          "jobParttimeType": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          "jobParttimePay": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      },
                      "companyVisibility": {
                        "type": "bool",
                        "example": "True"
                      },
                      "stillWork": {
                        "type": "bool",
                        "example": "True"
                      },
                      "salaryVisibility": {
                        "type": "bool",
                        "example": "False"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "companyName": {
                        "type": "str",
                        "example": "緯育股份有限公司"
                      },
                      "custNo": {
                        "type": "str",
                        "example": "1a2x6bjqy4"
                      },
                      "invoice": {
                        "type": "int",
                        "example": "24708053"
                      },
                      "logo": {
                        "type": "str",
                        "example": "https://static.104.com.tw/b_profile/cust_picture/2476/130000000082476/logo.png?v=20250410150005"
                      },
                      "industry": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "1001001001"
                            },
                            "des": {
                              "type": "str",
                              "example": "電腦系統整合服務業"
                            }
                          }
                        }
                      },
                      "companyScale": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "jobName": {
                        "type": "str",
                        "example": "AI 智慧應用開發實戰養成班"
                      },
                      "workArea": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "6001002004"
                            },
                            "des": {
                              "type": "str",
                              "example": "新北市汐止區"
                            }
                          }
                        }
                      },
                      "jobType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "全職"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      },
                      "jobCat": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "2007001004"
                            },
                            "des": {
                              "type": "str",
                              "example": "軟體工程師"
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "9"
                              },
                              "value": {
                                "type": "int",
                                "example": "9"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "1"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          }
                        }
                      },
                      "description": {
                        "type": "str",
                        "example": "● 負責功能整合成桌面應用及GUI呈現 #Let's Dance 舞蹈辨識系統\n● 使用 threading 平行化技術 達成遊戲同時多工效果\n● 使用 PyQt5 將跳舞遊玩結果以GUI呈現給消費者\n● 500小時學習資料收集、清洗，AI模型訓練，部署模型至雲端，資料視覺化等AI完整應用"
                      },
                      "skill": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "salary": {
                        "type": "object",
                        "properties": {
                          "monthPay": {
                            "type": "str",
                            "example": ""
                          },
                          "yearPay": {
                            "type": "str",
                            "example": ""
                          },
                          "jobParttimeType": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          "jobParttimePay": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      },
                      "companyVisibility": {
                        "type": "bool",
                        "example": "True"
                      },
                      "stillWork": {
                        "type": "bool",
                        "example": "False"
                      },
                      "salaryVisibility": {
                        "type": "bool",
                        "example": "False"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "companyName": {
                        "type": "str",
                        "example": "台灣積體電路製造股份有限公司"
                      },
                      "custNo": {
                        "type": "str",
                        "example": "a5h92m0"
                      },
                      "invoice": {
                        "type": "int",
                        "example": "22099131"
                      },
                      "logo": {
                        "type": "str",
                        "example": "https://static.104.com.tw/b_profile/cust_picture/1000/22099131000/logo.gif?v=20220111153850"
                      },
                      "industry": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "1001006002"
                            },
                            "des": {
                              "type": "str",
                              "example": "半導體製造業"
                            }
                          }
                        }
                      },
                      "companyScale": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "jobName": {
                        "type": "str",
                        "example": "台積電計畫研究生"
                      },
                      "workArea": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "6001006001"
                            },
                            "des": {
                              "type": "str",
                              "example": "新竹市"
                            }
                          }
                        }
                      },
                      "jobType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "兼職"
                          },
                          "value": {
                            "type": "int",
                            "example": "2"
                          }
                        }
                      },
                      "jobCat": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "2016001013"
                            },
                            "des": {
                              "type": "str",
                              "example": "研究助理"
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2021"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "9"
                              },
                              "value": {
                                "type": "int",
                                "example": "9"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "2"
                              },
                              "value": {
                                "type": "int",
                                "example": "2"
                              }
                            }
                          }
                        }
                      },
                      "description": {
                        "type": "str",
                        "example": "● 研究所期間與台積電為期半年的合作計畫\n● 使用 Matlab 對光的傳播進行傅立葉分析，模擬光阻內最小氣泡的位置，以提升元件良率"
                      },
                      "skill": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "salary": {
                        "type": "object",
                        "properties": {
                          "monthPay": {
                            "type": "str",
                            "example": ""
                          },
                          "yearPay": {
                            "type": "str",
                            "example": ""
                          },
                          "jobParttimeType": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          "jobParttimePay": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      },
                      "companyVisibility": {
                        "type": "bool",
                        "example": "True"
                      },
                      "stillWork": {
                        "type": "bool",
                        "example": "False"
                      },
                      "salaryVisibility": {
                        "type": "bool",
                        "example": "False"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "3"
                      },
                      "companyName": {
                        "type": "str",
                        "example": "友達光電股份有限公司"
                      },
                      "custNo": {
                        "type": "str",
                        "example": "12nokxe8"
                      },
                      "invoice": {
                        "type": "int",
                        "example": "84149738"
                      },
                      "logo": {
                        "type": "str",
                        "example": "https://static.104.com.tw/b_profile/cust_picture/8000/84149738000/logo.png?v=20250321110724"
                      },
                      "industry": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "1001004002"
                            },
                            "des": {
                              "type": "str",
                              "example": "光學器材製造業"
                            }
                          }
                        }
                      },
                      "companyScale": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "jobName": {
                        "type": "str",
                        "example": "實習生"
                      },
                      "workArea": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "6001006001"
                            },
                            "des": {
                              "type": "str",
                              "example": "新竹市"
                            }
                          }
                        }
                      },
                      "jobType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "兼職"
                          },
                          "value": {
                            "type": "int",
                            "example": "2"
                          }
                        }
                      },
                      "jobCat": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "2008001018"
                            },
                            "des": {
                              "type": "str",
                              "example": "光電工程師"
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2018"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "7"
                              },
                              "value": {
                                "type": "int",
                                "example": "7"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2018"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "9"
                              },
                              "value": {
                                "type": "int",
                                "example": "9"
                              }
                            }
                          }
                        }
                      },
                      "description": {
                        "type": "str",
                        "example": "● 研究所期間參與友達光電的暑期實習計畫\n● 75吋面板正視、側視收光量測\n● 學習產品TFT - LCD原理，反推defect成因並解決"
                      },
                      "skill": {
                        "type": "array",
                        "items": {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "顯示器技術"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "0"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "TFT知識"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "0"
                                }
                              }
                            }
                          ]
                        }
                      },
                      "salary": {
                        "type": "object",
                        "properties": {
                          "monthPay": {
                            "type": "str",
                            "example": ""
                          },
                          "yearPay": {
                            "type": "str",
                            "example": ""
                          },
                          "jobParttimeType": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "平均月薪"
                              },
                              "value": {
                                "type": "int",
                                "example": "3"
                              }
                            }
                          },
                          "jobParttimePay": {
                            "type": "int",
                            "example": "28000"
                          }
                        }
                      },
                      "companyVisibility": {
                        "type": "bool",
                        "example": "True"
                      },
                      "stillWork": {
                        "type": "bool",
                        "example": "False"
                      },
                      "salaryVisibility": {
                        "type": "bool",
                        "example": "False"
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "skill": {
          "type": "object",
          "properties": {
            "themeChoose": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "卡片式"
                },
                "value": {
                  "type": "int",
                  "example": "2"
                },
                "name": {
                  "type": "str",
                  "example": "SkillThemeCard"
                }
              }
            },
            "skills": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "name": {
                        "type": "str",
                        "example": "Programming Language"
                      },
                      "desc": {
                        "type": "str",
                        "example": "<p>熟悉的程式語言 :</p><p>● Matlab </p><p>● Python</p><p>正在學習的程式語言:</p><p>● C++ </p>"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "軟體程式設計"
                            },
                            "value": {
                              "type": "str",
                              "example": "11009005001"
                            }
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "name": {
                        "type": "str",
                        "example": "Back-End"
                      },
                      "desc": {
                        "type": "str",
                        "example": "後端網路伺服器架設技能 :\n●  Flask \n●  GCP \n●  AWS\n●  Docker\n●  Selenium \n● RESTful API"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "3"
                      },
                      "name": {
                        "type": "str",
                        "example": "DataBase"
                      },
                      "desc": {
                        "type": "str",
                        "example": "擅長使用的DB及查詢語言 : \n●  MySQL \n●  MongoDB"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "4"
                      },
                      "name": {
                        "type": "str",
                        "example": "AI"
                      },
                      "desc": {
                        "type": "str",
                        "example": "基礎機器學習、深度學習套件使用 :\n●  Scikit-learn\n●  Tensorflow \n●  PyTorch"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "Machine Learning"
                            },
                            "value": {
                              "type": "str",
                              "example": "11009005007"
                            }
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "5"
                      },
                      "name": {
                        "type": "str",
                        "example": "Engineering"
                      },
                      "desc": {
                        "type": "str",
                        "example": "<p>● Signal Processing : 目前做震動訊號處理(FFT, Hilbert Transform), Wavelet Transform, 朝向2D訊號處理學習中</p><p>● 強項為光學、電磁學</p>"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "6"
                      },
                      "name": {
                        "type": "str",
                        "example": "Tools"
                      },
                      "desc": {
                        "type": "str",
                        "example": "<p>其他工具進行開發管理、資料視覺化或前後端整合</p><p>● Linux作業系統 (熟悉使用Ubuntu)</p><p>● Kafka 串流平台 (IoT資料即時傳輸)</p><p>● Git 版控</p><p>● LineBot</p><p>● Notion</p><p>● HackMD</p><p>● SolidWorks : 基礎3D建模</p><p>● OSLO : 幾何光學設計</p>"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "Git"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12001002018"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "SolidWorks"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12002003012"
                                }
                              }
                            }
                          ]
                        }
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "certificate": {
          "type": "object",
          "properties": {
            "certificates": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "no": {
                    "type": "int",
                    "example": "4001001005"
                  },
                  "des": {
                    "type": "str",
                    "example": "TOEIC (多益測驗)"
                  }
                }
              }
            },
            "others": {
              "type": "str",
              "example": ""
            }
          }
        },
        "language": {
          "type": "object",
          "properties": {
            "foreign": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "sort": {
                    "type": "int",
                    "example": "1"
                  },
                  "type": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "英文"
                      },
                      "value": {
                        "type": "int",
                        "example": "1"
                      }
                    }
                  },
                  "listening": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "中等"
                      },
                      "value": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "speaking": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "中等"
                      },
                      "value": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "reading": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "中等"
                      },
                      "value": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "writing": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "中等"
                      },
                      "value": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "certificate": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "title": {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "TOEIC (多益測驗)"
                            },
                            "value": {
                              "type": "int",
                              "example": "4001001005"
                            }
                          }
                        },
                        "grade": {
                          "type": "str",
                          "example": "720"
                        }
                      }
                    }
                  }
                }
              }
            },
            "local": {
              "type": "array",
              "items": {
                "type": "any"
              }
            }
          }
        },
        "project": {
          "type": "object",
          "properties": {
            "projects": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "name": {
                        "type": "str",
                        "example": "Let's Dance - 舞蹈評分系統"
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "11"
                              },
                              "value": {
                                "type": "int",
                                "example": "11"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "1"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          }
                        }
                      },
                      "isInProgress": {
                        "type": "bool",
                        "example": "False"
                      },
                      "introduction": {
                        "type": "str",
                        "example": "疫情下，為了滿足消費者對於室內運動和娛樂的需求，團隊推出了「Let's Dance : 舞蹈評分系統」的桌面應用\n- 專案擔任角色 : GUI呈現\n  ● 系統整合 : 將遊戲中四大功能整合成桌面應用\n  ● threading : 平行化技術實現遊戲多工特性\n  ● PyQt5 :  Qt結合上面兩項任務，創建桌面GUI ， 供使用者更直觀的體驗\n\n- 遊戲其他功能\n  ● 臉部辨識系統 : 以face_recognition人臉辨識模型為基礎製作人臉辨識系統，並與資料庫串接\n  ● 舞蹈評分系統 : Mediapipe 體態辨識模型實現使用者 - 教練 姿勢即時比對系統\n  ● AI 體感操作模型 : Mediapipe+DNN網路 實現使用者以體感操作GUI介面的功能\n  ● 資料庫 : 使用於GCP上建立MySQL資料庫，以記錄玩家個人資訊、歷史分數等相關資料，以GUI顯示分數排名"
                      },
                      "url": {
                        "type": "str",
                        "example": "https://drive.google.com/file/d/1XdSRXETPWzP6Vd9y1L78KHUpwhe4tnCl/view?usp=sharing"
                      },
                      "img": {
                        "type": "object",
                        "properties": {
                          "pic": {
                            "type": "str",
                            "example": "1"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "achievement_img1.jpeg"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img1.jpeg?v=1707981972"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "name": {
                        "type": "str",
                        "example": "LoLi Nahida"
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "1"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "2"
                              },
                              "value": {
                                "type": "int",
                                "example": "2"
                              }
                            }
                          }
                        }
                      },
                      "isInProgress": {
                        "type": "bool",
                        "example": "False"
                      },
                      "introduction": {
                        "type": "str",
                        "example": "ChatGPT的流行，已為使用者帶來不少的方便性。\n如果將類似的功能部署至每日必用的LINE上，是否就像你的貼身小助手了呢?\n- 小作品功能 :\n● 撰寫LINEBOT API，並串接OpenAI的Text CompletionAPI，達成接收客戶請求，並以同個話題與客戶回應，進行流利對答。\n● 將LINEBOT功能已兩種方式部署至GCP :\n   ▲ 方法一 VM : 於GCP開啟VM啟用24hr服務，結合Nginx + DNS(from GoDaddy) + Let's Encrypt  產生 憑證(https)的API ， 以供客戶(LINE伺服器端)進行請求。\n   ▲ 方法二 容器化 : 將LINEBOT功能容器化，並部署至GCP CloudRun，即可擁有 DNS + 憑證(https)的 ， 但回應速度較慢 (客戶傳訊息才啟用服務)"
                      },
                      "url": {
                        "type": "str",
                        "example": "https://line.me/R/ti/p/%40965qbkve"
                      },
                      "img": {
                        "type": "object",
                        "properties": {
                          "pic": {
                            "type": "str",
                            "example": "1"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "achievement_img2.jpeg"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img2.jpeg?v=1707981972"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "3"
                      },
                      "name": {
                        "type": "str",
                        "example": "Crawler Training"
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "2"
                              },
                              "value": {
                                "type": "int",
                                "example": "2"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": ""
                          },
                          "endMonth": {
                            "type": "array",
                            "items": {
                              "type": "any"
                            }
                          }
                        }
                      },
                      "isInProgress": {
                        "type": "bool",
                        "example": "True"
                      },
                      "introduction": {
                        "type": "str",
                        "example": "使用Selenium撰寫爬蟲軟體，以整理出使用者需求的職缺。\n- 欲使用技術 : \n  ● Selenium : 模擬為人操作，訪問網頁並得到資料\n  ● Pandas : 進行資料清洗，並儲存為csv檔案\n  ● MultiProcessing & Threading (計畫中) : 平行化技術分配各個人力抓取不同職缺資訊"
                      },
                      "url": {
                        "type": "str",
                        "example": "https://github.com/joshsmiththenoob/CrawlerTraining"
                      },
                      "img": {
                        "type": "object",
                        "properties": {
                          "pic": {
                            "type": "str",
                            "example": "1"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "achievement_img3.jpeg"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img3.jpeg?v=1707981972"
                          }
                        }
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "portfolio": {
          "type": "object",
          "properties": {
            "portfolios": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "name": {
                        "type": "str",
                        "example": "軟體培訓簡歷表"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link"
                          },
                          "status": {
                            "type": "int",
                            "example": "0"
                          },
                          "fileId": {
                            "type": "str",
                            "example": ""
                          },
                          "url": {
                            "type": "str",
                            "example": "https://drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "連結"
                          },
                          "value": {
                            "type": "int",
                            "example": "2"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "name": {
                        "type": "str",
                        "example": "北科碩士成績"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "北科碩成績單.pdf"
                          },
                          "status": {
                            "type": "int",
                            "example": "2"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "upload1.pdf"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload1.pdf"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail1?v=1707981983"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "檔案"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "3"
                      },
                      "name": {
                        "type": "str",
                        "example": "TOEIC"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "TOIEC1101015.pdf"
                          },
                          "status": {
                            "type": "int",
                            "example": "2"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "upload2.pdf"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload2.pdf"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail2?v=1707981983"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "檔案"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "4"
                      },
                      "name": {
                        "type": "str",
                        "example": "簡歷表"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "傅騰緯_簡歷表.pdf"
                          },
                          "status": {
                            "type": "int",
                            "example": "2"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "upload3.pdf"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload3.pdf"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail3?v=1707981983"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "檔案"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "5"
                      },
                      "name": {
                        "type": "str",
                        "example": "聯合大學成績單"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "0826_傅騰緯_聯合大學102學年度學士班成績單.pdf"
                          },
                          "status": {
                            "type": "int",
                            "example": "2"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "upload4.pdf"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload4.pdf"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail4?v=1707981983"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "檔案"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "6"
                      },
                      "name": {
                        "type": "str",
                        "example": "Python-Nvidia Deep Learning Institute-深度學習基礎理論與實踐修課證明"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "DLI C-FX-01 修课证明 _ Deep Learning Institute.pdf"
                          },
                          "status": {
                            "type": "int",
                            "example": "2"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "upload5.pdf"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload5.pdf"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail5?v=1707981983"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "檔案"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "bio": {
          "type": "object",
          "properties": {
            "chi": {
              "type": "str",
              "example": "● 關於我 :\n\n您好! 我是傅騰緯，北科大光電所主修繞射光學、光資訊處理，研究所期間培養了傅立葉分析以及撰寫程式的能力，目前於商研院進修AI養成實戰班課程。\n在團隊中，我會主動提出想法與組員討論，且和組員討論過程中幫助我以不同的視野、邏輯看待同一件事情，這種教學相長的環境使我受益良多。為了團隊專案的完整性，我主動學習之前沒有碰過的新技能 ─ Qt、Threading，並應用在專案上。\n健身、打籃球、彈吉他的習慣讓我適時的放鬆並重整思路，也隨時保持體力面對挑戰。\n\n● 軟體業進修動機 :\n\n求學期間主修光電工程，研究方向以繞射分析、光學模擬為主，研究所畢業後，發覺特定產業不只需要光學知識，也需擁有Python、影像處理、影像辨識的能力，所以，在尋職的同時，我也找了網路資源學習Python，並開始對程式語言產生興趣，繼而萌生轉換跑道的念頭。在網路上找到了商研院開立的AI實戰養成班，再三思考下，決定全心全力投入四個月AI班課程，提升職場競爭力!\n\n● 進修作品 :\n\n在商研院開立的AI實戰養成班中，不僅學習到了基礎語法、資料探勘、AI模型訓練與部署及資料視覺化等知識外，也提供了專題實作的機會，讓我們可以將課堂上的知識應用在實務上。\n\n所屬團隊負責的專題為「Let's Dance : 舞蹈辨識評分系統」，目的是為了在嚴峻的疫情下，可以滿足消費者室內運動和娛樂的需求，專案技術分為五大項  : 臉部辨識、體感操作AI模型、舞蹈評分系統、資料庫以及GUI設計。\n\n在團隊中，我主要目負責的項目為 GUI設計，任務是將前四大項功能整合成Windows桌面應用，並利用threading平行化技術，達成遊戲多工的效果，最終以圖形介面的方式呈現給使用者。由於時間、人力的關係，目前專案成果為Windows桌面應用，本專案的最終目標是將該應用引入至嵌入式系統(Jetson Nano)，並以體感操作、成本低的特點成為具競爭力的商品 !\n\n● 碩論 - 三種應用於二次光學系統的數值分析方法之實現與比較：\n\n主要利用Matlab架設二次光學系統的模擬環境，並找出在不同環境下均有效、快速的光學模擬方案。\n\n● 經歷的困難及如何解決：\n\nChallenge : \n一個月內快速學習新技術 ─ Qt、threading，如何在專案結束前快速將系統整合，完成該項專案作品?\nHow To Solve: \n查找Qt、threading相關文檔，並參考Stack OverfLow解決相對應問題；重要的是，由於系統整合需要理解大家的功能及原理，所以與團隊溝通很重要。也感謝團隊成員們熱心討論、交流，才讓我得以快速整合！。\n\nChallenge : \n如何在一定的記憶體使用量內有效地模擬顯微鏡光學成像?\nHow To Solve : \n在光學本質上，使用不同種的繞射模擬方法，即可使用最少的記憶體模擬顯微鏡的光學成像，達成演算法優化的效果。\n\n\n● 未來期許：\n將培訓的技能應用在實務上，包括將功能包在Docker並部署至AWS上， 為公司提供商業價值；短期內加強自身軟體知識以及語文能力，期望自己的軟體、訊號處理能力為貴公司創造最大的價值!\n\n"
            },
            "eng": {
              "type": "str",
              "example": ""
            }
          }
        },
        "custom1": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "custom2": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "custom3": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "custom4": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "custom5": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "custom6": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "profile": {
          "type": "object",
          "properties": {
            "key": {
              "type": "str",
              "example": "3Cs09h2VRhp"
            },
            "headshotUrl": {
              "type": "str",
              "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/avatar?v=1743305442"
            },
            "imageUrl": {
              "type": "str",
              "example": "https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/background_img.jpeg?v=1743305442"
            },
            "nickname": {
              "type": "str",
              "example": "傅騰緯"
            },
            "title": {
              "type": "object",
              "properties": {
                "workExperience": {
                  "type": "int",
                  "example": "0"
                },
                "companyName": {
                  "type": "str",
                  "example": "神耀科技股份有限公司"
                },
                "jobName": {
                  "type": "str",
                  "example": "AI工程師"
                },
                "schoolName": {
                  "type": "str",
                  "example": ""
                },
                "majorName": {
                  "type": "str",
                  "example": ""
                },
                "degreeLevel": {
                  "type": "int",
                  "example": "0"
                }
              }
            },
            "aboutMe": {
              "type": "str",
              "example": "<p><span style=\"color: rgba(0, 0, 0, 0.9); background-color: rgb(255, 255, 255);\">Developing Deep Learning Solution : AutoEncoder or LSTM for Engineering including Wind speed or vibration signal analysis so far.</span></p><p><span style=\"color: rgba(0, 0, 0, 0.9); background-color: rgb(255, 255, 255);\">Good at 1-D Signal Processing (FFT 、wavelet Transform), ready to study 2-D Signal Processing</span></p><p><br /></p><p>Expertise: Good at Optics, <span style=\"background-color: rgb(255, 255, 255); color: rgb(77, 81, 86);\">Electromagnetism.</span></p><p>Self-Improving: learning C++, reviewing Linear Algebra, Electric knowledge after work shift.</p>"
            },
            "motto": {
              "type": "str",
              "example": ""
            },
            "abilities": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "團隊溝通"
                  },
                  {
                    "type": "str",
                    "example": "主動討論"
                  },
                  {
                    "type": "str",
                    "example": "角色適應"
                  },
                  {
                    "type": "str",
                    "example": "自強不息"
                  },
                  {
                    "type": "str",
                    "example": "持續學習"
                  }
                ]
              }
            },
            "preferJobTitle": {
              "type": "str",
              "example": "演算法工程師、軟/韌體工程師、資料科學家、後端工程師、光學(研發)工程師"
            },
            "viewCount": {
              "type": "int",
              "example": "3424"
            },
            "createdAt": {
              "type": "str",
              "example": "2024-02-15 15:26:08"
            },
            "isSelf": {
              "type": "bool",
              "example": "False"
            },
            "signIn": {
              "type": "bool",
              "example": "True"
            },
            "followerCount": {
              "type": "int",
              "example": "0"
            },
            "followedCount": {
              "type": "int",
              "example": "0"
            },
            "followed": {
              "type": "bool",
              "example": "False"
            },
            "isFollowed": {
              "type": "bool",
              "example": "False"
            },
            "isFollowingMe": {
              "type": "bool",
              "example": "False"
            },
            "hasBeenRequested": {
              "type": "bool",
              "example": "False"
            },
            "hasRequestedMe": {
              "type": "bool",
              "example": "False"
            },
            "publicStatus": {
              "type": "int",
              "example": "1"
            },
            "uuid": {
              "type": "str",
              "example": "cf3ab3b1-e057-419a-a0f2-747d778f178d"
            },
            "personalLink1Type": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "Github"
                },
                "value": {
                  "type": "int",
                  "example": "8"
                }
              }
            },
            "personalLink2Type": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "個人網站"
                },
                "value": {
                  "type": "int",
                  "example": "1"
                }
              }
            },
            "personalLink3Type": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "Facebook"
                },
                "value": {
                  "type": "int",
                  "example": "4"
                }
              }
            },
            "personalLink1Url": {
              "type": "str",
              "example": "https://github.com/joshsmiththenoob"
            },
            "personalLink2Url": {
              "type": "str",
              "example": "https://www.linkedin.com/in/josh-smith-706891241/"
            },
            "personalLink3Url": {
              "type": "str",
              "example": "https://www.facebook.com/profile.php?id=100002502312505"
            },
            "themeChoose": {
              "type": "object",
              "properties": {
                "selectedTheme": {
                  "type": "object",
                  "properties": {
                    "text": {
                      "type": "str",
                      "example": "經典風格"
                    },
                    "value": {
                      "type": "int",
                      "example": "1"
                    },
                    "name": {
                      "type": "str",
                      "example": "ProfileThemeClassic"
                    }
                  }
                },
                "backgroundColor": {
                  "type": "str",
                  "example": ""
                }
              }
            }
          }
        },
        "publicStatus": {
          "type": "int",
          "example": "1"
        }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {}
    }
  }
}
```

#### mle_sample5.json

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "item": {
          "type": "object",
          "properties": {
            "id": {
              "type": "int",
              "example": "1002587"
            },
            "name": {
              "type": "str",
              "example": "My CakeResume"
            },
            "description": {
              "type": "str",
              "example": "Chun-Jung Huang mortis.huang@gmail.comNational Chiao-Tung University, Ph.D. - Photonics,2015 ~ 2020 Member of The Phi Tau Phi Scholastic Honor Soci..."
            },
            "path": {
              "type": "str",
              "example": "mortis-huang"
            },
            "liked": {
              "type": "bool",
              "example": "False"
            },
            "is_owner": {
              "type": "bool",
              "example": "False"
            },
            "added_to_folder": {
              "type": "bool",
              "example": "False"
            },
            "votes_total": {
              "type": "int",
              "example": "38"
            },
            "lang": {
              "type": "str",
              "example": "en"
            },
            "theme": {
              "type": "str",
              "example": "default"
            },
            "editor_version": {
              "type": "int",
              "example": "0"
            },
            "style": {
              "type": "str",
              "example": "paper"
            },
            "style_config": {
              "type": "object",
              "properties": {}
            },
            "spacing": {
              "type": "str",
              "example": "normal"
            },
            "connected_with_posts": {
              "type": "bool",
              "example": "False"
            },
            "seems_spam": {
              "type": "bool",
              "example": "False"
            },
            "should_confirm_external_links": {
              "type": "bool",
              "example": "False"
            },
            "system_generated": {
              "type": "bool",
              "example": "False"
            },
            "exported_from_profile": {
              "type": "bool",
              "example": "True"
            },
            "body": {
              "type": "str",
              "example": "<div class=\"row snippet-profile-041\"><div class=\"col-sm-8\"><h1><b>Chun-Jung Huang</b></h1><p>mortis.huang@gmail.com</p><p>&nbsp;(+886)-988-728-641</p><p>National Chiao-Tung University, Ph.D. - Photonics,2015 ~ 2020&nbsp;</p><p>Member of The Phi Tau Phi Scholastic Honor Society of the Republic of China.<br></p></div><div class=\"col-sm-4\"><img data-no-retina=\"true\" src=\"https://images.cakeresume.com/XgMVZ/mortis-huang/191caa57-6fe0-4fd6-9b12-a9ce4ebafc0f.png\" style=\"border-radius: 0px;\" loading=\"\"></div></div><div class=\"row snippet-features-001\"><div class=\"col-sm-12\"><div class=\"row\"><div class=\"col-sm-12\"><h1><b>Skills</b></h1></div></div><div class=\"row\" title=\"\"><div class=\"col-sm-12 item\"><hr><p><b>Languages:</b> Python, MatLab, Shell scripting, LabVIEW&nbsp;</p><p><b>Deep Learning:</b> Proficient in CNNs, LLM development, and deployment.&nbsp;</p><p><b>GPU Programming: </b>Python CPU to GPU migration and acceleration optimization.&nbsp;</p><p><b>Developer Tools:</b>&nbsp;Obsidian, Nsight Systems, pdb (python debugger), and Git.\n\n</p></div></div></div></div><div class=\"row snippet-experiences-013\"><div class=\"col-xs-12\"><div class=\"row\"><div class=\"col-xs-12\"><h1><b>Work Experience</b><br></h1></div></div><div class=\"row\" title=\"\"><div class=\"col-xs-2 col-sm-1 item-bullet\"></div><div class=\"col-xs-10 col-sm-11 item\"><h3>TSMC, nPtD/OPC-III Chief Engineer (March 2020 - Now)</h3><p><b>- Advanced CNN Applications:</b>&nbsp;</p><p>Integrated CNNs for enhanced anomaly detection and image processing.<br></p><p><b>- Localization of LLM:</b>&nbsp;</p><p>Customized large language models to meet specific operational needs, enhancing internal AI capabilities.<br></p><p><b>- GPU Acceleration:&nbsp;</b></p><p>Directed the migration of large Python codebases from CPU to GPU, leveraging CuPy API, cp.fuse, and RawKernel to optimize performance and reduce runtime by over 50%.<br></p></div></div><div class=\"row\" title=\"\"><div class=\"col-xs-2 col-sm-1 item-bullet\"></div><div class=\"col-xs-10 col-sm-11 item\"><h3> The University of Tokyo, Foreign Researcher (Oct. 2017 - Sep. 2018)</h3><p>Developed a CNN-based cell image recognition system from scratch, contributing to advancements in biomedical imaging and analysis.<br></p></div></div></div></div><div class=\"row snippet-educations-013 snippet-experiences-013\"><div class=\"col-xs-12\"><div class=\"row\"><div class=\"col-xs-12\"><h1><b>Education</b><br></h1></div></div><div class=\"row\" title=\"\"><div class=\"col-xs-2 col-sm-1 item-bullet\"></div><div class=\"col-xs-10 col-sm-11 item\"><h3><b>National Chiao-Tung University, Ph.D. - Photonics, 2015 ~ 2020</b></h3><p>Development of Intelligent Wearable Near Infrared Spectroscopy</p></div></div><div class=\"row\" title=\"\"><div class=\"col-xs-2 col-sm-1 item-bullet\"></div><div class=\"col-xs-10 col-sm-11 item\"><h3><b>National Chiao-Tung University, Bachelor - Photonics, 2011 ~ 2015</b></h3></div></div></div></div><div class=\"row snippet-paragraphs-001\"><div class=\"col-xs-12\"><h1><b>Main Publications</b></h1><ul><li>Virtual-freezing fluorescence imaging flow cytometry - <b>Nature communications</b>&nbsp;(IF:14.9) - 2020&nbsp;<br></li><li>Intelligent classification of platelet aggregates by agonist type - <b>Elife</b> (IF:8.14) - 2020<br></li><li>Label-free chemical imaging flow cytometry by high-speed multicolor stimulated Raman scattering - <b>PNAS</b> (IF:11.2) - 2019<br></li><li>Functional connectivity during phonemic and semantic verbal fluency test: a multichannel near infrared spectroscopy study -<b> JSTQE&nbsp;</b>(IF:4.5)&nbsp;- 2015<br></li></ul><p></p></div></div>"
            },
            "body_json_v2": {
              "type": "NoneType",
              "example": "None"
            },
            "user": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "str",
                  "example": "Chun-Jung Huang"
                },
                "username": {
                  "type": "str",
                  "example": "mortis-huang"
                },
                "id": {
                  "type": "int",
                  "example": "669487"
                },
                "first_name": {
                  "type": "str",
                  "example": "Chun-Jung"
                },
                "last_name": {
                  "type": "str",
                  "example": "Huang"
                },
                "description": {
                  "type": "str",
                  "example": "To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success."
                },
                "cover_image": {
                  "type": "object",
                  "properties": {
                    "url": {
                      "type": "str",
                      "example": "https://media.cakeresume.com/image/upload/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                    },
                    "small": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/c_crop,h_360,w_720/c_scale,h_180,w_360/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    },
                    "medium": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--Vm8J95tp--/c_fill,h_360,w_720/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    },
                    "large": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--VrSkpH3n--/c_fill,h_500,w_1500/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    },
                    "small_3_1": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--YGPutB6G--/c_fill,f_auto,h_140,w_420/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    },
                    "medium_3_1": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--6GTJ9tLF--/c_fill,f_auto,h_314,w_942/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                        }
                      }
                    }
                  }
                },
                "avatar": {
                  "type": "object",
                  "properties": {
                    "url": {
                      "type": "str",
                      "example": "https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                    },
                    "tiny": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    },
                    "small": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    },
                    "medium": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    },
                    "large": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--9QlfPnJO--/c_fill,g_face,h_300,w_300/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    },
                    "xlarge": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--1eTMbnTr--/c_fill,g_face,h_600,w_600/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        }
                      }
                    }
                  }
                },
                "avatar_tiny_url": {
                  "type": "str",
                  "example": "https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                },
                "avatar_small_url": {
                  "type": "str",
                  "example": "https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                },
                "avatar_medium_url": {
                  "type": "str",
                  "example": "https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                },
                "has_phone": {
                  "type": "bool",
                  "example": "True"
                },
                "has_email": {
                  "type": "bool",
                  "example": "True"
                },
                "main_public_item_path": {
                  "type": "str",
                  "example": "mortis-huang"
                },
                "main_signed_url_non_hidden_item_path": {
                  "type": "NoneType",
                  "example": "None"
                },
                "posts_count": {
                  "type": "int",
                  "example": "0"
                },
                "published_posts_count": {
                  "type": "int",
                  "example": "0"
                },
                "profile_privacy_level": {
                  "type": "str",
                  "example": "public"
                },
                "online_status": {
                  "type": "str",
                  "example": "offline"
                },
                "recommendee_token": {
                  "type": "str",
                  "example": "56Vxmbj3Wn3YaZMkl0L2GP"
                },
                "public_recommendations_count": {
                  "type": "int",
                  "example": "0"
                },
                "mutual_connections_count": {
                  "type": "bool",
                  "example": "False"
                },
                "unique_impressions_count": {
                  "type": "int",
                  "example": "2380"
                },
                "is_premium": {
                  "type": "bool",
                  "example": "False"
                },
                "no_branding": {
                  "type": "bool",
                  "example": "False"
                },
                "seems_spam": {
                  "type": "bool",
                  "example": "False"
                },
                "desired_job_type": {
                  "type": "str",
                  "example": "full_time"
                },
                "job_search_progress": {
                  "type": "str",
                  "example": "ready_to_interview"
                },
                "current_employment_status": {
                  "type": "str",
                  "example": "employed"
                },
                "is_freelancer": {
                  "type": "str",
                  "example": "part_time_freelancer"
                },
                "work_experience": {
                  "type": "str",
                  "example": "four_six"
                },
                "relevant_work_experience": {
                  "type": "str",
                  "example": "four_six"
                },
                "desired_position": {
                  "type": "str",
                  "example": "AI工程師、機器學習工程師、深度學習工程師、資料科學家、Machine Learning Engineer、Deep Learning Engineer、Data Scientist"
                },
                "role": {
                  "type": "str",
                  "example": "Ph.D."
                },
                "languages": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "English,3"
                      },
                      {
                        "type": "str",
                        "example": "Chinese,4"
                      }
                    ]
                  }
                },
                "remote": {
                  "type": "str",
                  "example": "interested"
                },
                "country": {
                  "type": "str",
                  "example": "TW"
                },
                "city": {
                  "type": "NoneType",
                  "example": "None"
                },
                "city_name": {
                  "type": "NoneType",
                  "example": "None"
                },
                "city_name_en": {
                  "type": "NoneType",
                  "example": "None"
                },
                "google_place_id": {
                  "type": "str",
                  "example": "ChIJoSFawR-waDQR-6m5DFTfH-8"
                },
                "google_place_name": {
                  "type": "str",
                  "example": "Taiwan, 台灣"
                },
                "google_place_name_en": {
                  "type": "str",
                  "example": "Taiwan, 台灣"
                },
                "google_place_country_name_en": {
                  "type": "str",
                  "example": "Taiwan"
                },
                "google_place_region_name_en": {
                  "type": "str",
                  "example": "Taiwan Province"
                },
                "desired_location_google_place_ids": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "ChIJL1cHXAbzbjQRaVScvwTwEec"
                      },
                      {
                        "type": "str",
                        "example": "ChIJLxl_1w9OZzQRRFJmfNR1QvU"
                      },
                      {
                        "type": "str",
                        "example": "ChIJdZOLiiMR2jERxPWrUs9peIg"
                      }
                    ]
                  }
                },
                "desired_location_names": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Taiwan"
                      },
                      {
                        "type": "str",
                        "example": "Japan"
                      },
                      {
                        "type": "str",
                        "example": "Singapore"
                      }
                    ]
                  }
                },
                "desired_location_names_en": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Taiwan"
                      },
                      {
                        "type": "str",
                        "example": "Japan"
                      },
                      {
                        "type": "str",
                        "example": "Singapore"
                      }
                    ]
                  }
                },
                "desired_location_country_names_en": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Taiwan"
                      },
                      {
                        "type": "str",
                        "example": "Japan"
                      },
                      {
                        "type": "str",
                        "example": "Singapore"
                      }
                    ]
                  }
                },
                "desired_location_region_names_en": {
                  "type": "array",
                  "items": {
                    "type": "NoneType",
                    "example": "None"
                  }
                },
                "cr_location": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "str",
                      "example": "ChIJoSFawR-waDQR-6m5DFTfH-8"
                    },
                    "full_name": {
                      "type": "str",
                      "example": "Taiwan, 台灣"
                    },
                    "country": {
                      "type": "str",
                      "example": "Taiwan"
                    },
                    "admin_level_1": {
                      "type": "str",
                      "example": "Taiwan Province"
                    },
                    "locale": {
                      "type": "str",
                      "example": "zh-TW"
                    }
                  }
                },
                "cr_desired_locations": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "str",
                            "example": "ChIJL1cHXAbzbjQRaVScvwTwEec"
                          },
                          "full_name": {
                            "type": "str",
                            "example": "Taiwan"
                          },
                          "country": {
                            "type": "str",
                            "example": "Taiwan"
                          },
                          "admin_level_1": {
                            "type": "NoneType",
                            "example": "None"
                          },
                          "locale": {
                            "type": "str",
                            "example": "en"
                          }
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "str",
                            "example": "ChIJLxl_1w9OZzQRRFJmfNR1QvU"
                          },
                          "full_name": {
                            "type": "str",
                            "example": "Japan"
                          },
                          "country": {
                            "type": "str",
                            "example": "Japan"
                          },
                          "admin_level_1": {
                            "type": "NoneType",
                            "example": "None"
                          },
                          "locale": {
                            "type": "str",
                            "example": "en"
                          }
                        }
                      },
                      {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "str",
                            "example": "ChIJdZOLiiMR2jERxPWrUs9peIg"
                          },
                          "full_name": {
                            "type": "str",
                            "example": "Singapore"
                          },
                          "country": {
                            "type": "str",
                            "example": "Singapore"
                          },
                          "admin_level_1": {
                            "type": "NoneType",
                            "example": "None"
                          },
                          "locale": {
                            "type": "str",
                            "example": "en"
                          }
                        }
                      }
                    ]
                  }
                },
                "eligible_work_locations": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                },
                "graduated_from_school": {
                  "type": "str",
                  "example": "National Chiao-Tung University"
                },
                "graduated_from_field": {
                  "type": "str",
                  "example": "Ph.D. - Clinical Engineering"
                },
                "skill_list": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "Python"
                      },
                      {
                        "type": "str",
                        "example": "GPU"
                      },
                      {
                        "type": "str",
                        "example": "Machine Learning"
                      },
                      {
                        "type": "str",
                        "example": "AI"
                      },
                      {
                        "type": "str",
                        "example": "Linux OS"
                      },
                      {
                        "type": "str",
                        "example": "Automation"
                      },
                      {
                        "type": "str",
                        "example": "GPU Programming HPC"
                      }
                    ]
                  }
                },
                "professions": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "it_machine-learning-engineer"
                      },
                      {
                        "type": "str",
                        "example": "it_python-developer"
                      },
                      {
                        "type": "str",
                        "example": "it_semiconductor-engineering"
                      }
                    ]
                  }
                },
                "industries": {
                  "type": "array",
                  "items": {
                    "oneOf": [
                      {
                        "type": "str",
                        "example": "tech_semiconductor"
                      },
                      {
                        "type": "str",
                        "example": "tech_artificial-intelligence-machine-learning"
                      }
                    ]
                  }
                },
                "headline": {
                  "type": "str",
                  "example": "Ph.D."
                },
                "number_of_management": {
                  "type": "str",
                  "example": "one_five"
                },
                "education_level": {
                  "type": "str",
                  "example": "doctoral"
                },
                "last_seen_at_days_ago_level": {
                  "type": "int",
                  "example": "30"
                },
                "network_profile": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "str",
                      "example": "zbXd"
                    },
                    "avatar": {
                      "type": "object",
                      "properties": {
                        "url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/v1704774606/eamlf29dbenp1ll63knm.jpg"
                        },
                        "tiny": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--z9cNBI1Q--/c_fill,g_face,h_24,w_24/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        },
                        "small": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--wg4dVaga--/c_fill,g_face,h_60,w_60/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        },
                        "medium": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--1AVroZGi--/c_fill,g_face,h_120,w_120/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        },
                        "large": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--KsOWQeOQ--/c_fill,g_face,h_300,w_300/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        },
                        "xlarge": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/s--echNo8F4--/c_fill,g_face,h_600,w_600/v1704774606/eamlf29dbenp1ll63knm.jpg"
                            }
                          }
                        }
                      }
                    },
                    "status": {
                      "type": "str",
                      "example": "published"
                    },
                    "description": {
                      "type": "str",
                      "example": "交大Ph.D.\n台積電OPC\nMachine Learning Solutions"
                    },
                    "identity_types": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "mentor"
                          },
                          {
                            "type": "str",
                            "example": "job_seeker"
                          },
                          {
                            "type": "str",
                            "example": "professional"
                          }
                        ]
                      }
                    },
                    "topics_to_learn": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "job_openings"
                          },
                          {
                            "type": "str",
                            "example": "company_insights"
                          },
                          {
                            "type": "str",
                            "example": "skills_development"
                          }
                        ]
                      }
                    },
                    "topics_to_share": {
                      "type": "array",
                      "items": {
                        "oneOf": [
                          {
                            "type": "str",
                            "example": "company_insights"
                          },
                          {
                            "type": "str",
                            "example": "skills_development"
                          }
                        ]
                      }
                    },
                    "tags": {
                      "type": "array",
                      "items": {
                        "type": "any"
                      }
                    },
                    "badges": {
                      "type": "array",
                      "items": {
                        "type": "any"
                      }
                    },
                    "suspended": {
                      "type": "bool",
                      "example": "False"
                    },
                    "user": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "str",
                          "example": "Chun-Jung Huang"
                        },
                        "username": {
                          "type": "str",
                          "example": "mortis-huang"
                        },
                        "first_name": {
                          "type": "str",
                          "example": "Chun-Jung"
                        },
                        "last_name": {
                          "type": "str",
                          "example": "Huang"
                        },
                        "description": {
                          "type": "str",
                          "example": "To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success."
                        },
                        "cover_image": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                            },
                            "small": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/c_crop,h_360,w_720/c_scale,h_180,w_360/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            },
                            "medium": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--Vm8J95tp--/c_fill,h_360,w_720/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            },
                            "large": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--VrSkpH3n--/c_fill,h_500,w_1500/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            },
                            "small_3_1": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--YGPutB6G--/c_fill,f_auto,h_140,w_420/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            },
                            "medium_3_1": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--6GTJ9tLF--/c_fill,f_auto,h_314,w_942/v1654083207/q7uem8cxaqsnuwkorvbb.jpg"
                                }
                              }
                            }
                          }
                        },
                        "avatar": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                            },
                            "tiny": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            },
                            "small": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            },
                            "medium": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            },
                            "large": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--9QlfPnJO--/c_fill,g_face,h_300,w_300/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            },
                            "xlarge": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--1eTMbnTr--/c_fill,g_face,h_600,w_600/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                                }
                              }
                            }
                          }
                        },
                        "avatar_tiny_url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        },
                        "avatar_small_url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        },
                        "avatar_medium_url": {
                          "type": "str",
                          "example": "https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
                        },
                        "profile_privacy_level": {
                          "type": "str",
                          "example": "public"
                        },
                        "online_status": {
                          "type": "str",
                          "example": "offline"
                        },
                        "current_job_title": {
                          "type": "str",
                          "example": "OPC Chief Engineer"
                        },
                        "current_company": {
                          "type": "str",
                          "example": "TSMC"
                        },
                        "headline": {
                          "type": "str",
                          "example": "Ph.D."
                        },
                        "is_premium": {
                          "type": "bool",
                          "example": "False"
                        },
                        "status": {
                          "type": "str",
                          "example": "created"
                        }
                      }
                    },
                    "review_application": {
                      "type": "object",
                      "properties": {
                        "precedence": {
                          "type": "int",
                          "example": "-12551"
                        },
                        "status": {
                          "type": "str",
                          "example": "approved"
                        },
                        "reject_reason": {
                          "type": "NoneType",
                          "example": "None"
                        },
                        "reject_details": {
                          "type": "NoneType",
                          "example": "None"
                        }
                      }
                    }
                  }
                },
                "most_recent_work_experience": {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "str",
                      "example": "OPC Chief Engineer"
                    },
                    "currently_work_here": {
                      "type": "bool",
                      "example": "True"
                    },
                    "from_year": {
                      "type": "int",
                      "example": "2020"
                    },
                    "from_month": {
                      "type": "int",
                      "example": "3"
                    },
                    "end_year": {
                      "type": "NoneType",
                      "example": "None"
                    },
                    "end_month": {
                      "type": "NoneType",
                      "example": "None"
                    },
                    "organization": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "str",
                          "example": "TSMC"
                        },
                        "id": {
                          "type": "int",
                          "example": "464650"
                        },
                        "logo": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/v1604585338/pbqvfhcwccdzrdu0tved.png"
                            },
                            "tiny": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--PSVTyqPa--/c_pad,fl_png8,h_60,w_60/v1604585338/pbqvfhcwccdzrdu0tved.png"
                                }
                              }
                            },
                            "thumb": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--o7W3GKLx--/c_pad,fl_png8,h_100,w_100/v1604585338/pbqvfhcwccdzrdu0tved.png"
                                }
                              }
                            },
                            "medium": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--nGEg_GN8--/c_pad,fl_png8,h_200,w_200/v1604585338/pbqvfhcwccdzrdu0tved.png"
                                }
                              }
                            },
                            "large": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "NoneType",
                                  "example": "None"
                                }
                              }
                            },
                            "og_image": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "NoneType",
                                  "example": "None"
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                "most_recent_education": {
                  "type": "object",
                  "properties": {
                    "degree_type": {
                      "type": "str",
                      "example": "doctor_of_philosophy_phd"
                    },
                    "majors": {
                      "type": "array",
                      "items": {
                        "type": "str",
                        "example": "Ph.D. - Clinical Engineering"
                      }
                    },
                    "from_year": {
                      "type": "int",
                      "example": "2015"
                    },
                    "end_year": {
                      "type": "int",
                      "example": "2020"
                    },
                    "organization": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "str",
                          "example": "National Chiao-Tung University"
                        },
                        "id": {
                          "type": "int",
                          "example": "464666"
                        },
                        "logo": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "str",
                              "example": "https://media.cakeresume.com/image/upload/v1604586192/jjunzkeazgfytbttav1t.png"
                            },
                            "tiny": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--7rkjq4Gg--/c_pad,fl_png8,h_60,w_60/v1604586192/jjunzkeazgfytbttav1t.png"
                                }
                              }
                            },
                            "thumb": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--1qBAGmIY--/c_pad,fl_png8,h_100,w_100/v1604586192/jjunzkeazgfytbttav1t.png"
                                }
                              }
                            },
                            "medium": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "str",
                                  "example": "https://media.cakeresume.com/image/upload/s--7OjsoMvQ--/c_pad,fl_png8,h_200,w_200/v1604586192/jjunzkeazgfytbttav1t.png"
                                }
                              }
                            },
                            "large": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "NoneType",
                                  "example": "None"
                                }
                              }
                            },
                            "og_image": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "NoneType",
                                  "example": "None"
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            },
            "use_signed_url": {
              "type": "bool",
              "example": "False"
            },
            "no_branding": {
              "type": "bool",
              "example": "False"
            },
            "privacy_level": {
              "type": "int",
              "example": "0"
            },
            "signed_or_not_item_url": {
              "type": "str",
              "example": "https://www.cake.me/mortis-huang"
            },
            "metadata": {
              "type": "object",
              "properties": {
                "images": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "src": {
                        "type": "str",
                        "example": "https://images.cakeresume.com/XgMVZ/mortis-huang/191caa57-6fe0-4fd6-9b12-a9ce4ebafc0f.png"
                      },
                      "width": {
                        "type": "int",
                        "example": "564"
                      },
                      "height": {
                        "type": "int",
                        "example": "318"
                      }
                    }
                  }
                }
              }
            },
            "ga_tracking_code": {
              "type": "NoneType",
              "example": "None"
            },
            "has_permission_ga": {
              "type": "bool",
              "example": "False"
            },
            "draft_update_count": {
              "type": "int",
              "example": "429"
            }
          }
        },
        "meta_tags": {
          "type": "object",
          "properties": {
            "title": {
              "type": "str",
              "example": "Chun-Jung Huang"
            },
            "description": {
              "type": "str",
              "example": "To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success."
            },
            "canonical": {
              "type": "str",
              "example": "https://www.cake.me/mortis-huang"
            },
            "og": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "str",
                  "example": "profile"
                },
                "image": {
                  "type": "str",
                  "example": "https://media.cakeresume.com/image/url2png/s--cuUyBM8A--/c_crop,g_north,h_751,w_992/c_fit,g_north,h_606,w_800/b_rgb:F0F2F1,c_lpad,g_south,h_630,w_1200/l_fetch:aHR0cHM6Ly93d3cuY2FrZXJlc3VtZS5jb20vZmF2aWNvbnMvbXN0aWxlLTMxMHgzMTAucG5n/c_scale,w_103/fl_layer_apply,g_north_west,x_0,y_0/fl_png8/https://www.cake.me/mortis-huang%3Fno-page-layout%3Dtrue%26v%3D1/url2png/viewport%3D1480x1800%7Cfullpage%3Dfalse%7Cunique%3D958442"
                }
              }
            },
            "nofollow": {
              "type": "bool",
              "example": "True"
            },
            "noindex": {
              "type": "bool",
              "example": "False"
            },
            "amphtml": {
              "type": "str",
              "example": "https://www.cake.me/mortis-huang.amp"
            }
          }
        },
        "structured_data_sets": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "@context": {
                "type": "str",
                "example": "http://schema.org/"
              },
              "@type": {
                "type": "str",
                "example": "Person"
              },
              "name": {
                "type": "str",
                "example": "Chun-Jung Huang"
              },
              "image": {
                "type": "str",
                "example": "https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg"
              },
              "description": {
                "type": "str",
                "example": "To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success."
              },
              "url": {
                "type": "str",
                "example": "https://www.cake.me/mortis-huang"
              },
              "jobTitle": {
                "type": "str",
                "example": "OPC Chief Engineer"
              },
              "sameAs": {
                "type": "str",
                "example": "https://mortis.tech/"
              }
            }
          }
        }
      }
    }
  }
}
```

#### mle_sample2.json

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "sidebar": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "profile"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "education"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "skill"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "experience"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "jobCondition"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "certificate"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "language"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "custom2"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "custom1"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "custom3"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "custom4"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "bio"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "str",
                    "example": "portfolio"
                  }
                }
              }
            ]
          }
        },
        "jobCondition": {
          "type": "object",
          "properties": {
            "jobTimeType": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "text": {
                    "type": "str",
                    "example": "全職工作"
                  },
                  "value": {
                    "type": "int",
                    "example": "1"
                  }
                }
              }
            },
            "jobTimePeriod": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "text": {
                    "type": "str",
                    "example": "日班"
                  },
                  "value": {
                    "type": "int",
                    "example": "1"
                  }
                }
              }
            },
            "otherTimePeriod": {
              "type": "str",
              "example": ""
            },
            "workShift": {
              "type": "int",
              "example": "0"
            },
            "onBoardAfterGetOffer": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "隨時"
                },
                "value": {
                  "type": "int",
                  "example": "0"
                }
              }
            },
            "customOnBoardDate": {
              "type": "object",
              "properties": {
                "year": {
                  "type": "str",
                  "example": ""
                },
                "month": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                },
                "date": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                }
              }
            },
            "onBoardDate": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "錄取後"
                },
                "value": {
                  "type": "str",
                  "example": "1"
                }
              }
            },
            "salary": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "面議"
                },
                "value": {
                  "type": "int",
                  "example": "1"
                }
              }
            },
            "salaryPeriod": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "月薪"
                },
                "value": {
                  "type": "int",
                  "example": "5"
                }
              }
            },
            "salaryOfHours": {
              "type": "str",
              "example": ""
            },
            "salaryOfMonth": {
              "type": "object",
              "properties": {
                "unitOfTenThousand": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                },
                "unitOfThousand": {
                  "type": "array",
                  "items": {
                    "type": "any"
                  }
                }
              }
            },
            "salariesOfYear": {
              "type": "array",
              "items": {
                "type": "any"
              }
            },
            "preferJobTitle": {
              "type": "str",
              "example": "數據分析師、資料分析師、數據工程師、統計分析師、資料科學家、SAS programmer、data analyst、data scientist、data engineer"
            },
            "preferArea": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001001000"
                      },
                      "des": {
                        "type": "str",
                        "example": "台北市"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001002000"
                      },
                      "des": {
                        "type": "str",
                        "example": "新北市"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "6001006000"
                      },
                      "des": {
                        "type": "str",
                        "example": "新竹縣市"
                      }
                    }
                  }
                ]
              }
            },
            "preferJobType": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2007001004"
                      },
                      "des": {
                        "type": "str",
                        "example": "軟體工程師"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2016001007"
                      },
                      "des": {
                        "type": "str",
                        "example": "統計學研究員"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2004001010"
                      },
                      "des": {
                        "type": "str",
                        "example": "市場調查／市場分析"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2007002002"
                      },
                      "des": {
                        "type": "str",
                        "example": "資料庫管理人員"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "2003002008"
                      },
                      "des": {
                        "type": "str",
                        "example": "統計精算人員"
                      }
                    }
                  }
                ]
              }
            },
            "preferJobIndustry": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "1001000000"
                      },
                      "des": {
                        "type": "str",
                        "example": "電子資訊／軟體／半導體相關業"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "1004000000"
                      },
                      "des": {
                        "type": "str",
                        "example": "金融投顧及保險業"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "1012000000"
                      },
                      "des": {
                        "type": "str",
                        "example": "醫療保健及環境衛生業"
                      }
                    }
                  }
                ]
              }
            },
            "preferJobContent": {
              "type": "str",
              "example": ""
            },
            "remoteWork": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "對遠端工作有意願"
                },
                "value": {
                  "type": "int",
                  "example": "1"
                }
              }
            }
          }
        },
        "layout": {
          "type": "object",
          "properties": {
            "profile": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "經典風格"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "ProfileThemeClassic"
                        }
                      }
                    }
                  }
                }
              }
            },
            "skill": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "卡片式"
                        },
                        "value": {
                          "type": "int",
                          "example": "2"
                        },
                        "name": {
                          "type": "str",
                          "example": "SkillThemeCard"
                        }
                      }
                    }
                  }
                }
              }
            },
            "education": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "EducationThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "experience": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "ExperienceThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "jobCondition": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "JobConditionThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "language": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "LanguageThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "certificate": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "列表式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "CertificateThemeList"
                        }
                      }
                    }
                  }
                }
              }
            },
            "portfolio": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "三欄式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "PortfolioTheme3Column"
                        }
                      }
                    }
                  }
                }
              }
            },
            "project": {
              "type": "object",
              "properties": {
                "themeChoose": {
                  "type": "object",
                  "properties": {
                    "selectedTheme": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "str",
                          "example": "單欄式"
                        },
                        "value": {
                          "type": "int",
                          "example": "1"
                        },
                        "name": {
                          "type": "str",
                          "example": "ProjectTheme1Column"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "education": {
          "type": "object",
          "properties": {
            "educations": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "schoolId": {
                        "type": "int",
                        "example": "5180000000"
                      },
                      "name": {
                        "type": "str",
                        "example": "國立陽明交通大學"
                      },
                      "departments": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "生物醫學資訊研究所"
                            },
                            "type": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "no": {
                                    "type": "int",
                                    "example": "3009009000"
                                  },
                                  "des": {
                                    "type": "str",
                                    "example": "醫藥工程相關"
                                  }
                                }
                              }
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2021"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "3"
                              },
                              "value": {
                                "type": "int",
                                "example": "3"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "2"
                              },
                              "value": {
                                "type": "int",
                                "example": "2"
                              }
                            }
                          }
                        }
                      },
                      "highest": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "碩士"
                          },
                          "value": {
                            "type": "int",
                            "example": "2"
                          }
                        }
                      },
                      "status": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "畢業"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      },
                      "inSchoolStatus": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "foreign": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "region": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "台灣"
                          },
                          "value": {
                            "type": "int",
                            "example": "7001053000"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "schoolId": {
                        "type": "int",
                        "example": "5065000000"
                      },
                      "name": {
                        "type": "str",
                        "example": "長庚大學"
                      },
                      "departments": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "護理學系"
                            },
                            "type": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "no": {
                                    "type": "int",
                                    "example": "3009005000"
                                  },
                                  "des": {
                                    "type": "str",
                                    "example": "護理助產相關"
                                  }
                                }
                              }
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2015"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "9"
                              },
                              "value": {
                                "type": "int",
                                "example": "9"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2019"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "6"
                              },
                              "value": {
                                "type": "int",
                                "example": "6"
                              }
                            }
                          }
                        }
                      },
                      "highest": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "大學"
                          },
                          "value": {
                            "type": "int",
                            "example": "3"
                          }
                        }
                      },
                      "status": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "畢業"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      },
                      "inSchoolStatus": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "foreign": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "region": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "台灣"
                          },
                          "value": {
                            "type": "int",
                            "example": "7001053000"
                          }
                        }
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "experience": {
          "type": "object",
          "properties": {
            "seniority": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "1~2年"
                },
                "value": {
                  "type": "int",
                  "example": "1"
                }
              }
            },
            "experiences": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "companyName": {
                        "type": "str",
                        "example": "財團法人資訊工業策進會"
                      },
                      "custNo": {
                        "type": "str",
                        "example": "2byd7nl"
                      },
                      "invoice": {
                        "type": "int",
                        "example": "5076416"
                      },
                      "logo": {
                        "type": "str",
                        "example": "https://static.104.com.tw/b_profile/cust_picture/6001/5076416001/logo.gif?v=20241213151351"
                      },
                      "industry": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "1001001002"
                            },
                            "des": {
                              "type": "str",
                              "example": "電腦軟體服務業"
                            }
                          }
                        }
                      },
                      "companyScale": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "500人以上"
                          },
                          "value": {
                            "type": "int",
                            "example": "4"
                          }
                        }
                      },
                      "jobName": {
                        "type": "str",
                        "example": "軟體研究部門實習生"
                      },
                      "workArea": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "6001001004"
                            },
                            "des": {
                              "type": "str",
                              "example": "台北市松山區"
                            }
                          }
                        }
                      },
                      "jobType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "兼職"
                          },
                          "value": {
                            "type": "int",
                            "example": "2"
                          }
                        }
                      },
                      "jobCat": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "2002001011"
                            },
                            "des": {
                              "type": "str",
                              "example": "工讀生"
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "7"
                              },
                              "value": {
                                "type": "int",
                                "example": "7"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "12"
                              },
                              "value": {
                                "type": "int",
                                "example": "12"
                              }
                            }
                          }
                        }
                      },
                      "description": {
                        "type": "str",
                        "example": "● 此為經濟部工業局「Digitalent」實習計畫 – 「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」 專案\n1. 專案發想、時程規劃安排、論文技術討論\n2.負責與醫院端及產業端合作溝通\n3. 協助臨床數據收集\n4. 協助利用python以機器學習方式建置呼吸音辨識模型"
                      },
                      "skill": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "salary": {
                        "type": "object",
                        "properties": {
                          "monthPay": {
                            "type": "str",
                            "example": ""
                          },
                          "yearPay": {
                            "type": "str",
                            "example": ""
                          },
                          "jobParttimeType": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          "jobParttimePay": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      },
                      "companyVisibility": {
                        "type": "bool",
                        "example": "True"
                      },
                      "stillWork": {
                        "type": "bool",
                        "example": "False"
                      },
                      "salaryVisibility": {
                        "type": "bool",
                        "example": "False"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "companyName": {
                        "type": "str",
                        "example": "國立陽明交通大學"
                      },
                      "custNo": {
                        "type": "int",
                        "example": "0"
                      },
                      "invoice": {
                        "type": "int",
                        "example": "0"
                      },
                      "logo": {
                        "type": "str",
                        "example": ""
                      },
                      "industry": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "1005001007"
                            },
                            "des": {
                              "type": "str",
                              "example": "大專校院教育事業"
                            }
                          }
                        }
                      },
                      "companyScale": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "500人以上"
                          },
                          "value": {
                            "type": "int",
                            "example": "4"
                          }
                        }
                      },
                      "jobName": {
                        "type": "str",
                        "example": "吳俊穎教授實驗室研究助理"
                      },
                      "workArea": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "6001001009"
                            },
                            "des": {
                              "type": "str",
                              "example": "台北市北投區"
                            }
                          }
                        }
                      },
                      "jobType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "兼職"
                          },
                          "value": {
                            "type": "int",
                            "example": "2"
                          }
                        }
                      },
                      "jobCat": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "2016001013"
                            },
                            "des": {
                              "type": "str",
                              "example": "研究助理"
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "1"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": ""
                          },
                          "endMonth": {
                            "type": "array",
                            "items": {
                              "type": "any"
                            }
                          }
                        }
                      },
                      "description": {
                        "type": "str",
                        "example": "協助臨床研究收案，健保資料庫分析，實驗室相關庶務\n\n● 協助執行科技部計畫 – 「腸道微菌叢對於新冠肺炎疫苗相關免疫反應、副作用、持久性及突破性感染之角色」 \n1. 負責計畫部分臨床收案，需主動找尋受試者、和民眾溝通，與醫院單位協調\n2.進行實驗室血液檢體分析、檢體保存管理、估算使用成本等事務\n\n● 健保資料庫統計分析：\n1. 與醫學中心皮膚科醫師合作進行健康資料流行病學分析，曾處理過慢性腎臟病與類天疱瘡相關性、白斑與視網膜剝離的關聯性、系統性藥物治療的乾癬患者發生心血管疾病的風險、類天皰瘡與各感染疾病之關係等案件。\n2.藉由資料庫分析，處理過2300萬人的大型資料數據。\n\n● 就學期間曾修習相關領域課程：SAS資料分析及應用、資料科學軟體實作、雲端技術及網路服務實務、資料視覺化與視覺分析、進階流行病學研究設計、深度學習於生醫資料分析 、資料探勘，且於在學期間取得公衛師考試的資格。"
                      },
                      "skill": {
                        "type": "array",
                        "items": {
                          "type": "any"
                        }
                      },
                      "salary": {
                        "type": "object",
                        "properties": {
                          "monthPay": {
                            "type": "str",
                            "example": ""
                          },
                          "yearPay": {
                            "type": "str",
                            "example": ""
                          },
                          "jobParttimeType": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          "jobParttimePay": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      },
                      "companyVisibility": {
                        "type": "bool",
                        "example": "True"
                      },
                      "stillWork": {
                        "type": "bool",
                        "example": "True"
                      },
                      "salaryVisibility": {
                        "type": "bool",
                        "example": "False"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "3"
                      },
                      "companyName": {
                        "type": "str",
                        "example": "臺北榮民總醫院"
                      },
                      "custNo": {
                        "type": "str",
                        "example": "dqlsrl4"
                      },
                      "invoice": {
                        "type": "int",
                        "example": "29906905"
                      },
                      "logo": {
                        "type": "str",
                        "example": ""
                      },
                      "industry": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "1012001001"
                            },
                            "des": {
                              "type": "str",
                              "example": "醫院"
                            }
                          }
                        }
                      },
                      "companyScale": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "500人以上"
                          },
                          "value": {
                            "type": "int",
                            "example": "4"
                          }
                        }
                      },
                      "jobName": {
                        "type": "str",
                        "example": "急診護理師"
                      },
                      "workArea": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "6001001009"
                            },
                            "des": {
                              "type": "str",
                              "example": "台北市北投區"
                            }
                          }
                        }
                      },
                      "jobType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "全職"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      },
                      "jobCat": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "no": {
                              "type": "int",
                              "example": "2015001004"
                            },
                            "des": {
                              "type": "str",
                              "example": "護理師及護士"
                            }
                          }
                        }
                      },
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2019"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "10"
                              },
                              "value": {
                                "type": "int",
                                "example": "10"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2021"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "3"
                              },
                              "value": {
                                "type": "int",
                                "example": "3"
                              }
                            }
                          }
                        }
                      },
                      "description": {
                        "type": "str",
                        "example": "擔任急診護理師需具備刻苦耐勞的個性、能力上需反應快動作靈敏、與人可以良好溝通。工作內容主要為照顧病人，協助醫師診治，執行護理相關技術，急救處理(ACLS)。"
                      },
                      "skill": {
                        "type": "array",
                        "items": {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "護理指導及諮詢"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11012010016"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "執行靜脈或肌肉注射相關作業"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11012010008"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "預防保護之護理措施"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11012010012"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "健康問題之護理評估"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11007003010"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "急救甦醒器之使用與維護"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11012010020"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "協同專科醫師進行會診或轉診"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11012010001"
                                }
                              }
                            }
                          ]
                        }
                      },
                      "salary": {
                        "type": "object",
                        "properties": {
                          "monthPay": {
                            "type": "str",
                            "example": ""
                          },
                          "yearPay": {
                            "type": "str",
                            "example": ""
                          },
                          "jobParttimeType": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "平均時薪"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          },
                          "jobParttimePay": {
                            "type": "str",
                            "example": ""
                          }
                        }
                      },
                      "companyVisibility": {
                        "type": "bool",
                        "example": "True"
                      },
                      "stillWork": {
                        "type": "bool",
                        "example": "False"
                      },
                      "salaryVisibility": {
                        "type": "bool",
                        "example": "False"
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "skill": {
          "type": "object",
          "properties": {
            "themeChoose": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "卡片式"
                },
                "value": {
                  "type": "int",
                  "example": "2"
                },
                "name": {
                  "type": "str",
                  "example": "SkillThemeCard"
                }
              }
            },
            "skills": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "name": {
                        "type": "str",
                        "example": "程式語言"
                      },
                      "desc": {
                        "type": "str",
                        "example": "Python、R、SQL"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "Python"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12001003045"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "軟體程式設計"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11009005001"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "軟體工程系統開發"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11009002008"
                                }
                              }
                            }
                          ]
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "name": {
                        "type": "str",
                        "example": "統計軟體"
                      },
                      "desc": {
                        "type": "str",
                        "example": "SAS、SPSS、Stata"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "調查樣本統計分析"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11005004007"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "統計軟體操作"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11005004004"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "市場調查資料分析與報告撰寫"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11005004002"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "SPSS"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12003005011"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "SAS"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12003005009"
                                }
                              }
                            }
                          ]
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "3"
                      },
                      "name": {
                        "type": "str",
                        "example": "Microsoft Office"
                      },
                      "desc": {
                        "type": "str",
                        "example": "Word、Excel、PowerPoint"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "PowerPoint"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12001008012"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "Excel"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12001008003"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "Outlook"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12001008011"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "文件檔案資料處理、轉換及整合工作"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11001005007"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "文書處理╱排版能力"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11001005002"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "文件或資料輸入建檔處理"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11001005006"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "電話接聽與人員接待事項"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11001005005"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "報表彙整與管理"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11001005004"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "文件收發與檔案管理"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11001005001"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "Word"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12001008016"
                                }
                              }
                            }
                          ]
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "4"
                      },
                      "name": {
                        "type": "str",
                        "example": "數據分析-全民健保資料庫"
                      },
                      "desc": {
                        "type": "str",
                        "example": "公共衛生與流行病學統計，利用資料庫數據分析的方法，探討疾病間的關係\n在學期間協助4篇論文分析:\n1.慢性腎臟病與類天疱瘡發生風險之相關性：族群的世代研究\n2.白斑與視網膜剝離的關聯性：全台灣人口研究調查\n3.接受系統性藥物治療的乾癬患者發生心血管疾病的風險：以臺灣人口研究\n4.類天皰瘡與各感染疾病之關係"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "SAS"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "12003005009"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "撰寫研究報告與論文"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11017009011"
                                }
                              }
                            }
                          ]
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "5"
                      },
                      "name": {
                        "type": "str",
                        "example": "醫療護理"
                      },
                      "desc": {
                        "type": "str",
                        "example": "醫學統計:熟悉健保資料庫、醫學統計相關應用\n健康照護:熟悉病人照護、護理諮詢指導、護理技術執行\n緊急醫療處理:了解緊急狀況之醫療處置及救護"
                      },
                      "status": {
                        "type": "int",
                        "example": "1"
                      },
                      "tag": {
                        "type": "array",
                        "items": {
                          "oneOf": [
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "健康問題之護理評估"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11007003010"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "執行靜脈或肌肉注射相關作業"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11012010008"
                                }
                              }
                            },
                            {
                              "type": "object",
                              "properties": {
                                "text": {
                                  "type": "str",
                                  "example": "預防保護之護理措施"
                                },
                                "value": {
                                  "type": "str",
                                  "example": "11012010012"
                                }
                              }
                            }
                          ]
                        }
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "certificate": {
          "type": "object",
          "properties": {
            "certificates": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "4014003003"
                      },
                      "des": {
                        "type": "str",
                        "example": "高考護理師執照"
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "no": {
                        "type": "int",
                        "example": "4014003004"
                      },
                      "des": {
                        "type": "str",
                        "example": "CPR證照"
                      }
                    }
                  }
                ]
              }
            },
            "others": {
              "type": "str",
              "example": ""
            }
          }
        },
        "language": {
          "type": "object",
          "properties": {
            "foreign": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "sort": {
                    "type": "int",
                    "example": "1"
                  },
                  "type": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "英文"
                      },
                      "value": {
                        "type": "int",
                        "example": "1"
                      }
                    }
                  },
                  "listening": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "中等"
                      },
                      "value": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "speaking": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "中等"
                      },
                      "value": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "reading": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "中等"
                      },
                      "value": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "writing": {
                    "type": "object",
                    "properties": {
                      "text": {
                        "type": "str",
                        "example": "中等"
                      },
                      "value": {
                        "type": "int",
                        "example": "8"
                      }
                    }
                  },
                  "certificate": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "title": {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "str",
                              "example": "TOEIC (多益測驗)"
                            },
                            "value": {
                              "type": "int",
                              "example": "4001001005"
                            }
                          }
                        },
                        "grade": {
                          "type": "str",
                          "example": "925"
                        }
                      }
                    }
                  }
                }
              }
            },
            "local": {
              "type": "array",
              "items": {
                "type": "any"
              }
            }
          }
        },
        "project": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "portfolio": {
          "type": "object",
          "properties": {
            "portfolios": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "1"
                      },
                      "name": {
                        "type": "str",
                        "example": "Toeic成績單"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "toeic.png"
                          },
                          "status": {
                            "type": "int",
                            "example": "2"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "upload1"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload1"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail1?v=1674831901"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "檔案"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "2"
                      },
                      "name": {
                        "type": "str",
                        "example": "跨領域數位人才加速計畫成果發表第二名獎狀"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "Adobe Scan Jan 28, 2023-1.pdf"
                          },
                          "status": {
                            "type": "int",
                            "example": "2"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "upload2"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload2"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail2?v=1674925537"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "檔案"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      }
                    }
                  },
                  {
                    "type": "object",
                    "properties": {
                      "sort": {
                        "type": "int",
                        "example": "3"
                      },
                      "name": {
                        "type": "str",
                        "example": "實習結業證書"
                      },
                      "attach": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "str",
                            "example": "數轉部實習證書.pdf"
                          },
                          "status": {
                            "type": "int",
                            "example": "2"
                          },
                          "fileId": {
                            "type": "str",
                            "example": "upload3"
                          },
                          "url": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload3"
                          },
                          "src": {
                            "type": "str",
                            "example": "https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail3?v=1675062025"
                          }
                        }
                      },
                      "attachType": {
                        "type": "object",
                        "properties": {
                          "text": {
                            "type": "str",
                            "example": "檔案"
                          },
                          "value": {
                            "type": "int",
                            "example": "1"
                          }
                        }
                      }
                    }
                  }
                ]
              }
            }
          }
        },
        "bio": {
          "type": "object",
          "properties": {
            "chi": {
              "type": "str",
              "example": "「不求與人相比，但求超越自己」，這是在我在面對每一個新領域、新工作的價值觀與態度，跨領域經驗使我具備學習能力佳，願意嘗試新事物的特質。\n\n我是陳彥伶，在林口長庚大學護理系度過大學的生涯，畢業後任職臺北榮總急診室護理師一年半，離職後進入陽明交通大學生物醫學資訊所就讀。護理背景使我有良好的觀察與溝通能力，急診室分秒必爭的環境培養出我的抗壓性，資訊統計的背景也讓我對數據有敏感度，能夠察覺不合理之處，可以發現問題，有條不紊的分析可能原因，並且透過現有數據驗證假設與結果。熟悉SAS、R、python等軟體操作，論文以健保資料庫探討慢性腎病與皮膚疾病的關係。曾主動至交大校區上課，學習網路通訊、資料科學等課程。碩班期間也參加「DIGI+Talent 跨域數位人才加速躍升計畫」於資策會實習增加產業經驗，同時完成「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」的專案，從中利用python將睡眠時聲音轉換成數值進行機器學習並預測相關疾病。具備資料前處理、資料視覺化、統計分析的能力，並在學習的過程中發現自身對於數據分析的興趣\n\n「台上十分鐘，台下十年功」身為管樂人有深刻的領悟，從高中開始加入管樂團，重新學習銅管樂器，參與過數次學生團體音樂比賽獲得優等、特優的佳績，練習過程中透過自我要求、自律的每日定時練習彌補樂器演奏上的不足，也樂於分享自己的學習經驗予初學者。同時也主動肩負起團上的行政庶務，安排與各校的交流活動讓團員有更豐富的經驗，加強大家的團隊意識與凝聚力，對團體好的事情，都盡心盡力完成。\n\n經過醫院急診室生死離別的洗禮，培養出「快、狠、準」的做事方法與關懷他人、細心的工作態度，也從研究所習得數理統計、醫學研究、程式設計、電腦科學的相關知識，建立數據分析與解決問題的良好基礎。我抱著虛心求教、認真學習的態度面對每一份工作與挑戰，期待能透過我的能力與經驗協助貴公司快速掌握問題癥結，能有機會進入貴公司，與優秀團隊合作。"
            },
            "eng": {
              "type": "str",
              "example": "\"Don't compare yourself with others, but go beyond your own.\" This is my attitude when I face every new field or job. Interdisciplinary experiences have given me the good learning ability and willingness to take risks and try new things.\n\nI am Yen-Ling,Chen. I majored in nursing at Chang Gung University. After graduation,I worked as a nurse in the emergency room of Taipei Veterans General Hospital for one and a half years. Afterward, I was admitted to the Biomedical Information Institute of National Yang Ming Chiao Tung University.\nI have good observation and communication skills and I also perform well under stress from being a nurse in  the emergency room.The background of statistics also makes me sensitive to data. I have the ability to detect unreasonable numbers and analyze hypotheses or problems logically and  methodically.I am familiar with SAS, R, python and I have the ability of data pre-processing, data visualization, and statistical analysis.My dissertation also explored the relationship between chronic kidney disease and skin diseases from the health insurance database.During my master time, I also participated in the “DIGI+Talent Plan” and being an intern in the Institute for Information Industry.The project we implemented was “Applying smart speakers to recognition of sleep breathing sound and home sleep care”.We need to convert the sleeping sound to numerical values for machine learning.\n\n“One minute on the stage needs ten years of practice off stage”. I joined the orchestra in high school and learned how to play the french horn. I have participated in several group music competitions and won excellent results.I was also a self-disciplined player who practiced every day to pursue better performance and was willing to share my learning experience with beginners.At the same time, I took the responsibility to handle the administrative affairs, such as arranging exchange activities with other schools in order to strengthen members’ cohesion and widen our perspective.\n\nI face every job and challenge with a humble and active learning attitude. I am looking forward to helping your company quickly grasp the problem through my ability and experience.Hope to  have the opportunity to enter your company and cooperate with an excellent team."
            }
          }
        },
        "custom1": {
          "type": "object",
          "properties": {
            "custom": {
              "type": "object",
              "properties": {
                "sort": {
                  "type": "int",
                  "example": "1"
                },
                "name": {
                  "type": "str",
                  "example": "經濟部跨域數位人才加速躍升計畫"
                },
                "content": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "7"
                              },
                              "value": {
                                "type": "int",
                                "example": "7"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "12"
                              },
                              "value": {
                                "type": "int",
                                "example": "12"
                              }
                            }
                          }
                        }
                      },
                      "isInProgress": {
                        "type": "bool",
                        "example": "False"
                      },
                      "introduction": {
                        "type": "str",
                        "example": "【DIGI+Talent 跨域數位人才加速躍升計畫】\n此跨域計畫為行政院自2017年起推動「數位國家・創新經濟發展方案（簡稱DIGI+）」，入選為2022年智慧聯網類研習生，以「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」為主題，團隊於2022年底成果發表會42組隊伍中獲得第二名佳績。\n\n● 由資訊工業策進會業師指導，與醫院及國內業者合作推行專案\n● 經歷6個月實習，總時數超過240小時的研習及30小時線上課程學習。\n●專案內容涵蓋Python程式設計、智慧聯網、機器學習應用實務、語音辨識、萃取音訊特徵，對音訊進行分析等。"
                      },
                      "url": {
                        "type": "str",
                        "example": "https://www.youtube.com/watch?v=uWeHwZRZI6M&list=PLoQj70ABw1jnRdB-HBAOgFj2Ini6hEp1_&index=6"
                      }
                    }
                  }
                }
              }
            },
            "themeChoose": {
              "type": "object",
              "properties": {
                "selectedTheme": {
                  "type": "object",
                  "properties": {
                    "text": {
                      "type": "str",
                      "example": "經典風格"
                    },
                    "value": {
                      "type": "int",
                      "example": "1"
                    },
                    "name": {
                      "type": "str",
                      "example": "CustomThemeClassic"
                    }
                  }
                }
              }
            },
            "img": {
              "type": "object",
              "properties": {
                "pic": {
                  "type": "int",
                  "example": "1"
                },
                "fileId": {
                  "type": "str",
                  "example": "custom_content_img1"
                },
                "src": {
                  "type": "str",
                  "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img1?v=1675868589"
                }
              }
            },
            "img2": {
              "type": "object",
              "properties": {
                "pic": {
                  "type": "int",
                  "example": "0"
                },
                "fileId": {
                  "type": "str",
                  "example": ""
                },
                "src": {
                  "type": "str",
                  "example": ""
                }
              }
            }
          }
        },
        "custom2": {
          "type": "object",
          "properties": {
            "custom": {
              "type": "object",
              "properties": {
                "sort": {
                  "type": "int",
                  "example": "2"
                },
                "name": {
                  "type": "str",
                  "example": "論文專案"
                },
                "content": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2022"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "3"
                              },
                              "value": {
                                "type": "int",
                                "example": "3"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "1"
                              },
                              "value": {
                                "type": "int",
                                "example": "1"
                              }
                            }
                          }
                        }
                      },
                      "isInProgress": {
                        "type": "bool",
                        "example": "False"
                      },
                      "introduction": {
                        "type": "str",
                        "example": "【慢性腎臟病與類天皰瘡發生風險之相關性：族群的世代研究】\n● 運用大數據分析慢性腎臟病與類天皰瘡的關聯性之論文\n● 臺灣慢性腎臟病盛行率達11.9%，約200萬人受此疾病所苦\n● 使用2300萬人口的數據資料，處理過數億筆資料的經驗\n● 進行研究族群之人口學特徵描述性統計、計算不同分類人口中的發生率\n● 針對慢性腎臟病與類天皰瘡進行存活分析，觀察10年期間的變化\n●進行不同組間，不同疾病、年齡、性別間的風險比計算、分層分析"
                      },
                      "url": {
                        "type": "str",
                        "example": ""
                      }
                    }
                  }
                }
              }
            },
            "themeChoose": {
              "type": "object",
              "properties": {
                "selectedTheme": {
                  "type": "object",
                  "properties": {
                    "text": {
                      "type": "str",
                      "example": "經典風格"
                    },
                    "value": {
                      "type": "int",
                      "example": "1"
                    },
                    "name": {
                      "type": "str",
                      "example": "CustomThemeClassic"
                    }
                  }
                }
              }
            },
            "img": {
              "type": "object",
              "properties": {
                "pic": {
                  "type": "int",
                  "example": "1"
                },
                "fileId": {
                  "type": "str",
                  "example": "custom_content_img2"
                },
                "src": {
                  "type": "str",
                  "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img2?v=1675867362"
                }
              }
            },
            "img2": {
              "type": "object",
              "properties": {
                "pic": {
                  "type": "int",
                  "example": "0"
                },
                "fileId": {
                  "type": "str",
                  "example": ""
                },
                "src": {
                  "type": "str",
                  "example": ""
                }
              }
            }
          }
        },
        "custom3": {
          "type": "object",
          "properties": {
            "custom": {
              "type": "object",
              "properties": {
                "sort": {
                  "type": "int",
                  "example": "3"
                },
                "name": {
                  "type": "str",
                  "example": "國立陽明交通大學愛杏管弦樂團"
                },
                "content": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2021"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "3"
                              },
                              "value": {
                                "type": "int",
                                "example": "3"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2023"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "2"
                              },
                              "value": {
                                "type": "int",
                                "example": "2"
                              }
                            }
                          }
                        }
                      },
                      "isInProgress": {
                        "type": "bool",
                        "example": "False"
                      },
                      "introduction": {
                        "type": "str",
                        "example": "【克服樂團的困境，協助建立好的風氣】\n2022/10 - 2023/02\n於加入管弦樂團後第二年遭遇團上經費嚴重不足，團員流失嚴重，因此加入幹部團隊，協助樂團行政工作。\n\n●協助招募新團員:協助發布招募團員之文案\n●尋求經費上贊助:透過統計軟體整理歷屆團員聯絡資訊，協助連絡已畢業學長姐\n●協助舉行交大陽明校區巡迴演出活動"
                      },
                      "url": {
                        "type": "str",
                        "example": ""
                      }
                    }
                  }
                }
              }
            },
            "themeChoose": {
              "type": "object",
              "properties": {
                "selectedTheme": {
                  "type": "object",
                  "properties": {
                    "text": {
                      "type": "str",
                      "example": "經典風格"
                    },
                    "value": {
                      "type": "int",
                      "example": "1"
                    },
                    "name": {
                      "type": "str",
                      "example": "CustomThemeClassic"
                    }
                  }
                }
              }
            },
            "img": {
              "type": "object",
              "properties": {
                "pic": {
                  "type": "int",
                  "example": "1"
                },
                "fileId": {
                  "type": "str",
                  "example": "custom_content_img3"
                },
                "src": {
                  "type": "str",
                  "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img3?v=1675868597"
                }
              }
            },
            "img2": {
              "type": "object",
              "properties": {
                "pic": {
                  "type": "int",
                  "example": "0"
                },
                "fileId": {
                  "type": "str",
                  "example": ""
                },
                "src": {
                  "type": "str",
                  "example": ""
                }
              }
            }
          }
        },
        "custom4": {
          "type": "object",
          "properties": {
            "custom": {
              "type": "object",
              "properties": {
                "sort": {
                  "type": "int",
                  "example": "4"
                },
                "name": {
                  "type": "str",
                  "example": "長庚大學管樂團"
                },
                "content": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "duration": {
                        "type": "object",
                        "properties": {
                          "startYear": {
                            "type": "str",
                            "example": "2015"
                          },
                          "startMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "9"
                              },
                              "value": {
                                "type": "int",
                                "example": "9"
                              }
                            }
                          },
                          "endYear": {
                            "type": "str",
                            "example": "2019"
                          },
                          "endMonth": {
                            "type": "object",
                            "properties": {
                              "text": {
                                "type": "str",
                                "example": "6"
                              },
                              "value": {
                                "type": "int",
                                "example": "6"
                              }
                            }
                          }
                        }
                      },
                      "isInProgress": {
                        "type": "bool",
                        "example": "False"
                      },
                      "introduction": {
                        "type": "str",
                        "example": "【創造樂團輝煌時代】\n2016/6-2017/6\n接管幹部時，經歷團上意見紛歧、大家對於比賽想法不同等問題，與團隊一起努力透過溝通，把樂團創經營的更好更有向心力，經費與團員更加充足，且於全國比賽獲得佳績。\n\n●擔任社團幹部:負責藏譜管理、參與會議討論\n●管樂週以及校慶擺攤活動總召:利用中午時間與一般學生宣傳管樂團的特色、安排午餐音樂會、協助甜點販賣，一週為社團賺進2萬元的資金、校慶擺攤一個下午有4千元的業績\n● 參與4年度的全國學生音樂團體比賽:獲得三年學生音樂比賽優等，一年全國賽特優的佳績。"
                      },
                      "url": {
                        "type": "str",
                        "example": ""
                      }
                    }
                  }
                }
              }
            },
            "themeChoose": {
              "type": "object",
              "properties": {
                "selectedTheme": {
                  "type": "object",
                  "properties": {
                    "text": {
                      "type": "str",
                      "example": "經典風格"
                    },
                    "value": {
                      "type": "int",
                      "example": "1"
                    },
                    "name": {
                      "type": "str",
                      "example": "CustomThemeClassic"
                    }
                  }
                }
              }
            },
            "img": {
              "type": "object",
              "properties": {
                "pic": {
                  "type": "int",
                  "example": "1"
                },
                "fileId": {
                  "type": "str",
                  "example": "custom_content_img4"
                },
                "src": {
                  "type": "str",
                  "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img4?v=1675868603"
                }
              }
            },
            "img2": {
              "type": "object",
              "properties": {
                "pic": {
                  "type": "int",
                  "example": "0"
                },
                "fileId": {
                  "type": "str",
                  "example": ""
                },
                "src": {
                  "type": "str",
                  "example": ""
                }
              }
            }
          }
        },
        "custom5": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "custom6": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "profile": {
          "type": "object",
          "properties": {
            "key": {
              "type": "str",
              "example": "1ZSUUFKUw0r"
            },
            "headshotUrl": {
              "type": "str",
              "example": "https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/avatar?v=1743309994"
            },
            "imageUrl": {
              "type": "str",
              "example": ""
            },
            "nickname": {
              "type": "str",
              "example": "陳彥伶"
            },
            "title": {
              "type": "object",
              "properties": {
                "workExperience": {
                  "type": "int",
                  "example": "0"
                },
                "companyName": {
                  "type": "str",
                  "example": "陽明交通大學生物醫學資訊所"
                },
                "jobName": {
                  "type": "str",
                  "example": "研究助理"
                },
                "schoolName": {
                  "type": "str",
                  "example": "國立陽明交通大學"
                },
                "majorName": {
                  "type": "str",
                  "example": "生物醫學資訊研究所"
                },
                "degreeLevel": {
                  "type": "int",
                  "example": "0"
                }
              }
            },
            "aboutMe": {
              "type": "str",
              "example": "【急診護理師跨領域資料科學，喜歡透過數據說故事】\n我畢業於護理系曾於急診室工作，生醫資訊研究所畢業後具備健保資料庫分析與醫師合作的經驗，擅長利用SAS、R、python進行資料處理及統計分析，也上過機器與深度學習相關課程。熱愛嘗試新事物的人，不畏懼挑戰願意學習，面對問題會努力尋找解決方法，思考背後的原因，喜歡照顧別人，享受學習醫學與電腦科學相關知識，高中開始參加管樂團培養團隊合作及溝通的能力。"
            },
            "motto": {
              "type": "str",
              "example": ""
            },
            "abilities": {
              "type": "array",
              "items": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "資料處理"
                  },
                  {
                    "type": "str",
                    "example": "SAS統計分析"
                  },
                  {
                    "type": "str",
                    "example": "積極主動"
                  },
                  {
                    "type": "str",
                    "example": "團隊合作"
                  },
                  {
                    "type": "str",
                    "example": "學習力佳"
                  },
                  {
                    "type": "str",
                    "example": "抗壓性高"
                  }
                ]
              }
            },
            "preferJobTitle": {
              "type": "str",
              "example": "數據分析師、資料分析師、數據工程師、統計分析師、資料科學家、SAS programmer、data analyst、data scientist、data engineer"
            },
            "viewCount": {
              "type": "int",
              "example": "1566"
            },
            "createdAt": {
              "type": "str",
              "example": "2023-01-27 20:26:49"
            },
            "isSelf": {
              "type": "bool",
              "example": "False"
            },
            "signIn": {
              "type": "bool",
              "example": "True"
            },
            "followerCount": {
              "type": "int",
              "example": "0"
            },
            "followedCount": {
              "type": "int",
              "example": "0"
            },
            "followed": {
              "type": "bool",
              "example": "False"
            },
            "isFollowed": {
              "type": "bool",
              "example": "False"
            },
            "isFollowingMe": {
              "type": "bool",
              "example": "False"
            },
            "hasBeenRequested": {
              "type": "bool",
              "example": "False"
            },
            "hasRequestedMe": {
              "type": "bool",
              "example": "False"
            },
            "publicStatus": {
              "type": "int",
              "example": "1"
            },
            "uuid": {
              "type": "str",
              "example": "52bba939-8c84-49b7-9368-cfd355b724ee"
            },
            "personalLink1Type": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "個人網站"
                },
                "value": {
                  "type": "int",
                  "example": "1"
                }
              }
            },
            "personalLink2Type": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "Github"
                },
                "value": {
                  "type": "int",
                  "example": "8"
                }
              }
            },
            "personalLink3Type": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "str",
                  "example": "Facebook"
                },
                "value": {
                  "type": "int",
                  "example": "4"
                }
              }
            },
            "personalLink1Url": {
              "type": "str",
              "example": ""
            },
            "personalLink2Url": {
              "type": "str",
              "example": ""
            },
            "personalLink3Url": {
              "type": "str",
              "example": ""
            },
            "themeChoose": {
              "type": "object",
              "properties": {
                "selectedTheme": {
                  "type": "object",
                  "properties": {
                    "text": {
                      "type": "str",
                      "example": "經典風格"
                    },
                    "value": {
                      "type": "int",
                      "example": "1"
                    },
                    "name": {
                      "type": "str",
                      "example": "ProfileThemeClassic"
                    }
                  }
                },
                "backgroundColor": {
                  "type": "str",
                  "example": ""
                }
              }
            }
          }
        },
        "publicStatus": {
          "type": "int",
          "example": "1"
        }
      }
    },
    "metadata": {
      "type": "object",
      "properties": {}
    }
  }
}
```

### Field Descriptions

| Field Path | Type | Description |
|------------|------|-------------|
| data.experience.experiences[].duration.startMonth.value | int | 3 |
| data.experience.experiences[].duration.startMonth.value | int | 9 |
| data.experience.experiences[].duration.startMonth.value | int | 9 |
| data.experience.experiences[].duration.startMonth.value | int | 7 |
| data.experience.experiences[].duration.startMonth.value | int | 7 |
| data.experience.experiences[].duration.startMonth.value | int | 1 |
| data.experience.experiences[].duration.startMonth.value | int | 10 |
| data.experience.experiences[].duration.startMonth.text | str | 3 |
| data.experience.experiences[].duration.startMonth.text | str | 9 |
| data.experience.experiences[].duration.startMonth.text | str | 9 |
| data.experience.experiences[].duration.startMonth.text | str | 7 |
| data.experience.experiences[].duration.startMonth.text | str | 7 |
| data.experience.experiences[].duration.startMonth.text | str | 1 |
| data.experience.experiences[].duration.startMonth.text | str | 10 |
| data.experience.experiences[].duration.startYear | str | 2023 |
| data.experience.experiences[].duration.startYear | str | 2022 |
| data.experience.experiences[].duration.startYear | str | 2021 |
| data.experience.experiences[].duration.startYear | str | 2018 |
| data.experience.experiences[].duration.startYear | str | 2022 |
| data.experience.experiences[].duration.startYear | str | 2022 |
| data.experience.experiences[].duration.startYear | str | 2019 |
| data.experience.experiences[].duration.endMonth[] | any |  |
| data.experience.experiences[].duration.endMonth.text | str | 1 |
| data.experience.experiences[].duration.endMonth.value | int | 1 |
| data.experience.experiences[].duration.endMonth.text | str | 2 |
| data.experience.experiences[].duration.endMonth.value | int | 2 |
| data.experience.experiences[].duration.endMonth.text | str | 9 |
| data.experience.experiences[].duration.endMonth.value | int | 9 |
| data.experience.experiences[].duration.endMonth.text | str | 12 |
| data.experience.experiences[].duration.endMonth.value | int | 12 |
| data.experience.experiences[].duration.endMonth[] | any |  |
| data.experience.experiences[].duration.endMonth.text | str | 3 |
| data.experience.experiences[].duration.endMonth.value | int | 3 |
| data.experience.experiences[].duration.endYear | str |  |
| data.experience.experiences[].duration.endYear | str | 2023 |
| data.experience.experiences[].duration.endYear | str | 2022 |
| data.experience.experiences[].duration.endYear | str | 2018 |
| data.experience.experiences[].duration.endYear | str | 2022 |
| data.experience.experiences[].duration.endYear | str |  |
| data.experience.experiences[].duration.endYear | str | 2021 |
| data.experience.experiences[].jobName | str | 工程師 |
| data.experience.experiences[].jobName | str | AI 智慧應用開發實戰養成班 |
| data.experience.experiences[].jobName | str | 台積電計畫研究生 |
| data.experience.experiences[].jobName | str | 實習生 |
| data.experience.experiences[].jobName | str | 軟體研究部門實習生 |
| data.experience.experiences[].jobName | str | 吳俊穎教授實驗室研究助理 |
| data.experience.experiences[].jobName | str | 急診護理師 |
| data.experience.experiences[].jobType.value | int | 1 |
| data.experience.experiences[].jobType.value | int | 1 |
| data.experience.experiences[].jobType.value | int | 2 |
| data.experience.experiences[].jobType.value | int | 2 |
| data.experience.experiences[].jobType.value | int | 2 |
| data.experience.experiences[].jobType.value | int | 2 |
| data.experience.experiences[].jobType.value | int | 1 |
| data.experience.experiences[].jobType.text | str | 全職 |
| data.experience.experiences[].jobType.text | str | 全職 |
| data.experience.experiences[].jobType.text | str | 兼職 |
| data.experience.experiences[].jobType.text | str | 兼職 |
| data.experience.experiences[].jobType.text | str | 兼職 |
| data.experience.experiences[].jobType.text | str | 兼職 |
| data.experience.experiences[].jobType.text | str | 全職 |
| data.experience.experiences[].salaryVisibility | bool | False |
| data.experience.experiences[].salaryVisibility | bool | False |
| data.experience.experiences[].salaryVisibility | bool | False |
| data.experience.experiences[].salaryVisibility | bool | False |
| data.experience.experiences[].salaryVisibility | bool | False |
| data.experience.experiences[].salaryVisibility | bool | False |
| data.experience.experiences[].salaryVisibility | bool | False |
| data.experience.experiences[].companyScale[] | any |  |
| data.experience.experiences[].companyScale[] | any |  |
| data.experience.experiences[].companyScale[] | any |  |
| data.experience.experiences[].companyScale[] | any |  |
| data.experience.experiences[].companyScale.text | str | 500人以上 |
| data.experience.experiences[].companyScale.value | int | 4 |
| data.experience.experiences[].companyScale.text | str | 500人以上 |
| data.experience.experiences[].companyScale.value | int | 4 |
| data.experience.experiences[].companyScale.text | str | 500人以上 |
| data.experience.experiences[].companyScale.value | int | 4 |
| data.experience.experiences[].skill[] | any |  |
| data.experience.experiences[].skill[] | any |  |
| data.experience.experiences[].skill[] | any |  |
| data.experience.experiences[].skill[].text | str | 顯示器技術 |
| data.experience.experiences[].skill[].value | str | 0 |
| data.experience.experiences[].skill[].text | str | TFT知識 |
| data.experience.experiences[].skill[].value | str | 0 |
| data.experience.experiences[].skill[] | any |  |
| data.experience.experiences[].skill[] | any |  |
| data.experience.experiences[].skill[].text | str | 護理指導及諮詢 |
| data.experience.experiences[].skill[].value | str | 11012010016 |
| data.experience.experiences[].skill[].text | str | 執行靜脈或肌肉注射相關作業 |
| data.experience.experiences[].skill[].value | str | 11012010008 |
| data.experience.experiences[].skill[].text | str | 預防保護之護理措施 |
| data.experience.experiences[].skill[].value | str | 11012010012 |
| data.experience.experiences[].skill[].text | str | 健康問題之護理評估 |
| data.experience.experiences[].skill[].value | str | 11007003010 |
| data.experience.experiences[].skill[].text | str | 急救甦醒器之使用與維護 |
| data.experience.experiences[].skill[].value | str | 11012010020 |
| data.experience.experiences[].skill[].text | str | 協同專科醫師進行會診或轉診 |
| data.experience.experiences[].skill[].value | str | 11012010001 |
| data.experience.experiences[].stillWork | bool | True |
| data.experience.experiences[].stillWork | bool | False |
| data.experience.experiences[].stillWork | bool | False |
| data.experience.experiences[].stillWork | bool | False |
| data.experience.experiences[].stillWork | bool | False |
| data.experience.experiences[].stillWork | bool | True |
| data.experience.experiences[].stillWork | bool | False |
| data.experience.experiences[].sort | int | 4 |
| data.experience.experiences[].sort | int | 1 |
| data.experience.experiences[].sort | int | 2 |
| data.experience.experiences[].sort | int | 3 |
| data.experience.experiences[].sort | int | 1 |
| data.experience.experiences[].sort | int | 2 |
| data.experience.experiences[].sort | int | 3 |
| data.experience.experiences[].logo | str |  |
| data.experience.experiences[].logo | str | https://static.104.com.tw/b_profile/cust_picture/2476/130000000082476/logo.png?v=20250410150005 |
| data.experience.experiences[].logo | str | https://static.104.com.tw/b_profile/cust_picture/1000/22099131000/logo.gif?v=20220111153850 |
| data.experience.experiences[].logo | str | https://static.104.com.tw/b_profile/cust_picture/8000/84149738000/logo.png?v=20250321110724 |
| data.experience.experiences[].logo | str | https://static.104.com.tw/b_profile/cust_picture/6001/5076416001/logo.gif?v=20241213151351 |
| data.experience.experiences[].logo | str |  |
| data.experience.experiences[].logo | str |  |
| data.experience.experiences[].jobCat[].no | int | 2007001020 |
| data.experience.experiences[].jobCat[].no | int | 2007001004 |
| data.experience.experiences[].jobCat[].no | int | 2016001013 |
| data.experience.experiences[].jobCat[].no | int | 2008001018 |
| data.experience.experiences[].jobCat[].no | int | 2002001011 |
| data.experience.experiences[].jobCat[].no | int | 2016001013 |
| data.experience.experiences[].jobCat[].no | int | 2015001004 |
| data.experience.experiences[].jobCat[].des | str | AI工程師 |
| data.experience.experiences[].jobCat[].des | str | 軟體工程師 |
| data.experience.experiences[].jobCat[].des | str | 研究助理 |
| data.experience.experiences[].jobCat[].des | str | 光電工程師 |
| data.experience.experiences[].jobCat[].des | str | 工讀生 |
| data.experience.experiences[].jobCat[].des | str | 研究助理 |
| data.experience.experiences[].jobCat[].des | str | 護理師及護士 |
| data.experience.experiences[].invoice | int | 94096794 |
| data.experience.experiences[].invoice | int | 24708053 |
| data.experience.experiences[].invoice | int | 22099131 |
| data.experience.experiences[].invoice | int | 84149738 |
| data.experience.experiences[].invoice | int | 5076416 |
| data.experience.experiences[].invoice | int | 0 |
| data.experience.experiences[].invoice | int | 29906905 |
| data.experience.experiences[].workArea[].no | int | 6001001010 |
| data.experience.experiences[].workArea[].no | int | 6001002004 |
| data.experience.experiences[].workArea[].no | int | 6001006001 |
| data.experience.experiences[].workArea[].no | int | 6001006001 |
| data.experience.experiences[].workArea[].no | int | 6001001004 |
| data.experience.experiences[].workArea[].no | int | 6001001009 |
| data.experience.experiences[].workArea[].no | int | 6001001009 |
| data.experience.experiences[].workArea[].des | str | 台北市內湖區 |
| data.experience.experiences[].workArea[].des | str | 新北市汐止區 |
| data.experience.experiences[].workArea[].des | str | 新竹市 |
| data.experience.experiences[].workArea[].des | str | 新竹市 |
| data.experience.experiences[].workArea[].des | str | 台北市松山區 |
| data.experience.experiences[].workArea[].des | str | 台北市北投區 |
| data.experience.experiences[].workArea[].des | str | 台北市北投區 |
| data.experience.experiences[].description | str | <p><span style="background-color:rgb(255,255,255);color:rgba(0,0,0,0.9);">Developing Deep Learning Solution : AutoEncoder or LSTM for Engineering including Wind speed or vibration signal analysis so far.</span></p><p><span style="background-color:rgb(255,255,255);color:rgba(0,0,0,0.9);">Good at 1-D Signal Processing (FFT 、wavelet Transform), ready to study 2-D Signal Processing</span></p> |
| data.experience.experiences[].description | str | ● 負責功能整合成桌面應用及GUI呈現 #Let's Dance 舞蹈辨識系統
● 使用 threading 平行化技術 達成遊戲同時多工效果
● 使用 PyQt5 將跳舞遊玩結果以GUI呈現給消費者
● 500小時學習資料收集、清洗，AI模型訓練，部署模型至雲端，資料視覺化等AI完整應用 |
| data.experience.experiences[].description | str | ● 研究所期間與台積電為期半年的合作計畫
● 使用 Matlab 對光的傳播進行傅立葉分析，模擬光阻內最小氣泡的位置，以提升元件良率 |
| data.experience.experiences[].description | str | ● 研究所期間參與友達光電的暑期實習計畫
● 75吋面板正視、側視收光量測
● 學習產品TFT - LCD原理，反推defect成因並解決 |
| data.experience.experiences[].description | str | ● 此為經濟部工業局「Digitalent」實習計畫 – 「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」 專案
1. 專案發想、時程規劃安排、論文技術討論
2.負責與醫院端及產業端合作溝通
3. 協助臨床數據收集
4. 協助利用python以機器學習方式建置呼吸音辨識模型 |
| data.experience.experiences[].description | str | 協助臨床研究收案，健保資料庫分析，實驗室相關庶務

● 協助執行科技部計畫 – 「腸道微菌叢對於新冠肺炎疫苗相關免疫反應、副作用、持久性及突破性感染之角色」 
1. 負責計畫部分臨床收案，需主動找尋受試者、和民眾溝通，與醫院單位協調
2.進行實驗室血液檢體分析、檢體保存管理、估算使用成本等事務

● 健保資料庫統計分析：
1. 與醫學中心皮膚科醫師合作進行健康資料流行病學分析，曾處理過慢性腎臟病與類天疱瘡相關性、白斑與視網膜剝離的關聯性、系統性藥物治療的乾癬患者發生心血管疾病的風險、類天皰瘡與各感染疾病之關係等案件。
2.藉由資料庫分析，處理過2300萬人的大型資料數據。

● 就學期間曾修習相關領域課程：SAS資料分析及應用、資料科學軟體實作、雲端技術及網路服務實務、資料視覺化與視覺分析、進階流行病學研究設計、深度學習於生醫資料分析 、資料探勘，且於在學期間取得公衛師考試的資格。 |
| data.experience.experiences[].description | str | 擔任急診護理師需具備刻苦耐勞的個性、能力上需反應快動作靈敏、與人可以良好溝通。工作內容主要為照顧病人，協助醫師診治，執行護理相關技術，急救處理(ACLS)。 |
| data.experience.experiences[].companyName | str | 神耀科技股份有限公司 |
| data.experience.experiences[].companyName | str | 緯育股份有限公司 |
| data.experience.experiences[].companyName | str | 台灣積體電路製造股份有限公司 |
| data.experience.experiences[].companyName | str | 友達光電股份有限公司 |
| data.experience.experiences[].companyName | str | 財團法人資訊工業策進會 |
| data.experience.experiences[].companyName | str | 國立陽明交通大學 |
| data.experience.experiences[].companyName | str | 臺北榮民總醫院 |
| data.experience.experiences[].salary.yearPay | str |  |
| data.experience.experiences[].salary.yearPay | str |  |
| data.experience.experiences[].salary.yearPay | str |  |
| data.experience.experiences[].salary.yearPay | str |  |
| data.experience.experiences[].salary.yearPay | str |  |
| data.experience.experiences[].salary.yearPay | str |  |
| data.experience.experiences[].salary.yearPay | str |  |
| data.experience.experiences[].salary.jobParttimeType.value | int | 1 |
| data.experience.experiences[].salary.jobParttimeType.value | int | 1 |
| data.experience.experiences[].salary.jobParttimeType.value | int | 1 |
| data.experience.experiences[].salary.jobParttimeType.value | int | 3 |
| data.experience.experiences[].salary.jobParttimeType.value | int | 1 |
| data.experience.experiences[].salary.jobParttimeType.value | int | 1 |
| data.experience.experiences[].salary.jobParttimeType.value | int | 1 |
| data.experience.experiences[].salary.jobParttimeType.text | str | 平均時薪 |
| data.experience.experiences[].salary.jobParttimeType.text | str | 平均時薪 |
| data.experience.experiences[].salary.jobParttimeType.text | str | 平均時薪 |
| data.experience.experiences[].salary.jobParttimeType.text | str | 平均月薪 |
| data.experience.experiences[].salary.jobParttimeType.text | str | 平均時薪 |
| data.experience.experiences[].salary.jobParttimeType.text | str | 平均時薪 |
| data.experience.experiences[].salary.jobParttimeType.text | str | 平均時薪 |
| data.experience.experiences[].salary.monthPay | str |  |
| data.experience.experiences[].salary.monthPay | str |  |
| data.experience.experiences[].salary.monthPay | str |  |
| data.experience.experiences[].salary.monthPay | str |  |
| data.experience.experiences[].salary.monthPay | str |  |
| data.experience.experiences[].salary.monthPay | str |  |
| data.experience.experiences[].salary.monthPay | str |  |
| data.experience.experiences[].salary.jobParttimePay | str |  |
| data.experience.experiences[].salary.jobParttimePay | str |  |
| data.experience.experiences[].salary.jobParttimePay | str |  |
| data.experience.experiences[].salary.jobParttimePay | int | 28000 |
| data.experience.experiences[].salary.jobParttimePay | str |  |
| data.experience.experiences[].salary.jobParttimePay | str |  |
| data.experience.experiences[].salary.jobParttimePay | str |  |
| data.experience.experiences[].companyVisibility | bool | True |
| data.experience.experiences[].companyVisibility | bool | True |
| data.experience.experiences[].companyVisibility | bool | True |
| data.experience.experiences[].companyVisibility | bool | True |
| data.experience.experiences[].companyVisibility | bool | True |
| data.experience.experiences[].companyVisibility | bool | True |
| data.experience.experiences[].companyVisibility | bool | True |
| data.experience.experiences[].custNo | int | 0 |
| data.experience.experiences[].custNo | str | 1a2x6bjqy4 |
| data.experience.experiences[].custNo | str | a5h92m0 |
| data.experience.experiences[].custNo | str | 12nokxe8 |
| data.experience.experiences[].custNo | str | 2byd7nl |
| data.experience.experiences[].custNo | int | 0 |
| data.experience.experiences[].custNo | str | dqlsrl4 |
| data.experience.experiences[].industry[].no | int | 1001001001 |
| data.experience.experiences[].industry[].no | int | 1001001001 |
| data.experience.experiences[].industry[].no | int | 1001006002 |
| data.experience.experiences[].industry[].no | int | 1001004002 |
| data.experience.experiences[].industry[].no | int | 1001001002 |
| data.experience.experiences[].industry[].no | int | 1005001007 |
| data.experience.experiences[].industry[].no | int | 1012001001 |
| data.experience.experiences[].industry[].des | str | 電腦系統整合服務業 |
| data.experience.experiences[].industry[].des | str | 電腦系統整合服務業 |
| data.experience.experiences[].industry[].des | str | 半導體製造業 |
| data.experience.experiences[].industry[].des | str | 光學器材製造業 |
| data.experience.experiences[].industry[].des | str | 電腦軟體服務業 |
| data.experience.experiences[].industry[].des | str | 大專校院教育事業 |
| data.experience.experiences[].industry[].des | str | 醫院 |
| data.experience.seniority.value | int | 0 |
| data.experience.seniority.value | int | 1 |
| data.experience.seniority.text | str | 1年(含)以下 |
| data.experience.seniority.text | str | 1~2年 |
| data.custom1[] | any |  |
| data.custom1.custom.sort | int | 1 |
| data.custom1.custom.name | str | 經濟部跨域數位人才加速躍升計畫 |
| data.custom1.custom.content[].duration.startYear | str | 2022 |
| data.custom1.custom.content[].duration.startMonth.text | str | 7 |
| data.custom1.custom.content[].duration.startMonth.value | int | 7 |
| data.custom1.custom.content[].duration.endYear | str | 2022 |
| data.custom1.custom.content[].duration.endMonth.text | str | 12 |
| data.custom1.custom.content[].duration.endMonth.value | int | 12 |
| data.custom1.custom.content[].isInProgress | bool | False |
| data.custom1.custom.content[].introduction | str | 【DIGI+Talent 跨域數位人才加速躍升計畫】
此跨域計畫為行政院自2017年起推動「數位國家・創新經濟發展方案（簡稱DIGI+）」，入選為2022年智慧聯網類研習生，以「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」為主題，團隊於2022年底成果發表會42組隊伍中獲得第二名佳績。

● 由資訊工業策進會業師指導，與醫院及國內業者合作推行專案
● 經歷6個月實習，總時數超過240小時的研習及30小時線上課程學習。
●專案內容涵蓋Python程式設計、智慧聯網、機器學習應用實務、語音辨識、萃取音訊特徵，對音訊進行分析等。 |
| data.custom1.custom.content[].url | str | https://www.youtube.com/watch?v=uWeHwZRZI6M&list=PLoQj70ABw1jnRdB-HBAOgFj2Ini6hEp1_&index=6 |
| data.custom1.themeChoose.selectedTheme.text | str | 經典風格 |
| data.custom1.themeChoose.selectedTheme.value | int | 1 |
| data.custom1.themeChoose.selectedTheme.name | str | CustomThemeClassic |
| data.custom1.img.pic | int | 1 |
| data.custom1.img.fileId | str | custom_content_img1 |
| data.custom1.img.src | str | https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img1?v=1675868589 |
| data.custom1.img2.pic | int | 0 |
| data.custom1.img2.fileId | str |  |
| data.custom1.img2.src | str |  |
| data.custom2[] | any |  |
| data.custom2.custom.sort | int | 2 |
| data.custom2.custom.name | str | 論文專案 |
| data.custom2.custom.content[].duration.startYear | str | 2022 |
| data.custom2.custom.content[].duration.startMonth.text | str | 3 |
| data.custom2.custom.content[].duration.startMonth.value | int | 3 |
| data.custom2.custom.content[].duration.endYear | str | 2023 |
| data.custom2.custom.content[].duration.endMonth.text | str | 1 |
| data.custom2.custom.content[].duration.endMonth.value | int | 1 |
| data.custom2.custom.content[].isInProgress | bool | False |
| data.custom2.custom.content[].introduction | str | 【慢性腎臟病與類天皰瘡發生風險之相關性：族群的世代研究】
● 運用大數據分析慢性腎臟病與類天皰瘡的關聯性之論文
● 臺灣慢性腎臟病盛行率達11.9%，約200萬人受此疾病所苦
● 使用2300萬人口的數據資料，處理過數億筆資料的經驗
● 進行研究族群之人口學特徵描述性統計、計算不同分類人口中的發生率
● 針對慢性腎臟病與類天皰瘡進行存活分析，觀察10年期間的變化
●進行不同組間，不同疾病、年齡、性別間的風險比計算、分層分析 |
| data.custom2.custom.content[].url | str |  |
| data.custom2.themeChoose.selectedTheme.text | str | 經典風格 |
| data.custom2.themeChoose.selectedTheme.value | int | 1 |
| data.custom2.themeChoose.selectedTheme.name | str | CustomThemeClassic |
| data.custom2.img.pic | int | 1 |
| data.custom2.img.fileId | str | custom_content_img2 |
| data.custom2.img.src | str | https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img2?v=1675867362 |
| data.custom2.img2.pic | int | 0 |
| data.custom2.img2.fileId | str |  |
| data.custom2.img2.src | str |  |
| data.profile.uuid | str | cf3ab3b1-e057-419a-a0f2-747d778f178d |
| data.profile.uuid | str | 52bba939-8c84-49b7-9368-cfd355b724ee |
| data.profile.personalLink3Type.value | int | 4 |
| data.profile.personalLink3Type.value | int | 4 |
| data.profile.personalLink3Type.text | str | Facebook |
| data.profile.personalLink3Type.text | str | Facebook |
| data.profile.signIn | bool | True |
| data.profile.signIn | bool | True |
| data.profile.createdAt | str | 2024-02-15 15:26:08 |
| data.profile.createdAt | str | 2023-01-27 20:26:49 |
| data.profile.headshotUrl | str | https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/avatar?v=1743305442 |
| data.profile.headshotUrl | str | https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/avatar?v=1743309994 |
| data.profile.imageUrl | str | https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/background_img.jpeg?v=1743305442 |
| data.profile.imageUrl | str |  |
| data.profile.isSelf | bool | False |
| data.profile.isSelf | bool | False |
| data.profile.motto | str |  |
| data.profile.motto | str |  |
| data.profile.aboutMe | str | <p><span style="color: rgba(0, 0, 0, 0.9); background-color: rgb(255, 255, 255);">Developing Deep Learning Solution : AutoEncoder or LSTM for Engineering including Wind speed or vibration signal analysis so far.</span></p><p><span style="color: rgba(0, 0, 0, 0.9); background-color: rgb(255, 255, 255);">Good at 1-D Signal Processing (FFT 、wavelet Transform), ready to study 2-D Signal Processing</span></p><p><br /></p><p>Expertise: Good at Optics, <span style="background-color: rgb(255, 255, 255); color: rgb(77, 81, 86);">Electromagnetism.</span></p><p>Self-Improving: learning C++, reviewing Linear Algebra, Electric knowledge after work shift.</p> |
| data.profile.aboutMe | str | 【急診護理師跨領域資料科學，喜歡透過數據說故事】
我畢業於護理系曾於急診室工作，生醫資訊研究所畢業後具備健保資料庫分析與醫師合作的經驗，擅長利用SAS、R、python進行資料處理及統計分析，也上過機器與深度學習相關課程。熱愛嘗試新事物的人，不畏懼挑戰願意學習，面對問題會努力尋找解決方法，思考背後的原因，喜歡照顧別人，享受學習醫學與電腦科學相關知識，高中開始參加管樂團培養團隊合作及溝通的能力。 |
| data.profile.isFollowingMe | bool | False |
| data.profile.isFollowingMe | bool | False |
| data.profile.followed | bool | False |
| data.profile.followed | bool | False |
| data.profile.followerCount | int | 0 |
| data.profile.followerCount | int | 0 |
| data.profile.abilities[] | str | 團隊溝通 |
| data.profile.abilities[] | str | 主動討論 |
| data.profile.abilities[] | str | 角色適應 |
| data.profile.abilities[] | str | 自強不息 |
| data.profile.abilities[] | str | 持續學習 |
| data.profile.abilities[] | str | 資料處理 |
| data.profile.abilities[] | str | SAS統計分析 |
| data.profile.abilities[] | str | 積極主動 |
| data.profile.abilities[] | str | 團隊合作 |
| data.profile.abilities[] | str | 學習力佳 |
| data.profile.abilities[] | str | 抗壓性高 |
| data.profile.preferJobTitle | str | 演算法工程師、軟/韌體工程師、資料科學家、後端工程師、光學(研發)工程師 |
| data.profile.preferJobTitle | str | 數據分析師、資料分析師、數據工程師、統計分析師、資料科學家、SAS programmer、data analyst、data scientist、data engineer |
| data.profile.themeChoose.selectedTheme.name | str | ProfileThemeClassic |
| data.profile.themeChoose.selectedTheme.name | str | ProfileThemeClassic |
| data.profile.themeChoose.selectedTheme.value | int | 1 |
| data.profile.themeChoose.selectedTheme.value | int | 1 |
| data.profile.themeChoose.selectedTheme.text | str | 經典風格 |
| data.profile.themeChoose.selectedTheme.text | str | 經典風格 |
| data.profile.themeChoose.backgroundColor | str |  |
| data.profile.themeChoose.backgroundColor | str |  |
| data.profile.title.degreeLevel | int | 0 |
| data.profile.title.degreeLevel | int | 0 |
| data.profile.title.jobName | str | AI工程師 |
| data.profile.title.jobName | str | 研究助理 |
| data.profile.title.majorName | str |  |
| data.profile.title.majorName | str | 生物醫學資訊研究所 |
| data.profile.title.companyName | str | 神耀科技股份有限公司 |
| data.profile.title.companyName | str | 陽明交通大學生物醫學資訊所 |
| data.profile.title.schoolName | str |  |
| data.profile.title.schoolName | str | 國立陽明交通大學 |
| data.profile.title.workExperience | int | 0 |
| data.profile.title.workExperience | int | 0 |
| data.profile.personalLink2Url | str | https://www.linkedin.com/in/josh-smith-706891241/ |
| data.profile.personalLink2Url | str |  |
| data.profile.viewCount | int | 3424 |
| data.profile.viewCount | int | 1566 |
| data.profile.hasBeenRequested | bool | False |
| data.profile.hasBeenRequested | bool | False |
| data.profile.publicStatus | int | 1 |
| data.profile.publicStatus | int | 1 |
| data.profile.key | str | 3Cs09h2VRhp |
| data.profile.key | str | 1ZSUUFKUw0r |
| data.profile.followedCount | int | 0 |
| data.profile.followedCount | int | 0 |
| data.profile.personalLink1Url | str | https://github.com/joshsmiththenoob |
| data.profile.personalLink1Url | str |  |
| data.profile.personalLink3Url | str | https://www.facebook.com/profile.php?id=100002502312505 |
| data.profile.personalLink3Url | str |  |
| data.profile.nickname | str | 傅騰緯 |
| data.profile.nickname | str | 陳彥伶 |
| data.profile.personalLink1Type.value | int | 8 |
| data.profile.personalLink1Type.value | int | 1 |
| data.profile.personalLink1Type.text | str | Github |
| data.profile.personalLink1Type.text | str | 個人網站 |
| data.profile.hasRequestedMe | bool | False |
| data.profile.hasRequestedMe | bool | False |
| data.profile.personalLink2Type.value | int | 1 |
| data.profile.personalLink2Type.value | int | 8 |
| data.profile.personalLink2Type.text | str | 個人網站 |
| data.profile.personalLink2Type.text | str | Github |
| data.profile.isFollowed | bool | False |
| data.profile.isFollowed | bool | False |
| data.skill.skills[].sort | int | 1 |
| data.skill.skills[].sort | int | 2 |
| data.skill.skills[].sort | int | 3 |
| data.skill.skills[].sort | int | 4 |
| data.skill.skills[].sort | int | 5 |
| data.skill.skills[].sort | int | 6 |
| data.skill.skills[].sort | int | 1 |
| data.skill.skills[].sort | int | 2 |
| data.skill.skills[].sort | int | 3 |
| data.skill.skills[].sort | int | 4 |
| data.skill.skills[].sort | int | 5 |
| data.skill.skills[].name | str | Programming Language |
| data.skill.skills[].name | str | Back-End |
| data.skill.skills[].name | str | DataBase |
| data.skill.skills[].name | str | AI |
| data.skill.skills[].name | str | Engineering |
| data.skill.skills[].name | str | Tools |
| data.skill.skills[].name | str | 程式語言 |
| data.skill.skills[].name | str | 統計軟體 |
| data.skill.skills[].name | str | Microsoft Office |
| data.skill.skills[].name | str | 數據分析-全民健保資料庫 |
| data.skill.skills[].name | str | 醫療護理 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].status | int | 1 |
| data.skill.skills[].tag[].text | str | 軟體程式設計 |
| data.skill.skills[].tag[].value | str | 11009005001 |
| data.skill.skills[].tag[] | any |  |
| data.skill.skills[].tag[] | any |  |
| data.skill.skills[].tag[].text | str | Machine Learning |
| data.skill.skills[].tag[].value | str | 11009005007 |
| data.skill.skills[].tag[] | any |  |
| data.skill.skills[].tag[].text | str | Git |
| data.skill.skills[].tag[].value | str | 12001002018 |
| data.skill.skills[].tag[].text | str | SolidWorks |
| data.skill.skills[].tag[].value | str | 12002003012 |
| data.skill.skills[].tag[].text | str | Python |
| data.skill.skills[].tag[].value | str | 12001003045 |
| data.skill.skills[].tag[].text | str | 軟體程式設計 |
| data.skill.skills[].tag[].value | str | 11009005001 |
| data.skill.skills[].tag[].text | str | 軟體工程系統開發 |
| data.skill.skills[].tag[].value | str | 11009002008 |
| data.skill.skills[].tag[].text | str | 調查樣本統計分析 |
| data.skill.skills[].tag[].value | str | 11005004007 |
| data.skill.skills[].tag[].text | str | 統計軟體操作 |
| data.skill.skills[].tag[].value | str | 11005004004 |
| data.skill.skills[].tag[].text | str | 市場調查資料分析與報告撰寫 |
| data.skill.skills[].tag[].value | str | 11005004002 |
| data.skill.skills[].tag[].text | str | SPSS |
| data.skill.skills[].tag[].value | str | 12003005011 |
| data.skill.skills[].tag[].text | str | SAS |
| data.skill.skills[].tag[].value | str | 12003005009 |
| data.skill.skills[].tag[].text | str | PowerPoint |
| data.skill.skills[].tag[].value | str | 12001008012 |
| data.skill.skills[].tag[].text | str | Excel |
| data.skill.skills[].tag[].value | str | 12001008003 |
| data.skill.skills[].tag[].text | str | Outlook |
| data.skill.skills[].tag[].value | str | 12001008011 |
| data.skill.skills[].tag[].text | str | 文件檔案資料處理、轉換及整合工作 |
| data.skill.skills[].tag[].value | str | 11001005007 |
| data.skill.skills[].tag[].text | str | 文書處理╱排版能力 |
| data.skill.skills[].tag[].value | str | 11001005002 |
| data.skill.skills[].tag[].text | str | 文件或資料輸入建檔處理 |
| data.skill.skills[].tag[].value | str | 11001005006 |
| data.skill.skills[].tag[].text | str | 電話接聽與人員接待事項 |
| data.skill.skills[].tag[].value | str | 11001005005 |
| data.skill.skills[].tag[].text | str | 報表彙整與管理 |
| data.skill.skills[].tag[].value | str | 11001005004 |
| data.skill.skills[].tag[].text | str | 文件收發與檔案管理 |
| data.skill.skills[].tag[].value | str | 11001005001 |
| data.skill.skills[].tag[].text | str | Word |
| data.skill.skills[].tag[].value | str | 12001008016 |
| data.skill.skills[].tag[].text | str | SAS |
| data.skill.skills[].tag[].value | str | 12003005009 |
| data.skill.skills[].tag[].text | str | 撰寫研究報告與論文 |
| data.skill.skills[].tag[].value | str | 11017009011 |
| data.skill.skills[].tag[].text | str | 健康問題之護理評估 |
| data.skill.skills[].tag[].value | str | 11007003010 |
| data.skill.skills[].tag[].text | str | 執行靜脈或肌肉注射相關作業 |
| data.skill.skills[].tag[].value | str | 11012010008 |
| data.skill.skills[].tag[].text | str | 預防保護之護理措施 |
| data.skill.skills[].tag[].value | str | 11012010012 |
| data.skill.skills[].desc | str | <p>熟悉的程式語言 :</p><p>● Matlab </p><p>● Python</p><p>正在學習的程式語言:</p><p>● C++ </p> |
| data.skill.skills[].desc | str | 後端網路伺服器架設技能 :
●  Flask 
●  GCP 
●  AWS
●  Docker
●  Selenium 
● RESTful API |
| data.skill.skills[].desc | str | 擅長使用的DB及查詢語言 : 
●  MySQL 
●  MongoDB |
| data.skill.skills[].desc | str | 基礎機器學習、深度學習套件使用 :
●  Scikit-learn
●  Tensorflow 
●  PyTorch |
| data.skill.skills[].desc | str | <p>● Signal Processing : 目前做震動訊號處理(FFT, Hilbert Transform), Wavelet Transform, 朝向2D訊號處理學習中</p><p>● 強項為光學、電磁學</p> |
| data.skill.skills[].desc | str | <p>其他工具進行開發管理、資料視覺化或前後端整合</p><p>● Linux作業系統 (熟悉使用Ubuntu)</p><p>● Kafka 串流平台 (IoT資料即時傳輸)</p><p>● Git 版控</p><p>● LineBot</p><p>● Notion</p><p>● HackMD</p><p>● SolidWorks : 基礎3D建模</p><p>● OSLO : 幾何光學設計</p> |
| data.skill.skills[].desc | str | Python、R、SQL |
| data.skill.skills[].desc | str | SAS、SPSS、Stata |
| data.skill.skills[].desc | str | Word、Excel、PowerPoint |
| data.skill.skills[].desc | str | 公共衛生與流行病學統計，利用資料庫數據分析的方法，探討疾病間的關係
在學期間協助4篇論文分析:
1.慢性腎臟病與類天疱瘡發生風險之相關性：族群的世代研究
2.白斑與視網膜剝離的關聯性：全台灣人口研究調查
3.接受系統性藥物治療的乾癬患者發生心血管疾病的風險：以臺灣人口研究
4.類天皰瘡與各感染疾病之關係 |
| data.skill.skills[].desc | str | 醫學統計:熟悉健保資料庫、醫學統計相關應用
健康照護:熟悉病人照護、護理諮詢指導、護理技術執行
緊急醫療處理:了解緊急狀況之醫療處置及救護 |
| data.skill.themeChoose.name | str | SkillThemeCard |
| data.skill.themeChoose.name | str | SkillThemeCard |
| data.skill.themeChoose.value | int | 2 |
| data.skill.themeChoose.value | int | 2 |
| data.skill.themeChoose.text | str | 卡片式 |
| data.skill.themeChoose.text | str | 卡片式 |
| data.custom3[] | any |  |
| data.custom3.custom.sort | int | 3 |
| data.custom3.custom.name | str | 國立陽明交通大學愛杏管弦樂團 |
| data.custom3.custom.content[].duration.startYear | str | 2021 |
| data.custom3.custom.content[].duration.startMonth.text | str | 3 |
| data.custom3.custom.content[].duration.startMonth.value | int | 3 |
| data.custom3.custom.content[].duration.endYear | str | 2023 |
| data.custom3.custom.content[].duration.endMonth.text | str | 2 |
| data.custom3.custom.content[].duration.endMonth.value | int | 2 |
| data.custom3.custom.content[].isInProgress | bool | False |
| data.custom3.custom.content[].introduction | str | 【克服樂團的困境，協助建立好的風氣】
2022/10 - 2023/02
於加入管弦樂團後第二年遭遇團上經費嚴重不足，團員流失嚴重，因此加入幹部團隊，協助樂團行政工作。

●協助招募新團員:協助發布招募團員之文案
●尋求經費上贊助:透過統計軟體整理歷屆團員聯絡資訊，協助連絡已畢業學長姐
●協助舉行交大陽明校區巡迴演出活動 |
| data.custom3.custom.content[].url | str |  |
| data.custom3.themeChoose.selectedTheme.text | str | 經典風格 |
| data.custom3.themeChoose.selectedTheme.value | int | 1 |
| data.custom3.themeChoose.selectedTheme.name | str | CustomThemeClassic |
| data.custom3.img.pic | int | 1 |
| data.custom3.img.fileId | str | custom_content_img3 |
| data.custom3.img.src | str | https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img3?v=1675868597 |
| data.custom3.img2.pic | int | 0 |
| data.custom3.img2.fileId | str |  |
| data.custom3.img2.src | str |  |
| data.structured_data_sets[].@context | str | http://schema.org/ |
| data.structured_data_sets[].@type | str | Person |
| data.structured_data_sets[].name | str | Chun-Jung Huang |
| data.structured_data_sets[].image | str | https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.structured_data_sets[].description | str | To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success. |
| data.structured_data_sets[].url | str | https://www.cake.me/mortis-huang |
| data.structured_data_sets[].jobTitle | str | OPC Chief Engineer |
| data.structured_data_sets[].sameAs | str | https://mortis.tech/ |
| data.custom6[] | any |  |
| data.custom6[] | any |  |
| data.jobCondition.workShift | int | 1 |
| data.jobCondition.workShift | int | 0 |
| data.jobCondition.remoteWork.value | int | 1 |
| data.jobCondition.remoteWork.value | int | 1 |
| data.jobCondition.remoteWork.text | str | 對遠端工作有意願 |
| data.jobCondition.remoteWork.text | str | 對遠端工作有意願 |
| data.jobCondition.salaryOfHours | str |  |
| data.jobCondition.salaryOfHours | str |  |
| data.jobCondition.otherTimePeriod | str |  |
| data.jobCondition.otherTimePeriod | str |  |
| data.jobCondition.onBoardAfterGetOffer.value | int | 1 |
| data.jobCondition.onBoardAfterGetOffer.value | int | 0 |
| data.jobCondition.onBoardAfterGetOffer.text | str | 一週 |
| data.jobCondition.onBoardAfterGetOffer.text | str | 隨時 |
| data.jobCondition.onBoardDate.value | str | 1 |
| data.jobCondition.onBoardDate.value | str | 1 |
| data.jobCondition.onBoardDate.text | str | 錄取後 |
| data.jobCondition.onBoardDate.text | str | 錄取後 |
| data.jobCondition.jobTimeType[].value | int | 1 |
| data.jobCondition.jobTimeType[].value | int | 1 |
| data.jobCondition.jobTimeType[].text | str | 全職工作 |
| data.jobCondition.jobTimeType[].text | str | 全職工作 |
| data.jobCondition.preferJobContent | str |  |
| data.jobCondition.preferJobContent | str |  |
| data.jobCondition.preferJobIndustry[].no | int | 1001001000 |
| data.jobCondition.preferJobIndustry[].no | int | 1001004000 |
| data.jobCondition.preferJobIndustry[].no | int | 1004000000 |
| data.jobCondition.preferJobIndustry[].no | int | 1001000000 |
| data.jobCondition.preferJobIndustry[].no | int | 1004000000 |
| data.jobCondition.preferJobIndustry[].no | int | 1012000000 |
| data.jobCondition.preferJobIndustry[].des | str | 軟體及網路相關業 |
| data.jobCondition.preferJobIndustry[].des | str | 光電及光學相關業 |
| data.jobCondition.preferJobIndustry[].des | str | 金融投顧及保險業 |
| data.jobCondition.preferJobIndustry[].des | str | 電子資訊／軟體／半導體相關業 |
| data.jobCondition.preferJobIndustry[].des | str | 金融投顧及保險業 |
| data.jobCondition.preferJobIndustry[].des | str | 醫療保健及環境衛生業 |
| data.jobCondition.preferJobType[].no | int | 2008001018 |
| data.jobCondition.preferJobType[].no | int | 2008001019 |
| data.jobCondition.preferJobType[].no | int | 2007001012 |
| data.jobCondition.preferJobType[].no | int | 2007001006 |
| data.jobCondition.preferJobType[].no | int | 2007001004 |
| data.jobCondition.preferJobType[].no | int | 2016001007 |
| data.jobCondition.preferJobType[].no | int | 2004001010 |
| data.jobCondition.preferJobType[].no | int | 2007002002 |
| data.jobCondition.preferJobType[].no | int | 2003002008 |
| data.jobCondition.preferJobType[].des | str | 光電工程師 |
| data.jobCondition.preferJobType[].des | str | 光學工程師 |
| data.jobCondition.preferJobType[].des | str | 演算法工程師 |
| data.jobCondition.preferJobType[].des | str | Internet程式設計師 |
| data.jobCondition.preferJobType[].des | str | 軟體工程師 |
| data.jobCondition.preferJobType[].des | str | 統計學研究員 |
| data.jobCondition.preferJobType[].des | str | 市場調查／市場分析 |
| data.jobCondition.preferJobType[].des | str | 資料庫管理人員 |
| data.jobCondition.preferJobType[].des | str | 統計精算人員 |
| data.jobCondition.salary.value | int | 1 |
| data.jobCondition.salary.value | int | 1 |
| data.jobCondition.salary.text | str | 面議 |
| data.jobCondition.salary.text | str | 面議 |
| data.jobCondition.salariesOfYear[] | any |  |
| data.jobCondition.salariesOfYear[] | any |  |
| data.jobCondition.jobTimePeriod[].value | int | 1 |
| data.jobCondition.jobTimePeriod[].value | int | 1 |
| data.jobCondition.jobTimePeriod[].text | str | 日班 |
| data.jobCondition.jobTimePeriod[].text | str | 日班 |
| data.jobCondition.preferArea[].no | int | 6001001000 |
| data.jobCondition.preferArea[].no | int | 6001002000 |
| data.jobCondition.preferArea[].no | int | 6001005000 |
| data.jobCondition.preferArea[].no | int | 6001008000 |
| data.jobCondition.preferArea[].no | int | 6001014000 |
| data.jobCondition.preferArea[].no | int | 6001006000 |
| data.jobCondition.preferArea[].no | int | 6001001000 |
| data.jobCondition.preferArea[].no | int | 6001002000 |
| data.jobCondition.preferArea[].no | int | 6001006000 |
| data.jobCondition.preferArea[].des | str | 台北市 |
| data.jobCondition.preferArea[].des | str | 新北市 |
| data.jobCondition.preferArea[].des | str | 桃園市 |
| data.jobCondition.preferArea[].des | str | 台中市 |
| data.jobCondition.preferArea[].des | str | 台南市 |
| data.jobCondition.preferArea[].des | str | 新竹縣市 |
| data.jobCondition.preferArea[].des | str | 台北市 |
| data.jobCondition.preferArea[].des | str | 新北市 |
| data.jobCondition.preferArea[].des | str | 新竹縣市 |
| data.jobCondition.salaryPeriod.value | int | 5 |
| data.jobCondition.salaryPeriod.value | int | 5 |
| data.jobCondition.salaryPeriod.text | str | 月薪 |
| data.jobCondition.salaryPeriod.text | str | 月薪 |
| data.jobCondition.customOnBoardDate.date[] | any |  |
| data.jobCondition.customOnBoardDate.date[] | any |  |
| data.jobCondition.customOnBoardDate.month[] | any |  |
| data.jobCondition.customOnBoardDate.month[] | any |  |
| data.jobCondition.customOnBoardDate.year | str |  |
| data.jobCondition.customOnBoardDate.year | str |  |
| data.jobCondition.preferJobTitle | str | 演算法工程師、軟/韌體工程師、資料科學家、後端工程師、光學(研發)工程師 |
| data.jobCondition.preferJobTitle | str | 數據分析師、資料分析師、數據工程師、統計分析師、資料科學家、SAS programmer、data analyst、data scientist、data engineer |
| data.jobCondition.salaryOfMonth.unitOfThousand[] | any |  |
| data.jobCondition.salaryOfMonth.unitOfThousand[] | any |  |
| data.jobCondition.salaryOfMonth.unitOfTenThousand[] | any |  |
| data.jobCondition.salaryOfMonth.unitOfTenThousand[] | any |  |
| data.item.id | int | 1002587 |
| data.item.name | str | My CakeResume |
| data.item.description | str | Chun-Jung Huang mortis.huang@gmail.comNational Chiao-Tung University, Ph.D. - Photonics,2015 ~ 2020 Member of The Phi Tau Phi Scholastic Honor Soci... |
| data.item.path | str | mortis-huang |
| data.item.liked | bool | False |
| data.item.is_owner | bool | False |
| data.item.added_to_folder | bool | False |
| data.item.votes_total | int | 38 |
| data.item.lang | str | en |
| data.item.theme | str | default |
| data.item.editor_version | int | 0 |
| data.item.style | str | paper |
| data.item.spacing | str | normal |
| data.item.connected_with_posts | bool | False |
| data.item.seems_spam | bool | False |
| data.item.should_confirm_external_links | bool | False |
| data.item.system_generated | bool | False |
| data.item.exported_from_profile | bool | True |
| data.item.body | str | <div class="row snippet-profile-041"><div class="col-sm-8"><h1><b>Chun-Jung Huang</b></h1><p>mortis.huang@gmail.com</p><p>&nbsp;(+886)-988-728-641</p><p>National Chiao-Tung University, Ph.D. - Photonics,2015 ~ 2020&nbsp;</p><p>Member of The Phi Tau Phi Scholastic Honor Society of the Republic of China.<br></p></div><div class="col-sm-4"><img data-no-retina="true" src="https://images.cakeresume.com/XgMVZ/mortis-huang/191caa57-6fe0-4fd6-9b12-a9ce4ebafc0f.png" style="border-radius: 0px;" loading=""></div></div><div class="row snippet-features-001"><div class="col-sm-12"><div class="row"><div class="col-sm-12"><h1><b>Skills</b></h1></div></div><div class="row" title=""><div class="col-sm-12 item"><hr><p><b>Languages:</b> Python, MatLab, Shell scripting, LabVIEW&nbsp;</p><p><b>Deep Learning:</b> Proficient in CNNs, LLM development, and deployment.&nbsp;</p><p><b>GPU Programming: </b>Python CPU to GPU migration and acceleration optimization.&nbsp;</p><p><b>Developer Tools:</b>&nbsp;Obsidian, Nsight Systems, pdb (python debugger), and Git.

</p></div></div></div></div><div class="row snippet-experiences-013"><div class="col-xs-12"><div class="row"><div class="col-xs-12"><h1><b>Work Experience</b><br></h1></div></div><div class="row" title=""><div class="col-xs-2 col-sm-1 item-bullet"></div><div class="col-xs-10 col-sm-11 item"><h3>TSMC, nPtD/OPC-III Chief Engineer (March 2020 - Now)</h3><p><b>- Advanced CNN Applications:</b>&nbsp;</p><p>Integrated CNNs for enhanced anomaly detection and image processing.<br></p><p><b>- Localization of LLM:</b>&nbsp;</p><p>Customized large language models to meet specific operational needs, enhancing internal AI capabilities.<br></p><p><b>- GPU Acceleration:&nbsp;</b></p><p>Directed the migration of large Python codebases from CPU to GPU, leveraging CuPy API, cp.fuse, and RawKernel to optimize performance and reduce runtime by over 50%.<br></p></div></div><div class="row" title=""><div class="col-xs-2 col-sm-1 item-bullet"></div><div class="col-xs-10 col-sm-11 item"><h3> The University of Tokyo, Foreign Researcher (Oct. 2017 - Sep. 2018)</h3><p>Developed a CNN-based cell image recognition system from scratch, contributing to advancements in biomedical imaging and analysis.<br></p></div></div></div></div><div class="row snippet-educations-013 snippet-experiences-013"><div class="col-xs-12"><div class="row"><div class="col-xs-12"><h1><b>Education</b><br></h1></div></div><div class="row" title=""><div class="col-xs-2 col-sm-1 item-bullet"></div><div class="col-xs-10 col-sm-11 item"><h3><b>National Chiao-Tung University, Ph.D. - Photonics, 2015 ~ 2020</b></h3><p>Development of Intelligent Wearable Near Infrared Spectroscopy</p></div></div><div class="row" title=""><div class="col-xs-2 col-sm-1 item-bullet"></div><div class="col-xs-10 col-sm-11 item"><h3><b>National Chiao-Tung University, Bachelor - Photonics, 2011 ~ 2015</b></h3></div></div></div></div><div class="row snippet-paragraphs-001"><div class="col-xs-12"><h1><b>Main Publications</b></h1><ul><li>Virtual-freezing fluorescence imaging flow cytometry - <b>Nature communications</b>&nbsp;(IF:14.9) - 2020&nbsp;<br></li><li>Intelligent classification of platelet aggregates by agonist type - <b>Elife</b> (IF:8.14) - 2020<br></li><li>Label-free chemical imaging flow cytometry by high-speed multicolor stimulated Raman scattering - <b>PNAS</b> (IF:11.2) - 2019<br></li><li>Functional connectivity during phonemic and semantic verbal fluency test: a multichannel near infrared spectroscopy study -<b> JSTQE&nbsp;</b>(IF:4.5)&nbsp;- 2015<br></li></ul><p></p></div></div> |
| data.item.body_json_v2 | NoneType | None |
| data.item.user.name | str | Chun-Jung Huang |
| data.item.user.username | str | mortis-huang |
| data.item.user.id | int | 669487 |
| data.item.user.first_name | str | Chun-Jung |
| data.item.user.last_name | str | Huang |
| data.item.user.description | str | To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success. |
| data.item.user.cover_image.url | str | https://media.cakeresume.com/image/upload/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.cover_image.small.url | str | https://media.cakeresume.com/image/upload/c_crop,h_360,w_720/c_scale,h_180,w_360/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.cover_image.medium.url | str | https://media.cakeresume.com/image/upload/s--Vm8J95tp--/c_fill,h_360,w_720/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.cover_image.large.url | str | https://media.cakeresume.com/image/upload/s--VrSkpH3n--/c_fill,h_500,w_1500/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.cover_image.small_3_1.url | str | https://media.cakeresume.com/image/upload/s--YGPutB6G--/c_fill,f_auto,h_140,w_420/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.cover_image.medium_3_1.url | str | https://media.cakeresume.com/image/upload/s--6GTJ9tLF--/c_fill,f_auto,h_314,w_942/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.avatar.url | str | https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.avatar.tiny.url | str | https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.avatar.small.url | str | https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.avatar.medium.url | str | https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.avatar.large.url | str | https://media.cakeresume.com/image/upload/s--9QlfPnJO--/c_fill,g_face,h_300,w_300/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.avatar.xlarge.url | str | https://media.cakeresume.com/image/upload/s--1eTMbnTr--/c_fill,g_face,h_600,w_600/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.avatar_tiny_url | str | https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.avatar_small_url | str | https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.avatar_medium_url | str | https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.has_phone | bool | True |
| data.item.user.has_email | bool | True |
| data.item.user.main_public_item_path | str | mortis-huang |
| data.item.user.main_signed_url_non_hidden_item_path | NoneType | None |
| data.item.user.posts_count | int | 0 |
| data.item.user.published_posts_count | int | 0 |
| data.item.user.profile_privacy_level | str | public |
| data.item.user.online_status | str | offline |
| data.item.user.recommendee_token | str | 56Vxmbj3Wn3YaZMkl0L2GP |
| data.item.user.public_recommendations_count | int | 0 |
| data.item.user.mutual_connections_count | bool | False |
| data.item.user.unique_impressions_count | int | 2380 |
| data.item.user.is_premium | bool | False |
| data.item.user.no_branding | bool | False |
| data.item.user.seems_spam | bool | False |
| data.item.user.desired_job_type | str | full_time |
| data.item.user.job_search_progress | str | ready_to_interview |
| data.item.user.current_employment_status | str | employed |
| data.item.user.is_freelancer | str | part_time_freelancer |
| data.item.user.work_experience | str | four_six |
| data.item.user.relevant_work_experience | str | four_six |
| data.item.user.desired_position | str | AI工程師、機器學習工程師、深度學習工程師、資料科學家、Machine Learning Engineer、Deep Learning Engineer、Data Scientist |
| data.item.user.role | str | Ph.D. |
| data.item.user.languages[] | str | English,3 |
| data.item.user.languages[] | str | Chinese,4 |
| data.item.user.remote | str | interested |
| data.item.user.country | str | TW |
| data.item.user.city | NoneType | None |
| data.item.user.city_name | NoneType | None |
| data.item.user.city_name_en | NoneType | None |
| data.item.user.google_place_id | str | ChIJoSFawR-waDQR-6m5DFTfH-8 |
| data.item.user.google_place_name | str | Taiwan, 台灣 |
| data.item.user.google_place_name_en | str | Taiwan, 台灣 |
| data.item.user.google_place_country_name_en | str | Taiwan |
| data.item.user.google_place_region_name_en | str | Taiwan Province |
| data.item.user.desired_location_google_place_ids[] | str | ChIJL1cHXAbzbjQRaVScvwTwEec |
| data.item.user.desired_location_google_place_ids[] | str | ChIJLxl_1w9OZzQRRFJmfNR1QvU |
| data.item.user.desired_location_google_place_ids[] | str | ChIJdZOLiiMR2jERxPWrUs9peIg |
| data.item.user.desired_location_names[] | str | Taiwan |
| data.item.user.desired_location_names[] | str | Japan |
| data.item.user.desired_location_names[] | str | Singapore |
| data.item.user.desired_location_names_en[] | str | Taiwan |
| data.item.user.desired_location_names_en[] | str | Japan |
| data.item.user.desired_location_names_en[] | str | Singapore |
| data.item.user.desired_location_country_names_en[] | str | Taiwan |
| data.item.user.desired_location_country_names_en[] | str | Japan |
| data.item.user.desired_location_country_names_en[] | str | Singapore |
| data.item.user.desired_location_region_names_en[] | NoneType | None |
| data.item.user.cr_location.id | str | ChIJoSFawR-waDQR-6m5DFTfH-8 |
| data.item.user.cr_location.full_name | str | Taiwan, 台灣 |
| data.item.user.cr_location.country | str | Taiwan |
| data.item.user.cr_location.admin_level_1 | str | Taiwan Province |
| data.item.user.cr_location.locale | str | zh-TW |
| data.item.user.cr_desired_locations[].id | str | ChIJL1cHXAbzbjQRaVScvwTwEec |
| data.item.user.cr_desired_locations[].full_name | str | Taiwan |
| data.item.user.cr_desired_locations[].country | str | Taiwan |
| data.item.user.cr_desired_locations[].admin_level_1 | NoneType | None |
| data.item.user.cr_desired_locations[].locale | str | en |
| data.item.user.cr_desired_locations[].id | str | ChIJLxl_1w9OZzQRRFJmfNR1QvU |
| data.item.user.cr_desired_locations[].full_name | str | Japan |
| data.item.user.cr_desired_locations[].country | str | Japan |
| data.item.user.cr_desired_locations[].admin_level_1 | NoneType | None |
| data.item.user.cr_desired_locations[].locale | str | en |
| data.item.user.cr_desired_locations[].id | str | ChIJdZOLiiMR2jERxPWrUs9peIg |
| data.item.user.cr_desired_locations[].full_name | str | Singapore |
| data.item.user.cr_desired_locations[].country | str | Singapore |
| data.item.user.cr_desired_locations[].admin_level_1 | NoneType | None |
| data.item.user.cr_desired_locations[].locale | str | en |
| data.item.user.eligible_work_locations[] | any |  |
| data.item.user.graduated_from_school | str | National Chiao-Tung University |
| data.item.user.graduated_from_field | str | Ph.D. - Clinical Engineering |
| data.item.user.skill_list[] | str | Python |
| data.item.user.skill_list[] | str | GPU |
| data.item.user.skill_list[] | str | Machine Learning |
| data.item.user.skill_list[] | str | AI |
| data.item.user.skill_list[] | str | Linux OS |
| data.item.user.skill_list[] | str | Automation |
| data.item.user.skill_list[] | str | GPU Programming HPC |
| data.item.user.professions[] | str | it_machine-learning-engineer |
| data.item.user.professions[] | str | it_python-developer |
| data.item.user.professions[] | str | it_semiconductor-engineering |
| data.item.user.industries[] | str | tech_semiconductor |
| data.item.user.industries[] | str | tech_artificial-intelligence-machine-learning |
| data.item.user.headline | str | Ph.D. |
| data.item.user.number_of_management | str | one_five |
| data.item.user.education_level | str | doctoral |
| data.item.user.last_seen_at_days_ago_level | int | 30 |
| data.item.user.network_profile.id | str | zbXd |
| data.item.user.network_profile.avatar.url | str | https://media.cakeresume.com/image/upload/v1704774606/eamlf29dbenp1ll63knm.jpg |
| data.item.user.network_profile.avatar.tiny.url | str | https://media.cakeresume.com/image/upload/s--z9cNBI1Q--/c_fill,g_face,h_24,w_24/v1704774606/eamlf29dbenp1ll63knm.jpg |
| data.item.user.network_profile.avatar.small.url | str | https://media.cakeresume.com/image/upload/s--wg4dVaga--/c_fill,g_face,h_60,w_60/v1704774606/eamlf29dbenp1ll63knm.jpg |
| data.item.user.network_profile.avatar.medium.url | str | https://media.cakeresume.com/image/upload/s--1AVroZGi--/c_fill,g_face,h_120,w_120/v1704774606/eamlf29dbenp1ll63knm.jpg |
| data.item.user.network_profile.avatar.large.url | str | https://media.cakeresume.com/image/upload/s--KsOWQeOQ--/c_fill,g_face,h_300,w_300/v1704774606/eamlf29dbenp1ll63knm.jpg |
| data.item.user.network_profile.avatar.xlarge.url | str | https://media.cakeresume.com/image/upload/s--echNo8F4--/c_fill,g_face,h_600,w_600/v1704774606/eamlf29dbenp1ll63knm.jpg |
| data.item.user.network_profile.status | str | published |
| data.item.user.network_profile.description | str | 交大Ph.D.
台積電OPC
Machine Learning Solutions |
| data.item.user.network_profile.identity_types[] | str | mentor |
| data.item.user.network_profile.identity_types[] | str | job_seeker |
| data.item.user.network_profile.identity_types[] | str | professional |
| data.item.user.network_profile.topics_to_learn[] | str | job_openings |
| data.item.user.network_profile.topics_to_learn[] | str | company_insights |
| data.item.user.network_profile.topics_to_learn[] | str | skills_development |
| data.item.user.network_profile.topics_to_share[] | str | company_insights |
| data.item.user.network_profile.topics_to_share[] | str | skills_development |
| data.item.user.network_profile.tags[] | any |  |
| data.item.user.network_profile.badges[] | any |  |
| data.item.user.network_profile.suspended | bool | False |
| data.item.user.network_profile.user.name | str | Chun-Jung Huang |
| data.item.user.network_profile.user.username | str | mortis-huang |
| data.item.user.network_profile.user.first_name | str | Chun-Jung |
| data.item.user.network_profile.user.last_name | str | Huang |
| data.item.user.network_profile.user.description | str | To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success. |
| data.item.user.network_profile.user.cover_image.url | str | https://media.cakeresume.com/image/upload/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.network_profile.user.cover_image.small.url | str | https://media.cakeresume.com/image/upload/c_crop,h_360,w_720/c_scale,h_180,w_360/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.network_profile.user.cover_image.medium.url | str | https://media.cakeresume.com/image/upload/s--Vm8J95tp--/c_fill,h_360,w_720/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.network_profile.user.cover_image.large.url | str | https://media.cakeresume.com/image/upload/s--VrSkpH3n--/c_fill,h_500,w_1500/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.network_profile.user.cover_image.small_3_1.url | str | https://media.cakeresume.com/image/upload/s--YGPutB6G--/c_fill,f_auto,h_140,w_420/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.network_profile.user.cover_image.medium_3_1.url | str | https://media.cakeresume.com/image/upload/s--6GTJ9tLF--/c_fill,f_auto,h_314,w_942/v1654083207/q7uem8cxaqsnuwkorvbb.jpg |
| data.item.user.network_profile.user.avatar.url | str | https://media.cakeresume.com/image/upload/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.avatar.tiny.url | str | https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.avatar.small.url | str | https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.avatar.medium.url | str | https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.avatar.large.url | str | https://media.cakeresume.com/image/upload/s--9QlfPnJO--/c_fill,g_face,h_300,w_300/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.avatar.xlarge.url | str | https://media.cakeresume.com/image/upload/s--1eTMbnTr--/c_fill,g_face,h_600,w_600/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.avatar_tiny_url | str | https://media.cakeresume.com/image/upload/s--5YBkBzNp--/c_fill,g_face,h_24,w_24/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.avatar_small_url | str | https://media.cakeresume.com/image/upload/s--7DtsReE9--/c_fill,g_face,h_60,w_60/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.avatar_medium_url | str | https://media.cakeresume.com/image/upload/s--9-MDuNn1--/c_fill,g_face,h_120,w_120/v1654083169/yxyx0gn8is09jhiq7kzx.jpg |
| data.item.user.network_profile.user.profile_privacy_level | str | public |
| data.item.user.network_profile.user.online_status | str | offline |
| data.item.user.network_profile.user.current_job_title | str | OPC Chief Engineer |
| data.item.user.network_profile.user.current_company | str | TSMC |
| data.item.user.network_profile.user.headline | str | Ph.D. |
| data.item.user.network_profile.user.is_premium | bool | False |
| data.item.user.network_profile.user.status | str | created |
| data.item.user.network_profile.review_application.precedence | int | -12551 |
| data.item.user.network_profile.review_application.status | str | approved |
| data.item.user.network_profile.review_application.reject_reason | NoneType | None |
| data.item.user.network_profile.review_application.reject_details | NoneType | None |
| data.item.user.most_recent_work_experience.title | str | OPC Chief Engineer |
| data.item.user.most_recent_work_experience.currently_work_here | bool | True |
| data.item.user.most_recent_work_experience.from_year | int | 2020 |
| data.item.user.most_recent_work_experience.from_month | int | 3 |
| data.item.user.most_recent_work_experience.end_year | NoneType | None |
| data.item.user.most_recent_work_experience.end_month | NoneType | None |
| data.item.user.most_recent_work_experience.organization.name | str | TSMC |
| data.item.user.most_recent_work_experience.organization.id | int | 464650 |
| data.item.user.most_recent_work_experience.organization.logo.url | str | https://media.cakeresume.com/image/upload/v1604585338/pbqvfhcwccdzrdu0tved.png |
| data.item.user.most_recent_work_experience.organization.logo.tiny.url | str | https://media.cakeresume.com/image/upload/s--PSVTyqPa--/c_pad,fl_png8,h_60,w_60/v1604585338/pbqvfhcwccdzrdu0tved.png |
| data.item.user.most_recent_work_experience.organization.logo.thumb.url | str | https://media.cakeresume.com/image/upload/s--o7W3GKLx--/c_pad,fl_png8,h_100,w_100/v1604585338/pbqvfhcwccdzrdu0tved.png |
| data.item.user.most_recent_work_experience.organization.logo.medium.url | str | https://media.cakeresume.com/image/upload/s--nGEg_GN8--/c_pad,fl_png8,h_200,w_200/v1604585338/pbqvfhcwccdzrdu0tved.png |
| data.item.user.most_recent_work_experience.organization.logo.large.url | NoneType | None |
| data.item.user.most_recent_work_experience.organization.logo.og_image.url | NoneType | None |
| data.item.user.most_recent_education.degree_type | str | doctor_of_philosophy_phd |
| data.item.user.most_recent_education.majors[] | str | Ph.D. - Clinical Engineering |
| data.item.user.most_recent_education.from_year | int | 2015 |
| data.item.user.most_recent_education.end_year | int | 2020 |
| data.item.user.most_recent_education.organization.name | str | National Chiao-Tung University |
| data.item.user.most_recent_education.organization.id | int | 464666 |
| data.item.user.most_recent_education.organization.logo.url | str | https://media.cakeresume.com/image/upload/v1604586192/jjunzkeazgfytbttav1t.png |
| data.item.user.most_recent_education.organization.logo.tiny.url | str | https://media.cakeresume.com/image/upload/s--7rkjq4Gg--/c_pad,fl_png8,h_60,w_60/v1604586192/jjunzkeazgfytbttav1t.png |
| data.item.user.most_recent_education.organization.logo.thumb.url | str | https://media.cakeresume.com/image/upload/s--1qBAGmIY--/c_pad,fl_png8,h_100,w_100/v1604586192/jjunzkeazgfytbttav1t.png |
| data.item.user.most_recent_education.organization.logo.medium.url | str | https://media.cakeresume.com/image/upload/s--7OjsoMvQ--/c_pad,fl_png8,h_200,w_200/v1604586192/jjunzkeazgfytbttav1t.png |
| data.item.user.most_recent_education.organization.logo.large.url | NoneType | None |
| data.item.user.most_recent_education.organization.logo.og_image.url | NoneType | None |
| data.item.use_signed_url | bool | False |
| data.item.no_branding | bool | False |
| data.item.privacy_level | int | 0 |
| data.item.signed_or_not_item_url | str | https://www.cake.me/mortis-huang |
| data.item.metadata.images[].src | str | https://images.cakeresume.com/XgMVZ/mortis-huang/191caa57-6fe0-4fd6-9b12-a9ce4ebafc0f.png |
| data.item.metadata.images[].width | int | 564 |
| data.item.metadata.images[].height | int | 318 |
| data.item.ga_tracking_code | NoneType | None |
| data.item.has_permission_ga | bool | False |
| data.item.draft_update_count | int | 429 |
| data.meta_tags.title | str | Chun-Jung Huang |
| data.meta_tags.description | str | To find the most efficient working methods in fast-paced development environments, with a focus on achieving stable and rapid automation in programming while maximizing hardware utilization. Capable of quickly analyzing and overcoming challenges at work, I aspire to be an accelerator within the team, driving overall project success. |
| data.meta_tags.canonical | str | https://www.cake.me/mortis-huang |
| data.meta_tags.og.type | str | profile |
| data.meta_tags.og.image | str | https://media.cakeresume.com/image/url2png/s--cuUyBM8A--/c_crop,g_north,h_751,w_992/c_fit,g_north,h_606,w_800/b_rgb:F0F2F1,c_lpad,g_south,h_630,w_1200/l_fetch:aHR0cHM6Ly93d3cuY2FrZXJlc3VtZS5jb20vZmF2aWNvbnMvbXN0aWxlLTMxMHgzMTAucG5n/c_scale,w_103/fl_layer_apply,g_north_west,x_0,y_0/fl_png8/https://www.cake.me/mortis-huang%3Fno-page-layout%3Dtrue%26v%3D1/url2png/viewport%3D1480x1800%7Cfullpage%3Dfalse%7Cunique%3D958442 |
| data.meta_tags.nofollow | bool | True |
| data.meta_tags.noindex | bool | False |
| data.meta_tags.amphtml | str | https://www.cake.me/mortis-huang.amp |
| data.custom4[] | any |  |
| data.custom4.custom.sort | int | 4 |
| data.custom4.custom.name | str | 長庚大學管樂團 |
| data.custom4.custom.content[].duration.startYear | str | 2015 |
| data.custom4.custom.content[].duration.startMonth.text | str | 9 |
| data.custom4.custom.content[].duration.startMonth.value | int | 9 |
| data.custom4.custom.content[].duration.endYear | str | 2019 |
| data.custom4.custom.content[].duration.endMonth.text | str | 6 |
| data.custom4.custom.content[].duration.endMonth.value | int | 6 |
| data.custom4.custom.content[].isInProgress | bool | False |
| data.custom4.custom.content[].introduction | str | 【創造樂團輝煌時代】
2016/6-2017/6
接管幹部時，經歷團上意見紛歧、大家對於比賽想法不同等問題，與團隊一起努力透過溝通，把樂團創經營的更好更有向心力，經費與團員更加充足，且於全國比賽獲得佳績。

●擔任社團幹部:負責藏譜管理、參與會議討論
●管樂週以及校慶擺攤活動總召:利用中午時間與一般學生宣傳管樂團的特色、安排午餐音樂會、協助甜點販賣，一週為社團賺進2萬元的資金、校慶擺攤一個下午有4千元的業績
● 參與4年度的全國學生音樂團體比賽:獲得三年學生音樂比賽優等，一年全國賽特優的佳績。 |
| data.custom4.custom.content[].url | str |  |
| data.custom4.themeChoose.selectedTheme.text | str | 經典風格 |
| data.custom4.themeChoose.selectedTheme.value | int | 1 |
| data.custom4.themeChoose.selectedTheme.name | str | CustomThemeClassic |
| data.custom4.img.pic | int | 1 |
| data.custom4.img.fileId | str | custom_content_img4 |
| data.custom4.img.src | str | https://pda.104.com.tw/profiles/1ZSUUFKUw0r/files/custom_content_img4?v=1675868603 |
| data.custom4.img2.pic | int | 0 |
| data.custom4.img2.fileId | str |  |
| data.custom4.img2.src | str |  |
| data.education.educations[].duration.startMonth.value | int | 9 |
| data.education.educations[].duration.startMonth.value | int | 9 |
| data.education.educations[].duration.startMonth.value | int | 3 |
| data.education.educations[].duration.startMonth.value | int | 9 |
| data.education.educations[].duration.startMonth.text | str | 9 |
| data.education.educations[].duration.startMonth.text | str | 9 |
| data.education.educations[].duration.startMonth.text | str | 3 |
| data.education.educations[].duration.startMonth.text | str | 9 |
| data.education.educations[].duration.startYear | str | 2017 |
| data.education.educations[].duration.startYear | str | 2013 |
| data.education.educations[].duration.startYear | str | 2021 |
| data.education.educations[].duration.startYear | str | 2015 |
| data.education.educations[].duration.endMonth.value | int | 1 |
| data.education.educations[].duration.endMonth.value | int | 6 |
| data.education.educations[].duration.endMonth.value | int | 2 |
| data.education.educations[].duration.endMonth.value | int | 6 |
| data.education.educations[].duration.endMonth.text | str | 1 |
| data.education.educations[].duration.endMonth.text | str | 6 |
| data.education.educations[].duration.endMonth.text | str | 2 |
| data.education.educations[].duration.endMonth.text | str | 6 |
| data.education.educations[].duration.endYear | str | 2022 |
| data.education.educations[].duration.endYear | str | 2017 |
| data.education.educations[].duration.endYear | str | 2023 |
| data.education.educations[].duration.endYear | str | 2019 |
| data.education.educations[].highest.value | int | 2 |
| data.education.educations[].highest.value | int | 3 |
| data.education.educations[].highest.value | int | 2 |
| data.education.educations[].highest.value | int | 3 |
| data.education.educations[].highest.text | str | 碩士 |
| data.education.educations[].highest.text | str | 大學 |
| data.education.educations[].highest.text | str | 碩士 |
| data.education.educations[].highest.text | str | 大學 |
| data.education.educations[].inSchoolStatus[] | any |  |
| data.education.educations[].inSchoolStatus[] | any |  |
| data.education.educations[].inSchoolStatus[] | any |  |
| data.education.educations[].inSchoolStatus[] | any |  |
| data.education.educations[].schoolId | int | 5023000000 |
| data.education.educations[].schoolId | int | 5030000000 |
| data.education.educations[].schoolId | int | 5180000000 |
| data.education.educations[].schoolId | int | 5065000000 |
| data.education.educations[].foreign[] | any |  |
| data.education.educations[].foreign[] | any |  |
| data.education.educations[].foreign[] | any |  |
| data.education.educations[].foreign[] | any |  |
| data.education.educations[].sort | int | 1 |
| data.education.educations[].sort | int | 2 |
| data.education.educations[].sort | int | 1 |
| data.education.educations[].sort | int | 2 |
| data.education.educations[].name | str | 國立臺北科技大學 |
| data.education.educations[].name | str | 國立聯合大學 |
| data.education.educations[].name | str | 國立陽明交通大學 |
| data.education.educations[].name | str | 長庚大學 |
| data.education.educations[].departments[].name | str | 光電工程系 |
| data.education.educations[].departments[].name | str | 光電工程學系 |
| data.education.educations[].departments[].name | str | 生物醫學資訊研究所 |
| data.education.educations[].departments[].name | str | 護理學系 |
| data.education.educations[].departments[].type[].no | int | 3011016000 |
| data.education.educations[].departments[].type[].no | int | 3011016000 |
| data.education.educations[].departments[].type[].no | int | 3009009000 |
| data.education.educations[].departments[].type[].no | int | 3009005000 |
| data.education.educations[].departments[].type[].des | str | 光電工程相關 |
| data.education.educations[].departments[].type[].des | str | 光電工程相關 |
| data.education.educations[].departments[].type[].des | str | 醫藥工程相關 |
| data.education.educations[].departments[].type[].des | str | 護理助產相關 |
| data.education.educations[].status.value | int | 1 |
| data.education.educations[].status.value | int | 1 |
| data.education.educations[].status.value | int | 1 |
| data.education.educations[].status.value | int | 1 |
| data.education.educations[].status.text | str | 畢業 |
| data.education.educations[].status.text | str | 畢業 |
| data.education.educations[].status.text | str | 畢業 |
| data.education.educations[].status.text | str | 畢業 |
| data.education.educations[].region.value | int | 7001053000 |
| data.education.educations[].region.value | int | 7001053000 |
| data.education.educations[].region.value | int | 7001053000 |
| data.education.educations[].region.value | int | 7001053000 |
| data.education.educations[].region.text | str | 台灣 |
| data.education.educations[].region.text | str | 台灣 |
| data.education.educations[].region.text | str | 台灣 |
| data.education.educations[].region.text | str | 台灣 |
| data.publicStatus | int | 1 |
| data.publicStatus | int | 1 |
| data.project.projects[].sort | int | 1 |
| data.project.projects[].name | str | Let's Dance - 舞蹈評分系統 |
| data.project.projects[].duration.startYear | str | 2022 |
| data.project.projects[].duration.startMonth.text | str | 11 |
| data.project.projects[].duration.startMonth.value | int | 11 |
| data.project.projects[].duration.endYear | str | 2023 |
| data.project.projects[].duration.endMonth.text | str | 1 |
| data.project.projects[].duration.endMonth.value | int | 1 |
| data.project.projects[].isInProgress | bool | False |
| data.project.projects[].introduction | str | 疫情下，為了滿足消費者對於室內運動和娛樂的需求，團隊推出了「Let's Dance : 舞蹈評分系統」的桌面應用
- 專案擔任角色 : GUI呈現
  ● 系統整合 : 將遊戲中四大功能整合成桌面應用
  ● threading : 平行化技術實現遊戲多工特性
  ● PyQt5 :  Qt結合上面兩項任務，創建桌面GUI ， 供使用者更直觀的體驗

- 遊戲其他功能
  ● 臉部辨識系統 : 以face_recognition人臉辨識模型為基礎製作人臉辨識系統，並與資料庫串接
  ● 舞蹈評分系統 : Mediapipe 體態辨識模型實現使用者 - 教練 姿勢即時比對系統
  ● AI 體感操作模型 : Mediapipe+DNN網路 實現使用者以體感操作GUI介面的功能
  ● 資料庫 : 使用於GCP上建立MySQL資料庫，以記錄玩家個人資訊、歷史分數等相關資料，以GUI顯示分數排名 |
| data.project.projects[].url | str | https://drive.google.com/file/d/1XdSRXETPWzP6Vd9y1L78KHUpwhe4tnCl/view?usp=sharing |
| data.project.projects[].img.pic | str | 1 |
| data.project.projects[].img.fileId | str | achievement_img1.jpeg |
| data.project.projects[].img.src | str | https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img1.jpeg?v=1707981972 |
| data.project.projects[].sort | int | 2 |
| data.project.projects[].name | str | LoLi Nahida |
| data.project.projects[].duration.startYear | str | 2023 |
| data.project.projects[].duration.startMonth.text | str | 1 |
| data.project.projects[].duration.startMonth.value | int | 1 |
| data.project.projects[].duration.endYear | str | 2023 |
| data.project.projects[].duration.endMonth.text | str | 2 |
| data.project.projects[].duration.endMonth.value | int | 2 |
| data.project.projects[].isInProgress | bool | False |
| data.project.projects[].introduction | str | ChatGPT的流行，已為使用者帶來不少的方便性。
如果將類似的功能部署至每日必用的LINE上，是否就像你的貼身小助手了呢?
- 小作品功能 :
● 撰寫LINEBOT API，並串接OpenAI的Text CompletionAPI，達成接收客戶請求，並以同個話題與客戶回應，進行流利對答。
● 將LINEBOT功能已兩種方式部署至GCP :
   ▲ 方法一 VM : 於GCP開啟VM啟用24hr服務，結合Nginx + DNS(from GoDaddy) + Let's Encrypt  產生 憑證(https)的API ， 以供客戶(LINE伺服器端)進行請求。
   ▲ 方法二 容器化 : 將LINEBOT功能容器化，並部署至GCP CloudRun，即可擁有 DNS + 憑證(https)的 ， 但回應速度較慢 (客戶傳訊息才啟用服務) |
| data.project.projects[].url | str | https://line.me/R/ti/p/%40965qbkve |
| data.project.projects[].img.pic | str | 1 |
| data.project.projects[].img.fileId | str | achievement_img2.jpeg |
| data.project.projects[].img.src | str | https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img2.jpeg?v=1707981972 |
| data.project.projects[].sort | int | 3 |
| data.project.projects[].name | str | Crawler Training |
| data.project.projects[].duration.startYear | str | 2023 |
| data.project.projects[].duration.startMonth.text | str | 2 |
| data.project.projects[].duration.startMonth.value | int | 2 |
| data.project.projects[].duration.endYear | str |  |
| data.project.projects[].duration.endMonth[] | any |  |
| data.project.projects[].isInProgress | bool | True |
| data.project.projects[].introduction | str | 使用Selenium撰寫爬蟲軟體，以整理出使用者需求的職缺。
- 欲使用技術 : 
  ● Selenium : 模擬為人操作，訪問網頁並得到資料
  ● Pandas : 進行資料清洗，並儲存為csv檔案
  ● MultiProcessing & Threading (計畫中) : 平行化技術分配各個人力抓取不同職缺資訊 |
| data.project.projects[].url | str | https://github.com/joshsmiththenoob/CrawlerTraining |
| data.project.projects[].img.pic | str | 1 |
| data.project.projects[].img.fileId | str | achievement_img3.jpeg |
| data.project.projects[].img.src | str | https://pda.104.com.tw/profiles/3Cs09h2VRhp/files/achievement_img3.jpeg?v=1707981972 |
| data.project[] | any |  |
| data.portfolio.portfolios[].sort | int | 1 |
| data.portfolio.portfolios[].sort | int | 2 |
| data.portfolio.portfolios[].sort | int | 3 |
| data.portfolio.portfolios[].sort | int | 4 |
| data.portfolio.portfolios[].sort | int | 5 |
| data.portfolio.portfolios[].sort | int | 6 |
| data.portfolio.portfolios[].sort | int | 1 |
| data.portfolio.portfolios[].sort | int | 2 |
| data.portfolio.portfolios[].sort | int | 3 |
| data.portfolio.portfolios[].name | str | 軟體培訓簡歷表 |
| data.portfolio.portfolios[].name | str | 北科碩士成績 |
| data.portfolio.portfolios[].name | str | TOEIC |
| data.portfolio.portfolios[].name | str | 簡歷表 |
| data.portfolio.portfolios[].name | str | 聯合大學成績單 |
| data.portfolio.portfolios[].name | str | Python-Nvidia Deep Learning Institute-深度學習基礎理論與實踐修課證明 |
| data.portfolio.portfolios[].name | str | Toeic成績單 |
| data.portfolio.portfolios[].name | str | 跨領域數位人才加速計畫成果發表第二名獎狀 |
| data.portfolio.portfolios[].name | str | 實習結業證書 |
| data.portfolio.portfolios[].attach.fileId | str |  |
| data.portfolio.portfolios[].attach.fileId | str | upload1.pdf |
| data.portfolio.portfolios[].attach.fileId | str | upload2.pdf |
| data.portfolio.portfolios[].attach.fileId | str | upload3.pdf |
| data.portfolio.portfolios[].attach.fileId | str | upload4.pdf |
| data.portfolio.portfolios[].attach.fileId | str | upload5.pdf |
| data.portfolio.portfolios[].attach.fileId | str | upload1 |
| data.portfolio.portfolios[].attach.fileId | str | upload2 |
| data.portfolio.portfolios[].attach.fileId | str | upload3 |
| data.portfolio.portfolios[].attach.url | str | https://drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link |
| data.portfolio.portfolios[].attach.url | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload1.pdf |
| data.portfolio.portfolios[].attach.url | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload2.pdf |
| data.portfolio.portfolios[].attach.url | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload3.pdf |
| data.portfolio.portfolios[].attach.url | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload4.pdf |
| data.portfolio.portfolios[].attach.url | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/upload5.pdf |
| data.portfolio.portfolios[].attach.url | str | https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload1 |
| data.portfolio.portfolios[].attach.url | str | https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload2 |
| data.portfolio.portfolios[].attach.url | str | https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/upload3 |
| data.portfolio.portfolios[].attach.name | str | drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link |
| data.portfolio.portfolios[].attach.name | str | 北科碩成績單.pdf |
| data.portfolio.portfolios[].attach.name | str | TOIEC1101015.pdf |
| data.portfolio.portfolios[].attach.name | str | 傅騰緯_簡歷表.pdf |
| data.portfolio.portfolios[].attach.name | str | 0826_傅騰緯_聯合大學102學年度學士班成績單.pdf |
| data.portfolio.portfolios[].attach.name | str | DLI C-FX-01 修课证明 _ Deep Learning Institute.pdf |
| data.portfolio.portfolios[].attach.name | str | toeic.png |
| data.portfolio.portfolios[].attach.name | str | Adobe Scan Jan 28, 2023-1.pdf |
| data.portfolio.portfolios[].attach.name | str | 數轉部實習證書.pdf |
| data.portfolio.portfolios[].attach.status | int | 0 |
| data.portfolio.portfolios[].attach.status | int | 2 |
| data.portfolio.portfolios[].attach.status | int | 2 |
| data.portfolio.portfolios[].attach.status | int | 2 |
| data.portfolio.portfolios[].attach.status | int | 2 |
| data.portfolio.portfolios[].attach.status | int | 2 |
| data.portfolio.portfolios[].attach.status | int | 2 |
| data.portfolio.portfolios[].attach.status | int | 2 |
| data.portfolio.portfolios[].attach.status | int | 2 |
| data.portfolio.portfolios[].attach.src | str | https://drive.google.com/file/d/1RDKE2_YCS6eGFAV0SjzvQujtFJjTUUgX/view?usp=share_link |
| data.portfolio.portfolios[].attach.src | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail1?v=1707981983 |
| data.portfolio.portfolios[].attach.src | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail2?v=1707981983 |
| data.portfolio.portfolios[].attach.src | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail3?v=1707981983 |
| data.portfolio.portfolios[].attach.src | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail4?v=1707981983 |
| data.portfolio.portfolios[].attach.src | str | https://pda.104.com.tw/api/resumes/api/profiles/3Cs09h2VRhp/files/thumbnail5?v=1707981983 |
| data.portfolio.portfolios[].attach.src | str | https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail1?v=1674831901 |
| data.portfolio.portfolios[].attach.src | str | https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail2?v=1674925537 |
| data.portfolio.portfolios[].attach.src | str | https://pda.104.com.tw/api/resumes/api/profiles/1ZSUUFKUw0r/files/thumbnail3?v=1675062025 |
| data.portfolio.portfolios[].attachType.value | int | 2 |
| data.portfolio.portfolios[].attachType.value | int | 1 |
| data.portfolio.portfolios[].attachType.value | int | 1 |
| data.portfolio.portfolios[].attachType.value | int | 1 |
| data.portfolio.portfolios[].attachType.value | int | 1 |
| data.portfolio.portfolios[].attachType.value | int | 1 |
| data.portfolio.portfolios[].attachType.value | int | 1 |
| data.portfolio.portfolios[].attachType.value | int | 1 |
| data.portfolio.portfolios[].attachType.value | int | 1 |
| data.portfolio.portfolios[].attachType.text | str | 連結 |
| data.portfolio.portfolios[].attachType.text | str | 檔案 |
| data.portfolio.portfolios[].attachType.text | str | 檔案 |
| data.portfolio.portfolios[].attachType.text | str | 檔案 |
| data.portfolio.portfolios[].attachType.text | str | 檔案 |
| data.portfolio.portfolios[].attachType.text | str | 檔案 |
| data.portfolio.portfolios[].attachType.text | str | 檔案 |
| data.portfolio.portfolios[].attachType.text | str | 檔案 |
| data.portfolio.portfolios[].attachType.text | str | 檔案 |
| data.bio.chi | str | ● 關於我 :

您好! 我是傅騰緯，北科大光電所主修繞射光學、光資訊處理，研究所期間培養了傅立葉分析以及撰寫程式的能力，目前於商研院進修AI養成實戰班課程。
在團隊中，我會主動提出想法與組員討論，且和組員討論過程中幫助我以不同的視野、邏輯看待同一件事情，這種教學相長的環境使我受益良多。為了團隊專案的完整性，我主動學習之前沒有碰過的新技能 ─ Qt、Threading，並應用在專案上。
健身、打籃球、彈吉他的習慣讓我適時的放鬆並重整思路，也隨時保持體力面對挑戰。

● 軟體業進修動機 :

求學期間主修光電工程，研究方向以繞射分析、光學模擬為主，研究所畢業後，發覺特定產業不只需要光學知識，也需擁有Python、影像處理、影像辨識的能力，所以，在尋職的同時，我也找了網路資源學習Python，並開始對程式語言產生興趣，繼而萌生轉換跑道的念頭。在網路上找到了商研院開立的AI實戰養成班，再三思考下，決定全心全力投入四個月AI班課程，提升職場競爭力!

● 進修作品 :

在商研院開立的AI實戰養成班中，不僅學習到了基礎語法、資料探勘、AI模型訓練與部署及資料視覺化等知識外，也提供了專題實作的機會，讓我們可以將課堂上的知識應用在實務上。

所屬團隊負責的專題為「Let's Dance : 舞蹈辨識評分系統」，目的是為了在嚴峻的疫情下，可以滿足消費者室內運動和娛樂的需求，專案技術分為五大項  : 臉部辨識、體感操作AI模型、舞蹈評分系統、資料庫以及GUI設計。

在團隊中，我主要目負責的項目為 GUI設計，任務是將前四大項功能整合成Windows桌面應用，並利用threading平行化技術，達成遊戲多工的效果，最終以圖形介面的方式呈現給使用者。由於時間、人力的關係，目前專案成果為Windows桌面應用，本專案的最終目標是將該應用引入至嵌入式系統(Jetson Nano)，並以體感操作、成本低的特點成為具競爭力的商品 !

● 碩論 - 三種應用於二次光學系統的數值分析方法之實現與比較：

主要利用Matlab架設二次光學系統的模擬環境，並找出在不同環境下均有效、快速的光學模擬方案。

● 經歷的困難及如何解決：

Challenge : 
一個月內快速學習新技術 ─ Qt、threading，如何在專案結束前快速將系統整合，完成該項專案作品?
How To Solve: 
查找Qt、threading相關文檔，並參考Stack OverfLow解決相對應問題；重要的是，由於系統整合需要理解大家的功能及原理，所以與團隊溝通很重要。也感謝團隊成員們熱心討論、交流，才讓我得以快速整合！。

Challenge : 
如何在一定的記憶體使用量內有效地模擬顯微鏡光學成像?
How To Solve : 
在光學本質上，使用不同種的繞射模擬方法，即可使用最少的記憶體模擬顯微鏡的光學成像，達成演算法優化的效果。


● 未來期許：
將培訓的技能應用在實務上，包括將功能包在Docker並部署至AWS上， 為公司提供商業價值；短期內加強自身軟體知識以及語文能力，期望自己的軟體、訊號處理能力為貴公司創造最大的價值!

 |
| data.bio.chi | str | 「不求與人相比，但求超越自己」，這是在我在面對每一個新領域、新工作的價值觀與態度，跨領域經驗使我具備學習能力佳，願意嘗試新事物的特質。

我是陳彥伶，在林口長庚大學護理系度過大學的生涯，畢業後任職臺北榮總急診室護理師一年半，離職後進入陽明交通大學生物醫學資訊所就讀。護理背景使我有良好的觀察與溝通能力，急診室分秒必爭的環境培養出我的抗壓性，資訊統計的背景也讓我對數據有敏感度，能夠察覺不合理之處，可以發現問題，有條不紊的分析可能原因，並且透過現有數據驗證假設與結果。熟悉SAS、R、python等軟體操作，論文以健保資料庫探討慢性腎病與皮膚疾病的關係。曾主動至交大校區上課，學習網路通訊、資料科學等課程。碩班期間也參加「DIGI+Talent 跨域數位人才加速躍升計畫」於資策會實習增加產業經驗，同時完成「應用智慧音箱於睡眠呼吸音辨識及居家睡眠照護」的專案，從中利用python將睡眠時聲音轉換成數值進行機器學習並預測相關疾病。具備資料前處理、資料視覺化、統計分析的能力，並在學習的過程中發現自身對於數據分析的興趣

「台上十分鐘，台下十年功」身為管樂人有深刻的領悟，從高中開始加入管樂團，重新學習銅管樂器，參與過數次學生團體音樂比賽獲得優等、特優的佳績，練習過程中透過自我要求、自律的每日定時練習彌補樂器演奏上的不足，也樂於分享自己的學習經驗予初學者。同時也主動肩負起團上的行政庶務，安排與各校的交流活動讓團員有更豐富的經驗，加強大家的團隊意識與凝聚力，對團體好的事情，都盡心盡力完成。

經過醫院急診室生死離別的洗禮，培養出「快、狠、準」的做事方法與關懷他人、細心的工作態度，也從研究所習得數理統計、醫學研究、程式設計、電腦科學的相關知識，建立數據分析與解決問題的良好基礎。我抱著虛心求教、認真學習的態度面對每一份工作與挑戰，期待能透過我的能力與經驗協助貴公司快速掌握問題癥結，能有機會進入貴公司，與優秀團隊合作。 |
| data.bio.eng | str |  |
| data.bio.eng | str | "Don't compare yourself with others, but go beyond your own." This is my attitude when I face every new field or job. Interdisciplinary experiences have given me the good learning ability and willingness to take risks and try new things.

I am Yen-Ling,Chen. I majored in nursing at Chang Gung University. After graduation,I worked as a nurse in the emergency room of Taipei Veterans General Hospital for one and a half years. Afterward, I was admitted to the Biomedical Information Institute of National Yang Ming Chiao Tung University.
I have good observation and communication skills and I also perform well under stress from being a nurse in  the emergency room.The background of statistics also makes me sensitive to data. I have the ability to detect unreasonable numbers and analyze hypotheses or problems logically and  methodically.I am familiar with SAS, R, python and I have the ability of data pre-processing, data visualization, and statistical analysis.My dissertation also explored the relationship between chronic kidney disease and skin diseases from the health insurance database.During my master time, I also participated in the “DIGI+Talent Plan” and being an intern in the Institute for Information Industry.The project we implemented was “Applying smart speakers to recognition of sleep breathing sound and home sleep care”.We need to convert the sleeping sound to numerical values for machine learning.

“One minute on the stage needs ten years of practice off stage”. I joined the orchestra in high school and learned how to play the french horn. I have participated in several group music competitions and won excellent results.I was also a self-disciplined player who practiced every day to pursue better performance and was willing to share my learning experience with beginners.At the same time, I took the responsibility to handle the administrative affairs, such as arranging exchange activities with other schools in order to strengthen members’ cohesion and widen our perspective.

I face every job and challenge with a humble and active learning attitude. I am looking forward to helping your company quickly grasp the problem through my ability and experience.Hope to  have the opportunity to enter your company and cooperate with an excellent team. |
| data.custom5[] | any |  |
| data.custom5[] | any |  |
| data.sidebar[].id | str | profile |
| data.sidebar[].id | str | education |
| data.sidebar[].id | str | experience |
| data.sidebar[].id | str | jobCondition |
| data.sidebar[].id | str | language |
| data.sidebar[].id | str | skill |
| data.sidebar[].id | str | certificate |
| data.sidebar[].id | str | portfolio |
| data.sidebar[].id | str | bio |
| data.sidebar[].id | str | project |
| data.sidebar[].id | str | referrer |
| data.sidebar[].id | str | profile |
| data.sidebar[].id | str | education |
| data.sidebar[].id | str | skill |
| data.sidebar[].id | str | experience |
| data.sidebar[].id | str | jobCondition |
| data.sidebar[].id | str | certificate |
| data.sidebar[].id | str | language |
| data.sidebar[].id | str | custom2 |
| data.sidebar[].id | str | custom1 |
| data.sidebar[].id | str | custom3 |
| data.sidebar[].id | str | custom4 |
| data.sidebar[].id | str | bio |
| data.sidebar[].id | str | portfolio |
| data.layout.education.themeChoose.selectedTheme.name | str | EducationThemeList |
| data.layout.education.themeChoose.selectedTheme.name | str | EducationThemeList |
| data.layout.education.themeChoose.selectedTheme.value | int | 1 |
| data.layout.education.themeChoose.selectedTheme.value | int | 1 |
| data.layout.education.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.education.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.experience.themeChoose.selectedTheme.name | str | ExperienceThemeList |
| data.layout.experience.themeChoose.selectedTheme.name | str | ExperienceThemeList |
| data.layout.experience.themeChoose.selectedTheme.value | int | 1 |
| data.layout.experience.themeChoose.selectedTheme.value | int | 1 |
| data.layout.experience.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.experience.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.jobCondition.themeChoose.selectedTheme.name | str | JobConditionThemeList |
| data.layout.jobCondition.themeChoose.selectedTheme.name | str | JobConditionThemeList |
| data.layout.jobCondition.themeChoose.selectedTheme.value | int | 1 |
| data.layout.jobCondition.themeChoose.selectedTheme.value | int | 1 |
| data.layout.jobCondition.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.jobCondition.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.profile.themeChoose.selectedTheme.name | str | ProfileThemeClassic |
| data.layout.profile.themeChoose.selectedTheme.name | str | ProfileThemeClassic |
| data.layout.profile.themeChoose.selectedTheme.value | int | 1 |
| data.layout.profile.themeChoose.selectedTheme.value | int | 1 |
| data.layout.profile.themeChoose.selectedTheme.text | str | 經典風格 |
| data.layout.profile.themeChoose.selectedTheme.text | str | 經典風格 |
| data.layout.skill.themeChoose.selectedTheme.name | str | SkillThemeCard |
| data.layout.skill.themeChoose.selectedTheme.name | str | SkillThemeCard |
| data.layout.skill.themeChoose.selectedTheme.value | int | 2 |
| data.layout.skill.themeChoose.selectedTheme.value | int | 2 |
| data.layout.skill.themeChoose.selectedTheme.text | str | 卡片式 |
| data.layout.skill.themeChoose.selectedTheme.text | str | 卡片式 |
| data.layout.project.themeChoose.selectedTheme.name | str | ProjectTheme1Column |
| data.layout.project.themeChoose.selectedTheme.name | str | ProjectTheme1Column |
| data.layout.project.themeChoose.selectedTheme.value | int | 1 |
| data.layout.project.themeChoose.selectedTheme.value | int | 1 |
| data.layout.project.themeChoose.selectedTheme.text | str | 單欄式 |
| data.layout.project.themeChoose.selectedTheme.text | str | 單欄式 |
| data.layout.portfolio.themeChoose.selectedTheme.name | str | PortfolioTheme3Column |
| data.layout.portfolio.themeChoose.selectedTheme.name | str | PortfolioTheme3Column |
| data.layout.portfolio.themeChoose.selectedTheme.value | int | 1 |
| data.layout.portfolio.themeChoose.selectedTheme.value | int | 1 |
| data.layout.portfolio.themeChoose.selectedTheme.text | str | 三欄式 |
| data.layout.portfolio.themeChoose.selectedTheme.text | str | 三欄式 |
| data.layout.certificate.themeChoose.selectedTheme.name | str | CertificateThemeList |
| data.layout.certificate.themeChoose.selectedTheme.name | str | CertificateThemeList |
| data.layout.certificate.themeChoose.selectedTheme.value | int | 1 |
| data.layout.certificate.themeChoose.selectedTheme.value | int | 1 |
| data.layout.certificate.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.certificate.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.language.themeChoose.selectedTheme.name | str | LanguageThemeList |
| data.layout.language.themeChoose.selectedTheme.name | str | LanguageThemeList |
| data.layout.language.themeChoose.selectedTheme.value | int | 1 |
| data.layout.language.themeChoose.selectedTheme.value | int | 1 |
| data.layout.language.themeChoose.selectedTheme.text | str | 列表式 |
| data.layout.language.themeChoose.selectedTheme.text | str | 列表式 |
| data.certificate.certificates[].no | int | 4001001005 |
| data.certificate.certificates[].no | int | 4014003003 |
| data.certificate.certificates[].no | int | 4014003004 |
| data.certificate.certificates[].des | str | TOEIC (多益測驗) |
| data.certificate.certificates[].des | str | 高考護理師執照 |
| data.certificate.certificates[].des | str | CPR證照 |
| data.certificate.others | str |  |
| data.certificate.others | str |  |
| data.language.local[] | any |  |
| data.language.local[] | any |  |
| data.language.foreign[].writing.value | int | 8 |
| data.language.foreign[].writing.value | int | 8 |
| data.language.foreign[].writing.text | str | 中等 |
| data.language.foreign[].writing.text | str | 中等 |
| data.language.foreign[].sort | int | 1 |
| data.language.foreign[].sort | int | 1 |
| data.language.foreign[].speaking.value | int | 8 |
| data.language.foreign[].speaking.value | int | 8 |
| data.language.foreign[].speaking.text | str | 中等 |
| data.language.foreign[].speaking.text | str | 中等 |
| data.language.foreign[].listening.value | int | 8 |
| data.language.foreign[].listening.value | int | 8 |
| data.language.foreign[].listening.text | str | 中等 |
| data.language.foreign[].listening.text | str | 中等 |
| data.language.foreign[].type.value | int | 1 |
| data.language.foreign[].type.value | int | 1 |
| data.language.foreign[].type.text | str | 英文 |
| data.language.foreign[].type.text | str | 英文 |
| data.language.foreign[].certificate[].title.value | int | 4001001005 |
| data.language.foreign[].certificate[].title.value | int | 4001001005 |
| data.language.foreign[].certificate[].title.text | str | TOEIC (多益測驗) |
| data.language.foreign[].certificate[].title.text | str | TOEIC (多益測驗) |
| data.language.foreign[].certificate[].grade | str | 720 |
| data.language.foreign[].certificate[].grade | str | 925 |
| data.language.foreign[].reading.value | int | 8 |
| data.language.foreign[].reading.value | int | 8 |
| data.language.foreign[].reading.text | str | 中等 |
| data.language.foreign[].reading.text | str | 中等 |

## PM Resume Schemas

### Common Schema

This schema represents the common structure across all samples:

```json
{
  "type": "object",
  "properties": {
    "education": {
      "type": "object",
      "properties": {
        "highest": {
          "type": "object",
          "properties": {
            "degree": {
              "type": "str",
              "example": "碩士"
            },
            "school": {
              "type": "str",
              "example": "國立交通大學"
            },
            "department": {
              "type": "str",
              "example": "統計所"
            },
            "period": {
              "type": "str",
              "example": "2018/09~2020/07"
            }
          }
        },
        "degree": {
          "oneOf": [
            {
              "type": "str",
              "example": "碩士"
            },
            {
              "type": "str",
              "example": "碩士"
            }
          ]
        },
        "department": {
          "oneOf": [
            {
              "type": "str",
              "example": "統計學系"
            },
            {
              "type": "str",
              "example": "應用統計資訊"
            }
          ]
        },
        "period": {
          "oneOf": [
            {
              "type": "str",
              "example": "2020/8-2022/7"
            },
            {
              "type": "str",
              "example": "2018/8-2020/7"
            }
          ]
        },
        "school": {
          "oneOf": [
            {
              "type": "str",
              "example": "台北大學"
            },
            {
              "type": "str",
              "example": "私立東吳大學"
            }
          ]
        },
        "bachelor": {
          "type": "object",
          "properties": {
            "degree": {
              "type": "str",
              "example": "學士"
            },
            "school": {
              "type": "str",
              "example": "國立中央大學"
            },
            "department": {
              "type": "str",
              "example": "財務金融"
            },
            "period": {
              "type": "str",
              "example": "2014/09~2018/06"
            }
          }
        }
      }
    },
    "experience": {
      "type": "object",
      "properties": {
        "total_years": {
          "type": "str",
          "example": "3~4年工作經驗"
        },
        "roles": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "str",
                    "example": "資料科學家"
                  },
                  "duration": {
                    "type": "str",
                    "example": "1~2年"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "str",
                    "example": "演算法工程師"
                  },
                  "duration": {
                    "type": "str",
                    "example": "3~4年"
                  }
                }
              }
            ]
          }
        },
        "jobs": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "company": {
                    "type": "str",
                    "example": "XX電子工業股份有限公司"
                  },
                  "title": {
                    "type": "str",
                    "example": "資料科學家"
                  },
                  "period": {
                    "type": "str",
                    "example": "2023/08～(仍在職)"
                  },
                  "industry": {
                    "type": "str",
                    "example": "其他電子零組件相關業"
                  },
                  "category": {
                    "type": "str",
                    "example": "資料科學家"
                  },
                  "company_size": {
                    "type": "str",
                    "example": "500人以上"
                  },
                  "skills": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "str",
                          "example": "AI"
                        },
                        {
                          "type": "str",
                          "example": "機器學習"
                        },
                        {
                          "type": "str",
                          "example": "PyTorch"
                        },
                        {
                          "type": "str",
                          "example": "人工智慧"
                        }
                      ]
                    }
                  },
                  "description": {
                    "type": "str",
                    "example": "在XX電子擔任資料科學家"
                  },
                  "projects": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "最佳化系統"
                            },
                            "summary": {
                              "type": "str",
                              "example": "實現實時監控趨勢，根因分析與優化演算法，提升單位時間生產數量，導入9條生產線。"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "品質調優工具"
                            },
                            "summary": {
                              "type": "str",
                              "example": "根據品質結果調整設備參數，結合強化學習確保穩定與一致性。"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "產品健康度工具"
                            },
                            "summary": {
                              "type": "str",
                              "example": "使用深度學習預測結果，預測準確率達95%、recall達87%。"
                            }
                          }
                        }
                      ]
                    }
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "company": {
                    "type": "str",
                    "example": "XX電子股份有限公司"
                  },
                  "title": {
                    "type": "str",
                    "example": "資料科學家"
                  },
                  "period": {
                    "type": "str",
                    "example": "2021/08～(仍在職)"
                  },
                  "industry": {
                    "type": "str",
                    "example": "光學器材製造業"
                  },
                  "category": {
                    "type": "str",
                    "example": "演算法工程師"
                  },
                  "company_size": {
                    "type": "str",
                    "example": "500人以上"
                  },
                  "skills": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "str",
                          "example": "Python"
                        },
                        {
                          "type": "str",
                          "example": "MySQL"
                        },
                        {
                          "type": "str",
                          "example": "Machine Learning"
                        },
                        {
                          "type": "str",
                          "example": "爬蟲"
                        }
                      ]
                    }
                  },
                  "description": {
                    "type": "str",
                    "example": "XX電子擔任資料科學家，負責AI專案。"
                  },
                  "projects": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "人力減降"
                            },
                            "summary": {
                              "type": "str",
                              "example": "使用ANOVA與線性模型提升良率1.11%，降低瑕疵率9.3%。"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "廢棄分析"
                            },
                            "summary": {
                              "type": "str",
                              "example": "使用XGBoost建模報廢預測，平均廢棄率降低9.2%。"
                            }
                          }
                        }
                      ]
                    }
                  }
                }
              }
            ]
          }
        }
      }
    },
    "personal_info": {
      "type": "object",
      "properties": {
        "english_name": {
          "oneOf": [
            {
              "type": "str",
              "example": "Becky"
            },
            {
              "type": "str",
              "example": "Jason"
            }
          ]
        },
        "gender": {
          "oneOf": [
            {
              "type": "str",
              "example": "女"
            },
            {
              "type": "str",
              "example": "男"
            }
          ]
        },
        "driver_licenses": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "普通重型機車駕照"
              },
              {
                "type": "str",
                "example": "普通小型車駕照"
              },
              {
                "type": "str",
                "example": "普通重型機車駕照"
              },
              {
                "type": "str",
                "example": "普通小型車駕照"
              }
            ]
          }
        },
        "military_status": {
          "type": "str",
          "example": "役畢 (2018/2)"
        },
        "age": {
          "oneOf": [
            {
              "type": "int",
              "example": "27"
            },
            {
              "type": "int",
              "example": "29"
            }
          ]
        },
        "email": {
          "oneOf": [
            {
              "type": "str",
              "example": "XXXXXX"
            },
            {
              "type": "str",
              "example": "XXXXXX"
            }
          ]
        },
        "employment_status": {
          "oneOf": [
            {
              "type": "str",
              "example": "在職中"
            },
            {
              "type": "str",
              "example": "在職中"
            }
          ]
        },
        "address": {
          "oneOf": [
            {
              "type": "str",
              "example": ""
            },
            {
              "type": "str",
              "example": ""
            }
          ]
        }
      }
    },
    "skills": {
      "type": "object",
      "properties": {
        "collaboration": {
          "oneOf": [
            {
              "type": "str",
              "example": "與專案合作部門迅速達成共識並推進專案"
            },
            {
              "type": "str",
              "example": "擅於跨部門協作與溝通，具備領導與專案管理經驗"
            }
          ]
        },
        "specialties": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "數據分析"
              },
              {
                "type": "str",
                "example": "機器學習建模"
              },
              {
                "type": "str",
                "example": "資料視覺化"
              },
              {
                "type": "str",
                "example": "機器學習模型建置"
              },
              {
                "type": "str",
                "example": "資料視覺化"
              }
            ]
          }
        },
        "data_analysis": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "Python"
              },
              {
                "type": "str",
                "example": "SQL"
              },
              {
                "type": "str",
                "example": "Tableau"
              },
              {
                "type": "str",
                "example": "Python"
              },
              {
                "type": "str",
                "example": "R"
              },
              {
                "type": "str",
                "example": "SQL"
              },
              {
                "type": "str",
                "example": "Tableau"
              }
            ]
          }
        },
        "data_driven_decision_making": {
          "oneOf": [
            {
              "type": "str",
              "example": "利用數據分析結果優化產品及行銷策略"
            },
            {
              "type": "str",
              "example": "透過數據分析解決問題，提供決策、優化流程與業績提升"
            }
          ]
        }
      }
    },
    "certifications": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "str",
            "example": "AWS認證的機器學習-專家級認證"
          },
          "issuer": {
            "type": "str",
            "example": "Amazon Web Service"
          }
        }
      }
    },
    "job_preferences": {
      "type": "object",
      "properties": {
        "job_type": {
          "oneOf": [
            {
              "type": "str",
              "example": "全職"
            },
            {
              "type": "str",
              "example": "全職"
            },
            {
              "type": "str",
              "example": "全職"
            }
          ]
        },
        "preferred_locations": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "新竹縣市"
              },
              {
                "type": "str",
                "example": "台北市"
              },
              {
                "type": "str",
                "example": "台中市"
              },
              {
                "type": "str",
                "example": "台北市"
              },
              {
                "type": "str",
                "example": "台北市"
              },
              {
                "type": "str",
                "example": "新北市"
              }
            ]
          }
        },
        "preferred_category": {
          "type": "str",
          "example": "其他資訊專業人員"
        },
        "working_hours": {
          "oneOf": [
            {
              "type": "str",
              "example": "日班"
            },
            {
              "type": "str",
              "example": "日班"
            },
            {
              "type": "str",
              "example": "日班"
            }
          ]
        },
        "preferred_categories": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "數據分析師"
              },
              {
                "type": "str",
                "example": "商業分析師"
              },
              {
                "type": "str",
                "example": "數據分析師"
              },
              {
                "type": "str",
                "example": "資料科學家"
              }
            ]
          }
        },
        "preferred_content": {
          "type": "str",
          "example": "大數據分析，機器學習等工作內容"
        },
        "expected_salary": {
          "oneOf": [
            {
              "type": "str",
              "example": "面議"
            },
            {
              "type": "str",
              "example": "面議"
            },
            {
              "type": "str",
              "example": "面議"
            }
          ]
        },
        "availability": {
          "oneOf": [
            {
              "type": "str",
              "example": "錄取後一個月可上班"
            },
            {
              "type": "str",
              "example": "錄取後一個月可上班"
            },
            {
              "type": "str",
              "example": "錄取後二個月可上班"
            }
          ]
        },
        "preferred_industries": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "電子資訊"
              },
              {
                "type": "str",
                "example": "軟體"
              },
              {
                "type": "str",
                "example": "半導體相關業"
              }
            ]
          }
        },
        "remote_work": {
          "oneOf": [
            {
              "type": "str",
              "example": "對遠端工作有意願"
            },
            {
              "type": "str",
              "example": "對遠端工作有意願"
            },
            {
              "type": "str",
              "example": "對遠端工作有意願"
            }
          ]
        },
        "desired_titles": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "數據資訊人員"
              },
              {
                "type": "str",
                "example": "數據科學人員"
              },
              {
                "type": "str",
                "example": "大數據分析師"
              },
              {
                "type": "str",
                "example": "商業分析師"
              },
              {
                "type": "str",
                "example": "資料分析師"
              },
              {
                "type": "str",
                "example": "數據科學家"
              }
            ]
          }
        }
      }
    },
    "self_intro": {
      "type": "object",
      "properties": {
        "current_position": {
          "oneOf": [
            {
              "type": "str",
              "example": "台北富邦銀行-數據金融部"
            },
            {
              "type": "str",
              "example": "國泰綜合證券 - 數據分析部 (4年)"
            }
          ]
        },
        "future_goal": {
          "type": "str",
          "example": "參與更多不同領域的分析專案，提升分析能力與多元合作經驗"
        },
        "summary": {
          "type": "str",
          "example": "主修非線性模型估計，專精機器學習與深度學習。GPA 4.05。TOEIC 905。曾任替代役數據工程師，亦有海外經驗。下班後持續進修雲端與資料技術，如AWS、Python、SQL。"
        },
        "leadership": {
          "oneOf": [
            {
              "type": "str",
              "example": "擔任平台總PM，協助專案成員完成任務"
            },
            {
              "type": "str",
              "example": "擔任小組長，協助組員與專案管理"
            }
          ]
        }
      }
    },
    "work_experience": {
      "type": "object",
      "properties": {
        "total_years": {
          "oneOf": [
            {
              "type": "str",
              "example": "0~2年"
            },
            {
              "type": "str",
              "example": "4~5年"
            }
          ]
        },
        "jobs": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "數據分析師"
                  },
                  {
                    "type": "str",
                    "example": "數據分析師"
                  }
                ]
              },
              "company": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "台北富邦銀行"
                  },
                  {
                    "type": "str",
                    "example": "國泰綜合證券股份有限公司"
                  }
                ]
              },
              "company_size": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "500人以上"
                  },
                  {
                    "type": "str",
                    "example": "500人以上"
                  }
                ]
              },
              "location": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "台北市信義區"
                  },
                  {
                    "type": "str",
                    "example": "台北市大安區"
                  }
                ]
              },
              "description": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "以SQL挖掘客戶通路偏好行為，掌握各產品潛在目標客群。"
                    },
                    {
                      "type": "str",
                      "example": "定期追蹤與分析行銷活動之分群回應率與經營成效。"
                    },
                    {
                      "type": "str",
                      "example": "擔任客戶資料平台PM，蒐集用戶需求、簡化使用流程及活動規劃。"
                    },
                    {
                      "type": "str",
                      "example": "優化信用卡、財富管理及數位金融服務，藉由優化客群條件提升40%行銷成效。"
                    },
                    {
                      "type": "str",
                      "example": "業界首創額度計算系統，提升月均調額人數3倍，市占率提升超過40%。"
                    },
                    {
                      "type": "str",
                      "example": "兼任金控跨子公司專案落地協助。"
                    },
                    {
                      "type": "str",
                      "example": "透過數據分析與機器學習提供風控與名單建議，優化前端平台。"
                    },
                    {
                      "type": "str",
                      "example": "建置各式 Tableau 儀表板，減少人工作業、提升效率。"
                    }
                  ]
                }
              },
              "period": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "2022/8-仍在職"
                  },
                  {
                    "type": "str",
                    "example": "2020/8-仍在職"
                  }
                ]
              },
              "industry": {
                "oneOf": [
                  {
                    "type": "str",
                    "example": "銀行業"
                  },
                  {
                    "type": "str",
                    "example": "證券及期貨業"
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
}
```

### Sample-specific Schemas

#### pm_sample3.json

```json
{
  "type": "object",
  "properties": {
    "job_preferences": {
      "type": "object",
      "properties": {
        "job_type": {
          "type": "str",
          "example": "全職"
        },
        "desired_titles": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "數據資訊人員"
              },
              {
                "type": "str",
                "example": "數據科學人員"
              },
              {
                "type": "str",
                "example": "大數據分析師"
              }
            ]
          }
        },
        "preferred_content": {
          "type": "str",
          "example": "大數據分析，機器學習等工作內容"
        },
        "preferred_category": {
          "type": "str",
          "example": "其他資訊專業人員"
        },
        "preferred_industries": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "電子資訊"
              },
              {
                "type": "str",
                "example": "軟體"
              },
              {
                "type": "str",
                "example": "半導體相關業"
              }
            ]
          }
        },
        "preferred_locations": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "新竹縣市"
              },
              {
                "type": "str",
                "example": "台北市"
              },
              {
                "type": "str",
                "example": "台中市"
              }
            ]
          }
        },
        "remote_work": {
          "type": "str",
          "example": "對遠端工作有意願"
        },
        "expected_salary": {
          "type": "str",
          "example": "面議"
        },
        "availability": {
          "type": "str",
          "example": "錄取後一個月可上班"
        },
        "working_hours": {
          "type": "str",
          "example": "日班"
        }
      }
    },
    "experience": {
      "type": "object",
      "properties": {
        "total_years": {
          "type": "str",
          "example": "3~4年工作經驗"
        },
        "roles": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "str",
                    "example": "資料科學家"
                  },
                  "duration": {
                    "type": "str",
                    "example": "1~2年"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "str",
                    "example": "演算法工程師"
                  },
                  "duration": {
                    "type": "str",
                    "example": "3~4年"
                  }
                }
              }
            ]
          }
        },
        "jobs": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "company": {
                    "type": "str",
                    "example": "XX電子工業股份有限公司"
                  },
                  "title": {
                    "type": "str",
                    "example": "資料科學家"
                  },
                  "period": {
                    "type": "str",
                    "example": "2023/08～(仍在職)"
                  },
                  "industry": {
                    "type": "str",
                    "example": "其他電子零組件相關業"
                  },
                  "category": {
                    "type": "str",
                    "example": "資料科學家"
                  },
                  "company_size": {
                    "type": "str",
                    "example": "500人以上"
                  },
                  "skills": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "str",
                          "example": "AI"
                        },
                        {
                          "type": "str",
                          "example": "機器學習"
                        },
                        {
                          "type": "str",
                          "example": "PyTorch"
                        },
                        {
                          "type": "str",
                          "example": "人工智慧"
                        }
                      ]
                    }
                  },
                  "description": {
                    "type": "str",
                    "example": "在XX電子擔任資料科學家"
                  },
                  "projects": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "最佳化系統"
                            },
                            "summary": {
                              "type": "str",
                              "example": "實現實時監控趨勢，根因分析與優化演算法，提升單位時間生產數量，導入9條生產線。"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "品質調優工具"
                            },
                            "summary": {
                              "type": "str",
                              "example": "根據品質結果調整設備參數，結合強化學習確保穩定與一致性。"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "產品健康度工具"
                            },
                            "summary": {
                              "type": "str",
                              "example": "使用深度學習預測結果，預測準確率達95%、recall達87%。"
                            }
                          }
                        }
                      ]
                    }
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "company": {
                    "type": "str",
                    "example": "XX電子股份有限公司"
                  },
                  "title": {
                    "type": "str",
                    "example": "資料科學家"
                  },
                  "period": {
                    "type": "str",
                    "example": "2021/08～(仍在職)"
                  },
                  "industry": {
                    "type": "str",
                    "example": "光學器材製造業"
                  },
                  "category": {
                    "type": "str",
                    "example": "演算法工程師"
                  },
                  "company_size": {
                    "type": "str",
                    "example": "500人以上"
                  },
                  "skills": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "str",
                          "example": "Python"
                        },
                        {
                          "type": "str",
                          "example": "MySQL"
                        },
                        {
                          "type": "str",
                          "example": "Machine Learning"
                        },
                        {
                          "type": "str",
                          "example": "爬蟲"
                        }
                      ]
                    }
                  },
                  "description": {
                    "type": "str",
                    "example": "XX電子擔任資料科學家，負責AI專案。"
                  },
                  "projects": {
                    "type": "array",
                    "items": {
                      "oneOf": [
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "人力減降"
                            },
                            "summary": {
                              "type": "str",
                              "example": "使用ANOVA與線性模型提升良率1.11%，降低瑕疵率9.3%。"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "properties": {
                            "name": {
                              "type": "str",
                              "example": "廢棄分析"
                            },
                            "summary": {
                              "type": "str",
                              "example": "使用XGBoost建模報廢預測，平均廢棄率降低9.2%。"
                            }
                          }
                        }
                      ]
                    }
                  }
                }
              }
            ]
          }
        }
      }
    },
    "education": {
      "type": "object",
      "properties": {
        "highest": {
          "type": "object",
          "properties": {
            "degree": {
              "type": "str",
              "example": "碩士"
            },
            "school": {
              "type": "str",
              "example": "國立交通大學"
            },
            "department": {
              "type": "str",
              "example": "統計所"
            },
            "period": {
              "type": "str",
              "example": "2018/09~2020/07"
            }
          }
        },
        "bachelor": {
          "type": "object",
          "properties": {
            "degree": {
              "type": "str",
              "example": "學士"
            },
            "school": {
              "type": "str",
              "example": "國立中央大學"
            },
            "department": {
              "type": "str",
              "example": "財務金融"
            },
            "period": {
              "type": "str",
              "example": "2014/09~2018/06"
            }
          }
        }
      }
    },
    "self_intro": {
      "type": "object",
      "properties": {
        "summary": {
          "type": "str",
          "example": "主修非線性模型估計，專精機器學習與深度學習。GPA 4.05。TOEIC 905。曾任替代役數據工程師，亦有海外經驗。下班後持續進修雲端與資料技術，如AWS、Python、SQL。"
        }
      }
    }
  }
}
```

#### pm_sample2.json

```json
{
  "type": "object",
  "properties": {
    "personal_info": {
      "type": "object",
      "properties": {
        "gender": {
          "type": "str",
          "example": "女"
        },
        "age": {
          "type": "int",
          "example": "27"
        },
        "employment_status": {
          "type": "str",
          "example": "在職中"
        },
        "email": {
          "type": "str",
          "example": "XXXXXX"
        },
        "address": {
          "type": "str",
          "example": ""
        },
        "english_name": {
          "type": "str",
          "example": "Becky"
        },
        "driver_licenses": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "普通重型機車駕照"
              },
              {
                "type": "str",
                "example": "普通小型車駕照"
              }
            ]
          }
        }
      }
    },
    "education": {
      "type": "object",
      "properties": {
        "school": {
          "type": "str",
          "example": "台北大學"
        },
        "department": {
          "type": "str",
          "example": "統計學系"
        },
        "degree": {
          "type": "str",
          "example": "碩士"
        },
        "period": {
          "type": "str",
          "example": "2020/8-2022/7"
        }
      }
    },
    "work_experience": {
      "type": "object",
      "properties": {
        "total_years": {
          "type": "str",
          "example": "0~2年"
        },
        "jobs": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "company": {
                "type": "str",
                "example": "台北富邦銀行"
              },
              "industry": {
                "type": "str",
                "example": "銀行業"
              },
              "company_size": {
                "type": "str",
                "example": "500人以上"
              },
              "title": {
                "type": "str",
                "example": "數據分析師"
              },
              "location": {
                "type": "str",
                "example": "台北市信義區"
              },
              "period": {
                "type": "str",
                "example": "2022/8-仍在職"
              },
              "description": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "以SQL挖掘客戶通路偏好行為，掌握各產品潛在目標客群。"
                    },
                    {
                      "type": "str",
                      "example": "定期追蹤與分析行銷活動之分群回應率與經營成效。"
                    },
                    {
                      "type": "str",
                      "example": "擔任客戶資料平台PM，蒐集用戶需求、簡化使用流程及活動規劃。"
                    },
                    {
                      "type": "str",
                      "example": "優化信用卡、財富管理及數位金融服務，藉由優化客群條件提升40%行銷成效。"
                    }
                  ]
                }
              }
            }
          }
        }
      }
    },
    "skills": {
      "type": "object",
      "properties": {
        "data_analysis": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "Python"
              },
              {
                "type": "str",
                "example": "SQL"
              },
              {
                "type": "str",
                "example": "Tableau"
              }
            ]
          }
        },
        "specialties": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "數據分析"
              },
              {
                "type": "str",
                "example": "機器學習建模"
              },
              {
                "type": "str",
                "example": "資料視覺化"
              }
            ]
          }
        },
        "data_driven_decision_making": {
          "type": "str",
          "example": "利用數據分析結果優化產品及行銷策略"
        },
        "collaboration": {
          "type": "str",
          "example": "與專案合作部門迅速達成共識並推進專案"
        }
      }
    },
    "self_intro": {
      "type": "object",
      "properties": {
        "current_position": {
          "type": "str",
          "example": "台北富邦銀行-數據金融部"
        },
        "leadership": {
          "type": "str",
          "example": "擔任平台總PM，協助專案成員完成任務"
        }
      }
    },
    "job_preferences": {
      "type": "object",
      "properties": {
        "job_type": {
          "type": "str",
          "example": "全職"
        },
        "working_hours": {
          "type": "str",
          "example": "日班"
        },
        "availability": {
          "type": "str",
          "example": "錄取後一個月可上班"
        },
        "expected_salary": {
          "type": "str",
          "example": "面議"
        },
        "preferred_locations": {
          "type": "array",
          "items": {
            "type": "str",
            "example": "台北市"
          }
        },
        "remote_work": {
          "type": "str",
          "example": "對遠端工作有意願"
        },
        "desired_titles": {
          "type": "array",
          "items": {
            "type": "str",
            "example": "商業分析師"
          }
        },
        "preferred_categories": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "數據分析師"
              },
              {
                "type": "str",
                "example": "商業分析師"
              }
            ]
          }
        }
      }
    }
  }
}
```

#### pm_sample1.json

```json
{
  "type": "object",
  "properties": {
    "personal_info": {
      "type": "object",
      "properties": {
        "gender": {
          "type": "str",
          "example": "男"
        },
        "age": {
          "type": "int",
          "example": "29"
        },
        "military_status": {
          "type": "str",
          "example": "役畢 (2018/2)"
        },
        "employment_status": {
          "type": "str",
          "example": "在職中"
        },
        "email": {
          "type": "str",
          "example": "XXXXXX"
        },
        "address": {
          "type": "str",
          "example": ""
        },
        "english_name": {
          "type": "str",
          "example": "Jason"
        },
        "driver_licenses": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "普通重型機車駕照"
              },
              {
                "type": "str",
                "example": "普通小型車駕照"
              }
            ]
          }
        }
      }
    },
    "education": {
      "type": "object",
      "properties": {
        "school": {
          "type": "str",
          "example": "私立東吳大學"
        },
        "department": {
          "type": "str",
          "example": "應用統計資訊"
        },
        "degree": {
          "type": "str",
          "example": "碩士"
        },
        "period": {
          "type": "str",
          "example": "2018/8-2020/7"
        }
      }
    },
    "work_experience": {
      "type": "object",
      "properties": {
        "total_years": {
          "type": "str",
          "example": "4~5年"
        },
        "jobs": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "company": {
                "type": "str",
                "example": "國泰綜合證券股份有限公司"
              },
              "industry": {
                "type": "str",
                "example": "證券及期貨業"
              },
              "company_size": {
                "type": "str",
                "example": "500人以上"
              },
              "title": {
                "type": "str",
                "example": "數據分析師"
              },
              "location": {
                "type": "str",
                "example": "台北市大安區"
              },
              "period": {
                "type": "str",
                "example": "2020/8-仍在職"
              },
              "description": {
                "type": "array",
                "items": {
                  "oneOf": [
                    {
                      "type": "str",
                      "example": "業界首創額度計算系統，提升月均調額人數3倍，市占率提升超過40%。"
                    },
                    {
                      "type": "str",
                      "example": "兼任金控跨子公司專案落地協助。"
                    },
                    {
                      "type": "str",
                      "example": "透過數據分析與機器學習提供風控與名單建議，優化前端平台。"
                    },
                    {
                      "type": "str",
                      "example": "建置各式 Tableau 儀表板，減少人工作業、提升效率。"
                    }
                  ]
                }
              }
            }
          }
        }
      }
    },
    "skills": {
      "type": "object",
      "properties": {
        "data_analysis": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "Python"
              },
              {
                "type": "str",
                "example": "R"
              },
              {
                "type": "str",
                "example": "SQL"
              },
              {
                "type": "str",
                "example": "Tableau"
              }
            ]
          }
        },
        "specialties": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "機器學習模型建置"
              },
              {
                "type": "str",
                "example": "資料視覺化"
              }
            ]
          }
        },
        "data_driven_decision_making": {
          "type": "str",
          "example": "透過數據分析解決問題，提供決策、優化流程與業績提升"
        },
        "collaboration": {
          "type": "str",
          "example": "擅於跨部門協作與溝通，具備領導與專案管理經驗"
        }
      }
    },
    "self_intro": {
      "type": "object",
      "properties": {
        "current_position": {
          "type": "str",
          "example": "國泰綜合證券 - 數據分析部 (4年)"
        },
        "leadership": {
          "type": "str",
          "example": "擔任小組長，協助組員與專案管理"
        },
        "future_goal": {
          "type": "str",
          "example": "參與更多不同領域的分析專案，提升分析能力與多元合作經驗"
        }
      }
    },
    "job_preferences": {
      "type": "object",
      "properties": {
        "job_type": {
          "type": "str",
          "example": "全職"
        },
        "working_hours": {
          "type": "str",
          "example": "日班"
        },
        "availability": {
          "type": "str",
          "example": "錄取後二個月可上班"
        },
        "expected_salary": {
          "type": "str",
          "example": "面議"
        },
        "preferred_locations": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "台北市"
              },
              {
                "type": "str",
                "example": "新北市"
              }
            ]
          }
        },
        "remote_work": {
          "type": "str",
          "example": "對遠端工作有意願"
        },
        "desired_titles": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "資料分析師"
              },
              {
                "type": "str",
                "example": "數據科學家"
              }
            ]
          }
        },
        "preferred_categories": {
          "type": "array",
          "items": {
            "oneOf": [
              {
                "type": "str",
                "example": "數據分析師"
              },
              {
                "type": "str",
                "example": "資料科學家"
              }
            ]
          }
        }
      }
    },
    "certifications": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "str",
            "example": "AWS認證的機器學習-專家級認證"
          },
          "issuer": {
            "type": "str",
            "example": "Amazon Web Service"
          }
        }
      }
    }
  }
}
```

### Field Descriptions

| Field Path | Type | Description |
|------------|------|-------------|
| education.highest.degree | str | 碩士 |
| education.highest.school | str | 國立交通大學 |
| education.highest.department | str | 統計所 |
| education.highest.period | str | 2018/09~2020/07 |
| education.degree | str | 碩士 |
| education.degree | str | 碩士 |
| education.department | str | 統計學系 |
| education.department | str | 應用統計資訊 |
| education.period | str | 2020/8-2022/7 |
| education.period | str | 2018/8-2020/7 |
| education.school | str | 台北大學 |
| education.school | str | 私立東吳大學 |
| education.bachelor.degree | str | 學士 |
| education.bachelor.school | str | 國立中央大學 |
| education.bachelor.department | str | 財務金融 |
| education.bachelor.period | str | 2014/09~2018/06 |
| experience.total_years | str | 3~4年工作經驗 |
| experience.roles[].title | str | 資料科學家 |
| experience.roles[].duration | str | 1~2年 |
| experience.roles[].title | str | 演算法工程師 |
| experience.roles[].duration | str | 3~4年 |
| experience.jobs[].company | str | XX電子工業股份有限公司 |
| experience.jobs[].title | str | 資料科學家 |
| experience.jobs[].period | str | 2023/08～(仍在職) |
| experience.jobs[].industry | str | 其他電子零組件相關業 |
| experience.jobs[].category | str | 資料科學家 |
| experience.jobs[].company_size | str | 500人以上 |
| experience.jobs[].skills[] | str | AI |
| experience.jobs[].skills[] | str | 機器學習 |
| experience.jobs[].skills[] | str | PyTorch |
| experience.jobs[].skills[] | str | 人工智慧 |
| experience.jobs[].description | str | 在XX電子擔任資料科學家 |
| experience.jobs[].projects[].name | str | 最佳化系統 |
| experience.jobs[].projects[].summary | str | 實現實時監控趨勢，根因分析與優化演算法，提升單位時間生產數量，導入9條生產線。 |
| experience.jobs[].projects[].name | str | 品質調優工具 |
| experience.jobs[].projects[].summary | str | 根據品質結果調整設備參數，結合強化學習確保穩定與一致性。 |
| experience.jobs[].projects[].name | str | 產品健康度工具 |
| experience.jobs[].projects[].summary | str | 使用深度學習預測結果，預測準確率達95%、recall達87%。 |
| experience.jobs[].company | str | XX電子股份有限公司 |
| experience.jobs[].title | str | 資料科學家 |
| experience.jobs[].period | str | 2021/08～(仍在職) |
| experience.jobs[].industry | str | 光學器材製造業 |
| experience.jobs[].category | str | 演算法工程師 |
| experience.jobs[].company_size | str | 500人以上 |
| experience.jobs[].skills[] | str | Python |
| experience.jobs[].skills[] | str | MySQL |
| experience.jobs[].skills[] | str | Machine Learning |
| experience.jobs[].skills[] | str | 爬蟲 |
| experience.jobs[].description | str | XX電子擔任資料科學家，負責AI專案。 |
| experience.jobs[].projects[].name | str | 人力減降 |
| experience.jobs[].projects[].summary | str | 使用ANOVA與線性模型提升良率1.11%，降低瑕疵率9.3%。 |
| experience.jobs[].projects[].name | str | 廢棄分析 |
| experience.jobs[].projects[].summary | str | 使用XGBoost建模報廢預測，平均廢棄率降低9.2%。 |
| personal_info.english_name | str | Becky |
| personal_info.english_name | str | Jason |
| personal_info.gender | str | 女 |
| personal_info.gender | str | 男 |
| personal_info.driver_licenses[] | str | 普通重型機車駕照 |
| personal_info.driver_licenses[] | str | 普通小型車駕照 |
| personal_info.driver_licenses[] | str | 普通重型機車駕照 |
| personal_info.driver_licenses[] | str | 普通小型車駕照 |
| personal_info.military_status | str | 役畢 (2018/2) |
| personal_info.age | int | 27 |
| personal_info.age | int | 29 |
| personal_info.email | str | XXXXXX |
| personal_info.email | str | XXXXXX |
| personal_info.employment_status | str | 在職中 |
| personal_info.employment_status | str | 在職中 |
| personal_info.address | str |  |
| personal_info.address | str |  |
| skills.collaboration | str | 與專案合作部門迅速達成共識並推進專案 |
| skills.collaboration | str | 擅於跨部門協作與溝通，具備領導與專案管理經驗 |
| skills.specialties[] | str | 數據分析 |
| skills.specialties[] | str | 機器學習建模 |
| skills.specialties[] | str | 資料視覺化 |
| skills.specialties[] | str | 機器學習模型建置 |
| skills.specialties[] | str | 資料視覺化 |
| skills.data_analysis[] | str | Python |
| skills.data_analysis[] | str | SQL |
| skills.data_analysis[] | str | Tableau |
| skills.data_analysis[] | str | Python |
| skills.data_analysis[] | str | R |
| skills.data_analysis[] | str | SQL |
| skills.data_analysis[] | str | Tableau |
| skills.data_driven_decision_making | str | 利用數據分析結果優化產品及行銷策略 |
| skills.data_driven_decision_making | str | 透過數據分析解決問題，提供決策、優化流程與業績提升 |
| certifications[].name | str | AWS認證的機器學習-專家級認證 |
| certifications[].issuer | str | Amazon Web Service |
| job_preferences.job_type | str | 全職 |
| job_preferences.job_type | str | 全職 |
| job_preferences.job_type | str | 全職 |
| job_preferences.preferred_locations[] | str | 新竹縣市 |
| job_preferences.preferred_locations[] | str | 台北市 |
| job_preferences.preferred_locations[] | str | 台中市 |
| job_preferences.preferred_locations[] | str | 台北市 |
| job_preferences.preferred_locations[] | str | 台北市 |
| job_preferences.preferred_locations[] | str | 新北市 |
| job_preferences.preferred_category | str | 其他資訊專業人員 |
| job_preferences.working_hours | str | 日班 |
| job_preferences.working_hours | str | 日班 |
| job_preferences.working_hours | str | 日班 |
| job_preferences.preferred_categories[] | str | 數據分析師 |
| job_preferences.preferred_categories[] | str | 商業分析師 |
| job_preferences.preferred_categories[] | str | 數據分析師 |
| job_preferences.preferred_categories[] | str | 資料科學家 |
| job_preferences.preferred_content | str | 大數據分析，機器學習等工作內容 |
| job_preferences.expected_salary | str | 面議 |
| job_preferences.expected_salary | str | 面議 |
| job_preferences.expected_salary | str | 面議 |
| job_preferences.availability | str | 錄取後一個月可上班 |
| job_preferences.availability | str | 錄取後一個月可上班 |
| job_preferences.availability | str | 錄取後二個月可上班 |
| job_preferences.preferred_industries[] | str | 電子資訊 |
| job_preferences.preferred_industries[] | str | 軟體 |
| job_preferences.preferred_industries[] | str | 半導體相關業 |
| job_preferences.remote_work | str | 對遠端工作有意願 |
| job_preferences.remote_work | str | 對遠端工作有意願 |
| job_preferences.remote_work | str | 對遠端工作有意願 |
| job_preferences.desired_titles[] | str | 數據資訊人員 |
| job_preferences.desired_titles[] | str | 數據科學人員 |
| job_preferences.desired_titles[] | str | 大數據分析師 |
| job_preferences.desired_titles[] | str | 商業分析師 |
| job_preferences.desired_titles[] | str | 資料分析師 |
| job_preferences.desired_titles[] | str | 數據科學家 |
| self_intro.current_position | str | 台北富邦銀行-數據金融部 |
| self_intro.current_position | str | 國泰綜合證券 - 數據分析部 (4年) |
| self_intro.future_goal | str | 參與更多不同領域的分析專案，提升分析能力與多元合作經驗 |
| self_intro.summary | str | 主修非線性模型估計，專精機器學習與深度學習。GPA 4.05。TOEIC 905。曾任替代役數據工程師，亦有海外經驗。下班後持續進修雲端與資料技術，如AWS、Python、SQL。 |
| self_intro.leadership | str | 擔任平台總PM，協助專案成員完成任務 |
| self_intro.leadership | str | 擔任小組長，協助組員與專案管理 |
| work_experience.total_years | str | 0~2年 |
| work_experience.total_years | str | 4~5年 |
| work_experience.jobs[].title | str | 數據分析師 |
| work_experience.jobs[].title | str | 數據分析師 |
| work_experience.jobs[].company | str | 台北富邦銀行 |
| work_experience.jobs[].company | str | 國泰綜合證券股份有限公司 |
| work_experience.jobs[].company_size | str | 500人以上 |
| work_experience.jobs[].company_size | str | 500人以上 |
| work_experience.jobs[].location | str | 台北市信義區 |
| work_experience.jobs[].location | str | 台北市大安區 |
| work_experience.jobs[].description[] | str | 以SQL挖掘客戶通路偏好行為，掌握各產品潛在目標客群。 |
| work_experience.jobs[].description[] | str | 定期追蹤與分析行銷活動之分群回應率與經營成效。 |
| work_experience.jobs[].description[] | str | 擔任客戶資料平台PM，蒐集用戶需求、簡化使用流程及活動規劃。 |
| work_experience.jobs[].description[] | str | 優化信用卡、財富管理及數位金融服務，藉由優化客群條件提升40%行銷成效。 |
| work_experience.jobs[].description[] | str | 業界首創額度計算系統，提升月均調額人數3倍，市占率提升超過40%。 |
| work_experience.jobs[].description[] | str | 兼任金控跨子公司專案落地協助。 |
| work_experience.jobs[].description[] | str | 透過數據分析與機器學習提供風控與名單建議，優化前端平台。 |
| work_experience.jobs[].description[] | str | 建置各式 Tableau 儀表板，減少人工作業、提升效率。 |
| work_experience.jobs[].period | str | 2022/8-仍在職 |
| work_experience.jobs[].period | str | 2020/8-仍在職 |
| work_experience.jobs[].industry | str | 銀行業 |
| work_experience.jobs[].industry | str | 證券及期貨業 |

