from typing import Dict

import streamlit as st


def render_analysis_cards(analysis: Dict, sample: bool = False) -> None:
    stats = analysis.get("statistics", {})
    summary = analysis.get("summary", {})
    title = "✨ AI Analysis Results" + (" · SAMPLE DATA" if sample else "")
    st.markdown(f"## {title}")
    st.markdown(f"<div class=\"pm-card\"><span class=\"pm-eyebrow\">Overall Health</span><h3>{summary.get('overall_status', 'Not available')}</h3><p class=\"pm-muted\">{summary.get('summary_text', 'No summary available.')}</p></div>", unsafe_allow_html=True)
    cards = [
        ("normal", stats.get("normal", 0), "Normal", "Within range"),
        ("borderline", stats.get("borderline", 0), "Borderline", "Slightly outside range"),
        ("abnormal", stats.get("abnormal", 0), "Abnormal", "Needs attention"),
    ]
    columns = st.columns(3)
    for column, (kind, number, label, detail) in zip(columns, cards):
        with column:
            st.markdown(f'<div class="pm-card pm-metric {kind}"><div class="number">{number}</div><div class="label">{label}</div><div class="detail">{detail}</div></div>', unsafe_allow_html=True)

    with st.expander("View Detailed Analysis"):
        patient = analysis.get("patient_information", {})
        st.markdown("**Patient and report information**")
        info_columns = st.columns(5)
        for column, label in zip(
            info_columns,
            ["Name", "Age", "Gender", "Report Type", "Date"],
        ):
            key = label.lower().replace(" ", "_")
            column.metric(label, patient.get(key, "Not available"))
        st.markdown("**Parameter Analysis**")
        parameters = analysis.get("parameters", [])
        if parameters:
            st.dataframe(parameters, use_container_width=True, hide_index=True)
        else:
            st.info("No parameter-level results are available.")
