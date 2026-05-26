"""
FastAPI app to query commentaries by scripture reference.
"""
from fastapi import FastAPI, Query
from typing import List, Optional
import sqlite3
from pydantic import BaseModel

app = FastAPI()
DB_PATH = "catholic_commentary.db"

class CommentaryOut(BaseModel):
    id: int
    type: str
    author: Optional[str]
    title: Optional[str]
    date: Optional[str]
    source_url: Optional[str]
    text: str
    scripture_refs: List[str]

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def get_commentaries(book: str, chapter: int, verse: Optional[int] = None):
    conn = get_db_connection()
    cur = conn.cursor()
    # Find scripture_reference ids matching the query
    if verse:
        cur.execute("""
            SELECT id FROM scripture_reference
            WHERE book=? AND chapter=? AND (verse_start IS NULL OR verse_start<=? AND (verse_end IS NULL OR verse_end>=?))
        """, (book, chapter, verse, verse))
    else:
        cur.execute("SELECT id FROM scripture_reference WHERE book=? AND chapter=?", (book, chapter))
    scripture_ids = [row[0] for row in cur.fetchall()]
    if not scripture_ids:
        return []
    # Find commentaries linked to these scripture ids
    q_marks = ','.join(['?']*len(scripture_ids))
    cur.execute(f"""
        SELECT c.id, c.type, c.author, c.title, c.date, c.source_url, c.text, group_concat(sr.book || ' ' || sr.chapter ||
            CASE WHEN sr.verse_start IS NOT NULL THEN ':' || sr.verse_start ELSE '' END ||
            CASE WHEN sr.verse_end IS NOT NULL THEN '-' || sr.verse_end ELSE '' END)
        FROM commentary c
        JOIN commentary_scripture cs ON c.id = cs.commentary_id
        JOIN scripture_reference sr ON cs.scripture_id = sr.id
        WHERE cs.scripture_id IN ({q_marks})
        GROUP BY c.id
    """, scripture_ids)
    results = []
    for row in cur.fetchall():
        results.append(CommentaryOut(
            id=row[0], type=row[1], author=row[2], title=row[3], date=row[4], source_url=row[5], text=row[6], scripture_refs=row[7].split(',') if row[7] else []
        ))
    conn.close()
    return results

@app.get("/commentary/", response_model=List[CommentaryOut])
def commentary_lookup(book: str = Query(...), chapter: int = Query(...), verse: Optional[int] = Query(None)):
    """Query commentaries by scripture reference (book, chapter, optional verse)."""
    return get_commentaries(book, chapter, verse)
