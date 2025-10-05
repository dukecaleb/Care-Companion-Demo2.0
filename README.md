# Care Companion 2.0 (Health Universe Ready)

This repository contains a Streamlit app implementing the Care Companion 2.0 features:
- Quick-Capture Vitals & Med Reminders
- "N-of-1" Self-Experiments
- Community Map & Micro-Events
- Cultural & Accessibility Modes
- Trusted Resource Concierge
- Monetization Lanes That Add Value

## How to Deploy on Health Universe
Health Universe deploys apps from **GitHub**. The recommended path:
1. Create a **new GitHub repository** and upload this project (keep the folder structure intact).
2. On Health Universe, go to **Create** and choose **Select GitHub Repository**.
3. Choose **Runtime: Streamlit** and set **main file** to `streamlit_app.py`.
4. (Optional) Configure **Secrets** for any API keys you add later.
5. Click **Deploy App** and watch the logs until complete.

> Tip: After you push updates to GitHub, use **Re-deploy** in Health Universe to refresh your app.

## Local Development
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Data
CSV templates are provided in `/data`. You can replace these with your own data or connect to a database.
