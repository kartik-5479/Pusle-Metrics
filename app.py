import streamlit as st

from components.sidebar import render_sidebar
from pages import about, analysis_history, health_insights, home, tips_guides, upload_report
from services.history_service import initialize_database
from utils.styling import apply_styles


st.set_page_config(
    page_title="Pulse Metrics",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "page" not in st.session_state:
    st.session_state.page = "Home"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

apply_styles(st.session_state.dark_mode)
try:
    initialize_database()
except Exception:
    st.warning("History storage is unavailable right now. The dashboard can still be used.")

page = render_sidebar()
page_renderers = {
    "Home": home.render,
    "Upload Report": upload_report.render,
    "Analysis History": analysis_history.render,
    "Health Insights": health_insights.render,
    "Tips & Guides": tips_guides.render,
    "About": about.render,
}
page_renderers.get(page, home.render)()