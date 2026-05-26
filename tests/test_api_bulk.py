import pytest
import requests

BASE_URL = "http://127.0.0.1:8000/commentary/"

# 100 diverse scripture references (book, chapter)
QUERIES = [
    ("Matthew", 5), ("John", 1), ("Romans", 8), ("Genesis", 1), ("Exodus", 20),
    ("Leviticus", 6), ("Numbers", 21), ("Deuteronomy", 6), ("Joshua", 1), ("Judges", 6),
    ("Ruth", 1), ("1 Samuel", 17), ("2 Samuel", 7), ("1 Kings", 18), ("2 Kings", 2),
    ("1 Chronicles", 16), ("2 Chronicles", 7), ("Ezra", 3), ("Nehemiah", 8), ("Tobit", 12),
    ("Judith", 13), ("Esther", 4), ("Job", 1), ("Psalms", 23), ("Proverbs", 3),
    ("Ecclesiastes", 12), ("Song of Songs", 2), ("Wisdom", 7), ("Sirach", 2), ("Isaiah", 53),
    ("Jeremiah", 31), ("Lamentations", 3), ("Baruch", 3), ("Ezekiel", 37), ("Daniel", 7),
    ("Hosea", 11), ("Joel", 2), ("Amos", 5), ("Obadiah", 1), ("Jonah", 2),
    ("Micah", 6), ("Nahum", 1), ("Habakkuk", 2), ("Zephaniah", 3), ("Haggai", 2),
    ("Zechariah", 9), ("Malachi", 3), ("Mark", 1), ("Luke", 15), ("Acts", 2),
    ("Romans", 12), ("1 Corinthians", 13), ("2 Corinthians", 5), ("Galatians", 5), ("Ephesians", 2),
    ("Philippians", 4), ("Colossians", 3), ("1 Thessalonians", 4), ("2 Thessalonians", 2), ("1 Timothy", 6),
    ("2 Timothy", 4), ("Titus", 2), ("Philemon", 1), ("Hebrews", 11), ("James", 2),
    ("1 Peter", 3), ("2 Peter", 1), ("1 John", 4), ("2 John", 1), ("3 John", 1),
    ("Jude", 1), ("Revelation", 21), ("Matthew", 28), ("John", 3), ("Luke", 24),
    ("Mark", 16), ("Acts", 9), ("Romans", 5), ("1 Corinthians", 15), ("2 Corinthians", 12), ("Galatians", 2),
    ("Ephesians", 6), ("Philippians", 2), ("Colossians", 1), ("1 Thessalonians", 5), ("2 Thessalonians", 3),
    ("1 Timothy", 3), ("2 Timothy", 2), ("Titus", 1), ("Hebrews", 4), ("James", 1),
    ("1 Peter", 1), ("2 Peter", 3), ("1 John", 1), ("Revelation", 1), ("Revelation", 22),
    ("Isaiah", 9), ("Genesis", 22), ("Exodus", 3), ("Psalms", 51), ("Proverbs", 8)
]

@pytest.mark.parametrize("book,chapter", QUERIES)
def test_commentary_api(book, chapter):
    resp = requests.get(BASE_URL, params={"book": book, "chapter": chapter})
    assert resp.status_code == 200
    # Accept 0+ results, but print for manual review
    data = resp.json()
    print(f"{book} {chapter}: {len(data)} results")
    if data:
        print(f"First result title: {data[0].get('title')}")
