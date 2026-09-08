import hashlib
from typing import Optional

import streamlit as st

from services.document_service import DocumentProcessingError, process_document
from services.gemini_service import GeminiAnalysisError, GeminiConfigurationError, analyze_report
from utils.validators import validate_upload


def render_upload_section() -> Optional[dict]:
    """Render upload flow and return a newly completed analysis, if any."""
    st.markdown("<div class=\"pm-upload-heading\"><h2>Upload Your Medical Report</h2><p>PDF, JPG, JPEG, or PNG · maximum 10 MB</p></div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose a medical report",
        type=["pdf", "jpg", "jpeg", "png"],
        label_visibility="collapsed",
        key="report_uploader",
    )
    if uploaded_file is None:
        st.markdown('<div class="pm-upload-empty"><div class="pm-upload-icon">↑</div><strong>Drop your report here</strong><span>or choose a file above to get started</span></div>', unsafe_allow_html=True)
        return None

    validation_error = validate_upload(uploaded_file)
    if validation_error:
        st.error(validation_error)
        return None

    file_bytes = uploaded_file.getvalue()
    report_signature = hashlib.sha256(file_bytes).hexdigest()
    if st.session_state.get("processed_signature") == report_signature:
        return st.session_state.get("analysis")

    st.markdown(
        f'<div class="pm-upload-meta"><strong>{uploaded_file.name}</strong>'
        f'<span>{uploaded_file.size / 1024:.1f} KB · {uploaded_file.type or "Unknown type"}</span>'
        "</div>",
        unsafe_allow_html=True,
    )
    if not st.button("Analyze Report", type="primary", use_container_width=True):
        st.info(f"Ready to analyze **{uploaded_file.name}**.")
        return None

    try:
        with st.spinner("Reading your medical report..."):
            document = process_document(uploaded_file.name, file_bytes)
        with st.spinner("AI is analyzing your report..."):
            analysis = analyze_report(document)
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
