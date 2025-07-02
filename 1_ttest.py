import pandas as pd
from scipy.stats import ttest_ind
import numpy as np

# Load data
df = pd.read_csv("taxlevel_6_percentage_normalized.csv")

# Identify sample columns
control_cols = [col for col in df.columns if col.startswith("SRR") and col.endswith("man")]
disease_cols = [col for col in df.columns if col.startswith("SRR") and col not in control_cols]

# Prepare results
results = []

for _, row in df.iterrows():
    control_vals = row[control_cols].astype(float)
    disease_vals = row[disease_cols].astype(float)

    # Compute means and log2 fold change
    mean_control = np.mean(control_vals)
    mean_disease = np.mean(disease_vals)
    logFC = np.log2((mean_disease + 1e-6) / (mean_control + 1e-6))  # avoid log(0)

    # Perform t-test
    t_stat, p_val = ttest_ind(disease_vals, control_vals, equal_var=False)

    results.append({
        "taxon": row["taxon"],
        "log2FC": logFC,
        "t_statistic": t_stat,
        "p_value": p_val
    })

# Save results
pd.DataFrame(results).to_csv("species_ttest_results.csv", index=False)

print("✅ Analysis complete. Output saved to species_ttest_results.csv")
