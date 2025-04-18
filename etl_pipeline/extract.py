# National Risk Index https://hazards.fema.gov/nri/data-resources
# updated Nov/Oct annually --> which makes me think AWS Lambda in production  - roughly run job end of Dec at cheapest time and availability zone
# no dynamic content on page so beautifulsoup is a resonable choice.

# 1 time need Download the Data Dictionary
# 2 Iterate on Census Tract Level csv 

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

BASE_URL = "https://hazards.fema.gov/nri/data-resources"
LOCAL_DIR = os.getenv("LOCAL_DOWNLOAD_DIR", "downloads/nri_census_tract")


def get_fema_nri_census_tract_csv_links():
    print("""Scrape the FEMA NRI page for Census Tract level CSV download links.""")
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for a in soup.find_all("a", href=True):
        href = a['href']
        text = a.text.strip().lower()
        if "tract-level detail (table)" in text and href.endswith(".zip"):
            full_url = urljoin(BASE_URL, href)
            links.append(full_url)

    return links


def download_file(url, dest_folder):
    print("""Download file from URL to local directory with progress bar.""")
    os.makedirs(dest_folder, exist_ok=True)
    local_filename = os.path.join(dest_folder, os.path.basename(url))

    # CLI Progress Bar visulization
    # response = requests.get(url, stream=True)
    # total = int(response.headers.get('content-length', 0))
    # with open(local_filename, 'wb') as f, tqdm(
    #     desc=os.path.basename(url),
    #     total=total,
    #     unit='B',
    #     unit_scale=True,
    #     unit_divisor=1024,
    # ) as bar:
    #     for data in response.iter_content(chunk_size=1024):
    #         f.write(data)
    #         bar.update(len(data))

    return local_filename


def run_extract():
    print("🔍 Fetching Census Tract zipped CSV links from FEMA NRI site...")
    csv_links = get_fema_nri_census_tract_csv_links()
    print(csv_links)

    if not csv_links:
        print("❌ No links found.")
        return

    for url in csv_links:
        print(f"\n⬇️ Downloading {url}")
        local_path = '' # download_file(url, LOCAL_DIR) --> reinit later
        print(f"📁 Saved to {local_path}")


if __name__ == "__main__":
    run_extract()

