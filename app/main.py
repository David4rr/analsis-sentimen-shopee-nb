"""
Analisis Sentimen - Naive Bayes + Lexicon
Streamlit Web Application

Aplikasi web untuk menganalisis sentimen teks ulasan berbahasa Indonesia
menggunakan model Naive Bayes yang dikombinasikan dengan fitur Lexicon.
"""

import streamlit as st
import streamlit.components.v1 as components
import joblib
import os
import re
import string
import numpy as np
import time
import textwrap
import gdown

# ---------------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Analisis Sentimen | Naive Bayes + Lexicon",
    page_icon="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>NB</text></svg>",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Custom CSS - Modern, Clean, Professional (no emoji, no gradient)
# ---------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* ---- Reset & Base ---- */
    *, *::before, *::after { box-sizing: border-box; }

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }

    .stApp {
        background-color: #f8f9fb;
    }

    /* ---- Hide default Streamlit elements ---- */
    #MainMenu { visibility: hidden; }
    header { visibility: hidden; }
    footer { visibility: hidden; }
    .stDeployButton { display: none; }

    /* ---- Top Navigation Bar ---- */
    .top-bar {
        background-color: #ffffff;
        border-bottom: 1px solid #e2e5e9;
        padding: 16px 32px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: -80px -16px 32px -16px;
        position: relative;
        z-index: 10;
    }
    .top-bar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .top-bar-logo {
        width: 36px;
        height: 36px;
        background-color: #1a1a2e;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: -0.5px;
    }
    .top-bar-title {
        font-size: 18px;
        font-weight: 600;
        color: #1a1a2e;
        letter-spacing: -0.3px;
    }
    .top-bar-subtitle {
        font-size: 12px;
        color: #7c8597;
        font-weight: 400;
    }
    .top-bar-badge {
        background-color: #f0f2f5;
        border: 1px solid #e2e5e9;
        border-radius: 6px;
        padding: 6px 14px;
        font-size: 12px;
        font-weight: 500;
        color: #4a5568;
    }

    /* ---- Card Component ---- */
    .card {
        background: #ffffff;
        border: 1px solid #e2e5e9;
        border-radius: 12px;
        padding: 28px;
        margin-bottom: 20px;
        transition: box-shadow 0.2s ease;
    }
    .card:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
    }
    .card-header {
        font-size: 14px;
        font-weight: 600;
        color: #1a1a2e;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 20px;
        padding-bottom: 14px;
        border-bottom: 1px solid #f0f2f5;
    }

    /* ---- Metric Stat Cards ---- */
    .stat-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 16px;
        margin-bottom: 24px;
    }
    .stat-card {
        background: #ffffff;
        border: 1px solid #e2e5e9;
        border-radius: 10px;
        padding: 22px 24px;
        text-align: center;
        transition: transform 0.18s ease, box-shadow 0.18s ease;
    }
    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
    }
    .stat-label {
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #7c8597;
        margin-bottom: 8px;
    }
    .stat-value {
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    .stat-sub {
        font-size: 12px;
        color: #9ca3af;
        margin-top: 4px;
    }

    /* ---- Result Section ---- */
    .result-container {
        background: #ffffff;
        border: 1px solid #e2e5e9;
        border-radius: 12px;
        padding: 32px;
        margin-top: 24px;
    }
    .result-label {
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: #7c8597;
        margin-bottom: 12px;
    }
    .result-sentiment {
        font-size: 32px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 6px;
    }
    .result-confidence {
        font-size: 14px;
        font-weight: 500;
        color: #7c8597;
    }

    /* ---- Sentiment Colors ---- */
    .sentiment-positif { color: #0d9668; }
    .sentiment-negatif { color: #c53030; }
    .sentiment-netral  { color: #6b7280; }

    .bg-positif { background-color: #ecfdf5; border-color: #a7f3d0; }
    .bg-negatif { background-color: #fef2f2; border-color: #fecaca; }
    .bg-netral  { background-color: #f9fafb; border-color: #e5e7eb; }

    /* ---- Probability Bar ---- */
    .prob-row {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 10px;
    }
    .prob-label {
        width: 70px;
        font-size: 12px;
        font-weight: 600;
        text-transform: capitalize;
        color: #4a5568;
        text-align: right;
    }
    .prob-bar-track {
        flex: 1;
        height: 8px;
        background-color: #f0f2f5;
        border-radius: 4px;
        overflow: hidden;
    }
    .prob-bar-fill {
        height: 100%;
        border-radius: 4px;
        transition: width 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    .prob-bar-fill.positif { background-color: #0d9668; }
    .prob-bar-fill.negatif { background-color: #c53030; }
    .prob-bar-fill.netral  { background-color: #6b7280; }
    .prob-value {
        width: 52px;
        font-size: 13px;
        font-weight: 600;
        color: #1a1a2e;
        text-align: right;
        font-variant-numeric: tabular-nums;
    }

    /* ---- Preprocessing Detail ---- */
    .preprocess-box {
        background: #f8f9fb;
        border: 1px solid #e2e5e9;
        border-radius: 8px;
        padding: 16px 20px;
        margin-top: 16px;
        font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace;
        font-size: 13px;
        color: #4a5568;
        line-height: 1.7;
        word-break: break-word;
    }
    .preprocess-label {
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: #9ca3af;
        margin-bottom: 8px;
    }

    /* ---- How-It-Works Section ---- */
    .pipeline-step {
        display: flex;
        align-items: flex-start;
        gap: 16px;
        padding: 16px 0;
        border-bottom: 1px solid #f0f2f5;
    }
    .pipeline-step:last-child {
        border-bottom: none;
    }
    .step-number {
        width: 32px;
        height: 32px;
        min-width: 32px;
        background-color: #1a1a2e;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff;
        font-size: 13px;
        font-weight: 700;
    }
    .step-content h4 {
        font-size: 14px;
        font-weight: 600;
        color: #1a1a2e;
        margin: 0 0 4px 0;
    }
    .step-content p {
        font-size: 13px;
        color: #7c8597;
        margin: 0;
        line-height: 1.5;
    }

    /* ---- Textarea ---- */
    .stTextArea textarea {
        color: #1a1a2e !important;
        border: 1px solid #d1d5db !important;
        border-radius: 10px !important;
        padding: 16px !important;
        font-size: 15px !important;
        font-family: 'Inter', sans-serif !important;
        line-height: 1.6 !important;
        resize: vertical !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
        background-color: #ffffff !important;
        caret-color: #1a1a2e !important;
    }
    .stTextArea textarea:focus {
        border-color: #1a1a2e !important;
        box-shadow: 0 0 0 3px rgba(26, 26, 46, 0.08) !important;
    }

    /* ---- Button ---- */
    .stButton > button {
        background-color: #1a1a2e !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 32px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        letter-spacing: 0.3px !important;
        transition: background-color 0.2s ease, transform 0.15s ease !important;
        width: 100% !important;
    }
    .stButton > button:hover {
        background-color: #2d2d4e !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* ---- Batch Results Table ---- */
    .batch-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin-top: 16px;
    }
    .batch-table th {
        background-color: #f8f9fb;
        border-bottom: 2px solid #e2e5e9;
        padding: 12px 16px;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: #7c8597;
        text-align: left;
    }
    .batch-table td {
        padding: 14px 16px;
        border-bottom: 1px solid #f0f2f5;
        font-size: 13px;
        color: #1a1a2e;
        vertical-align: top;
    }
    .batch-table tr:last-child td {
        border-bottom: none;
    }
    .batch-table tr:hover td {
        background-color: #f8f9fb;
    }
    .sent-tag {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 5px;
        font-size: 12px;
        font-weight: 600;
        text-transform: capitalize;
    }
    .sent-tag.positif { background: #ecfdf5; color: #0d9668; }
    .sent-tag.negatif { background: #fef2f2; color: #c53030; }
    .sent-tag.netral  { background: #f3f4f6; color: #6b7280; }

    /* ---- Footer ---- */
    .app-footer {
        text-align: center;
        padding: 32px 16px;
        margin-top: 48px;
        border-top: 1px solid #e2e5e9;
        font-size: 12px;
        color: #9ca3af;
    }

    /* ---- Tabs Styling ---- */
    [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f0f2f5;
        padding: 6px;
        border-radius: 12px;
        margin-bottom: 24px;
        border-bottom: none;
    }
    [data-baseweb="tab"] {
        background-color: transparent !important;
        border-radius: 8px !important;
        padding: 10px 16px !important;
        color: #7c8597 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        border: none !important;
        margin: 0 !important;
    }
    [aria-selected="true"][data-baseweb="tab"] {
        background-color: #ffffff !important;
        color: #1a1a2e !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05) !important;
    }

    /* ---- Responsive ---- */
    @media (max-width: 768px) {
        .top-bar {
            flex-direction: column;
            align-items: flex-start;
            gap: 10px;
            padding: 14px 16px;
        }
        .stat-row {
            grid-template-columns: 1fr;
        }
        .result-sentiment {
            font-size: 24px;
        }
        .card {
            padding: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Preprocessing Functions (replicated from notebook)
# ---------------------------------------------------------------------------

# Stopwords (extended)
MORE_STOPWORDS = [
    'yg', 'dg', 'rt', 'dgn', 'ny', 'd', 'amp', 'biar', 'bikin', 'bilang',
    'krn', 'nya', 'nih', 'sih', 'si', 'tau', 'tuh', 'utk', 'ya', 'jd', 'sdh', 'aja', 'n',
    'nyg', 'hehe', 'pen', 'u', 'nan', 'loh', 'dan', 'atau', 'di', 'ke',
    'dari', 'yang', 'ini', 'itu', 'saya', 'kamu', 'dia', 'mereka', 'kita', 'ada', 'adalah',
    'kepada', 'oleh', 'pada', 'min', 'admin', 'mimin', 'kak', 'kk', 'gan', 'sis', 'bro',
    'bg', 'mba', 'mas', 'cs', 'dear', 'dong', 'lah', 'deh', 'yah', 'bpk', 'ibu'
]

NEGATION_WORDS = {
    'tidak', 'tak', 'bukan', 'jangan', 'kurang', 'belum', 'gak', 'ga', 'nggak',
    'enggak', 'ngga', 'kagak', 'ndak', 'gk', 'tdk'
}

CONTRAST_WORDS = {
    'tapi', 'namun', 'cuman', 'cuma', 'sayang', 'hanya', 'meski', 'walau', 'padahal'
}

SLANG_MAP = {
    'bgt': 'banget', 'bngt': 'banget', 'bgtt': 'banget',
    'gk': 'gak', 'ga': 'gak', 'ngga': 'nggak', 'ngak': 'nggak', 'kagak': 'gak',
    'ndak': 'tidak', 'tdk': 'tidak',
    'udh': 'sudah', 'sdh': 'sudah', 'dr': 'dari', 'krn': 'karena', 'karna': 'karena',
    'yg': 'yang', 'utk': 'untuk', 'dgn': 'dengan', 'tp': 'tapi', 'tpi': 'tapi',
    'pdhl': 'padahal',
    'klo': 'kalau', 'kalo': 'kalau', 'skrg': 'sekarang', 'kmrn': 'kemarin',
    'lg': 'lagi', 'msh': 'masih', 'td': 'tadi', 'bs': 'bisa', 'bsa': 'bisa',
    'gmn': 'gimana', 'pd': 'pada', 'kpd': 'kepada', 'pake': 'pakai', 'pke': 'pakai',
    'dpt': 'dapat', 'dapet': 'dapat', 'brg': 'barang', 'brng': 'barang',
    'ongk': 'ongkir', 'ongkirnya': 'ongkir', 'apk': 'aplikasi',
    'aplikasinya': 'aplikasi', 'app': 'aplikasi',
    'eror': 'error', 'lemot': 'lambat', 'recomended': 'recommended',
    'rekomen': 'rekomendasi',
    'trimakasih': 'terima kasih', 'mksh': 'makasih', 'tks': 'thanks',
    'ngotak': 'masuk akal', 'amanah': 'jujur', 'laa': 'lah', 'nyaa': 'nya',
    'atw': 'atau'
}

# Build stopwords set (same logic as notebook)
try:
    from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
    _base_sw = set(StopWordRemoverFactory().get_stop_words())
except (ModuleNotFoundError, ImportError):
    _base_sw = set(
        'yang untuk dengan dan atau ini itu di ke dari pada adalah '
        'saya kamu dia mereka kita ada'.split()
    )

_final_stopwords = (_base_sw - NEGATION_WORDS - CONTRAST_WORDS).union(set(MORE_STOPWORDS))
_final_stopwords = _final_stopwords - NEGATION_WORDS - CONTRAST_WORDS
_negation_skip_words = _final_stopwords.union(
    {'sangat', 'banget', 'sekali', 'amat', 'agak', 'cukup', 'terlalu', 'lebih', 'paling'}
) - CONTRAST_WORDS


def _normalize_slang_token(token):
    return SLANG_MAP.get(token, token)


def _normalize_tokens(tokens):
    normalized = []
    for tok in tokens:
        normalized.extend(_normalize_slang_token(tok).split())
    return normalized


def _apply_negation_scope(tokens):
    result = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok in NEGATION_WORDS:
            j = i + 1
            while j < len(tokens) and tokens[j] in _negation_skip_words:
                j += 1
            if j < len(tokens):
                result.append(f"tidak_{tokens[j]}")
                i = j + 1
                continue
        result.append(tok)
        i += 1
    return result


def preprocess_text(text):
    """Preprocess Indonesian text for sentiment analysis."""
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+|@[\w]+|#[\w]+', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    punct = string.punctuation.replace('_', '')
    text = text.translate(str.maketrans(punct, ' ' * len(punct)))
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)
    text = re.sub(r'\s+', ' ', text).strip()

    words = _normalize_tokens(text.split())
    words = _apply_negation_scope(words)
    words = [
        w for w in words
        if w not in _final_stopwords and w not in NEGATION_WORDS and len(w) > 1
    ]
    cleaned = ' '.join(words).strip()
    return cleaned if cleaned else 'kosong'


# ---------------------------------------------------------------------------
# Load Model (cached)
# ---------------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def load_model():
    """Load the trained model pipeline from disk."""
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model.pkl')
    if not os.path.exists(model_path):
        ok = _download_model_if_needed(model_path)
        if not ok:
            st.error(
                "Model file not found and download is not configured. "
                "Set GDRIVE_MODEL_URL or GDRIVE_MODEL_ID to a public file."
            )
            st.stop()
    return joblib.load(model_path)


def _extract_gdrive_file_id(value):
    if not value:
        return None
    if "drive.google.com" in value:
        match = re.search(r"/d/([a-zA-Z0-9_-]+)", value)
        if match:
            return match.group(1)
        match = re.search(r"[?&]id=([a-zA-Z0-9_-]+)", value)
        if match:
            return match.group(1)
    if re.fullmatch(r"[a-zA-Z0-9_-]{10,}", value):
        return value
    return None


def _download_model_if_needed(model_path):
    gdrive_value = os.environ.get("GDRIVE_MODEL_URL") or os.environ.get("GDRIVE_MODEL_ID")
    file_id = _extract_gdrive_file_id(gdrive_value)
    if not file_id:
        return False
    with st.spinner("Mengunduh model dari Google Drive..."):
        try:
            downloaded = gdown.download(
                id=file_id,
                output=model_path,
                quiet=False,
            )
        except Exception as exc:
            st.error(f"Gagal mengunduh model: {exc}")
            return False
    return bool(downloaded) and os.path.exists(model_path)


def predict_sentiment(text, model_components):
    """Run preprocessing and inference on a single text."""
    text_clean = preprocess_text(text)
    pipe = model_components['pipeline']
    pred = pipe.predict([text_clean])[0]
    proba = pipe.predict_proba([text_clean])[0]
    labels = pipe.classes_
    proba_dict = {labels[i]: float(proba[i]) for i in range(len(labels))}
    return pred, proba_dict, text_clean


# ---------------------------------------------------------------------------
# UI Components
# ---------------------------------------------------------------------------

def render_topbar():
    st.markdown("""
    <div class="top-bar">
        <div class="top-bar-brand">
            <div class="top-bar-logo">NB</div>
            <div>
                <div class="top-bar-title">Analisis Sentimen</div>
                <div class="top-bar-subtitle">Naive Bayes + Lexicon Based</div>
            </div>
        </div>
        <div class="top-bar-badge">Multinomial NB &middot; TF-IDF &middot; Lexicon Features</div>
    </div>
    <div style="margin: -10px 0 24px 0; color: #4a5568; font-size: 14px; max-width: 800px; line-height: 1.6;">
        Aplikasi ini membantu membaca sentimen ulasan bahasa Indonesia: positif, netral, atau negatif. Cukup tempel teks, lalu sistem memberi hasil dan tingkat keyakinannya.
    </div>
    """, unsafe_allow_html=True)


def render_model_stats(model_components):
    params = model_components.get('best_params', {})
    alpha = params.get('alpha', '-')
    lex_w = params.get('lex_weight', '-')
    note = model_components.get('preprocess_note', '-')

    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-card">
            <div class="stat-label">Accuracy</div>
            <div class="stat-value" style="color: #1a1a2e;">82.06%</div>
            <div class="stat-sub">Test Set</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Macro F1</div>
            <div class="stat-value" style="color: #1a1a2e;">0.6873</div>
            <div class="stat-sub">3-Class Average</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Alpha</div>
            <div class="stat-value" style="color: #1a1a2e;">{alpha}</div>
            <div class="stat-sub">Smoothing</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Lexicon Weight</div>
            <div class="stat-value" style="color: #1a1a2e;">{lex_w}</div>
            <div class="stat-sub">Feature Weight</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_probability_bars(proba_dict):
    """Build probability bars HTML for each class."""
    rows = []
    order = ['positif', 'netral', 'negatif']
    for label in order:
        value = proba_dict.get(label, 0.0)
        pct = value * 100
        rows.append(
            f"<div class=\"prob-row\">"
            f"<div class=\"prob-label\">{label}</div>"
            f"<div class=\"prob-bar-track\">"
            f"<div class=\"prob-bar-fill {label}\" style=\"width: {pct:.1f}%\"></div>"
            f"</div>"
            f"<div class=\"prob-value\">{pct:.1f}%</div>"
            f"</div>"
        )
    return "".join(rows)


def render_result(pred, proba_dict, clean_text, original_text):
    """Render prediction result card."""
    sentiment_labels = {
        'positif': 'Positif',
        'negatif': 'Negatif',
        'netral': 'Netral'
    }
    bg_class = f"bg-{pred}"
    color_class = f"sentiment-{pred}"
    confidence = proba_dict.get(pred, 0.0) * 100

    st.markdown(f"""
    <div class="result-container {bg_class}">
        <div class="result-label">Hasil Prediksi</div>
        <div class="result-sentiment {color_class}">{sentiment_labels.get(pred, pred)}</div>
        <div class="result-confidence">Confidence: {confidence:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 16px'></div>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        prob_html = render_probability_bars(proba_dict)
        st.markdown(f"""
        <div class="card">
            <div class="card-header">Distribusi Probabilitas</div>
            {prob_html}
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown(f"""
        <div class="card">
            <div class="card-header">Detail Preprocessing</div>
            <div class="preprocess-label">Input Asli</div>
            <div class="preprocess-box">{original_text}</div>
            <div style="height: 12px"></div>
            <div class="preprocess-label">Setelah Preprocessing</div>
            <div class="preprocess-box">{clean_text}</div>
        </div>
        """, unsafe_allow_html=True)


def render_batch_results(results):
    """Render table for batch prediction results."""
    rows = []
    for r in results:
        tag_class = r['sentiment']
        confidence = r['confidence'] * 100
        rows.append(
            f"<tr>"
            f"<td style=\"max-width:300px; word-wrap:break-word;\">{r['text'][:120]}{'...' if len(r['text']) > 120 else ''}</td>"
            f"<td><span class=\"sent-tag {tag_class}\">{r['sentiment']}</span></td>"
            f"<td style=\"font-variant-numeric: tabular-nums;\">{confidence:.1f}%</td>"
            f"<td style=\"max-width:280px; word-wrap:break-word; font-family: monospace; font-size: 12px; color: #6b7280;\">{r['clean'][:100]}{'...' if len(r['clean']) > 100 else ''}</td>"
            f"</tr>"
        )
    rows_html = "".join(rows)

    st.markdown(textwrap.dedent(f"""
    <div class="card" style="overflow-x: auto;">
        <div class="card-header">Hasil Analisis Batch</div>
        <table class="batch-table">
            <thead>
                <tr>
                    <th>Teks Ulasan</th>
                    <th>Sentimen</th>
                    <th>Confidence</th>
                    <th>Teks Bersih</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """).strip(), unsafe_allow_html=True)


def render_pipeline_info():
    """Render the methodology / how-it-works section."""
    html = textwrap.dedent("""
    <style>
        .pipeline-card {
            background: #ffffff;
            border: 1px solid #e2e5e9;
            border-radius: 12px;
            padding: 28px;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        .pipeline-header {
            font-size: 14px;
            font-weight: 600;
            color: #1a1a2e;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 20px;
            padding-bottom: 14px;
            border-bottom: 1px solid #f0f2f5;
        }
        .pipeline-step {
            display: flex;
            align-items: flex-start;
            gap: 16px;
            padding: 16px 0;
            border-bottom: 1px solid #f0f2f5;
        }
        .pipeline-step:last-child { border-bottom: none; }
        .step-number {
            width: 32px;
            height: 32px;
            min-width: 32px;
            background-color: #1a1a2e;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            font-size: 13px;
            font-weight: 700;
        }
        .step-content h4 {
            font-size: 14px;
            font-weight: 600;
            color: #1a1a2e;
            margin: 0 0 4px 0;
        }
        .step-content p {
            font-size: 13px;
            color: #7c8597;
            margin: 0;
            line-height: 1.5;
        }
    </style>
    <div class="pipeline-card">
        <div class="pipeline-header">Cara Kerja Aplikasi</div>

        <div class="pipeline-step">
            <div class="step-number">1</div>
            <div class="step-content">
                <h4>Bersihkan Teks</h4>
                <p>Link, tag, angka, dan karakter khusus dibuang supaya teks lebih rapi.</p>
            </div>
        </div>

        <div class="pipeline-step">
            <div class="step-number">2</div>
            <div class="step-content">
                <h4>Ubah Kata Gaul</h4>
                <p>Kata gaul atau singkatan diubah ke bentuk baku agar maknanya jelas.</p>
            </div>
        </div>

        <div class="pipeline-step">
            <div class="step-number">3</div>
            <div class="step-content">
                <h4>Tangani Kata Negasi</h4>
                <p>Kata seperti "tidak" atau "gak" digabung ke kata berikutnya agar arti tidak terbalik.</p>
            </div>
        </div>

        <div class="pipeline-step">
            <div class="step-number">4</div>
            <div class="step-content">
                <h4>Buang Kata Umum</h4>
                <p>Kata yang tidak penting untuk sentimen dihapus, tapi kata penyangkal tetap disimpan.</p>
            </div>
        </div>

        <div class="pipeline-step">
            <div class="step-number">5</div>
            <div class="step-content">
                <h4>Ambil Ciri Sentimen</h4>
                <p>Model membaca pola kata dan kamus sentimen untuk mengenali kecenderungan isi ulasan.</p>
            </div>
        </div>

        <div class="pipeline-step">
            <div class="step-number">6</div>
            <div class="step-content">
                <h4>Hasil Akhir</h4>
                <p>Ulasan diberi label: positif, netral, atau negatif.</p>
            </div>
        </div>
    </div>
    """).strip()
    components.html(html, height=560)


def render_footer():
    st.markdown("""
    <div class="app-footer">
        Analisis Sentimen Naive Bayes + Lexicon &middot; Skripsi Project &middot;
        Model: Multinomial NB with TF-IDF + Lexicon Features
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Main Application
# ---------------------------------------------------------------------------
def main():
    # Load model
    model_components = load_model()

    # Top bar
    render_topbar()

    # Model performance stats
    render_model_stats(model_components)

    # Main content area
    tab_single, tab_batch, tab_info = st.tabs([
        "Analisis Tunggal", "Analisis Batch", "Tentang Model"
    ])

    # --- Tab 1: Single Analysis ---
    with tab_single:
        st.markdown("<h3 style='margin-bottom: 16px; color: #1a1a2e; font-size: 18px; font-weight: 600;'>Analisis Teks Tunggal</h3>", unsafe_allow_html=True)

        user_input = st.text_area(
            label="Masukkan teks ulasan",
            placeholder="Ketik atau tempel teks ulasan di sini...",
            height=140,
            key="single_input",
            label_visibility="collapsed"
        )

        col_btn, col_spacer = st.columns([1, 3])
        with col_btn:
            analyze_btn = st.button("Analisis Sentimen", key="btn_single", use_container_width=True)

        if analyze_btn and user_input.strip():
            with st.spinner("Memproses..."):
                pred, proba_dict, clean_text = predict_sentiment(user_input.strip(), model_components)
            render_result(pred, proba_dict, clean_text, user_input.strip())

        elif analyze_btn and not user_input.strip():
            st.warning("Masukkan teks ulasan terlebih dahulu.")

    # --- Tab 2: Batch Analysis ---
    with tab_batch:
        st.markdown("""
        <h3 style='margin-bottom: 8px; color: #1a1a2e; font-size: 18px; font-weight: 600;'>Analisis Batch</h3>
        <p style="font-size:13px; color:#7c8597; margin-bottom:16px;">
            Masukkan beberapa ulasan sekaligus, satu ulasan per baris.
        </p>
        """, unsafe_allow_html=True)

        batch_input = st.text_area(
            label="Masukkan beberapa ulasan (satu per baris)",
            placeholder="Ulasan 1\nUlasan 2\nUlasan 3\n...",
            height=200,
            key="batch_input",
            label_visibility="collapsed"
        )

        col_btn2, col_spacer2 = st.columns([1, 3])
        with col_btn2:
            batch_btn = st.button("Analisis Semua", key="btn_batch", use_container_width=True)

        if batch_btn and batch_input.strip():
            lines = [line.strip() for line in batch_input.strip().split('\n') if line.strip()]
            if len(lines) > 50:
                st.warning("Maksimum 50 ulasan per batch. Hanya 50 pertama yang diproses.")
                lines = lines[:50]

            results = []
            progress = st.progress(0)
            for i, line in enumerate(lines):
                pred, proba, clean = predict_sentiment(line, model_components)
                results.append({
                    'text': line,
                    'sentiment': pred,
                    'confidence': proba.get(pred, 0.0),
                    'clean': clean,
                    'proba': proba
                })
                progress.progress((i + 1) / len(lines))
            progress.empty()

            # Summary stats
            pos_count = sum(1 for r in results if r['sentiment'] == 'positif')
            neg_count = sum(1 for r in results if r['sentiment'] == 'negatif')
            neu_count = sum(1 for r in results if r['sentiment'] == 'netral')

            st.markdown(f"""
            <div class="stat-row">
                <div class="stat-card">
                    <div class="stat-label">Total</div>
                    <div class="stat-value" style="color: #1a1a2e;">{len(results)}</div>
                    <div class="stat-sub">Ulasan Dianalisis</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Positif</div>
                    <div class="stat-value sentiment-positif">{pos_count}</div>
                    <div class="stat-sub">{pos_count/len(results)*100:.0f}% dari total</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Netral</div>
                    <div class="stat-value sentiment-netral">{neu_count}</div>
                    <div class="stat-sub">{neu_count/len(results)*100:.0f}% dari total</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Negatif</div>
                    <div class="stat-value sentiment-negatif">{neg_count}</div>
                    <div class="stat-sub">{neg_count/len(results)*100:.0f}% dari total</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            render_batch_results(results)

        elif batch_btn and not batch_input.strip():
            st.warning("Masukkan teks ulasan terlebih dahulu.")

    # --- Tab 3: About the Model ---
    with tab_info:
        render_pipeline_info()

        st.markdown("""
        <div class="card">
            <div class="card-header">Performa Model per Kelas</div>
            <table class="batch-table">
                <thead>
                    <tr>
                        <th>Kelas</th>
                        <th>Precision</th>
                        <th>Recall</th>
                        <th>F1-Score</th>
                        <th>Support</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><span class="sent-tag negatif">Negatif</span></td>
                        <td>0.8413</td>
                        <td>0.8920</td>
                        <td>0.8659</td>
                        <td>6,268</td>
                    </tr>
                    <tr>
                        <td><span class="sent-tag netral">Netral</span></td>
                        <td>0.2563</td>
                        <td>0.3673</td>
                        <td>0.3019</td>
                        <td>1,225</td>
                    </tr>
                    <tr>
                        <td><span class="sent-tag positif">Positif</span></td>
                        <td>0.9609</td>
                        <td>0.8360</td>
                        <td>0.8941</td>
                        <td>6,996</td>
                    </tr>
                    <tr style="background: #f8f9fb; font-weight: 600;">
                        <td>Macro Avg</td>
                        <td>0.6861</td>
                        <td>0.6985</td>
                        <td>0.6873</td>
                        <td>14,489</td>
                    </tr>
                    <tr style="background: #f8f9fb;">
                        <td>Weighted Avg</td>
                        <td>0.8496</td>
                        <td>0.8206</td>
                        <td>0.8318</td>
                        <td>14,489</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-header">Informasi Dataset</div>
            <table class="batch-table">
                <tbody>
                    <tr>
                        <td style="font-weight:600; width:200px;">Sumber Data</td>
                        <td>Ulasan Google Play Store - Shopee 12.12</td>
                    </tr>
                    <tr>
                        <td style="font-weight:600;">Jumlah Data</td>
                        <td>85.290 ulasan (setelah dibersihkan)</td>
                    </tr>
                    <tr>
                        <td style="font-weight:600;">Sebaran Label</td>
                        <td>Positif (39.924) | Netral (8.538) | Negatif (36.828)</td>
                    </tr>
                    <tr>
                        <td style="font-weight:600;">Aturan Label</td>
                        <td>Rating bintang: 1-2 negatif, 3 netral, 4-5 positif</td>
                    </tr>
                    <tr>
                        <td style="font-weight:600;">Pembersihan Label</td>
                        <td>12.848 data dihapus (15,1%) karena tidak sesuai isi teks</td>
                    </tr>
                    <tr>
                        <td style="font-weight:600;">Pembagian Data</td>
                        <td>80% latih (57.952) | 20% uji (14.489)</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    render_footer()


if __name__ == '__main__':
    main()
