from __future__ import annotations

import streamlit as st
import textwrap

from data.metrics import MetricsBundle
from ui.components import render_page_header


def render_about(bundle: MetricsBundle) -> None:
    render_page_header(
        "Tentang Sistem",
        "Arsitektur, metodologi, dan spesifikasi sistem analisis sentimen.",
    )

    dataset_summary = bundle.dataset_summary or {}
    total_clean = dataset_summary.get("total_clean", "-")
    train_size = dataset_summary.get("train_size", "-")
    test_size = dataset_summary.get("test_size", "-")

    tab1, tab2, tab3 = st.tabs(["Arsitektur", "Metodologi", "Spesifikasi"])

    with tab1:
        st.markdown(
            textwrap.dedent("""
            ### Arsitektur Sistem

            ```
            ┌─────────────────────────────────────────────────┐
            │                  Jupyter Notebook               │
            │  Dataset → Preprocessing → Training → Save      │
            └──────────────────────┬──────────────────────────┘
                                   │ models/*.pkl
            ┌──────────────────────▼──────────────────────────┐
            │              app.py (Streamlit UI)              │
            │  Load Models → Live Prediction → Visualization  │
            └─────────────────────────────────────────────────┘
            ```

            **Alur Analisis Sentimen:**
            Teks Ulasan &rarr; Preprocessing &rarr; Feature Extraction (TF-IDF + Lexicon) &rarr; Multinomial Naive Bayes &rarr; Prediksi Sentimen
            
            ### Modul:

            | Direktori / File | Deskripsi |
            |------------------|-----------|
            | `app/config.py` | Konfigurasi konstanta & *path* file |
            | `app/main.py` | *Entry point* aplikasi Streamlit & *routing* halaman |
            | `app/data/` | Modul pengelolaan *download* data, evaluasi (*metrics*), dan *model* |
            | `app/ui/` | Komponen antarmuka pengguna (UI) kustom dan injeksi CSS |
            | `app/views/` | Kode tampilan halaman (Dasbor, Prediksi, Performa, dan Tentang) |
            | `assets/metrics/` | File statis berupa hasil evaluasi (`cv_scores.csv`, `metrics.json`) |
            | `model.pkl` | File model Naive Bayes & TF-IDF terkompresi |
            | `requirements.txt` | Daftar dependensi *library* Python untuk *deployment* |
            """)
        )

    with tab2:
        st.markdown(
            textwrap.dedent("""
            ### Metodologi

            | Tahapan | Implementasi |
            |------|--------------|
            | 1. Data Source | Ulasan Shopee |
            | 2. Preprocessing | Cleaning, Normalisasi Slang, Stopword Removal, Stemming (Sastrawi) |
            | 3. Feature Extraction | Gabungan TF-IDF (5000 features) dan Lexicon-Based Score |
            | 4. Modeling | Multinomial Naive Bayes |
            | 5. Evaluation | Accuracy, Precision, Recall, F1-Score, Confusion Matrix |
            | 6. Deployment | Live prediction via Streamlit web app |

            ### Lexicon-Based Features
            - **Positive & Negative Lexicon**: Menggunakan kamus manual untuk Bahasa Indonesia.
            - Menghitung jumlah kata positif, kata negatif, dan selisih skor (sentiment score).
            
            ### Multinomial Naive Bayes
            - **Classifier**: Multinomial Naive Bayes dengan Laplace smoothing (alpha=1.0).
            - **Fitur Gabungan**: Menggabungkan probabilitas TF-IDF dengan skor lexicon menggunakan `scipy.sparse.hstack`.
            """)
        )

    with tab3:
        st.markdown(
            textwrap.dedent(f"""
            ### Spesifikasi Teknis

            | Parameter | Nilai |
            |-----------|-------|
            | Bahasa | Python |
            | Framework UI | Streamlit |
            | ML Library | scikit-learn, scipy |
            | Visualisasi | Plotly, Chart.js / Matplotlib |
            | NLP | Sastrawi |
            | TF-IDF Max Features | 5000 |
            | Model Classifier | MultinomialNB |
            
            ### Statistik Dataset

            | Keterangan | Jumlah |
            |------------|--------|
            | **Total Ulasan Bersih** | {total_clean} |
            | **Data Latih (Train)** | {train_size} |
            | **Data Uji (Test)** | {test_size} |
            """)
        )
