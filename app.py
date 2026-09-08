import streamlit as st

from components.sidebar import render_sidebar
from pages import about, detailed_analysis, home, tips_guides, upload_report
from utils.styling import apply_styles


st.set_page_config(
    page_title="Pulse Metrics",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "page" not in st.session_state:
    st.session_state.page = "Home"
apply_styles()

page = render_sidebar()
page_renderers = {
    "Home": home.render,
    "Upload Report": upload_report.render,
    "Tips & Guides": tips_guides.render,
    "About": about.render,
}
if page == "Detailed Analysis":
    analysis = st.session_state.get("analysis", home.SAMPLE_ANALYSIS)
    detailed_analysis.render(analysis, sample="analysis" not in st.session_state)
else:
    page_renderers.get(page, home.render)()