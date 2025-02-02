# JobsDbScrap-Demo
[JobsDb-HK](https://hk.jobsdb.com/) web Scraper

## Feature
Scrap recent 10k job spots with multithread

Output a CSV format as following examples:

| ID        | Company Name                | Title                     | Classification                 | Work Types | Bullet Points                                                                                   | URL                                           |
|-----------|-----------------------------|---------------------------|--------------------------------|------------|------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 12345678  | AlphaTech Solutions Ltd.    | Software Engineer         | Information Technology         | Full time  | 3+ years' experience in software development; Proficient in Python and JavaScript; Strong problem-solving skills | https://hk.jobsdb.com/job/12345678     |
| 23456789  | Global Logistics Inc.       | Operations Manager        | Logistics & Supply Chain       | Full time  | 5 years' experience in supply chain management; Excellent leadership skills; Degree in Business Administration | https://hk.jobsdb.com/job/23456789     |
| 34567890  | GreenEnergy Corp.           | Environmental Consultant  | Environmental & Sustainability | Part time  | Knowledge of environmental regulations; Degree in Environmental Science; Strong analytical skills | https://hk.jobsdb.com/job/34567890     |
| 45678901  | FinSecure Banking Group     | Financial Analyst         | Banking & Finance              | Full time  | 2+ years' experience in financial modeling; Proficient in Excel and financial software; CFA preferred | https://hk.jobsdb.com/job/45678901     |
| ... | ... | ... | ... | ... | ... | ... |

## How to use
Execute the following commands in the terminal:
```
git clone https://github.com/Benson-mk/JobsDbScrap-Demo.git
cd JobsDbScrap-Demo
pip install -r requirements.txt
python main.py
```

The ibipiano folder will be automatically generated in the current directory and the Scrap job spots will be saved in this folder.
