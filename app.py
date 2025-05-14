
import streamlit as st
import json
import os
from datetime import datetime, timedelta

DATA_DIR = "data"
PRESCRIPTIONS_PATH = os.path.join(DATA_DIR, "prescription.json")
PHARMACY_PATH = os.path.join(DATA_DIR, "pharmacy_data.json")

st.set_page_config(page_title="Smart Medicine Finder", layout="wide")

def load_prescriptions():
    with open(PRESCRIPTIONS_PATH, "r") as f:
        return json.load(f)

def save_prescription(entry):
    data = load_prescriptions()
    data.append(entry)
    with open(PRESCRIPTIONS_PATH, "w") as f:
        json.dump(data, f, indent=2)

def load_pharmacy_data():
    with open(PHARMACY_PATH, "r") as f:
        return json.load(f)

def add_background():
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("assets/background.jpg");
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

def navbar():
    selected = st.sidebar.radio("Navigation", ["Home", "Add Prescription", "Reminders", "Pharmacy Search"])
    return selected

def home():
    st.title("Smart Medicine Finder")
    st.write("Track your prescriptions and find medicines easily.")

def add_prescription():
    st.header("Add Prescription")
    name = st.text_input("Medicine Name")
    dosage = st.text_input("Dosage (e.g., 500mg)")
    time = st.time_input("Time to take medicine", datetime.now().time())

    if st.button("Save Prescription"):
        save_prescription({"name": name, "dosage": dosage, "time": str(time)})
        st.success("Prescription saved!")

def reminders():
    st.header("Medicine Reminders")
    data = load_prescriptions()
    now = datetime.now().time()
    for entry in data:
        med_time = datetime.strptime(entry["time"], "%H:%M:%S").time()
        status = "Upcoming" if med_time > now else "Missed or Taken"
        st.write(f"**{entry['name']}** ({entry['dosage']}) - {entry['time']} — *{status}*")

def pharmacy_search():
    st.header("Pharmacy Search")
    data = load_pharmacy_data()
    med_name = st.text_input("Enter medicine name")
    if med_name:
        matches = [m for m in data if med_name.lower() in m["name"].lower()]
        if matches:
            for match in matches:
                st.write(f"{match['name']}: ${match['price']} — {'Available' if match['availability'] else 'Unavailable'}")
        else:
            st.info("Searching nearby pharmacies... (simulation)")
            st.warning("No matches found. Try again later.")

add_background()
page = navbar()
if page == "Home":
    home()
elif page == "Add Prescription":
    add_prescription()
elif page == "Reminders":
    reminders()
elif page == "Pharmacy Search":
    pharmacy_search()
