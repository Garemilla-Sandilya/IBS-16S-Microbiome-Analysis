import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("taxlevel_6.csv")  # Adjust path as needed

# Prepare the data
abundance_data = df.set_index("taxon").iloc[:, 5:]
barplot_data = abundance_data.transpose()

# Plot
barplot_data.plot(kind="bar", stacked=True, figsize=(14, 8), width=0.8, colormap="tab20")
plt.title("Stacked Bar Plot of Microbial Abundance (Genus Level)")
plt.xlabel("Sample")
plt.ylabel("Abundance")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Taxon")
plt.tight_layout()
plt.savefig("stacked_barplot_microbial_abundance.png", dpi=300, bbox_inches="tight")
plt.show()
