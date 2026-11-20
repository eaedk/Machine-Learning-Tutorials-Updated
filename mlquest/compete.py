"""Competition helpers: a personal leaderboard for your experiments and clean submission files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .env import RUNS_DIR, SUBMISSIONS_DIR


class Leaderboard:
    """Log every experiment, compare them, never lose your best idea again.

    >>> lb = Leaderboard("titanic", metric="accuracy", higher_is_better=True)
    >>> lb.add("LogReg baseline", 0.79, notes="5 features")
    >>> lb.show()
    """

    def __init__(self, name: str, metric: str, higher_is_better: bool = True, persist: bool = False):
        self.name, self.metric, self.higher = name, metric, higher_is_better
        self.path = RUNS_DIR / f"leaderboard_{name}.csv"
        self.persist = persist
        if persist and self.path.exists():
            self.rows = pd.read_csv(self.path).to_dict("records")
        else:
            self.rows = []

    def add(self, model: str, score: float, **details) -> None:
        self.rows = [r for r in self.rows if r["model"] != model]  # re-running a cell replaces the entry
        self.rows.append({"model": model, self.metric: round(float(score), 5), **details})
        if self.persist:
            self.table().to_csv(self.path, index=False)
        best = self.table().iloc[0]["model"]
        crown = "  👑 new best!" if best == model and len(self.rows) > 1 else ""
        print(f"📋 {model}: {self.metric} = {score:.5f}{crown}")

    def table(self) -> pd.DataFrame:
        df = pd.DataFrame(self.rows)
        if df.empty:
            return df
        df = df.sort_values(self.metric, ascending=not self.higher).reset_index(drop=True)
        df.index = df.index + 1
        df.index.name = "rank"
        return df

    def show(self):
        df = self.table()
        if df.empty:
            print("Leaderboard is empty: train a model first!")
            return df
        medals = {1: "🥇", 2: "🥈", 3: "🥉"}
        df.insert(0, "", [medals.get(i, "") for i in df.index])
        return df

    def best(self) -> dict:
        return self.table().iloc[0].to_dict()


def make_submission(df: pd.DataFrame, filename: str, sample: pd.DataFrame | None = None) -> Path:
    """Save a submission CSV and run the classic sanity checks competitions will run on it."""
    if sample is not None:
        assert list(df.columns) == list(sample.columns), f"Columns must be {list(sample.columns)}"
        assert len(df) == len(sample), f"Expected {len(sample)} rows, got {len(df)}"
    assert not df.isna().any().any(), "Your submission contains missing values"
    path = SUBMISSIONS_DIR / filename
    df.to_csv(path, index=False)
    print(f"📤 Submission saved: submissions/{path.name}  ({len(df)} rows, columns={list(df.columns)})")
    return path
