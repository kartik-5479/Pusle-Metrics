import streamlit as st


NAV_ITEMS = [
    ("🏠", "Home"),
    ("📄", "Upload Report"),
    ("💡", "Tips & Guides"),
    ("ⓘ", "About"),
]


def render_sidebar() -> str:
    """Render native Streamlit navigation and return the selected page."""
    with st.sidebar:
        st.markdown(
            """<div class="pm-sidebar-brand-card">
                <div class="pm-sidebar-brand">
                    <div class="pm-sidebar-brand-mark"><span>♥</span></div>
                    <div class="pm-sidebar-brand-copy">
                        <div class="pm-sidebar-brand-name">Pulse Metrics</div>
                        <div class="pm-sidebar-brand-tagline">Understand Your Health Better</div>
                    </div>
                </div>
            </div>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="pm-sidebar-navigation-heading">Navigation</div>',
            unsafe_allow_html=True,
        )
        current_page = st.session_state.get("page", "Home")
        with st.container(key="sidebar_navigation_card"):
            for icon, label in NAV_ITEMS:
                if st.button(
                    f"{icon}  {label}",
                    key=f"nav_{label}",
                    use_container_width=True,
                    type="primary" if label == current_page else "secondary",
                ):
                    st.session_state.page = label
                    current_page = label

        st.markdown(
            """<div class="pm-sidebar-callout">
            <div class="pm-sidebar-callout-icon">✦</div>
            <strong>Early insights<br>for a healthier tomorrow</strong>
            <div class="pm-sidebar-callout-text">Understand your reports with clarity.</div>
            </div>""",
            unsafe_allow_html=True,
        )
    return current_page
