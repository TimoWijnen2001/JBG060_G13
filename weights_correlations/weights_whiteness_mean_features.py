import numpy as np
import pandas as pd
from numpy.linalg import inv

# Scenario 2 : Whiteness features
features = ["mean_raw_red", "mean_albedo", "mean_luminance", "mean_saturation"]

# correlations with bleaching (%)
r_xy = np.array([-0.27, 0.47, 0.45, 0.42])

# feature–feature correlations (symmetric)
R_xx = np.array([
    [1.00, -0.19, -0.22,  0.15],
    [-0.19, 1.00,  0.73,  0.47],
    [-0.22, 0.73,  1.00,  0.52],
    [0.15, 0.47,  0.52,  1.00],
])

# standardized regression weights
beta = inv(R_xx) @ r_xy

# relative importance shares
shares = np.abs(beta) / np.abs(beta).sum()

# summary table
df = pd.DataFrame({
    "feature": features,
    "beta (standardized weight)": beta,
    "importance share (|β|/Σ|β|)": shares
}).set_index("feature").sort_values("importance share (|β|/Σ|β|)", ascending=False)

print(df)
