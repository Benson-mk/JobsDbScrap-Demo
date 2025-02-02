import requests
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

API_URL = "https://hk.jobsdb.com/api/jobsearch/v5/search"
SITE_KEY = "HK-Main"
SORT_MODE = "ListedDate"
PAGE_SIZE = 100
TOTAL_JOBS = 10000
MAX_WORKERS = 4

CSV_FILE = "jobsdb_jobs.csv"
CSV_HEADERS = ["id", "companyName", "title", "classification", "workTypes", "bulletPoints", "URL"]

def fetch_jobs(page):
    params = {
        "siteKey": SITE_KEY,
        "sortmode": SORT_MODE,
        "page": page,
        "pageSize": PAGE_SIZE
    }
    try:
        response = requests.get(API_URL, params=params, timeout=100)
        response.raise_for_status()
        data = response.json()
        jobs = data.get("data", [])
        return jobs
    except requests.RequestException as e:
        print(f"Error fetching page {page}: {e}")
        return []

def extract_job_data(job):
    job_id = job.get("id", "")
    
    company_name = job.get("companyName")
    if not company_name:
        advertiser = job.get("advertiser", {})
        company_name = advertiser.get("description", "")
    
    title = job.get("title", "")
    
    classifications = job.get("classifications", [])
    if classifications:
        classification = classifications[0].get("classification", {}).get("description", "")
    else:
        classification = ""
    
    work_types = job.get("workTypes", [])
    bullet_points = job.get("bulletPoints", [])
    url = f"https://hk.jobsdb.com/job/{job_id}"
    
    return {
        "id": job_id,
        "companyName": company_name,
        "title": title,
        "classification": classification,
        "workTypes": "; ".join(work_types),
        "bulletPoints": "; ".join(bullet_points),
        "URL": url
    }

def write_to_csv(jobs, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADERS)
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)

def main():
    total_pages = (TOTAL_JOBS + PAGE_SIZE - 1) // PAGE_SIZE 
    pages = list(range(1, total_pages + 1))
    
    all_jobs = []
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_page = {executor.submit(fetch_jobs, page): page for page in pages}
        
        for future in as_completed(future_to_page):
            page = future_to_page[future]
            try:
                jobs = future.result()
                for job in jobs:
                    extracted = extract_job_data(job)
                    all_jobs.append(extracted)
                    if len(all_jobs) >= TOTAL_JOBS:
                        break
                print(f"Page {page} processed. Total jobs collected: {len(all_jobs)}")
            except Exception as e:
                print(f"Error processing page {page}: {e}")
            if len(all_jobs) >= TOTAL_JOBS:
                break
    
    all_jobs = all_jobs[:TOTAL_JOBS]
    
    write_to_csv(all_jobs, CSV_FILE)
    print(f"Scraping completed. {len(all_jobs)} jobs saved to {CSV_FILE}.")

if __name__ == "__main__":
    main()
