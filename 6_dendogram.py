import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.preprocessing import StandardScaler

# Step 1: Load the data
df = pd.read_csv("final.csv")

# Step 2: Extract only the sample columns (SRR...)
sample_cols = [col for col in df.columns if col.startswith("SRR")]
sample_data = df[sample_cols]

# Step 3: Transpose data so each sample is a row
sample_data_T = sample_data.T

# Step 4: Standardize the transposed data
scaler = StandardScaler()
scaled_data_T = scaler.fit_transform(sample_data_T)

# Step 5: Compute linkage matrix using Ward's method
linkage_matrix = sch.linkage(scaled_data_T, method='ward')

# Step 6: Plot the dendrogram
plt.figure(figsize=(12, 6))
dendrogram = sch.dendrogram(linkage_matrix, labels=sample_data_T.index, leaf_rotation=90)
plt.title("Hierarchical Clustering of Samples")
plt.xlabel("Sample")
plt.ylabel("Distance")
plt.tight_layout()
plt.savefig("dendogram_plot.png", dpi=300)
plt.show()