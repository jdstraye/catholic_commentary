"""
Scraper for New Advent Church Fathers index and documents.
This script fetches the index, downloads a few sample works, and saves them for further processing.
"""

import requests
from bs4 import BeautifulSoup
import os
import time
import re

BASE_URL = "https://www.newadvent.org/fathers/"
DEST_DIR = "downloaded_sources/newadvent_fathers"
INDEX_URL = BASE_URL + "index.html"

os.makedirs(DEST_DIR, exist_ok=True)

def get_index_links():
    resp = requests.get(INDEX_URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Match links like ../fathers/3402.htm or /fathers/3402.htm
        m = re.match(r".*?/fathers/(\d{3,6})\.htm$", href)
        if m:
            # Normalize to absolute URL
            abs_url = "https://www.newadvent.org/fathers/" + m.group(1) + ".htm"
            links.append(abs_url)
    return links

def download_and_save(url):
    filename = url.split("/")[-1]
    dest_path = os.path.join(DEST_DIR, filename)
    if os.path.exists(dest_path):
        print(f"Already downloaded: {filename}")
        return dest_path
    resp = requests.get(url)
    resp.raise_for_status()
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(resp.text)
    print(f"Downloaded: {filename}")
    time.sleep(1)  # Be polite to the server
    return dest_path

def main():
    links = get_index_links()
    print(f"Found {len(links)} documents. Downloading all...")
    for url in links:
        download_and_save(url)

if __name__ == "__main__":
    main()
