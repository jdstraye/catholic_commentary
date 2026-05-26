"""
Automated data collection for Catholic commentary sources.
This script downloads and saves sample documents from authoritative sources.
For demonstration, it will fetch a Church Father text from New Advent.
"""
import requests
import os

def download_url(url, dest_folder, filename=None):
    os.makedirs(dest_folder, exist_ok=True)
    if not filename:
        filename = url.split("/")[-1]
    dest_path = os.path.join(dest_folder, filename)
    resp = requests.get(url)
    resp.raise_for_status()
    with open(dest_path, "wb") as f:
        f.write(resp.content)
    return dest_path

def main():
    # Example: Download "On the Holy Spirit" by St. Basil (New Advent)
    url = "https://www.newadvent.org/fathers/3203.htm"
    dest = download_url(url, "downloaded_sources", "basil_on_the_holy_spirit.html")
    print(f"Downloaded to {dest}")

if __name__ == "__main__":
    main()
