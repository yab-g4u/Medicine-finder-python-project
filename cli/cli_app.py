import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils.core import load_prescriptions, save_prescriptions
from utils.reminder import check_reminders

def add_prescription():
    name = input("Enter medicine name: ")
    dosage = input("Enter dosage (e.g., 1 tablet): ")
    time = input("Enter time (HH:MM, e.g., 08:00): ")

    prescriptions = load_prescriptions()
    prescriptions.append({"name": name, "dosage": dosage, "time": time})
    save_prescriptions(prescriptions)
    print(f"[✔️] Prescription for {name} added.")

def view_prescriptions():
    prescriptions = load_prescriptions()
    if not prescriptions:
        print("[!] No prescriptions found.")
        return
    for idx, p in enumerate(prescriptions, 1):
        print(f"{idx}. {p['name']} — {p['dosage']} at {p['time']}")

def view_reminders():
    reminders = check_reminders()
    if not reminders:
        print("[!] No reminders right now.")
        return
    for r in reminders:
        print(f"Reminder: Take {r['name']} — {r['dosage']} at {r['time']}")

def cli():
    while True:
        print("\n==== Smart Medicine CLI ====")
        print("1. Add Prescription")
        print("2. View Prescriptions")
        print("3. Check Reminders")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_prescription()
        elif choice == '2':
            view_prescriptions()
        elif choice == '3':
            view_reminders()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("[!] Invalid option. Try again.")

if __name__ == "__main__":
    cli()
