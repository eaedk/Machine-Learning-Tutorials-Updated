<div align="center">

# 🧭 ML Quest

### Machine Learning Tutorials, updated: from your first model to the leaderboard

**Guided notebooks to complete · real competition-style applications · stories, concepts and a bit of fun**

[![Python](https://img.shields.io/badge/python-3.10%20→%203.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/env-uv-DE5FE9?logo=uv&logoColor=white)](https://docs.astral.sh/uv/)
[![Runs on](https://img.shields.io/badge/runs%20on-Windows%20·%20macOS%20·%20Linux%20·%20Colab-2563eb)](#-quick-start)
[![Notebooks](https://img.shields.io/badge/notebooks-32-f97316)](#%EF%B8%8F-the-map)
[![License: MIT](https://img.shields.io/badge/license-MIT-16a34a)](LICENSE)

</div>

---

Most people learn machine learning by reading. Competitors learn it by **doing**: a dataset, a metric, a deadline, a
leaderboard. This repository turns that into a guided journey. Each notebook is a *quest* with a real problem, the
story behind it, the concepts you need, and a score telling you how well you did.

It is the second edition of the [ML Step-by-Step Guide](https://github.com/eaedk/Machine-Learning-Tutorials), grown
from one tabular template into **five tracks**: tabular data, time series, computer vision, NLP and audio.

<table>
<tr>
<td width="50%">

**🎯 Quests**: guided notebooks *to complete*
- `# TODO` cells for you to fill
- auto-checks (`check(...)`) that tell you if you're on track
- hidden solutions, one click away
- XP, levels and badges 🎮

</td>
<td width="50%">

**🚀 Applications**: full, executed notebooks
- real datasets from the Zindi, Kaggle and open-research ecosystems
- every phase explained: *what*, *why*, *traps*
- results, charts and submission files included
- "Your turn" challenges at the end

</td>
</tr>
</table>

## 🚀 Quick start

```bash
# 1. Install uv (once):  macOS/Linux ↓   ·   Windows: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Get the course and install everything (Python 3.12 included)
git clone https://github.com/eaedk/Machine-Learning-Tutorials-Updated.git
cd Machine-Learning-Tutorials-Updated
uv sync --all-groups          # or only one track: uv sync --group tabular

# 3. Play
uv run jupyter lab            # open 00_start_here/00_welcome.ipynb
```

Prefer an activated environment? `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\Activate.ps1` (Windows).
Everything about uv, GPUs (CUDA / Apple Silicon), Colab and troubleshooting: **[INSTALL.md](INSTALL.md)**.

No install at all? Every notebook has an **Open in Colab** badge and sets itself up.

## 🗺️ The map

Legend: 🎯 quest (to complete) · 🚀 application (executed) · ⭐ bonus. Times measured on a laptop (Apple M4 Pro).

### 🧭 00 · Start here
| # | Notebook | What you'll do |
|---|---|---|
| 0 | [Welcome & setup check](00_start_here/00_welcome.ipynb) | check your machine, a short history of ML competitions, your first model in 10 lines |
| 1 | [The ML step-by-step template](00_start_here/01_ml_step_by_step_template.ipynb) | the reusable map for any tabular project (2nd edition of the original guide) |
| 2 | [The competition playbook](00_start_here/02_competition_playbook.ipynb) | simulate a leaderboard shake-up, group leakage, 90% accuracy on noise, adversarial validation, ensembling |

### 📊 01 · Tabular data
| # | Notebook | Dataset · story | Key ideas | Result |
|---|---|---|---|---|
| 1 | 🎯 [Would you have survived the Titanic?](01_tabular/01_classification_quest_titanic.ipynb) | Titanic (1912) · Kaggle's "hello world" | EDA, leakage hunt, features from names, pipelines, CV, tuning | ~0.83 CV accuracy |
| 2 | 🚀 [Who is about to leave? Telecom churn](01_tabular/02_classification_app_telco_churn.ipynb) | IBM Telco churn · cf. Zindi Expresso challenge | LightGBM · XGBoost · CatBoost, Optuna, OOF blend, profit curve, SHAP | AUC 0.85 |
| 3 | 🎯 [The price of a Californian dream](01_tabular/03_regression_quest_california.ipynb) | 1990 California census | MAE/RMSE/R², residual maps, geo features, trees vs linear | RMSE 0.44 (R² 0.85) |
| 4 | 🚀 [House Prices, the Kaggle classic](01_tabular/04_regression_app_house_prices.ipynb) | Ames, Iowa (De Cock, 2011) | meaningful missing values, ordinal encoding, log target, Ridge/Lasso vs boosting, blend | RMSLE 0.124 |
| 5 | ⭐ [Who are our customers? Clustering](01_tabular/05_clustering_app_customer_segments.ipynb) | Wholesale customers (Lisbon) | scaling for distances, k-means, silhouette, PCA, personas, DBSCAN, GMM | hidden channel recovered (ARI 0.62) |
| 6 | ⭐ [The million-dollar movie night](01_tabular/06_recommender_app_movielens.ipynb) | MovieLens · the Netflix Prize | biases, item-item CF, matrix factorisation from scratch, precision@k, *your* recommendations | RMSE 0.84 |

### ⏳ 02 · Time series
| # | Notebook | Dataset · story | Key ideas | Result |
|---|---|---|---|---|
| 1 | 🎯 [The planet's breathing curve](02_time_series/01_forecasting_quest_co2.ipynb) | Mauna Loa CO₂ (Keeling curve) | trend/seasonality, STL, naive baselines, time split, SARIMA, Holt-Winters | MAE 0.71 ppm |
| 2 | 🚀 [Forecasting bike demand](02_time_series/02_forecasting_app_bike_demand.ipynb) | Capital Bikeshare · Kaggle 2014 | lags & calendar features, gradient boosting, recursive vs direct, **Chronos** foundation model zero-shot | RMSLE 0.54 |
| 3 | 🎯 [Gun or Point?](02_time_series/03_classification_quest_gunpoint.ipynb) | UCR archive | 1-NN + DTW, catch22 features, MiniRocket | 99.3% accuracy |
| 4 | 🚀 [Your phone knows what you're doing](02_time_series/04_classification_app_human_activity.ipynb) | UCI HAR smartphones | split by person, MiniRocket vs 1D-CNN (PyTorch) | 97.3% accuracy |
| 5 | 🚀 [What disturbed New York's taxis?](02_time_series/05_anomaly_detection_nyc_taxi.ipynb) | NAB NYC taxi | z-scores, STL residuals, Isolation Forest, evaluation vs known events | 5/5 events found |

### 👁️ 03 · Computer vision
| # | Notebook | Dataset · story | Key ideas | Result |
|---|---|---|---|---|
| 1 | 🎯 [Teach a computer to recognise clothes](03_computer_vision/01_image_classification_quest_fashion.ipynb) | Fashion-MNIST · LeNet → AlexNet | tensors, DataLoader, CNN from scratch, training loop, overfitting, augmentation | 91.6% accuracy |
| 2 | 🚀 [Diagnosing bean diseases in Uganda](03_computer_vision/02_image_classification_app_beans.ipynb) | Makerere AI Lab beans | transfer learning (timm), fine-tuning, TTA, Grad-CAM | 96.1% test accuracy |
| 3 | 🎯 [What is in the picture, and where?](03_computer_vision/03_object_detection_quest_yolo.ipynb) | COCO · YOLO 2015 → YOLO26 | boxes, IoU & NMS by hand, mAP, fine-tuning | mAP50 0.80 |
| 4 | 🚀 [An AI ranger for African wildlife](03_computer_vision/04_object_detection_app_african_wildlife.ipynb) | buffalo · elephant · rhino · zebra | YOLO26 fine-tuning, error analysis, counting animals | mAP50 0.98 |
| 5 | 🚀 [Inspecting cracks](03_computer_vision/05_instance_segmentation_app_cracks.ipynb) | infrastructure cracks | instance segmentation (masks vs boxes), severity report | mask mAP50 0.63 |
| 6 | 🎯 [Painting pixels](03_computer_vision/06_semantic_segmentation_quest_shapes.ipynb) | synthetic shapes + Cityscapes | U-Net from scratch, pixel accuracy vs IoU/Dice, YOLO26-sem | mIoU 0.98 |
| 7 | 🚀 [Finding polyps](03_computer_vision/07_semantic_segmentation_app_polyps.ipynb) | Kvasir-SEG (medical) | U-Net + pretrained encoder, Dice loss, thresholds, RLE submission | Dice 0.87 |
| 8 | 🚀 [Seen from the sky](03_computer_vision/08_oriented_boxes_app_aerial.ipynb) | DOTA aerial images | oriented bounding boxes (OBB), leakage in benchmark configs | mAP50 0.28 (honest!) |
| 9 | 🚀 [Skeletons and keypoints](03_computer_vision/09_keypoints_pose_app.ipynb) | COCO pose + tigers | pose estimation, OKS, joint-angle "coach" | pose mAP50 0.995 |
| 10 | 🚀 [Recognising actions in videos](03_computer_vision/10_video_classification_app_ucf101.ipynb) | UCF101 | decoding video, frame embeddings baseline, VideoMAE, group leakage | 95.2% accuracy |
| 11 | ⭐ [How far is everything?](03_computer_vision/11_depth_estimation_bonus.ipynb) | depth8 | monocular depth, AbsRel/δ metrics, portrait blur, 3D point cloud | |

### 💬 04 · Natural language processing
| # | Notebook | Dataset · story | Key ideas | Result |
|---|---|---|---|---|
| 1 | 🎯 [How does Naija feel today?](04_nlp/01_text_classification_quest_afrisenti.ipynb) | AfriSenti (Nigerian Pidgin tweets) | tokenisation, bag-of-words, TF-IDF, macro-F1, error analysis | macro-F1 0.47 |
| 2 | 🚀 [Sorting Swahili news](04_nlp/02_text_classification_app_swahili_news.ipynb) | Swahili news · Zindi challenge | TF-IDF baseline, fine-tuning AfroXLMR, blending | macro-F1 0.82 |
| 3 | 🚀 [Who, where and when in Swahili](04_nlp/03_named_entity_recognition_masakhaner.ipynb) | MasakhaNER 2.0 · Masakhane | BIO tags, sub-word alignment, token classification, seqeval | entity F1 0.91 |
| 4 | 🚀 [Search by meaning](04_nlp/04_embeddings_semantic_search.ipynb) | multilingual corpus | word vectors → sentence embeddings, semantic search, zero-shot, RAG idea | |
| 5 | 🚀 [Train your own tiny GPT](04_nlp/05_text_generation_tiny_gpt.ipynb) | West African Folk-Tales (Gutenberg) | Markov → n-grams → Transformer, char-level GPT from scratch, temperature | loss 4.54 → 1.35 |

### 🔊 05 · Audio
| # | Notebook | Dataset · story | Key ideas | Result |
|---|---|---|---|---|
| 1 | 🎯 [Teach your computer to hear digits](05_audio/01_audio_classification_quest_spoken_digits.ipynb) | Free Spoken Digit Dataset · Bell Labs' Audrey (1952) | waveforms, spectrograms, MFCC, speaker-wise split, CNN | 76% on unseen speakers |
| 2 | 🚀 [Speech recognition with Whisper](05_audio/02_speech_recognition_whisper.ipynb) | FLEURS (English, French, Swahili, Lingala) | ASR pipelines, WER/CER, multilingual limits, fine-tuning pointers | WER 11% (English) |

## 🎮 How the game works

```python
quest("Would you have survived the Titanic?", xp=300)   # each notebook starts a quest
check(answer_is_right, "Correct!", "Hint: ...")          # auto-graded exercises
checkpoint("titanic/models", xp=80)                       # earn XP (once per checkpoint)
badge("Titanic Survivor", "🚢")                           # collect badges
progress()                                                # 🥚 Curious Rookie → … → 👑 Grandmaster-in-the-making
```

Levels: 🥚 Curious Rookie → 🐣 Data Explorer → 🧭 Feature Pathfinder → ⚔️ Model Knight → 🏹 Validation Ranger →
🧙 Ensemble Wizard → 🐉 Leaderboard Dragon → 👑 Grandmaster-in-the-making. Your progress stays on your machine
(`.mlquest_progress.json`).

## 🧰 What's in the box

```
Machine-Learning-Tutorials-Updated/
├── 00_start_here/        welcome, the step-by-step template, the competition playbook
├── 01_tabular/           classification, regression, clustering, recommender systems
├── 02_time_series/       forecasting, classification, anomaly detection
├── 03_computer_vision/   classification, detection, segmentation, OBB, pose, video, depth
├── 04_nlp/               text classification, NER, embeddings & search, text generation
├── 05_audio/             sound classification, speech recognition
├── mlquest/              tiny shared toolkit: paths, downloads, seeding, device, leaderboard, game layer
├── pyproject.toml        dependencies, grouped by track (uv)
├── uv.lock               exact versions, for reproducible installs
└── INSTALL.md
```

Datasets are downloaded on first use into `data/` (git-ignored), models and logs go to `runs/`, submission files to
`submissions/`. Delete any of them at any time.

**Design choices**
- 💻 **Laptop-first**: every notebook was executed on a laptop (Apple M4 Pro, 24 GB) in minutes, not hours. NVIDIA
  GPUs (`cuda`), Apple GPUs (`mps`) and CPUs are detected automatically.
- 🪟🍎🐧 **Cross-platform**: `pathlib` everywhere, no shell commands in notebooks, safe DataLoader settings on
  Windows/macOS.
- 🧪 **Honest evaluation**: validation strategy before modelling, pipelines against leakage, baselines first,
  hidden test sets to compare with your CV.
- 🌍 **Data with a story**, often from Africa: Makerere University's crop disease images, Masakhane's African-language
  NLP datasets, Zindi challenges, alongside the classics (Titanic, Netflix Prize, Kaggle House Prices, COCO…).

## 🏆 Where to compete next

| Platform | Why |
|---|---|
| [Zindi](https://zindi.africa/competitions) | Africa's data science community: problems on agriculture, health, finance, African languages |
| [Kaggle](https://www.kaggle.com/competitions) | the largest platform; start with *Getting Started* and *Playground* competitions |
| [DrivenData](https://www.drivendata.org/competitions/) | social-impact challenges |
| [AIcrowd](https://www.aicrowd.com/challenges) | research-oriented challenges |

## 👥 Contributors

<table>
<tr>
<td align="center"><a href="https://github.com/eaedk"><img src="https://github.com/eaedk.png" width="100" alt="eaedk"/><br/><b>Emmanuel KOUPOH</b></a><br/><sub>@eaedk</sub></td>
<td align="center"><a href="https://github.com/NazarioR9"><img src="https://github.com/NazarioR9.png" width="100" alt="NazarioR9"/><br/><b>Muhamed Tuo</b></a><br/><sub>@NazarioR9</sub></td>
<td align="center"><a href="https://github.com/dric2018"><img src="https://github.com/dric2018.png" width="100" alt="dric2018"/><br/><b>Cedric Manouan</b></a><br/><sub>@dric2018</sub></td>
</tr>
</table>

Found a bug, a typo, an idea for a new quest? Issues and pull requests are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).

## 🙏 Credits

The datasets belong to their creators and are downloaded from their original hosts: OpenML, the UCI Machine Learning
Repository, Hugging Face (Makerere AI Lab, Masakhane, MTEB…), GroupLens (MovieLens), Ultralytics, Numenta (NAB), the
UCR/UEA time-series archive, Project Gutenberg and others. Each notebook cites its sources; please check each
dataset's license before any commercial use.

## 📄 License

Code and notebooks: [MIT](LICENSE).
