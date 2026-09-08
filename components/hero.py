import streamlit as st


def render_hero() -> None:
    st.markdown(
        """<section class="pm-hero">
        <div class="pm-eyebrow">A clearer view of your health</div>
        <h1>Your Health Report,<br><span>Simplified with AI</span></h1>
        <p class="pm-muted">Upload your medical reports and get easy-to-understand insights, personalized analysis and health recommendations.</p>
        </section>""",
        unsafe_allow_html=True,
    )
    columns = st.columns(3)
    features = [
        ("🛡️", "Secure & Private", "Your data stays safe"),
        ("⚡", "AI-Powered Analysis", "Quick & Accurate"),
        ("👥", "Easy to Understand", "Medical terms made simple"),
    ]
    for column, (icon, title, detail) in zip(columns, features):
        with column:
            st.markdown(
                f'<div class="pm-card pm-feature"><div class="pm-feature-icon">{icon}</div><strong>{title}</strong><span>{detail}</span></div>',
                unsafe_allow_html=True,
            )
