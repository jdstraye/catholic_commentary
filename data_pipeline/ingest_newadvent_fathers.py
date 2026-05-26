"""
Extract main text and scripture references from downloaded New Advent Church Fathers HTML files and ingest into the database.
"""
import os
from bs4 import BeautifulSoup
from data_pipeline.scripture_mapper import map_scripture_references
from data_pipeline.db_schema import create_schema
import sqlite3

SRC_DIR = "downloaded_sources/newadvent_fathers"
DB_PATH = "catholic_commentary.db"

def extract_main_text(html_path):
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        # Remove navigation, scripts, styles
        for tag in soup(["script", "style", "nav", "header", "footer"]):
            tag.decompose()
        # Main content is usually in <body>
        body = soup.body
        if not body:
            return ""
        return body.get_text(separator=" ", strip=True)

def ingest_document(html_path, conn):
    text = extract_main_text(html_path)
    refs = map_scripture_references(text)
    # Insert commentary
    cur = conn.cursor()
    cur.execute('''INSERT INTO commentary (type, author, title, date, source_url, text) VALUES (?, ?, ?, ?, ?, ?)''',
                ("church_father", None, os.path.basename(html_path), None, None, text))
    commentary_id = cur.lastrowid
    # Insert scripture refs and links
    for ref in refs:
        cur.execute('''INSERT INTO scripture_reference (book, chapter, verse_start, verse_end) VALUES (?, ?, ?, ?)''',
                    (ref.book, ref.chapter, ref.verse_start, ref.verse_end))
        scripture_id = cur.lastrowid
        cur.execute('''INSERT INTO commentary_scripture (commentary_id, scripture_id) VALUES (?, ?)''',
                    (commentary_id, scripture_id))
    conn.commit()
    print(f"Ingested {os.path.basename(html_path)} with {len(refs)} scripture refs.")

def main():
    conn = sqlite3.connect(DB_PATH)
    create_schema(conn)
    for fname in os.listdir(SRC_DIR):
        if fname.endswith(".htm") or fname.endswith(".html"):
            ingest_document(os.path.join(SRC_DIR, fname), conn)
    conn.close()

if __name__ == "__main__":
    main()
