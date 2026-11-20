"""Plotting helpers shared by the notebooks."""

from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np

PALETTE = ["#2563eb", "#f97316", "#16a34a", "#dc2626", "#9333ea", "#0891b2", "#ca8a04", "#db2777"]


def set_style() -> None:
    """A clean, readable default style for every chart in the course."""
    try:
        import seaborn as sns

        sns.set_theme(style="whitegrid", palette=PALETTE, font_scale=1.0)
    except ImportError:
        pass
    plt.rcParams.update({
        "figure.figsize": (9, 4.5),
        "figure.dpi": 100,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titleweight": "bold",
    })


def show_images(images, titles=None, ncols: int = 6, size: float = 2.2, cmap=None, suptitle: str | None = None):
    """Display a grid of images (numpy arrays, PIL images or tensors in CHW)."""
    images = list(images)
    n = len(images)
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * size, nrows * size))
    axes = np.atleast_1d(axes).ravel()
    for i, ax in enumerate(axes):
        ax.axis("off")
        if i >= n:
            continue
        img = images[i]
        if hasattr(img, "detach"):
            img = img.detach().cpu().numpy()
            if img.ndim == 3 and img.shape[0] in (1, 3):
                img = np.transpose(img, (1, 2, 0))
        img = np.asarray(img)
        if img.ndim == 3 and img.shape[-1] == 1:
            img = img[..., 0]
        ax.imshow(img, cmap=cmap)
        if titles is not None:
            ax.set_title(str(titles[i]), fontsize=9)
    if suptitle:
        fig.suptitle(suptitle, fontweight="bold")
    plt.tight_layout()
    plt.show()
