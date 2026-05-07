import streamlit as st
import requests

st.title("Smart EV Charging Dashboard")

response = requests.get("http://127.0.0.1:5000/stations")

stations = response.json()

for station in stations:
    st.subheader(station["name"])
    st.write("Location:", station["location"])
    st.write("Available Chargers:", station["available_chargers"])