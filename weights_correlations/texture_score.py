import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ========= 1) CONFIG =========
INPUT_CSV = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\bleaching_texture_features_standardized - bleaching_texture_features_standardized.csv"
OUTPUT_CSV = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\bleaching_texture_with_score.csv"
HEATMAP_PNG = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\texture_correlation_heatmap.png"

# ========= 2) LOAD =========
df = pd.read_csv(INPUT_CSV)

required_cols = [
    "glcm_correlation_std",
    "lbp_var_gray_masked_std",
    "lap_var_gray_masked_std",
    "perc_bleached",
]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Missing required column(s): {missing}")

# ========= 3) COMPUTE texture_score =========
df["texture_score"] = (
    0.333153 * df["glcm_correlation_std"]
    + 0.074896 * df["lbp_var_gray_masked_std"]
    - 0.016813 * df["lap_var_gray_masked_std"]
)

cols = list(df.columns)
cols = [c for c in cols if c != "texture_score"] + ["texture_score"]
df = df[cols]

# ========= 4) SAVE UPDATED CSV =========
df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved updated dataset with texture_score to: {Path(OUTPUT_CSV).resolve()}")

# ========= 5) CORRELATION (including texture_score) =========
corr_features = [
    "lap_var_gray_masked_std",
    "lbp_var_gray_masked_std",
    "glcm_correlation_std",
    "texture_score",
    "perc_bleached",
]
df_corr = df.dropna(subset=corr_features)[corr_features]

corr_matrix = df_corr.corr()
print("\nCorrelation Matrix — Texture Features, Texture Score, and % Coral Bleached\n")
print(corr_matrix.round(3))

# ========= 6) PLOT & SAVE HEATMAP =========
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix.round(2),
    annot=True,
    fmt=".2f",
    cmap="RdBu_r",
    vmin=-1,
    vmax=1,
    center=0,
)
plt.title("Correlation Matrix — Texture Features & % Coral Bleached", fontsize=12)
plt.tight_layout()
plt.savefig(HEATMAP_PNG, dpi=300)
plt.show()
print(f"Saved correlation heatmap to: {Path(HEATMAP_PNG).resolve()}")

