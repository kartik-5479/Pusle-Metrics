import datetime

import streamlit as st

from components.header import render_header
from services.history_service import get_analysis, list_analyses


def render() -> None:
    render_header()
    st.title("Analysis History")
    st.caption("Only analysis summaries are retained. Original report contents are not stored.")
    try:
        records = list_analyses()
    except Exception:
        st.error("Analysis history is temporarily unavailable.")
        return
    if not records:
        st.info("No analysis history available yet.")
        return
    for record in records:
        timestamp = record.get("timestamp", "")
        try:
            timestamp = datetime.datetime.fromisoformat(timestamp).strftime("%d %b %Y, %H:%M")
        except ValueError:
            pass
        with st.container(border=True):
            columns = st.columns([2, 2, 1, 1])
            columns[0].markdown(f"**{record['report_name']}**\n\n{timestamp}")
            columns[1].markdown(f"{record.get('report_type', 'Not available')}\n\n{record.get('overall_status', 'Not available')}")
            columns[2].metric("Normal", record["normal_count"])
            columns[3].metric("Attention", record["borderline_count"] + record["abnormal_count"])
            if st.button("Open summary", key=f"history_{record['id']}"):
                selected = get_analysis(record["id"])
                if selected:
                    st.session_state.analysis = selected["analysis"]
                    st.session_state.page = "Home"
                    st.rerun()
