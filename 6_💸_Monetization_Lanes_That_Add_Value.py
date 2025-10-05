import streamlit as st
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parents[1] / "data"

st.title("💸 Monetization Lanes That Add Value")

plans = pd.read_csv(DATA_DIR / "monetization.csv")
st.write("Plans & Value")
st.dataframe(plans, use_container_width=True)

st.caption("Keep user-first: emphasize value, transparency, and optionality.")
