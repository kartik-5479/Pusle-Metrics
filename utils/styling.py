import streamlit as st


LIGHT_THEME = {
    "background": "#F8FAFC",
    "card": "#FFFFFF",
    "text": "#0F172A",
    "muted": "#64748B",
    "border": "#E2E8F0",
}
DARK_THEME = {
    "background": "#111827",
    "card": "#1F2937",
    "text": "#F8FAFC",
    "muted": "#CBD5E1",
    "border": "#374151",
}


def apply_styles(dark_mode: bool = False) -> None:
    colors = DARK_THEME if dark_mode else LIGHT_THEME
    st.markdown(
        f"""
        <style>
        :root {{
            --pm-background: {colors['background']};
            --pm-card: {colors['card']};
            --pm-text: {colors['text']};
            --pm-muted: {colors['muted']};
            --pm-border: {colors['border']};
            --pm-primary: #2563EB;
        }}
        .stApp {{ background: var(--pm-background); color: var(--pm-text); }}
        .block-container {{ max-width: 1440px; padding-top: 1.5rem; padding-bottom: 3rem; }}
        #MainMenu, footer {{ visibility: hidden; }}
        header[data-testid="stHeader"] {{ background: transparent; }}
        [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {{ background: #0F172A; }}
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{ color: #FFFFFF; }}
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {{
            color: #94A3B8; font-size: .72rem; letter-spacing: .1em;
            text-transform: uppercase; margin: 1rem 0 .45rem;
        }}
        [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {{
            width: 100%; min-height: 2.5rem; justify-content: flex-start;
            border: 1px solid transparent; border-radius: 10px; background: transparent;
            color: #CBD5E1; font-weight: 600; transition: all .2s ease;
        }}
        [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover {{
            background: #1E293B; border-color: #334155; color: #FFFFFF;
            transform: translateY(-1px);
        }}
        .pm-card {{ background: var(--pm-card); border: 1px solid var(--pm-border); border-radius: 16px;
            box-shadow: 0 8px 24px rgba(15, 23, 42, .06); padding: 1.25rem; }}
        .pm-eyebrow {{ color: #2563EB; font-size: .75rem; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; }}
        .pm-muted {{ color: var(--pm-muted); }}
        .pm-disclaimer {{ background: #FFF7ED; border: 1px solid #FED7AA; border-radius: 12px; padding: 1rem; color: #9A3412; }}
        .pm-hero {{ padding: 2.25rem 0 1.25rem; }}
        .pm-hero h1 {{ color: var(--pm-text); font-size: clamp(2rem, 4vw, 3.5rem); line-height: 1.08; margin: .35rem 0 1rem; }}
        .pm-hero h1 span {{ color: #2563EB; }}
        .pm-feature {{ min-height: 100px; }}
        .pm-feature strong {{ display: block; color: var(--pm-text); margin-bottom: .35rem; }}
        .pm-feature span {{ color: var(--pm-muted); font-size: .9rem; }}
        .pm-metric {{ border-top: 3px solid #2563EB; }}
        .pm-metric.normal {{ border-top-color: #16A34A; }}
        .pm-metric.borderline {{ border-top-color: #F97316; }}
        .pm-metric.abnormal {{ border-top-color: #DC2626; }}
        .pm-metric .number {{ font-size: 2rem; font-weight: 800; color: var(--pm-text); }}
        .pm-metric .label {{ font-weight: 700; color: var(--pm-text); }}
        .pm-metric .detail {{ color: var(--pm-muted); font-size: .85rem; }}
        .pm-status {{ display: inline-block; border-radius: 999px; padding: .25rem .65rem; font-size: .75rem; font-weight: 700; }}
        .pm-status.normal {{ background: #DCFCE7; color: #166534; }}
        .pm-status.borderline {{ background: #FFEDD5; color: #9A3412; }}
        .pm-status.abnormal {{ background: #FEE2E2; color: #991B1B; }}
        @media (max-width: 768px) {{ .block-container {{ padding: 1rem; }} .pm-hero {{ padding-top: 1rem; }} }}
        </style>
        """,
        unsafe_allow_html=True,
    )
