from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from data.metrics import MetricsBundle
from ui.components import render_kpi_cards, render_page_header


def _render_confusion_matrix(confusion_matrix: pd.DataFrame | None) -> None:
    if confusion_matrix is None or confusion_matrix.empty:
        st.info("Confusion matrix belum tersedia.")
        return

    fig = px.imshow(
        confusion_matrix.values,
        text_auto=True,
        x=confusion_matrix.columns,
        y=confusion_matrix.index,
        color_continuous_scale="Blues",
        labels=dict(x="Predicted", y="Actual", color="Count"),
    )
    fig.update_layout(
        height=360,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e2e8f0"),
        margin=dict(l=20, r=20, t=10, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)


def _render_cv_scores(cv_scores: pd.DataFrame | None) -> None:
    st.markdown("<div class='section-title' style='margin-top: 16px;'>5-Fold Cross Validation Results</div>", unsafe_allow_html=True)
    if cv_scores is None or cv_scores.empty:
        st.info("Data Cross Validation belum tersedia.")
        return

    cv_scores = cv_scores.copy()
    cv_scores['fold_str'] = 'Fold ' + cv_scores['fold'].astype(str)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cv_scores['fold_str'], 
        y=cv_scores['accuracy'],
        name='Accuracy',
        marker_color='#3b82f6',
        text=cv_scores['accuracy'].apply(lambda x: f"{x:.4f}"),
        textposition='outside'
    ))
    fig.add_trace(go.Bar(
        x=cv_scores['fold_str'], 
        y=cv_scores['macro_f1'],
        name='Macro F1',
        marker_color='#10b981',
        text=cv_scores['macro_f1'].apply(lambda x: f"{x:.4f}"),
        textposition='outside'
    ))

    mean_acc = cv_scores['accuracy'].mean()
    mean_f1 = cv_scores['macro_f1'].mean()

    fig.add_hline(y=mean_acc, line_dash="dash", line_color="#3b82f6", annotation_text=f"Mean Acc: {mean_acc:.4f}", annotation_position="top right")
    fig.add_hline(y=mean_f1, line_dash="dash", line_color="#10b981", annotation_text=f"Mean F1: {mean_f1:.4f}", annotation_position="top right")

    fig.update_layout(
        barmode='group',
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e2e8f0"),
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        yaxis=dict(range=[0, 1.1], gridcolor='rgba(148,163,184,0.1)')
    )
    st.plotly_chart(fig, use_container_width=True)


def render_performance(bundle: MetricsBundle) -> None:
    render_page_header(
        "Performa Model",
        "Ringkasan metrik utama, confusion matrix, dan laporan per kelas.",
    )

    if bundle.error:
        st.warning(bundle.error)

    metrics = bundle.metrics or {}
    def _fmt(value):
        return f"{value:.4f}" if isinstance(value, (int, float)) else "-"

    kpis = [
        {"label": "Accuracy", "value": _fmt(metrics.get("accuracy")), "sub": "Test set"},
        {"label": "Macro F1", "value": _fmt(metrics.get("macro_f1")), "sub": "3-class"},
        {
            "label": "Macro Precision",
            "value": _fmt(metrics.get("macro_precision")),
            "sub": "Average",
        },
        {"label": "Macro Recall", "value": _fmt(metrics.get("macro_recall")), "sub": "Average"},
    ]
    render_kpi_cards(kpis)

    col_left, col_right = st.columns([1, 1])
    with col_left:
        st.markdown("<div class='section-title'>Confusion Matrix</div>", unsafe_allow_html=True)
        _render_confusion_matrix(bundle.confusion_matrix)
    with col_right:
        st.markdown("<div class='section-title'>Classification Report</div>", unsafe_allow_html=True)
        class_metrics = metrics.get("class_metrics") or []
        if class_metrics:
            df = pd.DataFrame(class_metrics)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Classification report belum tersedia.")

    _render_cv_scores(bundle.cv_scores)
