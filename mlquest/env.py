"""Environment helpers: reproducibility, hardware detection and a quick health check."""

from __future__ import annotations

import os
import platform
import random
import sys
from pathlib import Path

import numpy as np


def find_root(start: Path | None = None) -> Path:
    """Return the repository root (the folder that contains ``mlquest/``)."""
    here = Path(start or Path.cwd()).resolve()
    for p in [here, *here.parents]:
        if (p / "mlquest").is_dir() and (p / "pyproject.toml").exists():
            return p
    return here


ROOT = find_root(Path(__file__).parent)
DATA_DIR = ROOT / "data"          # every dataset lands here (git-ignored)
RUNS_DIR = ROOT / "runs"          # models, logs, predictions (git-ignored)
SUBMISSIONS_DIR = ROOT / "submissions"
for _d in (DATA_DIR, RUNS_DIR, SUBMISSIONS_DIR):
    _d.mkdir(exist_ok=True)

IS_WINDOWS = os.name == "nt"
IS_COLAB = "google.colab" in sys.modules
# Jupyter + multiprocessing is fragile on Windows/macOS ("spawn" start method):
# 0 workers is always safe; bump it on Linux for speed.
NUM_WORKERS = 0 if (IS_WINDOWS or platform.system() == "Darwin") else min(4, os.cpu_count() or 1)


_SEED = 42


def _seed_torch(seed: int) -> None:
    torch = sys.modules["torch"]
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def seed_everything(seed: int = 42) -> int:
    """Make experiments repeatable: same seed -> same split -> same score.

    PyTorch is seeded only if it is already imported (``get_device()`` seeds it when it loads it).
    We never import it here on purpose: on macOS, loading PyTorch next to LightGBM or XGBoost
    in the same process crashes (two copies of the OpenMP runtime), and tabular notebooks don't need it.
    """
    global _SEED
    _SEED = seed
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    if "torch" in sys.modules:
        _seed_torch(seed)
    return seed


def get_device(verbose: bool = True) -> str:
    """Pick the fastest available accelerator: NVIDIA GPU > Apple GPU > CPU."""
    try:
        import torch
    except ImportError:
        return "cpu"
    _seed_torch(_SEED)
    if torch.cuda.is_available():
        device = "cuda"
        name = torch.cuda.get_device_name(0)
    elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        device = "mps"
        name = "Apple Silicon GPU (Metal)"
    else:
        device = "cpu"
        name = platform.processor() or "CPU"
    if verbose:
        print(f"⚙️  Using device: {device}  ({name})")
    return device


def system_report(packages: tuple[str, ...] = ()) -> None:
    """Print a friendly summary of your machine and the key library versions."""
    from importlib.metadata import PackageNotFoundError, version

    exe = Path(sys.executable)
    exe = exe.relative_to(ROOT) if ROOT in exe.parents else exe
    print(f"🐍 Python   {platform.python_version()}  ({exe})")
    print(f"💻 System   {platform.system()} {platform.release()} · {platform.machine()}")
    print(f"📁 Repo     {ROOT.name}")
    for pkg in packages:
        try:
            print(f"   ✔ {pkg:<26} {version(pkg)}")
        except PackageNotFoundError:
            print(f"   ✘ {pkg:<26} not installed  →  uv sync --all-groups")
    get_device()
