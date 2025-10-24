# --- Correlation Between Texture, Whiteness, Severity, and % Bleached ---

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import os

# ========= 1) CONFIG =========
texture_path = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\bleaching_texture_with_score.csv"      
whiteness_path = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\whiteness_scores_added.csv"          
output_csv = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\merged_with_severity.csv"
output_heatmap = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\heatmap_severity_whiteness_texture.png"

# ========= 2) LOAD BOTH DATASETS =========
tex = pd.read_csv(texture_path)
wh = pd.read_csv(whiteness_path)

# ========= 3) NORMALIZE KEYS =========
def normalize_key(x):
    """Get lowercase basename without extension."""
    if pd.isna(x):
        return None
    base = os.path.basename(str(x)).strip()
    stem = os.path.splitext(base)[0]
    return stem.lower()

tex["key"] = tex["image"].apply(normalize_key)
wh["key"] = wh["image_path"].apply(normalize_key)

# ========= 4) MERGE =========
merged = pd.merge(
    tex[["key", "texture_score", "perc_bleached"]],
    wh[["key", "median_whiteness_score"]],
    on="key",
    how="inner"
)

print(f"Merged rows: {len(merged)}")

# ========= 5) COMPUTE SEVERITY SCORE =========
merged["severity"] = (
    0.465928 * merged["median_whiteness_score"]
    + 0.371539 * merged["texture_score"]
)

# ========= 6) SAVE UPDATED DATAFRAME =========
merged.to_csv(output_csv, index=False)
print(f"✅ Saved dataset with severity score to: {Path(output_csv).resolve()}")

# ========= 7) CORRELATION MATRIX =========
corr_features = ["median_whiteness_score", "texture_score", "severity", "perc_bleached"]
corr_matrix = merged[corr_features].corr()

print("\nCorrelation Matrix — Whiteness, Texture, Severity, and % Bleached\n")
print(corr_matrix.round(3))

# ========= 8) PLOT HEATMAP =========
plt.figure(figsize=(6, 5))
sns.heatmap(
    corr_matrix.round(2),
    annot=True,
    cmap="RdBu_r",
    vmin=-1,
    vmax=1,
    center=0,
    fmt=".2f"
)
plt.title("Correlation Matrix — Severity, Whiteness, Texture & % Bleached", fontsize=12)
plt.tight_layout()
plt.savefig(output_heatmap, dpi=300)
plt.show()

print(f"✅ Saved heatmap to: {Path(output_heatmap).resolve()}")

