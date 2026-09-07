import streamlit as st

from components.header import render_header
from services.history_service import list_analyses


def render() -> None:
    render_header()
    st.title("Health Insights")
    try:
        records = list_analyses()
    except Exception:
        st.error("Health insights are temporarily unavailable.")
        return
    if not records:
        st.info("No analysis history available yet.")
        return
    total = len(records)
    normal = sum(item["normal_count"] for item in records)
    borderline = sum(item["borderline_count"] for item in records)
    abnormal = sum(item["abnormal_count"] for item in records)
    columns = st.columns(4)
    for column, label, value in zip(columns, ["Reports Analyzed", "Normal Parameters", "Borderline Parameters", "Abnormal Parameters"], [total, normal, borderline, abnormal]):
        column.metric(label, value)
    st.subheader("Parameter distribution")
    st.bar_chart({"Normal": normal, "Borderline": borderline, "Abnormal": abnormal})
    st.subheader("Recent Analysis")
    latest = records[0]
    st.markdown(f'<div class="pm-card"><strong>{latest["report_name"]}</strong><br>{latest.get("overall_status", "Not available")}</div>', unsafe_allow_html=True)
