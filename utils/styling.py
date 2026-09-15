import streamlit as st


LIGHT_THEME = {
    "background": "#F8FAFC",
    "card": "#FFFFFF",
    "text": "#0F172A",
    "muted": "#64748B",
    "border": "#E2E8F0",
}
def apply_styles() -> None:
    colors = LIGHT_THEME
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
        [data-testid="stAppViewContainer"] {{
            background-color: var(--pm-background);
            background-image: linear-gradient(rgba(37,99,235,.055) 1px, transparent 1px),
                linear-gradient(90deg, rgba(37,99,235,.055) 1px, transparent 1px);
            background-size: 32px 32px;
            background-position: center top;
        }}
        [data-testid="stAppViewContainer"] .main {{ background: transparent; }}
        .block-container {{ max-width: 1440px; padding-top: 1.5rem; padding-bottom: 3rem; }}
        #MainMenu, footer {{ visibility: hidden; }}
        header[data-testid="stHeader"] {{ background: transparent; }}
        /* The app uses custom navigation inside the native sidebar. */
        [data-testid="stSidebarNav"] {{ display: none; }}
        [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {{ background: #0F172A; }}
        [data-testid="stSidebar"] > div:first-child {{ padding-top: 1.1rem; }}
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{ color: #FFFFFF; }}
        .pm-sidebar-brand-card {{ position:relative; width:90%; margin:0 auto 1.35rem; padding:1rem .8rem;
            border:1px solid rgba(148,163,184,.2); border-radius:16px;
            background:rgba(30,41,59,.42); box-shadow:inset 0 1px 0 rgba(255,255,255,.08);
            backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); }}
        .pm-sidebar-brand {{ position:relative; z-index:1; display:flex; align-items:center; justify-content:center; gap:.85rem; }}
        .pm-sidebar-brand-mark {{ position:relative; display:flex; align-items:center; justify-content:center;
            flex:0 0 3rem; width:3rem; height:3rem; border-radius:1rem;
            background:linear-gradient(145deg, #3B82F6, #2563EB);
            box-shadow:0 6px 14px rgba(37, 99, 235, .25), inset 0 1px 0 rgba(255,255,255,.25); }}
        .pm-sidebar-brand-mark::after {{ content:""; position:absolute; inset:.3rem; border:1px solid rgba(255,255,255,.16); border-radius:.75rem; }}
        .pm-sidebar-brand-mark span {{ position:relative; z-index:1; color:#FFFFFF; font-size:1.35rem; line-height:1; }}
        .pm-sidebar-brand-copy {{ min-width:0; }}
        .pm-sidebar-brand-name {{ color:#FFFFFF; font-size:1.08rem; font-weight:800; letter-spacing:-.02em; line-height:1.15; }}
        .pm-sidebar-brand-tagline {{ color:#BFDBFE; font-size:.68rem; line-height:1.35; margin-top:.42rem; white-space:nowrap; }}
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {{
            color: #94A3B8; font-size: .72rem; letter-spacing: .1em;
            text-transform: uppercase; margin: 1rem 0 .45rem;
        }}
        .pm-sidebar-navigation-heading {{ color: #94A3B8; font-size: .72rem; font-weight: 800;
            letter-spacing: .1em; text-align: center; text-transform: uppercase;
            margin: 1.3rem 0 .9rem; }}
        [data-testid="stSidebar"] [class*="st-key-sidebar_navigation_card"] {{ width:92%; margin:0 auto; padding:.55rem .35rem;
            border:1px solid rgba(148,163,184,.14); border-radius:16px;
            background:rgba(30,41,59,.42); box-shadow:inset 0 1px 0 rgba(255,255,255,.06);
            backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px); }}
        [data-testid="stSidebar"] [class*="st-key-sidebar_navigation_card"] .stButton > button {{
            width: 92%; min-height: 2.65rem; justify-content: center; margin: 0 auto .3rem;
            border: 1px solid transparent; border-radius: 11px; background: transparent;
            color: #CBD5E1; font-weight: 600; text-align: center; padding: .65rem .85rem;
            transition: background-color .2s ease, border-color .2s ease,
                box-shadow .2s ease, transform .2s ease, color .2s ease;
        }}
        [data-testid="stSidebar"] [class*="st-key-sidebar_navigation_card"] .stButton > button:hover {{
            background: #1E293B; border-color: #334155; color: #FFFFFF;
            box-shadow: 0 6px 16px rgba(2, 6, 23, .2); transform: translateY(-1px);
        }}
        [data-testid="stSidebar"] [class*="st-key-sidebar_navigation_card"] .stButton > button[kind="primary"] {{
            border-color: #3B82F6; background: linear-gradient(135deg, #2563EB, #1D4ED8);
            color: #FFFFFF; font-weight: 700; box-shadow: 0 7px 18px rgba(37, 99, 235, .3);
        }}
        [data-testid="stSidebar"] [class*="st-key-sidebar_navigation_card"] .stButton > button[kind="primary"]:hover {{
            background: linear-gradient(135deg, #3B82F6, #2563EB);
            border-color: #60A5FA; transform: translateY(-1px);
        }}
        .pm-sidebar-callout {{ width: 88%; margin: 2rem auto 0; padding: 1.25rem 1rem;
            border-radius: 18px; background: linear-gradient(135deg, #1D4ED8, #2563EB);
            box-shadow: 0 12px 26px rgba(37, 99, 235, .28); text-align: center;
            color: #FFFFFF; }}
        .pm-sidebar-callout-icon {{ display: inline-flex; align-items: center; justify-content: center;
            width: 2rem; height: 2rem; margin-bottom: .65rem; border-radius: 50%;
            background: rgba(255, 255, 255, .14); color: #FFFFFF; font-size: 1.1rem; }}
        .pm-sidebar-callout strong {{ display: block; font-size: 1rem; line-height: 1.45; }}
        .pm-sidebar-callout-text {{ margin-top: .7rem; color: #DBEAFE; font-size: .78rem; line-height: 1.4; }}
        .stButton > button:hover {{ transform: translateY(-1px); box-shadow: 0 6px 16px rgba(37, 99, 235, .14); }}
        .pm-card {{ background: var(--pm-card); border: 1px solid var(--pm-border); border-radius: 16px;
            box-shadow: 0 8px 24px rgba(15, 23, 42, .06); padding: 1.25rem; }}
        .pm-report-card {{ background: var(--pm-card); border: 1px solid var(--pm-border); border-radius: 16px;
            box-shadow: 0 8px 24px rgba(15, 23, 42, .06); padding: 1.25rem; margin: 1rem 0; }}
        .pm-sample-section {{ margin:1.5rem 0 1rem; padding:1.35rem 1.5rem; border:1px solid #BFDBFE;
            border-radius:18px; background:linear-gradient(135deg,rgba(239,246,255,.88),rgba(224,242,254,.62));
            text-align:center; box-shadow:0 8px 22px rgba(37,99,235,.07); }}
        .pm-sample-badge {{ display:inline-block; padding:.35rem .7rem; border-radius:999px;
            background:#DBEAFE; color:#1D4ED8; font-size:.7rem; font-weight:800; letter-spacing:.1em; }}
        .pm-sample-section h2 {{ color:var(--pm-text); margin:.65rem 0 .4rem; font-size:1.35rem; letter-spacing:-.02em; }}
        .pm-sample-section p {{ max-width:680px; margin:0 auto; color:var(--pm-muted); line-height:1.55; font-size:.9rem; }}
        .pm-report-heading {{ display:flex; justify-content:space-between; align-items:flex-start; gap:1rem; }}
        .pm-report-heading h3 {{ color: var(--pm-text); margin: .35rem 0 .15rem; }}
        .pm-report-details {{ display:grid; grid-template-columns:repeat(5, minmax(0, 1fr)); gap:1rem;
            border-top:1px solid var(--pm-border); margin-top:1rem; padding-top:1rem; }}
        .pm-report-details > div {{ text-align:center; }}
        .pm-report-details span {{ display:block; color:var(--pm-muted); font-size:.75rem; margin-bottom:.3rem; }}
        .pm-report-details strong {{ color:var(--pm-text); font-size:.9rem; }}
        .pm-overall {{ background: linear-gradient(135deg, var(--pm-card), #EFF6FF); margin-bottom: .8rem; }}
        .pm-analysis-banner {{ width:88%; margin:1.8rem auto 1rem; padding:1.05rem 1.25rem;
            border-radius:18px; background:linear-gradient(135deg, #1D4ED8, #2563EB);
            box-shadow:0 12px 26px rgba(37, 99, 235, .28); color:#FFFFFF;
            text-align:center; font-size:clamp(1.35rem, 2.7vw, 2.15rem); font-weight:800;
            letter-spacing:-.025em; line-height:1.2; }}
        [class*="st-key-view_detailed_analysis"] .stButton > button {{
            min-height:3.75rem; border:1px solid #3B82F6; border-radius:16px;
            background:linear-gradient(135deg, #1D4ED8, #2563EB); color:#FFFFFF;
            box-shadow:0 12px 26px rgba(37, 99, 235, .24);
        }}
        [class*="st-key-view_detailed_analysis"] .stButton > button:hover {{
            border-color:#60A5FA; background:linear-gradient(135deg, #2563EB, #3B82F6);
            color:#FFFFFF; box-shadow:0 16px 30px rgba(37, 99, 235, .3);
        }}
        [class*="st-key-view_detailed_analysis"] .stButton > button p {{
            color:#FFFFFF; font-size:1.05rem; font-weight:800;
        }}
        .pm-overall {{ text-align:center; padding:1.6rem; }}
        .pm-upload-meta {{ display:flex; justify-content:space-between; gap:1rem; align-items:center;
            border: 2px dashed #93C5FD; border-radius: 14px; padding: 1rem; margin: .8rem 0; background: #EFF6FF; color: #1E3A8A; }}
        .pm-upload-meta span {{ color: #64748B; font-size: .85rem; }}
        [class*="st-key-analyze_report_action"] {{ max-width: 760px; margin: 1.15rem auto .95rem; }}
        [class*="st-key-analyze_report_action"] .stButton > button {{
            min-height: 4.25rem; border-radius: 16px;
        }}
        [class*="st-key-analyze_report_action"] .stButton > button p {{
            font-size: 1.65rem; font-weight: 900; letter-spacing: .01em;
        }}
        .pm-table-wrap {{ overflow-x:auto; border: 1px solid var(--pm-border); border-radius: 14px; background: var(--pm-card); }}
        .pm-table {{ border-collapse: collapse; width: 100%; min-width: 820px; color: var(--pm-text); }}
        .pm-table th, .pm-table td {{ border-bottom: 1px solid var(--pm-border); padding: .85rem; text-align: left; vertical-align: top; }}
        .pm-table th {{ color: var(--pm-muted); font-size: .75rem; text-transform: uppercase; letter-spacing: .05em; }}
        .pm-explanation-card {{ margin:.8rem 0; padding:1.15rem 1.25rem; border:1px solid var(--pm-border);
            border-left:4px solid #2563EB; border-radius:14px; background:var(--pm-card);
            box-shadow:0 6px 18px rgba(15,23,42,.04); }}
        .pm-explanation-heading {{ display:flex; align-items:center; justify-content:space-between; gap:1rem; }}
        .pm-explanation-heading h4 {{ color:var(--pm-text); margin:0; font-size:1rem; }}
        .pm-explanation-value {{ color:var(--pm-muted); margin-top:.55rem; font-size:.85rem; }}
        .pm-explanation-card p {{ color:var(--pm-text); line-height:1.65; margin:.7rem 0 0; }}
        .pm-eyebrow {{ color: #2563EB; font-size: .75rem; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; }}
        .pm-muted {{ color: var(--pm-muted); }}
        .pm-page-intro {{ padding:1.2rem 0 1.35rem; max-width:720px; }}
        .pm-page-intro h1 {{ color:var(--pm-text); font-size:clamp(2rem, 4vw, 3.15rem); line-height:1.05; margin:.45rem 0 .8rem; letter-spacing:-.035em; }}
        .pm-page-intro p {{ color:var(--pm-muted); font-size:1.02rem; line-height:1.65; margin:0; }}
        .pm-flow-card {{ min-height:110px; padding:1rem 1.1rem; border:1px solid var(--pm-border); border-radius:14px; background:var(--pm-card); box-shadow:0 6px 18px rgba(15,23,42,.04); transition:transform .2s ease, box-shadow .2s ease; }}
        .pm-flow-card:hover {{ transform:translateY(-3px); box-shadow:0 12px 24px rgba(37,99,235,.1); }}
        .pm-flow-card span {{ display:inline-flex; align-items:center; justify-content:center; width:1.7rem; height:1.7rem; margin-bottom:.7rem; border-radius:50%; background:#DBEAFE; color:#1D4ED8; font-size:.7rem; font-weight:800; }}
        .pm-flow-card strong {{ display:block; color:var(--pm-text); font-size:.95rem; }}
        .pm-flow-card p {{ color:var(--pm-muted); font-size:.8rem; line-height:1.4; margin:.35rem 0 0; }}
        .pm-upload-panel {{ margin-top:1.5rem; padding:1.45rem; border:1px solid #DBEAFE; border-radius:20px; background:linear-gradient(145deg,#FFFFFF,#F0F7FF); box-shadow:0 14px 32px rgba(15,23,42,.06); }}
        .pm-upload-heading {{ text-align:center; padding:.35rem 0 .4rem; }}
        .pm-upload-heading h2 {{ position:relative; color:var(--pm-text); margin:0; font-size:clamp(1.55rem, 2.4vw, 2rem);
            font-weight:800; letter-spacing:-.035em; line-height:1.15; }}
        .pm-upload-heading h2::after {{ content:""; display:block; width:3rem; height:3px; margin:.7rem auto .65rem;
            border-radius:999px; background:linear-gradient(90deg, #60A5FA, #2563EB); }}
        .pm-upload-heading p {{ color:#647B91; margin:0 0 .65rem; font-size:.92rem; font-weight:500; letter-spacing:.01em; }}
        .pm-upload-heading a {{ display:none; }}
        .pm-upload-empty {{ display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:145px; margin-top:.75rem; border:1px dashed #93C5FD; border-radius:15px; background:rgba(239,246,255,.7); text-align:center; }}
        .pm-upload-icon {{ display:flex; align-items:center; justify-content:center; width:2.6rem; height:2.6rem; margin-bottom:.55rem; border-radius:50%; background:#DBEAFE; color:#2563EB; font-size:1.6rem; font-weight:700; }}
        .pm-upload-empty strong {{ color:#1E3A8A; font-size:.95rem; }}
        .pm-upload-empty span {{ color:#64748B; font-size:.8rem; margin-top:.25rem; }}
        [data-testid="stFileUploaderDropzone"] {{ border:1px dashed #93C5FD; border-radius:14px; background:rgba(239,246,255,.7); padding:.9rem; transition:border-color .2s ease, background-color .2s ease, box-shadow .2s ease; }}
        [data-testid="stFileUploaderDropzone"]:hover {{ border-color:#2563EB; background:#EFF6FF; box-shadow:0 0 0 4px rgba(37,99,235,.08); }}
        [data-testid="stFileUploaderDropzone"] {{ display:flex; flex-direction:column;
            align-items:center; justify-content:center; text-align:center; gap:.55rem; }}
        [data-testid="stFileUploaderDropzone"] > span,
        [data-testid="stFileUploaderDropzone"] > div {{ display:flex; justify-content:center; align-items:center; }}
        [data-testid="stFileUploaderDropzone"] button {{ margin:0 auto; }}
        [data-testid="stFileUploaderDropzone"] button {{ border-radius:9px; border:1px solid #BFDBFE; background:#FFFFFF; color:#1D4ED8; font-weight:700; }}
        [data-testid="stFileUploaderDropzone"] button:hover {{ border-color:#2563EB; background:#DBEAFE; }}
        .pm-complete-card {{ display:flex; flex-direction:column; gap:.3rem; margin-top:1.25rem; padding:1rem 1.1rem; border:1px solid #BBF7D0; border-radius:13px; background:#F0FDF4; color:#166534; }}
        .pm-complete-card strong {{ font-size:.95rem; }}
        .pm-complete-card span {{ font-size:.85rem; }}
        .pm-disclaimer {{ background: #FFF7ED; border: 1px solid #FED7AA; border-radius: 12px; padding: 1rem; color: #9A3412; }}
        .pm-hero {{ padding: 3.25rem 0 1.7rem; text-align:center; }}
        .pm-hero h1 {{ color: var(--pm-text); font-size: clamp(2rem, 4vw, 3.5rem); line-height: 1.08; margin: .55rem 0 1.1rem; letter-spacing:-.035em; }}
        .pm-hero h1 span {{ color: #2563EB; }}
        .pm-hero > p {{ max-width:650px; margin:0 auto; font-size:1.05rem; line-height:1.65; }}
        .pm-feature {{ position:relative; min-height:100px; text-align:center; overflow:hidden;
            border:1px solid rgba(56,189,248,.4); background:linear-gradient(145deg,
                rgba(224,242,254,.92), rgba(186,230,253,.72));
            box-shadow:0 10px 24px rgba(14,116,144,.1), inset 0 1px 0 rgba(255,255,255,.78);
            backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);
            transition:transform .25s ease, box-shadow .25s ease, border-color .25s ease; }}
        .pm-feature::before {{ content:""; position:absolute; width:7rem; height:7rem; top:-4rem; right:-2rem;
            border-radius:50%; background:rgba(56,189,248,.25); filter:blur(18px); pointer-events:none; }}
        .pm-feature:hover {{ transform:translateY(-5px); border-color:#38BDF8;
            box-shadow:0 18px 34px rgba(14,116,144,.16), 0 0 0 1px rgba(56,189,248,.18), inset 0 1px 0 rgba(255,255,255,.95); }}
        .pm-feature-icon {{ position:relative; z-index:1; display:flex; align-items:center; justify-content:center;
            min-height:2rem; margin-bottom:.65rem; font-size:1.5rem; }}
        .pm-feature strong {{ display: block; color: #0F172A; margin-bottom: .35rem; }}
        .pm-feature span {{ position:relative; z-index:1; color: #355B73; font-size: .9rem; }}
        .pm-insight-heading {{ color:var(--pm-text); margin:2rem 0 .95rem; text-align:center; letter-spacing:-.025em; }}
        .pm-metric {{ border-top: 3px solid #2563EB; text-align:center; margin-bottom:1.1rem; }}
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
        @media (max-width: 768px) {{
            .block-container {{ padding: 1rem; }} .pm-hero {{ padding-top: 1rem; }}
            .pm-report-heading {{ flex-direction:column; }}
            .pm-report-details {{ grid-template-columns:repeat(2, minmax(0, 1fr)); }}
            .pm-upload-panel {{ padding:1rem; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
