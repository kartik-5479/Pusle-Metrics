import streamlit as st

from components.analysis_cards import render_analysis_cards
from components.hero import render_hero
from components.header import render_header
from components.insights import render_insights
from components.recommendations import render_recommendations
from components.upload_section import render_upload_section
from utils.helpers import normalize_analysis


SAMPLE_ANALYSIS = normalize_analysis({
    "patient_information": {"name": "Not Visible (For Privacy)", "age": "28 years", "gender": "Female", "report_type": "Routine Blood Test", "date": "12 Aug 2025"},
    "summary": {"overall_status": "Mostly within range", "summary_text": "Three reviewed values are within the supplied ranges. Vitamin D and fasting glucose are close to or slightly above the ranges shown and may be worth discussing in context."},
    "parameters": [
        {"name": "Hemoglobin", "value": "13.6", "unit": "g/dL", "reference_range": "12.0-16.0", "status": "Normal", "explanation": "Hemoglobin is a red blood cell protein that carries oxygen. The reported value is within the range supplied by this sample report."},
        {"name": "Total Cholesterol", "value": "178", "unit": "mg/dL", "reference_range": "120-200", "status": "Normal", "explanation": "Cholesterol is a substance the body uses for important functions. This reported value falls within the sample report's stated range."},
        {"name": "ALT", "value": "31", "unit": "U/L", "reference_range": "7-35", "status": "Normal", "explanation": "ALT is an enzyme often included when reviewing liver-related results. This value is within the reference range shown in the sample report."},
        {"name": "Vitamin D", "value": "24", "unit": "ng/mL", "reference_range": "30-100", "status": "Borderline", "explanation": "Vitamin D is a nutrient involved in bone and muscle health. The reported value is below the range shown in this sample report and should be interpreted with the person's overall context."},
        {"name": "Fasting Glucose", "value": "108", "unit": "mg/dL", "reference_range": "70-100", "status": "Borderline", "explanation": "Fasting glucose is the amount of sugar measured in the blood after fasting. This sample value is slightly above the supplied range and does not by itself establish a diagnosis."},
    ],
    "breakdown": ["Hemoglobin, total cholesterol, and ALT are within the ranges shown in the report.", "Vitamin D is below the supplied range and fasting glucose is slightly above it; these findings need context rather than a conclusion from this sample alone."],
    "key_insights": ["The main pattern is mostly in-range results with two values that may deserve a follow-up conversation.", "A single laboratory result is interpreted alongside symptoms, history, and the laboratory's own ranges."],
    "precautions": ["Discuss the Vitamin D and fasting glucose results with a qualified healthcare professional before taking supplements or changing your routine."],
    "recommendations": ["Keep the original report and ask whether repeat testing or follow-up is appropriate.", "Do not start, stop, or change medication based on this sample dashboard."],
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
    if sample:
        st.markdown(
            """<section class="pm-sample-section">
            <div class="pm-sample-badge">SAMPLE REPORT PREVIEW</div>
            <h2>Explore a Pulse Metrics analysis</h2>
            <p>This demonstration report keeps the patient identity private and shows how results, explanations, precautions, and recommendations appear together.</p>
            </section>""",
            unsafe_allow_html=True,
        )
    if not sample:
        st.divider()
    render_analysis_cards(
        analysis,
        sample=sample,
        report_name=st.session_state.get("report_name"),
    )
    insight_column, recommendation_column = st.columns(2)
    with insight_column:
        render_insights(analysis)
    with recommendation_column:
        render_recommendations(analysis)
