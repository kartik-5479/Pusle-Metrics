import streamlit as st

from components.header import render_header


GUIDES = {
    "Understanding Blood Tests": "Blood tests measure substances in your blood at one point in time. Results are interpreted together with your symptoms, history, and the laboratory's own reference ranges.",
    "Understanding Reference Ranges": "A reference range describes values commonly seen in a reference population. A result outside it is a prompt for context, not a diagnosis by itself.",
    "How to Read a Medical Report": "Start with the report date and type, then review each test's value, unit, and reference range. Look for patterns rather than interpreting one number in isolation.",
    "When to Discuss Results With a Doctor": "Discuss unexpected, persistent, or concerning findings with a qualified healthcare professional, especially when they are paired with new symptoms.",
    "Healthy Lifestyle Basics": "Balanced nutrition, regular movement, adequate sleep, and appropriate preventive care support general health. Personal plans should come from a healthcare professional.",
}


def render() -> None:
    render_header()
    st.title("Tips & Guides")
    st.markdown("Educational information to help you prepare better questions. This is not personalized medical advice.")
    for title, content in GUIDES.items():
        with st.expander(title):
            st.write(content)
