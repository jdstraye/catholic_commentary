"""
Basic data ingestion script for Catholic commentary sources.
For now, this script will only print the sources and demonstrate scripture parsing.
"""
from .sources import COMMENTARY_SOURCES
from .scripture_parser import parse_scripture_reference

if __name__ == "__main__":
    print("Catholic Commentary Data Ingestion Demo\n")
    print("Sources:")
    for src in COMMENTARY_SOURCES:
        print(f"- {src['name']} ({src['type']}): {src['url']}")
    
    # Demo scripture parsing
    refs = ["Lev 6", "Leviticus 6:1-7", "John 3:16"]
    print("\nScripture Reference Parsing Demo:")
    for ref in refs:
        parsed = parse_scripture_reference(ref)
        print(f"{ref} -> {parsed}")
