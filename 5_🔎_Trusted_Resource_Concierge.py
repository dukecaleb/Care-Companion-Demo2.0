import streamlit as st
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parents[1] / "data"

st.title("🔎 Trusted Resource Concierge")

resources = pd.read_csv(DATA_DIR / "resources.csv")
st.write("Recommended Resources")
st.dataframe(resources, use_container_width=True)

query = st.text_input("Search keywords")
if query:
    mask = resources.apply(lambda row: query.lower() in row.to_string().lower(), axis=1)
    st.write("Search Results")
    st.dataframe(resources[mask], use_container_width=True)
