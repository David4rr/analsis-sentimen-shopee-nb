from __future__ import annotations

import textwrap

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from data.metrics import MetricsBundle
from data.model import ModelBundle
from ui.components import format_percent, render_kpi_cards, render_page_header


def _render_dataset_chart(dataset_summary: dict) -> None:
    dist = dataset_summary.get("label_distribution") or {}
    if not dist:
        st.info("Distribusi label belum tersedia.")
        return

    labels = list(dist.keys())
    values = [dist[label] for label in labels]
    colors = {
        "positif": "#22c55e",
        "netral": "#f59e0b",
        "negatif": "#ef4444",
    }
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.6,
                marker=dict(colors=[colors.get(label, "#64748b") for label in labels]),
                textinfo="label+percent",
            )
        ]
    )
    fig.update_layout(
        height=320,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e2e8f0"),
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)


def _plot_top_words(feature_names, log_probs, label_name, colorscale_name):
    top_indices = np.argsort(log_probs)[-15:]
    top_words = [feature_names[i] for i in top_indices]
    top_scores = [np.exp(log_probs[i]) * 1000 for i in top_indices]
    
    fig = go.Figure(go.Bar(
        x=top_scores,
        y=top_words,
        orientation='h',
        marker=dict(
            color=top_scores,
            colorscale=colorscale_name,
            showscale=False
        )
    ))
    fig.update_layout(
        height=350,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e2e8f0"),
        margin=dict(l=20, r=20, t=10, b=20),
        xaxis_title="Relative Importance"
    )
    st.plotly_chart(fig, use_container_width=True)


def _render_top_keywords(model_bundle: ModelBundle) -> None:
    if not model_bundle.ready or not model_bundle.model:
        st.info("Top keywords belum tersedia karena model tidak termuat.")
        return
        
    try:
        pipe = model_bundle.model['pipeline']
        fu = pipe.named_steps['features']
        tfidf = fu.transformer_list[0][1]
        lexicon = fu.transformer_list[1][1]
        
        tfidf_names = tfidf.get_feature_names_out()
        lexicon_names = lexicon.get_feature_names_out()
        feature_names = np.concatenate([tfidf_names, lexicon_names])
        
        clf = pipe.named_steps['clf']
        
        tabs = st.tabs(["Top Kata Positif", "Top Kata Negatif"])
        
        with tabs[0]:
            _plot_top_words(feature_names, clf.feature_log_prob_[2], "Positif", "Tealgrn")
            
        with tabs[1]:
            _plot_top_words(feature_names, clf.feature_log_prob_[0], "Negatif", "Sunsetdark")
            
    except Exception as e:
        st.warning(f"Gagal memuat top keywords: {e}")



def render_dashboard(bundle: MetricsBundle, model_bundle: ModelBundle) -> None:
    render_page_header(
        "Dashboard",
        "Ringkasan performa model dan statistik data untuk analisis sentimen Shopee.",
    )

    if bundle.error:
        st.warning(bundle.error)

    metrics = bundle.metrics or {}
    dataset_summary = bundle.dataset_summary or {}

    macro_f1 = metrics.get("macro_f1")
    total_clean = dataset_summary.get("total_clean")
    kpis = [
        {
            "label": "Accuracy",
            "value": format_percent(metrics.get("accuracy")),
            "sub": "Test set",
        },
        {
            "label": "Macro F1",
            "value": f"{macro_f1:.4f}" if isinstance(macro_f1, (int, float)) else "-",
            "sub": "3-class average",
        },
        {
            "label": "Dataset",
            "value": f"{total_clean:,}".replace(",", ".") if isinstance(total_clean, int) else "-",
            "sub": "Ulasan bersih",
        },
        {
            "label": "Model",
            "value": "NB + Lexicon",
            "sub": "Pipeline",
        },
    ]
    render_kpi_cards(kpis)

    col_left, col_right = st.columns([1.2, 1])
    with col_left:
        st.markdown("<div class='section-title' style='margin-top: 16px;'>Distribusi Sentimen</div>", unsafe_allow_html=True)
        _render_dataset_chart(dataset_summary)
    with col_right:
        st.markdown("<div class='section-title' style='margin-top: 16px;'>Info Model</div>", unsafe_allow_html=True)
        params = metrics.get("best_params", {}) if metrics else {}
        preprocess_note = metrics.get("preprocess_note", "-")
        st.markdown(
            textwrap.dedent(f"""
            <div class="card">
                <div><b>Alpha:</b> {params.get("alpha", "-")}</div>
                <div><b>Fit Prior:</b> {params.get("fit_prior", "-")}</div>
                <div><b>Lexicon Weight:</b> {params.get("lex_weight", "-")}</div>
                <div style="margin-top: 10px;"><b>Preprocess:</b> {preprocess_note}</div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    st.markdown("<div class='section-title' style='margin-top: 16px;'>Top Kata Kunci (Keywords)</div>", unsafe_allow_html=True)
    _render_top_keywords(model_bundle)

