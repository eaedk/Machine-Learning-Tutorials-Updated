"""A tiny game layer: XP, levels, badges and friendly auto-checks.

Learning is a long game. Seeing your progress bar grow is a surprisingly good motivator.
Your progress is stored locally in ``.mlquest_progress.json`` (git-ignored).
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

from .env import ROOT

PROGRESS_FILE = Path(os.environ.get("MLQUEST_PROGRESS", ROOT / ".mlquest_progress.json"))

LEVELS = [
    (0, "🥚 Curious Rookie"),
    (100, "🐣 Data Explorer"),
    (300, "🧭 Feature Pathfinder"),
    (600, "⚔️ Model Knight"),
    (1000, "🏹 Validation Ranger"),
    (1500, "🧙 Ensemble Wizard"),
    (2200, "🐉 Leaderboard Dragon"),
    (3000, "👑 Grandmaster-in-the-making"),
]


def _load() -> dict:
    try:
        return json.loads(Path(PROGRESS_FILE).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {"xp": 0, "done": {}}


def _save(state: dict) -> None:
    try:
        Path(PROGRESS_FILE).write_text(json.dumps(state, indent=2), encoding="utf-8")
    except OSError:
        pass  # read-only environments: the game is optional


def level_of(xp: int) -> tuple[str, int | None]:
    name, nxt = LEVELS[0][1], None
    for i, (threshold, label) in enumerate(LEVELS):
        if xp >= threshold:
            name = label
            nxt = LEVELS[i + 1][0] if i + 1 < len(LEVELS) else None
    return name, nxt


def _bar(xp: int, nxt: int | None, width: int = 24) -> str:
    if nxt is None:
        return "█" * width + " MAX"
    prev = max(t for t, _ in LEVELS if t <= xp)
    frac = (xp - prev) / max(1, nxt - prev)
    full = int(frac * width)
    return "█" * full + "░" * (width - full) + f" {xp}/{nxt} XP"


def quest(title: str, chapter: str = "", xp: int = 0) -> None:
    """Announce the quest of the notebook."""
    state = _load()
    lvl, nxt = level_of(state["xp"])
    print("━" * 60)
    print(f"🗺️  QUEST · {title}")
    if chapter:
        print(f"   {chapter}")
    if xp:
        print(f"   Reward: up to {xp} XP")
    print(f"   You are: {lvl}   {_bar(state['xp'], nxt)}")
    print("━" * 60)


def checkpoint(key: str, xp: int = 10, msg: str = "") -> None:
    """Award XP once per checkpoint (re-running a cell does not farm XP 😉)."""
    state = _load()
    before = level_of(state["xp"])[0]
    if key not in state["done"]:
        state["done"][key] = {"xp": xp, "at": time.strftime("%Y-%m-%d %H:%M")}
        state["xp"] += xp
        _save(state)
        gained = f"+{xp} XP"
    else:
        gained = "already unlocked"
    lvl, nxt = level_of(state["xp"])
    print(f"✅ Checkpoint · {key} ({gained}) {msg}".rstrip())
    if lvl != before:
        print(f"🎉 LEVEL UP! You are now {lvl}")
    print(f"   {_bar(state['xp'], nxt)}")


def check(condition: bool, success: str = "Looks good!", hint: str = "Not quite yet.") -> None:
    """A gentle auto-grader: tells you if your answer looks right, with a hint otherwise."""
    if condition:
        print(f"✅ {success}")
    else:
        print(f"🤔 {hint}")


def badge(name: str, emoji: str = "🏅", text: str = "") -> None:
    """Unlock a badge (shown in ``progress()``)."""
    state = _load()
    state.setdefault("badges", {})
    first = name not in state["badges"]
    state["badges"].setdefault(name, emoji)
    _save(state)
    box = f" {emoji}  BADGE {'UNLOCKED' if first else 'OWNED'}: {name} "
    print("╔" + "═" * len(box) + "╗\n║" + box + "║\n╚" + "═" * len(box) + "╝")
    if text:
        print(text)


def progress() -> None:
    """Show your level, XP and badges."""
    state = _load()
    lvl, nxt = level_of(state["xp"])
    print(f"{lvl}\n{_bar(state['xp'], nxt)}")
    print(f"Checkpoints unlocked: {len(state['done'])}")
    if state.get("badges"):
        print("Badges: " + "  ".join(f"{e} {n}" for n, e in state["badges"].items()))


def reset_progress() -> None:
    """Start the adventure from scratch."""
    Path(PROGRESS_FILE).unlink(missing_ok=True)
    print("🔄 Progress reset. A new adventure begins!")
