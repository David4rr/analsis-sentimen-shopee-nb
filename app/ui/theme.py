import streamlit as st


def apply_theme() -> None:
    css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        :root {
            /* Background remains dark */
            --bg: #0b1220;
            --text: #e2e8f0;
            --muted: #94a3b8;
            --border: #1f2937;
            
            /* Professional Light Container Palette (Off-white / Slate 50) */
            --card-bg: #f8fafc;
            --card-text: #0f172a;
            --card-muted: #64748b;
            --card-border: #e2e8f0;
            
            /* Accents */
            --accent-lime: #d9f99d; /* User-requested lime, now an accent */
            --accent-blue: #3b82f6;
            
            /* Adjusted badge colors for light background */
            --positive: #15803d; 
            --negative: #b91c1c;
            --neutral: #b45309;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: var(--bg);
            color: var(--text);
        }

        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        .stDeployButton { display: none; }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
            border-right: 1px solid var(--border);
        }

        .sidebar-brand {
            text-align: center;
            padding: 12px 8px 16px 8px;
        }
        .sidebar-title {
            font-weight: 700;
            font-size: 1.1rem;
            color: var(--text);
            margin-top: 6px;
        }
        .sidebar-subtitle {
            font-size: 0.8rem;
            color: var(--muted);
        }

        .page-header {
            padding: 8px 0 20px 0;
        }
        .page-title {
            font-size: 2.0rem;
            font-weight: 700;
            color: var(--text);
            margin: 0;
        }
        .page-subtitle {
            font-size: 0.95rem;
            color: var(--muted);
            margin-top: 6px;
        }

        /* Clean Light Card */
        .card {
            background: var(--card-bg);
            color: var(--card-text);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
        }
        .card .muted { color: var(--card-muted); }
        .card .section-title { color: var(--card-muted); }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
        }
        /* KPI Card with Accent Top Line */
        .kpi-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 14px;
            padding: 20px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease;
        }
        .kpi-card:hover {
            transform: translateY(-3px);
        }
        .kpi-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-lime));
        }
        .kpi-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--card-muted);
        }
        .kpi-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--card-text);
            margin-top: 8px;
        }
        .kpi-sub {
            font-size: 0.8rem;
            color: var(--card-muted);
            margin-top: 4px;
        }

        .badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.02em;
        }
        .badge-positif { background: rgba(21, 128, 61, 0.15); color: var(--positive); }
        .badge-negatif { background: rgba(185, 28, 28, 0.15); color: var(--negative); }
        .badge-netral { background: rgba(180, 83, 9, 0.15); color: var(--neutral); }
        .badge-sarkasme { background: rgba(126, 34, 206, 0.15); color: #7e22ce; }

        .prob-row {
            display: grid;
            grid-template-columns: 70px 1fr 60px;
            gap: 12px;
            align-items: center;
            margin-bottom: 10px;
        }
        .prob-row p {
            margin: 0 !important;
            padding: 0 !important;
            line-height: 1 !important;
        }
        .prob-label {
            font-size: 0.75rem;
            color: var(--card-muted);
            text-transform: capitalize;
            line-height: 1;
        }
        .prob-bar-track {
            height: 8px;
            background: rgba(15, 23, 42, 0.1);
            border-radius: 6px;
            overflow: hidden;
        }
        .prob-bar-fill {
            height: 100%;
            border-radius: 6px;
        }
        .prob-bar-fill.positif { background: var(--positive); }
        .prob-bar-fill.negatif { background: var(--negative); }
        .prob-bar-fill.netral { background: var(--neutral); }
        .prob-value {
            text-align: right;
            font-size: 0.75rem;
            color: var(--card-muted);
            font-variant-numeric: tabular-nums;
            line-height: 1;
        }

        /* Clean White Text Area */
        .stTextArea textarea {
            background: #ffffff !important;
            color: var(--card-text) !important;
            caret-color: var(--card-text) !important;
            border: 1px solid #cbd5e1 !important;
            border-radius: 12px !important;
            padding: 14px !important;
            transition: all 0.2s ease;
        }
        .stTextArea textarea::placeholder {
            color: #94a3b8 !important;
        }
        .stTextArea textarea:focus {
            border-color: var(--accent-blue) !important;
            box-shadow: 0 0 0 1px var(--accent-blue) !important;
        }

        /* Form Container off-white */
        [data-testid="stForm"] {
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: 16px !important;
            padding: 24px !important;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3) !important;
        }
        
        [data-testid="stFormSubmitButton"] button {
            width: 100% !important;
        }

        /* Button Dark with Lime Accent */
        .stButton > button {
            background: #0f172a !important;
            color: var(--accent-lime) !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 10px 22px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
        }
        .stButton > button:hover {
            background: #1e293b !important;
            transform: translateY(-2px);
        }

        .section-title {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--muted);
            margin-bottom: 10px;
        }

        .muted {
            color: var(--muted);
        }

        /* Streamlit Native Component Overrides */
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] span {
            color: var(--text) !important;
        }
        
        .stRadio label, .stRadio p, .stRadio span {
            color: var(--text) !important;
        }

        .stTabs [data-baseweb="tab"] p, .stTabs [data-baseweb="tab"] span {
            color: var(--text) !important;
        }
        
        [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] span {
            color: var(--text) !important;
        }
        
        .streamlit-expanderHeader, .streamlit-expanderHeader p, .streamlit-expanderHeader span {
            color: var(--text) !important;
        }
        
        /* Force Form Label Colors to be Dark */
        [data-testid="stForm"] [data-testid="stWidgetLabel"] p,
        [data-testid="stForm"] [data-testid="stWidgetLabel"] span {
            color: var(--card-text) !important;
            font-weight: 600 !important;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
