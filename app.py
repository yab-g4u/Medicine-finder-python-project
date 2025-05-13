import streamlit as st
import sys
from Src import Main, Search, Tracker, Remainder

sys.path.append('./Src')

# Page navigation using a sidebar
st.sidebar.title("Medicine Assistant App")
page = st.sidebar.radio("Choose a page:", ["Home", "Search Medicine", "Set Reminder", "Track Usage"])

if page == "Home":
    Main.home()
elif page == "Search Medicine":
    Search.search_medicine()
elif page == "Set Reminder":
    Remainder.set_reminder()
elif page == "Track Usage":
    Tracker.track_usage()
