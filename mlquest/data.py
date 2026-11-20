"""Dataset helpers: download once, cache forever, load anywhere (Windows, macOS, Linux, Colab)."""

from __future__ import annotations

import shutil
import tarfile
import zipfile
from pathlib import Path

import pandas as pd
import requests
from tqdm.auto import tqdm

from .env import DATA_DIR

HF_PARQUET_API = "https://huggingface.co/api/datasets/{repo}/parquet/{config}/{split}"


def download(url: str, dest: str | Path, force: bool = False, chunk: int = 1 << 20) -> Path:
    """Download ``url`` to ``dest`` with a progress bar. Skips the download if the file exists."""
    dest = Path(dest)
    if dest.exists() and dest.stat().st_size > 0 and not force:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with requests.get(url, stream=True, timeout=60, headers={"User-Agent": "mlquest/2.0"}) as r:
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0)) or None
        with open(tmp, "wb") as f, tqdm(total=total, unit="B", unit_scale=True, desc=f"⬇️  {dest.name}") as bar:
            for block in r.iter_content(chunk):
                f.write(block)
                bar.update(len(block))
    tmp.replace(dest)
    return dest


def extract(archive: str | Path, dest: str | Path | None = None) -> Path:
    """Extract a .zip / .tar(.gz) archive next to itself (or into ``dest``)."""
    archive = Path(archive)
    dest = Path(dest) if dest else archive.parent
    dest.mkdir(parents=True, exist_ok=True)
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as z:
            z.extractall(dest)
    elif tarfile.is_tarfile(archive):
        with tarfile.open(archive) as t:
            t.extractall(dest, filter="data") if hasattr(tarfile, "data_filter") else t.extractall(dest)
    else:
        raise ValueError(f"Unknown archive format: {archive}")
    return dest


def download_and_extract(url: str, name: str, marker: str | None = None) -> Path:
    """Download an archive into ``data/<name>/`` and extract it once.

    ``marker`` is a path (relative to ``data/<name>``) that proves the extraction already happened.
    """
    folder = DATA_DIR / name
    if marker and (folder / marker).exists():
        return folder
    archive = download(url, folder / Path(url.split("?")[0]).name)
    extract(archive, folder)
    archive.unlink(missing_ok=True)  # save disk space
    return folder


def hf_parquet(repo: str, split: str = "train", config: str = "default") -> pd.DataFrame:
    """Load a split of a Hugging Face dataset as a DataFrame, through its Parquet export.

    No account, no token, no ``datasets`` magic: just files you can inspect in ``data/hf/``.
    """
    files = requests.get(HF_PARQUET_API.format(repo=repo, config=config, split=split), timeout=60).json()
    if isinstance(files, dict) and "error" in files:
        raise RuntimeError(files["error"])
    frames = []
    for i, url in enumerate(files):
        local = DATA_DIR / "hf" / repo.replace("/", "__") / config / f"{split}-{i:03d}.parquet"
        frames.append(pd.read_parquet(download(url, local)))
    return pd.concat(frames, ignore_index=True)


def openml(data_id: int) -> pd.DataFrame:
    """Fetch an OpenML dataset (cached in ``data/openml``) as a single DataFrame (features + target)."""
    from sklearn.datasets import fetch_openml

    bunch = fetch_openml(data_id=data_id, as_frame=True, data_home=str(DATA_DIR / "openml"), parser="auto")
    return bunch.frame


def disk_usage() -> pd.DataFrame:
    """How much space each downloaded dataset uses (delete folders in ``data/`` freely)."""
    rows = []
    for p in sorted(DATA_DIR.iterdir()):
        size = sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) if p.is_dir() else p.stat().st_size
        rows.append({"dataset": p.name, "MB": round(size / 1e6, 1)})
    return pd.DataFrame(rows)


def clean(name: str) -> None:
    """Delete ``data/<name>`` to free disk space."""
    shutil.rmtree(DATA_DIR / name, ignore_errors=True)
