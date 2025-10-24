# --- Correlation Between Texture Score and Median Whiteness Score ---

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ========= 1) LOAD BOTH DATASETS =========
texture_path = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\bleaching_texture_with_score.csv"      
whiteness_path = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\whiteness_scores_added.csv"

# ========= 2) Load =========
tex = pd.read_csv(texture_path)
wh = pd.read_csv(whiteness_path)

# ========= 3) Normalize keys to a common ID =========
def to_key(x):
    """Return lowercase basename without extension, with whitespace stripped."""
    if pd.isna(x):
        return None
    base = os.path.basename(str(x)).strip()
    stem = os.path.splitext(base)[0]
    return stem.lower()

if "image" not in tex.columns:
    raise ValueError("Expected column 'image' in texture CSV.")
tex["key"] = tex["image"].apply(to_key)

if "image_path" not in wh.columns:
    raise ValueError("Expected column 'image_path' in whiteness CSV.")
wh["key"] = wh["image_path"].apply(to_key)

# ========= 4) Quick diagnostics =========
print(f"Texture rows:   {len(tex)}   | unique keys: {tex['key'].nunique()}")
print(f"Whiteness rows: {len(wh)}   | unique keys: {wh['key'].nunique()}")

intersection = set(tex["key"].dropna()) & set(wh["key"].dropna())
print(f"Common keys found: {len(intersection)}")

if len(intersection) == 0:
    # Show a few example keys to visually compare
    print("\nNo common keys! Examples:")
    print("Texture keys (first 5):", tex["key"].dropna().head(5).tolist())
    print("Whiteness keys (first 5):", wh["key"].dropna().head(5).tolist())
    raise SystemExit(0)

# ========= 5) Merge on normalized key =========
merged = pd.merge(
    tex[["key", "texture_score"]],
    wh[["key", "median_whiteness_score", "mean_whiteness_score"]],
    on="key",
    how="inner"
)

print(f"Merged rows: {len(merged)}")
merged = merged.dropna(subset=["texture_score", "median_whiteness_score", "mean_whiteness_score"])

# ========= 6) Compute correlations =========
corr_median = merged["texture_score"].corr(merged["median_whiteness_score"])
corr_mean   = merged["texture_score"].corr(merged["mean_whiteness_score"])

print(f"\nCorrelation (texture ↔ median whiteness): {corr_median:.3f}")
print(f"Correlation (texture ↔ mean whiteness):   {corr_mean:.3f}")

# ========= 7) Plots =========
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.regplot(
    data=merged, x="texture_score", y="median_whiteness_score",
    scatter_kws={"alpha": 0.6}, line_kws={"color": "red"}
)
plt.title(f"Texture vs Median Whiteness (r = {corr_median:.2f})")
plt.xlabel("Texture Score")
plt.ylabel("Median Whiteness Score")

plt.subplot(1, 2, 2)
sns.regplot(
    data=merged, x="texture_score", y="mean_whiteness_score",
    scatter_kws={"alpha": 0.6}, line_kws={"color": "red"}
)
plt.title(f"Texture vs Mean Whiteness (r = {corr_mean:.2f})")
plt.xlabel("Texture Score")
plt.ylabel("Mean Whiteness Score")

plt.tight_layout()

plt.show()

