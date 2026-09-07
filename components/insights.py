from typing import Dict

import streamlit as st


def render_insights(analysis: Dict) -> None:
    insights = analysis.get("key_insights", [])
    st.markdown("## 💡 Key Insights")
    if not insights:
        st.info("No specific insights were returned for this report.")
        return
    for insight in insights:
        st.markdown(f'<div class="pm-card" style="margin-bottom:.7rem">{insight}</div>', unsafe_allow_html=True)
