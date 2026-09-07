from pathlib import Path
from typing import Optional

import streamlit as st

from services.document_service import DocumentProcessingError, process_document
from services.gemini_service import GeminiAnalysisError, GeminiConfigurationError, analyze_report
from services.history_service import save_analysis
from utils.validators import validate_upload


def render_upload_section() -> Optional[dict]:
    """Render upload flow and return a newly completed analysis, if any."""
    st.markdown("## Upload Your Medical Report")
    st.caption("Drag and drop your report here or browse files. Supported formats: PDF, JPG, PNG (Max 10 MB).")
    uploaded_file = st.file_uploader(
        "Choose a medical report",
        type=["pdf", "jpg", "jpeg", "png"],
        label_visibility="collapsed",
        key="report_uploader",
    )
    if uploaded_file is None:
        return None

    validation_error = validate_upload(uploaded_file)
    if validation_error:
        st.error(validation_error)
        return None

    report_signature = f"{uploaded_file.name}:{uploaded_file.size}"
    if st.session_state.get("processed_signature") == report_signature:
        return st.session_state.get("analysis")

    if not st.button("Analyze Report", type="primary", use_container_width=True):
        st.info(f"Ready to analyze **{uploaded_file.name}**.")
        return None

    try:
        with st.spinner("Reading your medical report..."):
            document = process_document(uploaded_file.name, uploaded_file.getvalue())
        with st.spinner("AI is analyzing your report..."):
            analysis = analyze_report(document)
        with st.spinner("Preparing your health insights..."):
            save_analysis(uploaded_file.name, analysis)
        st.session_state.analysis = analysis
        st.session_state.report_name = uploaded_file.name
        st.session_state.processed_signature = report_signature
        st.success("Your report was analyzed successfully.")
        return analysis
    except (DocumentProcessingError, GeminiConfigurationError, GeminiAnalysisError) as exc:
        st.error(str(exc))
    except Exception:
        st.error("Something went wrong while processing the report. Please try again.")
    return None
