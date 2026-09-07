import streamlit as st

from components.analysis_cards import render_analysis_cards
from components.hero import render_hero
from components.header import render_header
from components.insights import render_insights
from components.recommendations import render_recommendations
from components.upload_section import render_upload_section
from utils.helpers import normalize_analysis


SAMPLE_ANALYSIS = normalize_analysis({
    "patient_information": {"name": "Not Visible (For Privacy)", "age": "28 years", "gender": "Female", "report_type": "Blood Test", "date": "12 Aug 2025"},
    "summary": {"overall_status": "Mostly Normal", "summary_text": "This SAMPLE REPORT contains mostly values within the provided reference ranges."},
    "statistics": {"normal": 12, "borderline": 3, "abnormal": 2},
    "parameters": [],
    "key_insights": ["SAMPLE DATA: Some values may be outside the provided reference ranges.", "SAMPLE DATA: Results should always be interpreted in context by a healthcare professional."],
    "recommendations": ["SAMPLE DATA: Maintain a balanced diet and regular physical activity.", "SAMPLE DATA: Discuss any concerning findings with a qualified healthcare professional."],
})


def render() -> None:
    render_header()
    render_hero()
    st.divider()
    new_analysis = render_upload_section()
    analysis = new_analysis or st.session_state.get("analysis")
    if analysis is None:
        analysis = SAMPLE_ANALYSIS
        sample = True
    else:
        sample = False
    st.divider()
    render_analysis_cards(analysis, sample=sample)
    insight_column, recommendation_column = st.columns(2)
    with insight_column:
        render_insights(analysis)
    with recommendation_column:
        render_recommendations(analysis)
