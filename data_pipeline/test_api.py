"""
Basic test script for the commentary API.
"""
import requests

BASE_URL = "http://127.0.0.1:8000/commentary/"

params = {
    "book": "Leviticus",
    "chapter": 6
}

resp = requests.get(BASE_URL, params=params)
print(f"Status: {resp.status_code}")
print("Response:")
print(resp.json())
