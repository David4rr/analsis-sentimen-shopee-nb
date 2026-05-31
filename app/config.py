from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"
METRICS_DIR = ASSETS_DIR / "metrics"

REQUIRED_METRICS_FILES = (
    "metrics.json",
    "cv_scores.csv",
    "confusion_matrix.csv",
    "dataset_summary.json",
)
