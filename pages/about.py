import streamlit as st

from components.header import render_header
from components.recommendations import DISCLAIMER


def render() -> None:
    render_header()
    st.title("About Pulse Metrics")
    st.markdown("### A clearer way to understand medical reports")
    st.write("Pulse Metrics helps turn report language into structured, plain-language information. It highlights the values and reference ranges that appear in a document so you can have more informed conversations with a healthcare professional.")
    columns = st.columns(2)
    with columns[0]:
        st.markdown('<div class="pm-card"><h3>How it works</h3><p>Upload a supported report, let the document service read it, and Gemini returns a validated structured summary. The app does not invent missing patient information or test values.</p></div>', unsafe_allow_html=True)
    with columns[1]:
        st.markdown('<div class="pm-card"><h3>Technology</h3><p>Python · Streamlit · Google GenAI · PyMuPDF · Pillow · SQLite · Pandas</p></div>', unsafe_allow_html=True)
    st.subheader("Privacy approach")
    st.write("API credentials are loaded from environment variables. Original uploaded files are processed in memory and are not stored by the history service. The local database stores summaries for history views.")
    st.markdown(f'<div class="pm-disclaimer">❤️ {DISCLAIMER}</div>', unsafe_allow_html=True)
