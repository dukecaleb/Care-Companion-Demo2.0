import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

DATA_DIR = Path(__file__).parents[1] / "data"

st.title("🧪 N-of-1 Self-Experiments")

exps = pd.read_csv(DATA_DIR / "experiments.csv")
st.write("Active & Planned Experiments")
st.dataframe(exps, use_container_width=True)

st.subheader("Create / Update Experiment")
with st.form("exp_form"):
    c1, c2, c3 = st.columns(3)
    with c1:
        name = st.text_input("Experiment Name", "Caffeine → Sleep Quality")
    with c2:
        start = st.date_input("Start", datetime.now().date())
    with c3:
        duration = st.number_input("Duration (days)", 1, 120, 14)
    c4, c5, c6 = st.columns(3)
    with c4:
        variable = st.text_input("Independent Variable", "Caffeine mg/day")
    with c5:
        outcome = st.text_input("Outcome", "Sleep score (1-10)")
    with c6:
        design = st.selectbox("Design", ["ABAB", "ABA", "Randomized Crossover", "A/B"])
    submit = st.form_submit_button("Save Experiment")
    if submit and name:
        exps.loc[len(exps)] = [name, str(start), int(duration), variable, outcome, design, "planned"]
        exps.to_csv(DATA_DIR / "experiments.csv", index=False)
        st.success("Experiment saved.")
