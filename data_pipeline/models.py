"""
Data model definitions for Catholic Commentary Data Pipeline
"""
from enum import Enum
from typing import List, Optional
from dataclasses import dataclass

class CommentaryType(Enum):
    ENCYCLICAL = "encyclical"
    HOMILY = "homily"
    SAINT = "saint"
    CHURCH_FATHER = "church_father"
    CATECHISM = "catechism"
    OTHER = "other"

@dataclass
class ScriptureReference:
    book: str
    chapter: int
    verse_start: Optional[int] = None
    verse_end: Optional[int] = None

@dataclass
class Commentary:
    id: str
    type: CommentaryType
    author: str
    title: str
    date: Optional[str]
    source_url: Optional[str]
    scripture_refs: List[ScriptureReference]
    text: str
