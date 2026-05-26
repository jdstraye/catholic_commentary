"""
Test API for 5 different scripture references likely to be found in Church Fathers' works.
"""
import requests

BASE_URL = "http://127.0.0.1:8000/commentary/"

queries = [
    {"book": "Matthew", "chapter": 5},
    {"book": "John", "chapter": 1},
    {"book": "Romans", "chapter": 8},
    {"book": "Psalms", "chapter": 23},
    {"book": "Genesis", "chapter": 1}
]

for params in queries:
    print(f"Query: {params}")
    resp = requests.get(BASE_URL, params=params)
    print(f"Status: {resp.status_code}")
    try:
        data = resp.json()
        print(f"Results: {len(data)}")
        if data:
            print(f"First result title: {data[0].get('title')}")
    except Exception as e:
        print(f"Error: {e}")
    print("-"*40)
