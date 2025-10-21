# --- Coral Texture Feature Correlation Matrix ---
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === 1. Load the dataset ===
file_path = r"C:\Users\20220848\OneDrive - TU Eindhoven\Desktop\TuE\4th year\Q1\DC3\Mathematical approach\bleaching_texture_features_standardized - bleaching_texture_features_standardized.csv"
df = pd.read_csv(file_path)

# === 2. Clean the data (remove rows with missing relevant columns) ===
df_clean = df.dropna(subset=[
    'perc_bleached',
    'lap_var_gray_masked_std',
    'lbp_var_gray_masked_std',
    'glcm_correlation_std'
])

# === 3. Select relevant columns for correlation ===
corr_features = df_clean[[
    'lap_var_gray_masked_std',
    'lbp_var_gray_masked_std',
    'glcm_correlation_std',
    'perc_bleached'
]]

# === 4. Compute correlation matrix ===
corr_matrix = corr_features.corr()

# === 5. Print correlation matrix ===
print("\nCorrelation Matrix — Texture Features and % Coral Bleached\n")
print(corr_matrix.round(3))

# === 6. Plot heatmap ===
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix.round(2),
    annot=True,
    cmap='RdBu_r',
    center=0,
    vmin=-1,
    vmax=1,
    fmt=".2f"
)
plt.title("Correlation Matrix — Texture Features and % Coral Bleached", fontsize=12)
plt.tight_layout()
plt.show()
