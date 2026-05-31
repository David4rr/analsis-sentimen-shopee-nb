from __future__ import annotations

import math
import textwrap
from typing import Iterable

import streamlit as st


def render_sidebar_brand() -> None:
    st.markdown(
        textwrap.dedent("""
        <div class="sidebar-brand">
            <div style="font-size: 2rem;">🛒</div>
            <div class="sidebar-title">Shopee Sentiment</div>
            <div class="sidebar-subtitle">Naive Bayes + Lexicon</div>
        </div>
        """),
        unsafe_allow_html=True,
    )


def render_page_header(title: str, subtitle: str) -> None:
    st.markdown(
        textwrap.dedent(f"""
        <div class="page-header">
            <div class="page-title">{title}</div>
            <div class="page-subtitle">{subtitle}</div>
        </div>
        """),
        unsafe_allow_html=True,
    )


def render_kpi_cards(kpis: Iterable[dict]) -> None:
    cards_html = []
    for item in kpis:
        label = item.get("label", "-")
        value = item.get("value", "-")
        sub = item.get("sub")
        cards_html.append(
            textwrap.dedent(f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-sub">{sub or "&nbsp;"}</div>
            </div>
            """)
        )
    st.markdown(f"<div class=\"kpi-grid\">{''.join(cards_html)}</div>", unsafe_allow_html=True)


def render_probability_bars(proba_dict: dict[str, float]) -> str:
    rows = []
    order = ["positif", "netral", "negatif"]
    for label in order:
        value = float(proba_dict.get(label, 0.0))
        pct = max(0.0, min(100.0, value * 100))
        rows.append(f'<div class="prob-row"><div class="prob-label">{label}</div><div class="prob-bar-track"><div class="prob-bar-fill {label}" style="width: {pct:.1f}%"></div></div><div class="prob-value">{pct:.1f}%</div></div>')
    return "".join(rows)


def format_percent(value: float | None, digits: int = 2) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "-"
    return f"{value * 100:.{digits}f}%"
