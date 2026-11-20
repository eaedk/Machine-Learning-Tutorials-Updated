# ⚙️ Installation guide (Windows · macOS · Linux)

This course uses **[uv](https://docs.astral.sh/uv/)**, a Python package and project manager written in Rust by Astral
(2024). It replaces `pip`, `venv`, `pip-tools`, `pyenv` and `virtualenv` with a single tool, and it is **10 to 100×
faster** than pip. One command installs the right Python version, creates an isolated environment and installs the
exact library versions pinned in `uv.lock`, so everyone gets the same setup.

> **Why an environment?** Each project gets its own folder of libraries (`.venv/`). Projects can't break each
> other, and deleting `.venv/` gives you a clean slate.

---

## 1. Install uv (once per computer)

**macOS / Linux** (terminal):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows** (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Alternatives: `brew install uv` (macOS), `winget install --id=astral-sh.uv -e` (Windows), `pipx install uv`.

Close and reopen your terminal, then check:

```bash
uv --version
```

You do **not** need to install Python yourself: uv downloads the version written in `.python-version` (3.12).

## 2. Get the course

```bash
git clone https://github.com/eaedk/Machine-Learning-Tutorials-Updated.git
cd Machine-Learning-Tutorials-Updated
```

(No git? Click **Code → Download ZIP** on GitHub and unzip it.)

## 3. Create the environment and install the libraries

The libraries are grouped by track so you only download what you need:

| Command | Installs | Disk |
|---|---|---|
| `uv sync` | core: numpy, pandas, scikit-learn, matplotlib, seaborn, JupyterLab | ~0.5 GB |
| `uv sync --group tabular` | + LightGBM, XGBoost, CatBoost, Optuna, SHAP, imbalanced-learn | ~0.8 GB |
| `uv sync --group timeseries` | + statsmodels, aeon, PyTorch, Chronos | ~1.5 GB |
| `uv sync --group vision` | + PyTorch, torchvision, timm, Ultralytics YOLO, segmentation-models-pytorch, PyAV | ~2 GB |
| `uv sync --group nlp` | + PyTorch, Transformers, Datasets, Sentence-Transformers | ~2 GB |
| `uv sync --group audio` | + PyTorch, Transformers, librosa | ~1.5 GB |
| `uv sync --all-groups` | everything | ~2.5 GB |

Groups can be combined: `uv sync --group tabular --group nlp`.

`uv sync` creates a `.venv/` folder inside the project. Run it again whenever `pyproject.toml` changes (after a
`git pull`, for example).

## 4. Activate the environment (optional but handy)

Activation makes `python` and `jupyter` point to the project's environment in the current terminal.

| System | Command |
|---|---|
| macOS / Linux (bash, zsh) | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows cmd | `.venv\Scripts\activate.bat` |
| fish | `source .venv/bin/activate.fish` |

Your prompt now starts with `(machine-learning-tutorials-updated)`. Leave with `deactivate`.

> **PowerShell says "running scripts is disabled"?** Run once:
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

**No activation needed with `uv run`:** `uv run <command>` always uses the project environment.

## 5. Launch Jupyter

```bash
uv run jupyter lab
```

Your browser opens JupyterLab. Start with `00_start_here/00_welcome.ipynb`: its first cells check that everything works.

**VS Code / Cursor / PyCharm:** open the folder, open a notebook, and select the kernel/interpreter
`.venv` (Python 3.12) in the top-right corner. Install the *Jupyter* extension in VS Code if asked.

## 6. Everyday uv commands

| I want to… | Command |
|---|---|
| add a library to the project | `uv add polars` (or `uv add --group nlp spacy`) |
| remove a library | `uv remove polars` |
| run a script in the environment | `uv run python my_script.py` |
| upgrade all libraries | `uv lock --upgrade && uv sync --all-groups` |
| try a library without adding it | `uv pip install rich` (inside the env) |
| start from scratch | delete `.venv/` then `uv sync --all-groups` |
| see what is installed | `uv pip list` / `uv tree` |

## 7. GPU notes 🚀

- **Apple Silicon (M1-M4):** nothing to do. PyTorch uses the GPU through Metal (`mps`), detected automatically by
  `get_device()` in the notebooks.
- **Linux + NVIDIA:** the default PyTorch wheels from PyPI include CUDA. Check with
  `uv run python -c "import torch; print(torch.cuda.is_available())"`.
- **Windows + NVIDIA:** PyPI ships CPU-only PyTorch for Windows. After `uv sync`, replace it with a CUDA build:
  ```powershell
  uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128 --reinstall
  ```
  (pick the CUDA version matching your driver on [pytorch.org](https://pytorch.org/get-started/locally/)). Note that a
  later `uv sync` reinstalls the CPU wheels.
- **No GPU:** every notebook is sized to run on a laptop CPU (deep learning ones take longer; reduce epochs if needed).

## 8. Google Colab ☁️

Every notebook has an **Open in Colab** badge. The first code cell detects Colab, clones this repository and installs
the few missing libraries automatically. For deep learning, enable a GPU: *Runtime → Change runtime type → T4 GPU*.

## 9. Troubleshooting 🧯

| Problem | Fix |
|---|---|
| `uv: command not found` | reopen the terminal; on Windows, log out/in so the PATH updates |
| a notebook can't import `mlquest` | launch Jupyter from the repository folder (or any sub-folder) |
| `ModuleNotFoundError: lightgbm` (or another library) | `uv sync --all-groups`, then restart the kernel |
| kernel crashes when a notebook uses PyTorch **and** LightGBM/XGBoost (macOS) | known OpenMP clash between their wheels; restart the kernel and avoid mixing them in one session (the course never does) |
| download is slow or fails behind a proxy | set `HTTPS_PROXY`; with a corporate certificate, also `SSL_CERT_FILE` / `REQUESTS_CA_BUNDLE` (uv: `--native-tls`) |
| disk is full | datasets live in `data/` and models in `runs/`: delete any sub-folder safely, it will be downloaded again |
| Windows: `DataLoader` hangs | the notebooks already use `num_workers=0` on Windows/macOS (`NUM_WORKERS` in `mlquest`) |
