from html import escape
from typing import Dict

import streamlit as st


def render_insights(analysis: Dict) -> None:
    breakdown = analysis.get("breakdown", [])
    insights = analysis.get("key_insights", [])
    st.markdown('<h2 class="pm-insight-heading">🔎 Report Breakdown</h2>', unsafe_allow_html=True)
    items = breakdown or insights
    if not items:
        st.info("No detailed breakdown was returned for this report.")
    for index, item in enumerate(items, start=1):
        safe_item = escape(str(item))
        st.markdown(f'<div class="pm-card pm-list-item" style="margin-bottom:.7rem"><strong>Finding {index}</strong><br>{safe_item}</div>', unsafe_allow_html=True)

    st.markdown('<h2 class="pm-insight-heading">💡 Key Insights</h2>', unsafe_allow_html=True)
    if not insights:
        st.info("No specific insights were returned for this report.")
        return
    for index, insight in enumerate(insights, start=1):
        safe_insight = escape(str(insight))
        st.markdown(f'<div class="pm-card pm-list-item" style="margin-bottom:.7rem"><strong>Insight {index}</strong><br>{safe_insight}</div>', unsafe_allow_html=True)
