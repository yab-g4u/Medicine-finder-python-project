
import streamlit as st
from utils.core import load_prescriptions, save_prescriptions, load_pharmacy_data, check_reminders
from datetime import datetime

st.set_page_config(page_title="Smart Medicine Finder", layout="wide")
st.sidebar.image("assets/background.jpg", use_column_width=True)
st.title("💊 Smart Medicine Finder & Reminder App")

menu = st.sidebar.radio("Navigate", ["Home", "Search Medicine", "Add Prescription", "Reminders"])

if menu == "Home":
    st.markdown("### Welcome to the Smart Medicine App")
    st.write("Manage your prescriptions, receive timely reminders, and search for available medicines near you.")

elif menu == "Search Medicine":
    st.header("Search for Medicines")
    med = st.text_input("Enter medicine name")
    if med:
        st.info("Simulating search...")
        matches = [m for m in load_pharmacy_data() if med.lower() in m["name"].lower()]
        if matches:
            for m in matches:
                st.success(f"{m['name']} - ${m['price']} at {m['pharmacy']} - {'Available' if m['availability'] else 'Unavailable'}")
        else:
            st.warning("Medicine not found or currently unavailable.")

elif menu == "Add Prescription":
    st.header("Add a New Prescription")
    name = st.text_input("Medicine Name")
    dosage = st.text_input("Dosage")
    time = st.time_input("Reminder Time", datetime.now().time())

    if st.button("Save"):
        entry = {"name": name, "dosage": dosage, "time": time.strftime("%H:%M")}
        data = load_prescriptions()
        data.append(entry)
        save_prescriptions(data)
        st.success("Prescription saved!")

elif menu == "Reminders":
    st.header("Today's Reminders")
    data = check_reminders()
    if data:
        for d in data:
            st.write(f"Take **{d['name']}** ({d['dosage']}) at **{d['time']}**")
    else:
        st.info("No reminders at the moment.")
