from html import escape
from typing import Dict, Optional

import streamlit as st


def render_analysis_cards(
    analysis: Dict,
    sample: bool = False,
    report_name: Optional[str] = None,
) -> None:
    stats = analysis.get("statistics", {})
    summary = analysis.get("summary", {})
    patient = analysis.get("patient_information", {})
    title = "✨ AI Analysis Results" + (" · SAMPLE DATA" if sample else "")
    display_name = report_name or ("Blood_Test_Report.pdf" if sample else "Report")
    safe_name = escape(str(display_name))
    safe_status = escape(str(summary.get("overall_status", "Not available")))
    st.markdown(f'<div class="pm-analysis-banner">{title}</div>', unsafe_allow_html=True)
    st.markdown(
        f"""<div class="pm-report-card">
        <div class="pm-report-heading">
            <div><div class="pm-eyebrow">{'SAMPLE REPORT' if sample else 'ANALYZED REPORT'}</div>
            <h3>{safe_name}</h3><span class="pm-muted">{'245 KB' if sample else 'Processed in memory'} · ✓ Ready</span></div>
            <span class="pm-status normal">{safe_status}</span>
        </div>
        <div class="pm-report-details">
            <div><span>Name</span><strong>{escape(str(patient.get('name', 'Not available')))}</strong></div>
            <div><span>Age</span><strong>{escape(str(patient.get('age', 'Not available')))}</strong></div>
            <div><span>Gender</span><strong>{escape(str(patient.get('gender', 'Not available')))}</strong></div>
            <div><span>Report Type</span><strong>{escape(str(patient.get('report_type', 'Not available')))}</strong></div>
            <div><span>Date</span><strong>{escape(str(patient.get('date', 'Not available')))}</strong></div>
        </div>
        </div>""",
        unsafe_allow_html=True,
    )
    button_column = st.columns([1, 2, 1])[1]
    with button_column:
        if st.button("View Detailed Analysis →", key="view_detailed_analysis", type="secondary", use_container_width=True):
            st.session_state.page = "Detailed Analysis"
            st.rerun()
    st.markdown(f"<div class=\"pm-card pm-overall\"><span class=\"pm-eyebrow\">Overall Health</span><h3>{summary.get('overall_status', 'Not available')}</h3><p class=\"pm-muted\">{summary.get('summary_text', 'No summary available.')}</p></div>", unsafe_allow_html=True)
    cards = [
        ("normal", stats.get("normal", 0), "Normal", "Within range"),
        ("borderline", stats.get("borderline", 0), "Borderline", "Slightly outside range"),
        ("abnormal", stats.get("abnormal", 0), "Abnormal", "Needs attention"),
    ]
    columns = st.columns(3)
    for column, (kind, number, label, detail) in zip(columns, cards):
        with column:
            st.markdown(f'<div class="pm-card pm-metric {kind}"><div class="number">{number}</div><div class="label">{label}</div><div class="detail">{detail}</div></div>', unsafe_allow_html=True)

