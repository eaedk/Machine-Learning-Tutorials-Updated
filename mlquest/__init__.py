"""mlquest: the small toolkit shared by every notebook of the course.

    from mlquest import *

gives you paths (ROOT, DATA_DIR, RUNS_DIR), reproducibility (seed_everything, get_device),
data loaders (download, hf_parquet, openml), the game layer (quest, checkpoint, check, badge)
and competition helpers (Leaderboard, make_submission).
"""

from .compete import Leaderboard, make_submission
from .data import clean, disk_usage, download, download_and_extract, extract, hf_parquet, openml
from .env import (
    DATA_DIR,
    IS_COLAB,
    IS_WINDOWS,
    NUM_WORKERS,
    ROOT,
    RUNS_DIR,
    SUBMISSIONS_DIR,
    get_device,
    seed_everything,
    system_report,
)
from .game import badge, check, checkpoint, progress, quest, reset_progress
from .viz import PALETTE, set_style, show_images

__all__ = [
    "ROOT", "DATA_DIR", "RUNS_DIR", "SUBMISSIONS_DIR", "IS_COLAB", "IS_WINDOWS", "NUM_WORKERS",
    "seed_everything", "get_device", "system_report",
    "download", "extract", "download_and_extract", "hf_parquet", "openml", "disk_usage", "clean",
    "quest", "checkpoint", "check", "badge", "progress", "reset_progress",
    "Leaderboard", "make_submission",
    "set_style", "show_images", "PALETTE",
]
__version__ = "2.0.0"
