import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_csv("final.csv")  # Ya phir aapke local path se load karein

# Step 2: Extract only sample columns (starting with 'SRR')
sample_cols = [col for col in df.columns if col.startswith("SRR")]
sample_data = df[sample_cols]

# Step 3: Transpose data to perform PCA across samples
sample_data_T = sample_data.T

# Step 4: Standardize the transposed data
scaler = StandardScaler()
scaled_data_T = scaler.fit_transform(sample_data_T)

# Step 5: Perform PCA
pca = PCA(n_components=2)
pca_result_T = pca.fit_transform(scaled_data_T)

# Step 6: Make a DataFrame for PCA results
pca_df_T = pd.DataFrame(pca_result_T, columns=["PC1", "PC2"])
pca_df_T["Sample"] = sample_data_T.index

# Step 7: Plot PCA
plt.figure(figsize=(10, 7))
plt.scatter(pca_df_T["PC1"], pca_df_T["PC2"], alpha=0.8)

# Annotate each point with its sample ID
for i, sample in enumerate(pca_df_T["Sample"]):
    plt.text(pca_df_T["PC1"][i], pca_df_T["PC2"][i], sample, fontsize=9)

plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.2f}% variance)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.2f}% variance)")
plt.title("PCA Across Samples")
plt.grid(True)
plt.tight_layout()
plt.savefig("pca_plot.png", dpi=300)
plt.show()
