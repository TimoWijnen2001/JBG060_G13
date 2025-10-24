# --- Compute Whiteness Scores (Mean & Median) and Creates Correlation Heatmaps ---

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ========= 1) CONFIG =========
INPUT_CSV = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\standardized_feature_score_per_image.csv"
OUTPUT_CSV = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\whiteness_scores_added.csv"
HEATMAP_PNG = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\whiteness_correlation_heatmap.png"

# ========= 2) LOAD =========
df = pd.read_csv(INPUT_CSV)

# ========= 3) CLEAN =========
required_cols = [
    "bleached_percentage",
    "mean_raw_red_z", "mean_albedo_z", "mean_luminance_z", "mean_saturation_z",
    "median_raw_red_z", "median_albedo_z", "median_luminance_z", "median_saturation_z"
]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Missing required column(s): {missing}")

df = df.dropna(subset=required_cols)

# ========= 4) COMPUTE SCORES =========
# Median whiteness score
df["median_whiteness_score"] = (
    -0.180092 * df["median_raw_red_z"]
    + 0.168412 * df["median_albedo_z"]
    + 0.094557 * df["median_luminance_z"]
    + 0.297242 * df["median_saturation_z"]
)

# Mean whiteness score
df["mean_whiteness_score"] = (
    -0.262306 * df["mean_raw_red_z"]
    + 0.224061 * df["mean_albedo_z"]
    + 0.061169 * df["mean_luminance_z"]
    + 0.322229 * df["mean_saturation_z"]
)

cols = list(df.columns)
for new_col in ["median_whiteness_score", "mean_whiteness_score"]:
    cols = [c for c in cols if c != new_col] + [new_col]
df = df[cols]

# ========= 5) SAVE UPDATED CSV =========
df.to_csv(OUTPUT_CSV, index=False)
print(f"✅ Saved updated dataset with whiteness scores to: {Path(OUTPUT_CSV).resolve()}")

# ========= 6) CORRELATION MATRIX =========
corr_features = [
    "mean_raw_red_z", "mean_albedo_z", "mean_luminance_z", "mean_saturation_z",
    "median_raw_red_z", "median_albedo_z", "median_luminance_z", "median_saturation_z",
    "mean_whiteness_score", "median_whiteness_score", "bleached_percentage"
]

corr_matrix = df[corr_features].corr()

# ========= 7) PRINT CORRELATION MATRIX =========
print("\nCorrelation Matrix — Whiteness Features, Scores, and % Coral Bleached\n")
print(corr_matrix.round(3))

# ========= 8) PLOT HEATMAP =========
plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix.round(2),
    annot=True,
    fmt=".2f",
    cmap="RdBu_r",
    center=0,
    vmin=-1,
    vmax=1
)
plt.title("Correlation Matrix — Whiteness Features & % Coral Bleached", fontsize=12)
plt.tight_layout()
plt.savefig(HEATMAP_PNG, dpi=300)
plt.show()

print(f"✅ Saved correlation heatmap to: {Path(HEATMAP_PNG).resolve()}")

