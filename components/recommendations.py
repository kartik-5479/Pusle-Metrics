from typing import Dict

import streamlit as st


DISCLAIMER = "This analysis is for informational purposes only and is not a medical diagnosis. Please consult a qualified healthcare professional for medical advice."


def render_recommendations(analysis: Dict) -> None:
    st.markdown("## 📄 Recommendations")
    recommendations = analysis.get("recommendations", [])
    if not recommendations:
        st.info("No general recommendations were returned for this report.")
    for recommendation in recommendations:
        st.markdown(f'<div class="pm-card" style="margin-bottom:.7rem">{recommendation}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pm-disclaimer">❤️ {DISCLAIMER}</div>', unsafe_allow_html=True)
