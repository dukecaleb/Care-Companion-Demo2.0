import streamlit as st
from datetime import date, datetime, timedelta
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Care Companion 2.0", page_icon="💚", layout="wide")

DATA_DIR = Path(__file__).parent / "data"

def load_csv(name):
    p = DATA_DIR / name
    if p.exists():
        return pd.read_csv(p)
    return pd.DataFrame()

st.sidebar.title("Care Companion 2.0")
st.sidebar.success("Pick a feature page ➡️")

st.title("💚 Care Companion 2.0")
st.caption("HealthUniverse-ready Streamlit app")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Active Users", 128)
with col2:
    st.metric("Experiments Running", 17)
with col3:
    st.metric("Check-ins Today", 64)

st.markdown("---")
st.subheader("Quick Start")
st.write("Use the pages on the left to capture vitals, manage medications, set up N-of-1 experiments, find micro-events nearby, switch accessibility & cultural modes, browse trusted resources, and explore monetization options that add value.")
st.markdown("> **Note**: This starter uses CSV templates for simplicity. You can later swap to a database and add authentication/secrets via Health Universe.")

# Lightweight demo dashboard
vitals = load_csv("vitals.csv")
meds = load_csv("medications.csv")
events = load_csv("events.csv")

c1, c2 = st.columns(2)
with c1:
    st.write("### Recent Vitals")
    st.dataframe(vitals.tail(10), use_container_width=True)
with c2:
    st.write("### Upcoming Meds")
    st.dataframe(meds[meds['status'].isin(['scheduled','pending'])].head(10) if not meds.empty else meds, use_container_width=True)

st.write("### Nearby Micro-Events (demo)")
st.dataframe(events.head(10), use_container_width=True)
