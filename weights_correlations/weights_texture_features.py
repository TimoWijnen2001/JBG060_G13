import numpy as np
import pandas as pd
from numpy.linalg import inv

# === Scenario 1: Texture features ===
features = ["lap_var", "lbp_var", "glcm_corr"]

# correlations with bleaching (%)
r_xy = np.array([-0.19, 0.05, 0.34])

# feature–feature correlations (symmetric)
R_xx = np.array([
    [1.00,  0.49, -0.63],
    [0.49,  1.00, -0.05],
    [-0.63, -0.05, 1.00],
])

# standardized regression weights
beta = inv(R_xx) @ r_xy

# importance shares
shares = np.abs(beta) / np.abs(beta).sum()

# display
df = pd.DataFrame({
    "feature": features,
    "beta (standardized weight)": beta,
    "importance share (|β|/Σ|β|)": shares
}).set_index("feature").sort_values("importance share (|β|/Σ|β|)", ascending=False)

print(df)
