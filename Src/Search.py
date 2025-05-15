
import json
import os

PHARMACY_FILE = 'data/pharmacy.json'

def search_medicine(query):
    if not os.path.exists(PHARMACY_FILE):
        return []
    with open(PHARMACY_FILE, 'r') as f:
        data = json.load(f)
        return [item for item in data if query.lower() in item['name'].lower()]
