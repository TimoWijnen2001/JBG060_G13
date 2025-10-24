import numpy as np
import pandas as pd
from numpy.linalg import inv

# Whiteness features
features = ["median_raw_red", "median_albedo", "median_luminance", "median_saturation"]

# correlations with bleaching (%)
r_xy = np.array([-0.21, 0.42, 0.42, 0.38])

# feature–feature correlations (symmetric)
R_xx = np.array([
    [1.00, -0.31, -0.33,  0.18],
    [-0.31, 1.00,  0.75,  0.42],
    [-0.33, 0.75,  1.00,  0.47],
    [0.18, 0.42,  0.47,  1.00],
])

# standardized regression weights
beta = inv(R_xx) @ r_xy

# relative importance shares
shares = np.abs(beta) / np.abs(beta).sum()

# summary
df = pd.DataFrame({
    "feature": features,
    "beta (standardized weight)": beta,
    "importance share (|β|/Σ|β|)": shares
}).set_index("feature").sort_values("importance share (|β|/Σ|β|)", ascending=False)

print(df)

