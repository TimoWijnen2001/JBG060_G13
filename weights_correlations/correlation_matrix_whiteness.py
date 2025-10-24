# --- Coral Bleaching Feature Correlation Matrices (Mean & Median) ---
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === 1. Load the dataset ===
file_path = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\standardized_feature_score_per_image.csv"
df = pd.read_csv(file_path)

# === 2. Clean the data ===
df_clean = df.dropna(subset=[
    'bleached_percentage',
    'mean_raw_red_z', 'mean_albedo_z', 'mean_luminance_z', 'mean_saturation_z',
    'median_raw_red_z', 'median_albedo_z', 'median_luminance_z', 'median_saturation_z'
])

# === 3. Select relevant columns ===
mean_features = df_clean[[
    'mean_raw_red_z',
    'mean_albedo_z',
    'mean_luminance_z',
    'mean_saturation_z',
    'bleached_percentage'
]]

median_features = df_clean[[
    'median_raw_red_z',
    'median_albedo_z',
    'median_luminance_z',
    'median_saturation_z',
    'bleached_percentage'
]]

# === 4. Compute correlation matrices ===
corr_mean = mean_features.corr()
corr_median = median_features.corr()

# === 5. Display correlation matrices in console ===
print("\nCorrelation Matrix — Mean Standardized Feature Scores and % Coral Bleached\n")
print(corr_mean.round(3))
print("\nCorrelation Matrix — Median Standardized Feature Scores and % Coral Bleached\n")
print(corr_median.round(3))

# === 6. Plot both heatmaps side by side ===
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.heatmap(
    corr_mean.round(2),
    annot=True,
    cmap='RdBu_r',
    center=0,
    vmin=-1,
    vmax=1,
    fmt=".2f",
    ax=axes[0]
)
axes[0].set_title("Mean Standardized Feature Scores vs. % Coral Bleached", fontsize=12)

sns.heatmap(
    corr_median.round(2),
    annot=True,
    cmap='RdBu_r',
    center=0,
    vmin=-1,
    vmax=1,
    fmt=".2f",
    ax=axes[1]
)
axes[1].set_title("Median Standardized Feature Scores vs. % Coral Bleached", fontsize=12)

plt.tight_layout()
plt.show()

