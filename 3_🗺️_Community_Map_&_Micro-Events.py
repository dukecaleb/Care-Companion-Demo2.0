import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parents[1] / "data"

st.title("🗺️ Community Map & Micro-Events")

events = pd.read_csv(DATA_DIR / "events.csv")
st.write("Upcoming Micro-Events")
st.dataframe(events, use_container_width=True)

st.info("This starter uses a simple table view for portability. You can integrate maps (e.g., streamlit-folium) later.")
