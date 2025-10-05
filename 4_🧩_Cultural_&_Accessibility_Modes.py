import streamlit as st

st.title("🧩 Cultural & Accessibility Modes")

st.subheader("Accessibility")
theme = st.selectbox("Theme", ["System", "High Contrast", "Large Text"])
motion = st.checkbox("Reduce Motion / Animations", value=False)
dyslexic = st.checkbox("Dyslexia-Friendly Fonts", value=False)

st.subheader("Cultural Modes")
locale = st.selectbox("Preferred Locale", ["en-US", "es-ES", "fr-FR", "zh-CN"])
units = st.selectbox("Units", ["US (lb/in, °F)", "Metric (kg/cm, °C)"])
dietary = st.multiselect("Dietary Preferences", ["Halal", "Kosher", "Vegetarian", "Vegan", "Gluten-free"])

st.success("Your preferences are applied for this session. Persist to a profile store when ready.")
