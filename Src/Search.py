import json

def search_medicine(query):
    with open("data/pharmacy_data.json", "r") as f:
        data = json.load(f)
    matches = [m for m in data if query.lower() in m['name'].lower()]
    return matches

