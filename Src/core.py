
import json
import os

PRESCRIPTIONS_FILE = 'data/prescription.json'

def load_prescriptions():
    if not os.path.exists(PRESCRIPTIONS_FILE):
        return []
    with open(PRESCRIPTIONS_FILE, 'r') as file:
        return json.load(file)

def save_prescriptions(data):
    with open(PRESCRIPTIONS_FILE, 'w') as file:
        json.dump(data, file, indent=4)
