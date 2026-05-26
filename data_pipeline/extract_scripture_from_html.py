"""
Extract and map scripture references from downloaded HTML file.
"""
import re
from bs4 import BeautifulSoup
from data_pipeline.scripture_mapper import map_scripture_references

INPUT_FILE = "downloaded_sources/basil_on_the_holy_spirit.html"


def extract_text_from_html(filepath):
    with open(filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        # Remove scripts/styles
        for tag in soup(["script", "style"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)

def main():
    text = extract_text_from_html(INPUT_FILE)
    refs = map_scripture_references(text)
    print(f"Found {len(refs)} scripture references.")
    for ref in refs[:10]:  # Show first 10
        print(ref)

if __name__ == "__main__":
    main()
