import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the t-test result CSV
df = pd.read_csv("species_ttest_results.csv")

# Calculate -log10(p-value)
df["neg_log10_p"] = -np.log10(df["p_value"])

# Set significance and fold change thresholds
pval_threshold = 0.05
fc_threshold = 1  # log2FC threshold

# Classify species for coloring in the volcano plot
def classify_species(row):
    if row["p_value"] < pval_threshold:
        if row["log2FC"] > fc_threshold:
            return "High abundance (Diseased)"
        elif row["log2FC"] < -fc_threshold:
            return "High abundance (Control)"
    return "Not Significant"

df["category"] = df.apply(classify_species, axis=1)

# Print species in each significant category
print("High abundance (Diseased) species:")
diseased_species = df[df["category"] == "High abundance (Diseased)"]["taxon"]
print(diseased_species.to_list())

print("\nHigh abundance (Control) species:")
control_species = df[df["category"] == "High abundance (Control)"]["taxon"]
print(control_species.to_list())

# Plot the volcano plot
plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=df,
    x="log2FC",
    y="neg_log10_p",
    hue="category",
    palette={"High abundance (Diseased)": "red", "High abundance (Control)": "blue", "Not Significant": "grey"},
    edgecolor=None,
    alpha=0.8
)

# Add threshold lines
plt.axhline(-np.log10(pval_threshold), color='black', linestyle='--', linewidth=1)
plt.axvline(fc_threshold, color='black', linestyle='--', linewidth=1)
plt.axvline(-fc_threshold, color='black', linestyle='--', linewidth=1)

plt.title("Volcano Plot of Species Abundance")
plt.xlabel("log2 Fold Change")
plt.ylabel("-log10(p-value)")
plt.legend(title="Category")
plt.tight_layout()

# Save plot
volcano_path = "volcano_plot.png"
plt.savefig(volcano_path)
