
import streamlit as st
from datetime import datetime
from utils.core import load_prescriptions, save_prescriptions
from utils.search import search_medicine
from utils.reminder import check_reminders

st.set_page_config(page_title="Smart Medicine App", layout="centered")
st.title("💊 Smart Medicine Finder")
st.sidebar.image("C:/Users/yeabkab/Downloads/Telegram Desktop/Smart_Medicine_App (2)/streamlit/assets/background.jpg", use_container_width=True)
page = st.sidebar.radio("Navigate", ["Home", "Search Medicine", "Add Prescription", "Reminders"])

if page == "Home":
    st.header("Welcome to Smart Medicine App")
    st.markdown("Use the sidebar to navigate the app.")

elif page == "Search Medicine":
    st.header("Search for Medicines")
    query = st.text_input("Enter medicine name:")
    if st.button("Search"):
        with st.spinner("Searching nearby pharmacies..."):
            matches = search_medicine(query)
            if matches:
                st.success("Medicine found!")
                for m in matches:
                    availability = "Available" if m['availability'] else "Unavailable"
                    st.write(f"**{m['name']}** - ${m['price']} — {availability}")
            else:
                st.warning("No matches found. Try another name.")

elif page == "Add Prescription":
    st.header("Add Your Prescription")
    name = st.text_input("Medicine Name")
    dosage = st.text_input("Dosage")
    time = st.time_input("Reminder Time", datetime.now().time())
    if st.button("Save Prescription"):
        new_entry = {"name": name, "dosage": dosage, "time": time.strftime("%H:%M")}
        prescriptions = load_prescriptions()
        prescriptions.append(new_entry)
        save_prescriptions(prescriptions)
        st.success("Prescription saved!")

elif page == "Reminders":
    st.header("Today's Reminders")
    reminders = check_reminders()
    if reminders:
        for r in reminders:
            st.write(f"Take **{r['name']}** ({r['dosage']}) at **{r['time']}**")
    else:
        st.info("No reminders for now.")
