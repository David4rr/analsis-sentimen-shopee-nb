from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path

import pandas as pd
import streamlit as st

from config import METRICS_DIR, REQUIRED_METRICS_FILES
from data.gdrive import download_file, download_folder, extract_gdrive_file_id


_FILE_ENV_MAP = {
    "metrics.json": ("GDRIVE_METRICS_JSON_URL", "GDRIVE_METRICS_JSON_ID"),
    "cv_scores.csv": ("GDRIVE_CV_SCORES_URL", "GDRIVE_CV_SCORES_ID"),
    "confusion_matrix.csv": ("GDRIVE_CONFUSION_MATRIX_URL", "GDRIVE_CONFUSION_MATRIX_ID"),
    "dataset_summary.json": ("GDRIVE_DATASET_SUMMARY_URL", "GDRIVE_DATASET_SUMMARY_ID"),
}


@dataclass(frozen=True)
class MetricsBundle:
    metrics: dict
    cv_scores: pd.DataFrame | None
    confusion_matrix: pd.DataFrame | None
    dataset_summary: dict
    missing_files: tuple[str, ...]
    error: str | None


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _load_cv_scores(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    df = pd.read_csv(path)
    if df.empty:
        return None
    return df


def _load_confusion_matrix(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    df = pd.read_csv(path, index_col=0)
    if df.empty:
        return None
    return df


def _resolve_env_file_id(names: tuple[str, str]) -> str | None:
    value = os.environ.get(names[0]) or os.environ.get(names[1])
    return extract_gdrive_file_id(value)


def _attempt_download_metrics(missing: list[str]) -> list[str]:
    folder_value = os.environ.get("GDRIVE_METRICS_FOLDER_URL") or os.environ.get(
        "GDRIVE_METRICS_FOLDER_ID"
    )
    if folder_value:
        folder_id = extract_gdrive_file_id(folder_value)
        if folder_id:
            download_folder(folder_id, METRICS_DIR, "metrics assets")
        else:
            st.error("GDRIVE_METRICS_FOLDER_URL/ID tidak valid.")

    remaining = [name for name in missing if not (METRICS_DIR / name).exists()]
    for filename in remaining:
        env_names = _FILE_ENV_MAP.get(filename)
        if not env_names:
            continue
        file_id = _resolve_env_file_id(env_names)
        if not file_id:
            continue
        download_file(file_id, METRICS_DIR / filename, filename)

    return [name for name in missing if not (METRICS_DIR / name).exists()]


def _ensure_metrics_assets() -> tuple[tuple[str, ...], str | None]:
    METRICS_DIR.mkdir(parents=True, exist_ok=True)
    missing = [name for name in REQUIRED_METRICS_FILES if not (METRICS_DIR / name).exists()]
    if not missing:
        return tuple(), None

    remaining = _attempt_download_metrics(missing)
    if remaining:
        return tuple(remaining), "Sebagian metrics assets belum tersedia."
    return tuple(), None


@st.cache_data(show_spinner=False)
def load_metrics_bundle() -> MetricsBundle:
    missing, error = _ensure_metrics_assets()
    metrics = _load_json(METRICS_DIR / "metrics.json")
    dataset_summary = _load_json(METRICS_DIR / "dataset_summary.json")
    cv_scores = _load_cv_scores(METRICS_DIR / "cv_scores.csv")
    confusion_matrix = _load_confusion_matrix(METRICS_DIR / "confusion_matrix.csv")
    return MetricsBundle(
        metrics=metrics,
        cv_scores=cv_scores,
        confusion_matrix=confusion_matrix,
        dataset_summary=dataset_summary,
        missing_files=missing,
        error=error,
    )
