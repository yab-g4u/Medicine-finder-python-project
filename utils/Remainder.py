
from datetime import datetime
from utils.core import load_prescriptions

def check_reminders():
    prescriptions = load_prescriptions()
    now = datetime.now().time()
    due = []
    for entry in prescriptions:
        try:
            entry_time = datetime.strptime(entry['time'], "%H:%M").time()
            if now >= entry_time:
                due.append(entry)
        except Exception:
            continue
    return due
