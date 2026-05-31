import streamlit as st


def apply_theme() -> None:
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

            :root {
                --bg: #0b1220;
                --card: #111827;
                --card-2: #0f172a;
                --border: #1f2937;
                --text: #e2e8f0;
                --muted: #94a3b8;
                --accent: #f97316;
                --accent-2: #fb923c;
                --positive: #22c55e;
                --negative: #ef4444;
                --neutral: #f59e0b;
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

            .card {
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 20px 22px;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
            }

            .kpi-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 16px;
            }
            .kpi-card {
                background: var(--card-2);
                border: 1px solid var(--border);
                border-radius: 14px;
                padding: 18px 20px;
            }
            .kpi-label {
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                color: var(--muted);
            }
            .kpi-value {
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--text);
                margin-top: 8px;
            }
            .kpi-sub {
                font-size: 0.8rem;
                color: var(--muted);
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
            .badge-positif { background: rgba(34, 197, 94, 0.2); color: var(--positive); }
            .badge-negatif { background: rgba(239, 68, 68, 0.2); color: var(--negative); }
            .badge-netral { background: rgba(245, 158, 11, 0.2); color: var(--neutral); }
            .badge-sarkasme { background: rgba(168, 85, 247, 0.2); color: #a855f7; }

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
                color: var(--muted);
                text-transform: capitalize;
                line-height: 1;
            }
            .prob-bar-track {
                height: 8px;
                background: #1f2937;
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
                color: var(--muted);
                font-variant-numeric: tabular-nums;
                line-height: 1;
            }

            .stTextArea textarea {
                background: #0f172a !important;
                color: var(--text) !important;
                border: 1px solid var(--border) !important;
                border-radius: 12px !important;
                padding: 14px !important;
            }

            .stButton > button {
                background: linear-gradient(90deg, var(--accent), var(--accent-2)) !important;
                color: #111827 !important;
                border: none !important;
                border-radius: 12px !important;
                padding: 10px 22px !important;
                font-weight: 600 !important;
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
        </style>
        """,
        unsafe_allow_html=True,
    )
