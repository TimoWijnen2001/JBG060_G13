# --- Whiteness: median-only heatmap + single-row scores-vs-%bleached heatmap ---

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# ========= 1) CONFIG =========
INPUT_CSV = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\whiteness_scores_added.csv"
HEATMAP_MEDIAN_PNG = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\heatmap_whiteness_median_only.png"
HEATMAP_SCORES_PNG = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\heatmap_whiteness_scores_vs_bleached.png"

# ========= 2) LOAD =========
df = pd.read_csv(INPUT_CSV)
# ========= 5) HEATMAP A: MEDIAN-ONLY (no mean columns) =========
median_cols = [
    "median_raw_red_z",
    "median_albedo_z",
    "median_luminance_z",
    "median_saturation_z",
    "median_whiteness_score",
    "bleached_percentage",
]
df_med = df.dropna(subset=median_cols)[median_cols]
corr_median = df_med.corr()

print("\nCorrelation (Median-only):")
print(corr_median.round(3))

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_median.round(2),
    annot=True, fmt=".2f",
    cmap="RdBu_r", vmin=-1, vmax=1, center=0
)
plt.title("Correlation Matrix — Median Features, Median Whiteness Score & % Bleached", fontsize=12)
plt.tight_layout()
plt.savefig(HEATMAP_MEDIAN_PNG, dpi=300)
plt.show()
print(f"Saved: {Path(HEATMAP_MEDIAN_PNG).resolve()}")

# ========= 6) HEATMAP B: single row like your example =========
# Correlation of % bleached with the two whiteness scores
score_cols = ["median_whiteness_score", "mean_whiteness_score", "bleached_percentage"]
df_scores = df.dropna(subset=score_cols)[score_cols]

# Compute correlations of bleached_percentage vs each score
corr_series = df_scores[["median_whiteness_score", "mean_whiteness_score"]].corrwith(df_scores["bleached_percentage"])
# Turn into 1x2 DataFrame for a single-row heatmap
one_row = corr_series.to_frame().T
one_row.index = ["% bleached"]  # label like the example

print("\nCorrelation of % bleached with whiteness scores:")
print(one_row.round(3))

plt.figure(figsize=(6, 2.6))  # short and wide, like your example
sns.heatmap(
    one_row.round(2),
    annot=True, fmt=".2f",
    cmap="RdBu_r", vmin=-1, vmax=1, center=0,
    cbar=True
)
plt.title("Whiteness score vs % Bleached (Pearson r)", fontsize=11)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(HEATMAP_SCORES_PNG, dpi=300)
plt.show()
print(f"Saved: {Path(HEATMAP_SCORES_PNG).resolve()}")