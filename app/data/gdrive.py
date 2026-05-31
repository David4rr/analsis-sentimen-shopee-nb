from __future__ import annotations

import re
from pathlib import Path

import gdown
import streamlit as st


def extract_gdrive_file_id(value: str | None) -> str | None:
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


def download_file(file_id: str, output_path: Path, label: str) -> bool:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with st.spinner(f"Mengunduh {label} dari Google Drive..."):
        downloaded = gdown.download(id=file_id, output=str(output_path), quiet=False)
    if not downloaded or not output_path.exists():
        st.error(f"Gagal mengunduh {label} dari Google Drive.")
        return False
    return True


def download_folder(folder_id: str, output_dir: Path, label: str) -> bool:
    if not hasattr(gdown, "download_folder"):
        st.error("gdown tidak mendukung download_folder. Gunakan ID per file.")
        return False
    output_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    with st.spinner(f"Mengunduh {label} dari Google Drive..."):
        result = gdown.download_folder(url=url, output=str(output_dir), quiet=False)
    if not result:
        st.error(f"Gagal mengunduh {label} dari Google Drive.")
        return False
    return True
