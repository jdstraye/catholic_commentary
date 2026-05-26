"""
Scripture reference mapping utility.
Given a block of text, extract all scripture references and return normalized references.
"""
import re
from typing import List
from .scripture_parser import parse_scripture_reference, SCRIPTURE_REF_REGEX

def extract_scripture_references(text: str) -> List[str]:
    """Find all scripture reference strings in the text."""
    return [m.group(0) for m in SCRIPTURE_REF_REGEX.finditer(text)]

def map_scripture_references(text: str):
    """Return all normalized ScriptureReference objects found in the text."""
    refs = extract_scripture_references(text)
    return [parse_scripture_reference(ref) for ref in refs if parse_scripture_reference(ref)]

if __name__ == "__main__":
    sample = "See Lev 6 and Leviticus 6:1-7. Compare with John 3:16."
    print("Extracted references:", extract_scripture_references(sample))
    print("Mapped references:", map_scripture_references(sample))
