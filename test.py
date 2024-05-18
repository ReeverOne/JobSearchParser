import json
import requests
import re
from bs4 import BeautifulSoup

# User Agent to use for scraping to get around 403 errors
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.2478.97"}

def load_urls_from_json(file_path):
    with open(file_path, 'r') as file:
        urls = json.load(file)
        for x, url in enumerate(urls):
            if not url.startswith('http'):
                urls[x] = 'https://' + url
    return urls

def fetch_page(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def find_career_page(home_page_content, base_url):
    soup = BeautifulSoup(home_page_content, 'html.parser')
    career_links = soup.find_all('a', href=True, string=lambda x: x and ('career' in x.lower() or 'join our team' in x.lower() or 'job' in x.lower()))
    for x in career_links:
        href = x['href']
        if href.startswith('/'):
            href = requests.compat.urljoin(base_url, href)
        return href
    return None

def parse_job_requirements(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    job_listings = soup.find_all(string=lambda text: text and ("project manager" in text.lower() or "project management" in text.lower() or "analyst" in text.lower()))

    job_positions = []
    for listing in job_listings:
        job_section = listing.find_parent('section') or listing.find_parent('div') or listing.find_parent('article')
        if job_section:
            requirements = job_section.get_text(separator="\n")
            job_positions.append(requirements)
    
    return job_positions

def save_results_to_json(results, file_path):
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)

def main():
    input_file = 'example.json'
    output_file = 'project_management_positions.json'
    
    urls = load_urls_from_json(input_file)
    results = []
    
    for url in urls:
        home_page_content = fetch_page(url)
        if home_page_content:
            career_page_url = find_career_page(home_page_content, url)
            if career_page_url:
                career_page_content = fetch_page(career_page_url)
                if career_page_content:
                    job_positions = parse_job_requirements(career_page_content)
                    if job_positions:
                        for position in job_positions:
                            results.append({
                                'company': url.split("//")[-1].split("/")[0],  # Extracting company domain name from URL
                                'url': career_page_url,
                                'requirements': position
                            })

    save_results_to_json(results, output_file)

if __name__ == "__main__":
    main()
