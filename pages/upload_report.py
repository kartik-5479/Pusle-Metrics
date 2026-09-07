import streamlit as st

from components.header import render_header
from components.upload_section import render_upload_section


def render() -> None:
    render_header()
    st.title("Upload Report")
    st.markdown("Upload a PDF or image report to extract and explain the information it contains.")
    render_upload_section()
    if st.session_state.get("analysis"):
        st.success("Analysis available. Open Home to review the summary.")
