"""
Basic scripture reference parser for recognizing and normalizing references like 'Lev 6', 'Leviticus 6:1-7', etc.
"""
import re
from typing import Optional
from .models import ScriptureReference


# List of all canonical Bible books and common abbreviations
CANONICAL_BOOKS = {
    # Old Testament
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Tobit", "Judith", "Esther", "1 Maccabees", "2 Maccabees", "Job", "Psalms", "Proverbs", "Ecclesiastes", "Song of Songs", "Wisdom", "Sirach", "Isaiah", "Jeremiah", "Lamentations", "Baruch", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi",
    # New Testament
    "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"
}

# Expanded aliases for matching
BOOK_ALIASES = {
    "Gen": "Genesis", "Ex": "Exodus", "Lev": "Leviticus", "Leviticus": "Leviticus", "Num": "Numbers", "Deut": "Deuteronomy", "Josh": "Joshua", "Jdg": "Judges", "Judg": "Judges", "Ruth": "Ruth", "1Sam": "1 Samuel", "2Sam": "2 Samuel", "1Kgs": "1 Kings", "2Kgs": "2 Kings", "1Chr": "1 Chronicles", "2Chr": "2 Chronicles", "Ezra": "Ezra", "Neh": "Nehemiah", "Tob": "Tobit", "Jdt": "Judith", "Esth": "Esther", "1Mac": "1 Maccabees", "2Mac": "2 Maccabees", "Job": "Job", "Ps": "Psalms", "Prov": "Proverbs", "Eccl": "Ecclesiastes", "Song": "Song of Songs", "Wis": "Wisdom", "Sir": "Sirach", "Isa": "Isaiah", "Jer": "Jeremiah", "Lam": "Lamentations", "Bar": "Baruch", "Ezek": "Ezekiel", "Dan": "Daniel", "Hos": "Hosea", "Joel": "Joel", "Amos": "Amos", "Obad": "Obadiah", "Jon": "Jonah", "Mic": "Micah", "Nah": "Nahum", "Hab": "Habakkuk", "Zeph": "Zephaniah", "Hag": "Haggai", "Zech": "Zechariah", "Mal": "Malachi", "Mt": "Matthew", "Matt": "Matthew", "Mk": "Mark", "Lk": "Luke", "Jn": "John", "Acts": "Acts", "Rom": "Romans", "1Cor": "1 Corinthians", "2Cor": "2 Corinthians", "Gal": "Galatians", "Eph": "Ephesians", "Phil": "Philippians", "Col": "Colossians", "1Thess": "1 Thessalonians", "2Thess": "2 Thessalonians", "1Tim": "1 Timothy", "2Tim": "2 Timothy", "Tit": "Titus", "Phlm": "Philemon", "Heb": "Hebrews", "Jas": "James", "1Pet": "1 Peter", "2Pet": "2 Peter", "1Jn": "1 John", "2Jn": "2 John", "3Jn": "3 John", "Jude": "Jude", "Rev": "Revelation"
}

# Improved regex: match only valid book names/abbreviations
BOOK_PATTERN = r"(?:" + "|".join(sorted(BOOK_ALIASES.keys(), key=lambda x: -len(x))) + r"|" + "|".join(sorted(CANONICAL_BOOKS, key=lambda x: -len(x))) + r")"
SCRIPTURE_REF_REGEX = re.compile(rf"({BOOK_PATTERN})\s*(\d+)(?::(\d+)(?:-(\d+))?)?", re.IGNORECASE)

def parse_scripture_reference(ref: str) -> Optional[ScriptureReference]:
    match = SCRIPTURE_REF_REGEX.match(ref)
    if not match:
        return None
    book, chapter, verse_start, verse_end = match.groups()
    book = BOOK_ALIASES.get(book, book)
    # Only accept canonical books
    if book not in CANONICAL_BOOKS:
        return None
    chapter = int(chapter)
    verse_start = int(verse_start) if verse_start else None
    verse_end = int(verse_end) if verse_end else None
    return ScriptureReference(book=book, chapter=chapter, verse_start=verse_start, verse_end=verse_end)
