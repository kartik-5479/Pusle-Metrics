from html import escape
from typing import Dict

import streamlit as st


DISCLAIMER = "This analysis is for informational purposes only and is not a medical diagnosis. Please consult a qualified healthcare professional for medical advice."


def render_recommendations(analysis: Dict) -> None:
    precautions = analysis.get("precautions", [])
    st.markdown('<h2 class="pm-insight-heading">📄 Recommendations</h2>', unsafe_allow_html=True)
    recommendations = analysis.get("recommendations", [])
    if not recommendations:
        st.info("No general recommendations were returned for this report.")
    for index, recommendation in enumerate(recommendations, start=1):
        safe_recommendation = escape(str(recommendation))
        st.markdown(f'<div class="pm-card pm-list-item" style="margin-bottom:.7rem"><strong>Recommendation {index}</strong><br>{safe_recommendation}</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="pm-insight-heading">⚠️ Precautions</h2>', unsafe_allow_html=True)
    if not precautions:
        st.info("No additional precautions were returned. Discuss unexpected findings with a qualified healthcare professional.")
    for index, precaution in enumerate(precautions, start=1):
        safe_precaution = escape(str(precaution))
        st.markdown(f'<div class="pm-card pm-list-item" style="margin-bottom:.7rem"><strong>Precaution {index}</strong><br>{safe_precaution}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pm-disclaimer">❤️ {DISCLAIMER}</div>', unsafe_allow_html=True)
