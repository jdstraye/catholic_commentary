"""
Basic data ingestion script: stores a sample commentary and scripture mapping in the database.
"""
import sqlite3
from .db_schema import create_schema
from .scripture_parser import parse_scripture_reference

def insert_scripture(conn, ref):
    cur = conn.cursor()
    cur.execute('''INSERT INTO scripture_reference (book, chapter, verse_start, verse_end)
                   VALUES (?, ?, ?, ?)''',
                (ref.book, ref.chapter, ref.verse_start, ref.verse_end))
    return cur.lastrowid

def insert_commentary(conn, type_, author, title, date, source_url, text):
    cur = conn.cursor()
    cur.execute('''INSERT INTO commentary (type, author, title, date, source_url, text)
                   VALUES (?, ?, ?, ?, ?, ?)''',
                (type_, author, title, date, source_url, text))
    return cur.lastrowid

def link_commentary_scripture(conn, commentary_id, scripture_id):
    cur = conn.cursor()
    cur.execute('''INSERT INTO commentary_scripture (commentary_id, scripture_id)
                   VALUES (?, ?)''', (commentary_id, scripture_id))

def main():
    conn = sqlite3.connect("catholic_commentary.db")
    create_schema(conn)
    # Example: Insert a commentary on Lev 6
    ref = parse_scripture_reference("Lev 6")
    scripture_id = insert_scripture(conn, ref)
    commentary_id = insert_commentary(
        conn,
        "encyclical",
        "Pope Example",
        "On the Sacrifice",
        "1900-01-01",
        "https://www.vatican.va/",
        "This is a sample commentary on Leviticus 6."
    )
    link_commentary_scripture(conn, commentary_id, scripture_id)
    conn.commit()
    print("Sample commentary and scripture reference inserted.")
    conn.close()

if __name__ == "__main__":
    main()
