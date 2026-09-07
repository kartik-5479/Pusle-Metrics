import streamlit as st


def render_header() -> None:
    """Render the lightweight application header."""
    left, right = st.columns([3, 1])
    with left:
        st.markdown('<span class="pm-eyebrow">PULSE METRICS / HEALTH OVERVIEW</span>', unsafe_allow_html=True)
    with right:
        st.markdown('<div style="text-align:right;color:#64748B;font-size:.9rem">👤 Hello, <strong>User</strong> &nbsp;⌄</div>', unsafe_allow_html=True)
