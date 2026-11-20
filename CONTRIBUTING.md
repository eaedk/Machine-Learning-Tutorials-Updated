# 🤝 Contributing

Thanks for helping other learners! A few guidelines keep the course consistent.

## Set up
```bash
uv sync --all-groups
uv run jupyter lab
```

## Adding or editing a notebook
- **One notebook = one quest.** Start with a story (where does the problem come from?), state the mission and the
  metric, then explain each phase: *what* we do, *why*, and the classic *traps*.
- Start with the standard setup cell (copy it from any notebook): it imports the `mlquest` toolkit and works on
  Windows, macOS, Linux and Colab.
- Download data with `mlquest` helpers (`download_and_extract`, `hf_parquet`, `openml`) into `DATA_DIR`; never
  commit data, weights or outputs of training runs.
- Use `pathlib`, `get_device()` and `NUM_WORKERS`; no shell commands (`!wget`, `!unzip`…) so notebooks run everywhere.
- Keep it laptop-sized: a notebook should run in ~15 minutes on a recent laptop.
- **Quests** (`*_quest_*`): `# TODO` cells, a `check(...)` after each exercise, the solution in a
  `<details>` block, and no outputs committed.
- **Applications**: commit them executed (outputs visible on GitHub), end with "🚀 Your turn" challenges.
- On macOS, don't mix PyTorch with LightGBM/XGBoost in the same notebook (their OpenMP runtimes clash).

## Pull requests
1. Fork, create a branch (`git checkout -b quest/my-new-quest`).
2. Run the notebook top to bottom with a fresh kernel.
3. Open a PR describing the quest, the dataset (and its license) and the runtime.
