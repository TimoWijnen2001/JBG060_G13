import numpy as np
import pandas as pd
from numpy.linalg import inv

# === Combined Severity Score ===
features = ["whiteness", "texture"]

# correlations
r_xy = np.array([0.51, 0.35])  # correlations with bleaching
R_xx = np.array([[1.0, 0.16],
                 [0.16, 1.0]])  # feature–feature correlations

# standardized regression weights
beta = inv(R_xx) @ r_xy

# relative importance shares
shares = np.abs(beta) / np.abs(beta).sum()

df = pd.DataFrame({
    "feature": features,
    "beta (standardized weight)": beta,
    "importance share (|β|/Σ|β|)": shares
}).set_index("feature")

print(df)
