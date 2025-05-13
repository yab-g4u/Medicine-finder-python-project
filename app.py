import streamlit as st
import json
import os
from datetime import datetime

def load_prescriptions():
    if not os.path.exists("prescriptions.json"):
        return []
    with open("prescriptions.json", "r") as f:
        return json.load(f)

def save_prescriptions(data):
    with open("prescriptions.json", "w") as f:
        json.dump(data, f, indent=4)

def load_pharmacy_data():
    if not os.path.exists("pharmacy_data.json"):
        return []
    with open("pharmacy_data.json", "r") as f:
        return json.load(f)

st.title("Smart Medicine Finder")

menu = st.sidebar.selectbox("Menu", ["Add Prescription", "View Prescriptions", "Search Medicine"])

if menu == "Add Prescription":
    st.header("Add a new prescription")
    name = st.text_input("Medicine Name")
    dosage = st.text_input("Dosage")
    time_ = st.time_input("Reminder Time")

    if st.button("Save Prescription"):
        data = load_prescriptions()
        data.append({
            "name": name,
            "dosage": dosage,
            "time": time_.strftime("%H:%M")
        })
        save_prescriptions(data)
        st.success("Prescription saved!")

elif menu == "View Prescriptions":
    st.header("Your Prescriptions")
    data = load_prescriptions()
    if not data:
        st.info("No prescriptions found.")
    else:
        for p in data:
            st.write(f"- **{p['name']}** | {p['dosage']} at {p['time']}")
        now = datetime.now().strftime("%H:%M")
        st.subheader("Reminders for now:")
        for p in data:
            if p["time"] == now:
                st.warning(f"Reminder: Take {p['name']} - {p['dosage']}")

elif menu == "Search Medicine":
    st.header("Search for Medicine Availability")
    query = st.text_input("Enter medicine name to search")
    if st.button("Search"):
        meds = load_pharmacy_data()
        found = False
        for med in meds:
            if med["name"].lower() == query.lower():
                st.success(f"{med['name']} is available at {med['pharmacy']} for ${med['price']}")
                found = True
        if not found:
            st.error("Medicine not found in database.")
