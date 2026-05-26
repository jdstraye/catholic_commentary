"""
List of authoritative Catholic commentary sources for ingestion.
"""

COMMENTARY_SOURCES = [
    {
        "name": "Vatican Encyclicals",
        "type": "encyclical",
        "url": "https://www.vatican.va/",
        "notes": "Official Vatican archive of papal documents."
    },
    {
        "name": "New Advent Church Fathers",
        "type": "church_father",
        "url": "https://www.newadvent.org/fathers/",
        "notes": "English translations of Church Fathers' writings."
    },
    {
        "name": "Catechism of the Catholic Church",
        "type": "catechism",
        "url": "https://www.vatican.va/archive/ENG0015/_INDEX.HTM",
        "notes": "Full text of the Catechism."
    },
    {
        "name": "Homilies of the Popes",
        "type": "homily",
        "url": "https://www.vatican.va/content/vatican/en.html",
        "notes": "Recent papal homilies."
    },
    {
        "name": "Saints' Reflections",
        "type": "saint",
        "url": "https://www.catholic.org/saints/",
        "notes": "Biographies and writings of saints."
    }
]
