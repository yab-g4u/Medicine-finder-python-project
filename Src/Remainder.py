import json
import datetime

def check_reminders():
    now = datetime.datetime.now().strftime("%H:%M")
    with open("data/prescription.json", "r") as f:
        prescriptions = json.load(f)
    return [p for p in prescriptions if p['time'] == now]
