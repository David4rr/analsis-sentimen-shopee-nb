from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path

import joblib
import streamlit as st

from config import BASE_DIR
from data.gdrive import download_file, extract_gdrive_file_id


MODEL_PATH = BASE_DIR / "model.pkl"


@dataclass(frozen=True)
class ModelBundle:
    ready: bool
    model: dict | None
    error: str | None


@st.cache_resource(show_spinner=False)
def load_model_bundle() -> ModelBundle:
    if MODEL_PATH.exists():
        try:
            return ModelBundle(True, joblib.load(MODEL_PATH), None)
        except Exception as exc:  # noqa: BLE001 - surface exact error
            return ModelBundle(False, None, f"Gagal memuat model: {exc}")

    gdrive_value = os.environ.get("GDRIVE_MODEL_URL") or os.environ.get("GDRIVE_MODEL_ID")
    file_id = extract_gdrive_file_id(gdrive_value)
    if not file_id:
        return ModelBundle(
            False,
            None,
            "Model belum tersedia. Set GDRIVE_MODEL_URL atau GDRIVE_MODEL_ID.",
        )

    if not download_file(file_id, MODEL_PATH, "model"):
        return ModelBundle(False, None, "Gagal mengunduh model dari Google Drive.")

    try:
        return ModelBundle(True, joblib.load(MODEL_PATH), None)
    except Exception as exc:  # noqa: BLE001 - surface exact error
        return ModelBundle(False, None, f"Gagal memuat model: {exc}")
