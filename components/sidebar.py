import streamlit as st


NAV_ITEMS = [
    ("🏠", "Home"),
    ("📄", "Upload Report"),
    ("🕘", "Analysis History"),
    ("📊", "Health Insights"),
    ("💡", "Tips & Guides"),
    ("ⓘ", "About"),
]


def render_sidebar() -> str:
    """Render native Streamlit navigation and return the selected page."""
    with st.sidebar:
        st.markdown(
            """<div style="display:flex;gap:12px;align-items:center;padding:8px 4px 20px">
            <div style="background:#2563EB;border-radius:12px;padding:9px 11px;font-size:22px">♥</div>
            <div><strong style="font-size:18px;color:#fff">Pulse Metrics</strong>
            <div style="font-size:11px;color:#94A3B8;margin-top:3px">Understand Your Health Better</div></div>
            </div>""",
            unsafe_allow_html=True,
        )
        st.markdown("### Navigation")
        current_page = st.session_state.get("page", "Home")
        for icon, label in NAV_ITEMS:
            if st.button(
                f"{icon}  {label}",
                key=f"nav_{label}",
                use_container_width=True,
                type="primary" if label == current_page else "secondary",
            ):
                st.session_state.page = label
                current_page = label

        st.markdown("---")
        st.markdown("### Settings")
        st.toggle("🌙 Dark Mode", key="dark_mode")
        st.toggle("🔔 Notifications", value=True, key="notifications")
        st.markdown(
            """<div style="background:linear-gradient(135deg,#1D4ED8,#2563EB);border-radius:14px;padding:16px;margin-top:28px">
            <div style="font-size:20px">✦</div><strong style="color:#fff">Early insights<br>for a healthier tomorrow</strong>
            <div style="color:#DBEAFE;font-size:12px;margin-top:8px">Understand your reports with clarity.</div>
            </div>""",
            unsafe_allow_html=True,
        )
    return current_page
