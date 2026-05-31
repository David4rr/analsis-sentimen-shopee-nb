import sys
import os
import streamlit as st

# Ensure `app` package modules (app/data, app/pages, app/ui) importable
sys.path.insert(0, os.path.dirname(__file__))

from data.metrics import load_metrics_bundle
from data.model import load_model_bundle
from views.about import render_about
from views.dashboard import render_dashboard
from views.performance import render_performance
from views.prediction import render_prediction
from ui.components import render_sidebar_brand
from ui.theme import apply_theme


def main() -> None:
    st.set_page_config(
        page_title="Shopee Sentiment Analyzer",
        page_icon="🛒",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    apply_theme()

    model_bundle = load_model_bundle()
    metrics_bundle = load_metrics_bundle()

    with st.sidebar:
        render_sidebar_brand()
        st.markdown("---")
        page = st.radio(
            "Navigasi",
            ["Dashboard", "Prediksi Langsung", "Performa Model", "Tentang Sistem"],
            label_visibility="collapsed",
        )
        st.markdown("---")
        if model_bundle.ready:
            st.success("Model siap digunakan")
        else:
            st.error("Model belum tersedia")
            if model_bundle.error:
                st.caption(model_bundle.error)

        if metrics_bundle.missing_files:
            st.warning("Metrics belum lengkap")
            st.caption(", ".join(metrics_bundle.missing_files))
        else:
            st.success("Metrics siap digunakan")

    if page == "Dashboard":
        render_dashboard(metrics_bundle, model_bundle)
    elif page == "Prediksi Langsung":
        render_prediction(model_bundle)
    elif page == "Performa Model":
        render_performance(metrics_bundle)
    else:
        render_about(metrics_bundle)


if __name__ == "__main__":
    main()
