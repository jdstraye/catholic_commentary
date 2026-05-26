"""
Database schema definition for Catholic Commentary project.
Using SQLite for simplicity; can be adapted to PostgreSQL or others.
"""
import sqlite3

def create_schema(conn):
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS scripture_reference (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book TEXT NOT NULL,
        chapter INTEGER NOT NULL,
        verse_start INTEGER,
        verse_end INTEGER
    );
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS commentary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        author TEXT,
        title TEXT,
        date TEXT,
        source_url TEXT,
        text TEXT NOT NULL
    );
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS commentary_scripture (
        commentary_id INTEGER,
        scripture_id INTEGER,
        FOREIGN KEY(commentary_id) REFERENCES commentary(id),
        FOREIGN KEY(scripture_id) REFERENCES scripture_reference(id)
    );
    ''')
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("catholic_commentary.db")
    create_schema(conn)
    print("Database schema created.")
    conn.close()
