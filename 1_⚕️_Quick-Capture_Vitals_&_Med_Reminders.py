import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

DATA_DIR = Path(__file__).parents[1] / "data"

st.title("⚕️ Quick-Capture Vitals & Med Reminders")

# Vitals quick capture
st.subheader("Quick-Capture Vitals")
with st.form("vitals_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        ts = st.datetime_input("Timestamp", value=datetime.now())
        hr = st.number_input("Heart Rate (bpm)", 30, 220, 72)
        bp_sys = st.number_input("Systolic (mmHg)", 70, 240, 118)
    with col2:
        bp_dia = st.number_input("Diastolic (mmHg)", 40, 160, 76)
        spo2 = st.number_input("SpO₂ (%)", 50.0, 100.0, 98.0, step=0.1)
        temp = st.number_input("Temperature (°F)", 90.0, 110.0, 98.6, step=0.1)
    with col3:
        weight = st.number_input("Weight (lb)", 50.0, 600.0, 170.0, step=0.1)
        note = st.text_input("Note", "")
    submitted = st.form_submit_button("Save Vitals")
    if submitted:
        df = pd.read_csv(DATA_DIR / "vitals.csv")
        df.loc[len(df)] = [ts.isoformat(), hr, bp_sys, bp_dia, spo2, temp, weight, note]
        df.to_csv(DATA_DIR / "vitals.csv", index=False)
        st.success("Vitals saved.")

st.divider()

# Med reminders
st.subheader("Medication Reminders")
meds = pd.read_csv(DATA_DIR / "medications.csv")
st.dataframe(meds, use_container_width=True)

with st.form("add_med"):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        med = st.text_input("Medication")
    with c2:
        dose = st.text_input("Dose")
    with c3:
        schedule = st.selectbox("Schedule", ["daily", "BID", "TID", "weekly", "PRN"])
    with c4:
        next_time = st.datetime_input("Next Dose", value=datetime.now() + timedelta(hours=4))
    add = st.form_submit_button("Add / Update")
    if add and med:
        meds.loc[len(meds)] = [med, dose, schedule, next_time.isoformat(), "scheduled"]
        meds.to_csv(DATA_DIR / "medications.csv", index=False)
        st.success("Medication added/updated.")        
