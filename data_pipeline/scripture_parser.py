"""
Basic scripture reference parser for recognizing and normalizing references like 'Lev 6', 'Leviticus 6:1-7', etc.
"""
import re
from typing import Optional
from .models import ScriptureReference

BOOK_ALIASES = {
    "Lev": "Leviticus",
    "Leviticus": "Leviticus",
    # Add more aliases as needed
}

SCRIPTURE_REF_REGEX = re.compile(r"([A-Za-z]+)\s*(\d+)(?::(\d+)(?:-(\d+))?)?")

def parse_scripture_reference(ref: str) -> Optional[ScriptureReference]:
    match = SCRIPTURE_REF_REGEX.match(ref)
    if not match:
        return None
    book, chapter, verse_start, verse_end = match.groups()
    book = BOOK_ALIASES.get(book, book)
    chapter = int(chapter)
    verse_start = int(verse_start) if verse_start else None
    verse_end = int(verse_end) if verse_end else None
    return ScriptureReference(book=book, chapter=chapter, verse_start=verse_start, verse_end=verse_end)
