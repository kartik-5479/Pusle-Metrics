import streamlit as st

from components.header import render_header
from components.upload_section import render_upload_section


def render() -> None:
    render_header()
    st.markdown(
        """<div class="pm-page-intro">
        <div class="pm-eyebrow">REPORT WORKSPACE</div>
        <h1>Turn your report into clarity.</h1>
        <p>Upload a medical report and let Pulse Metrics organize the information into simple, useful insights.</p>
        </div>""",
        unsafe_allow_html=True,
    )
    feature_columns = st.columns(3)
    features = [
        ("01", "Upload securely", "Your file is processed in memory."),
        ("02", "Let AI read it", "Gemini extracts the reported values."),
        ("03", "Understand clearly", "Review simple explanations and statuses."),
    ]
    for column, (number, title, detail) in zip(feature_columns, features):
        with column:
            st.markdown(
                f'<div class="pm-flow-card"><span>{number}</span><strong>{title}</strong><p>{detail}</p></div>',
                unsafe_allow_html=True,
            )
    st.markdown('<div class="pm-upload-panel">', unsafe_allow_html=True)
    render_upload_section()
    st.markdown('</div>', unsafe_allow_html=True)
    if st.session_state.get("analysis"):
        st.markdown(
            '<div class="pm-complete-card"><strong>Analysis ready</strong>'
            '<span>Your latest report has been analyzed. Open Home to review the summary and insights.</span></div>',
            unsafe_allow_html=True,
        )
