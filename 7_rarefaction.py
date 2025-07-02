import pandas as pd
import matplotlib.pyplot as plt

# Load the rarefaction file
df = pd.read_csv("final.opti_mcc.groups.rarefaction", sep='\t')

# Set the first column as x-axis (numsampled)
x = df.iloc[:, 0]
samples = df.columns[1:]

# Plot each sample's curve
plt.figure(figsize=(10, 6))
for sample in samples:
    plt.plot(x, df[sample], label=sample)

plt.xlabel("Number of Sequences Sampled")
plt.ylabel("Number of Observed OTUs")
plt.title("Rarefaction Curves")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.savefig("rarefaction_curves.png")
plt.show()

print("successfully completed")
