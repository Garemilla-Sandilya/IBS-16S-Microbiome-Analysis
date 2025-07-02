import pandas as pd
df = pd.read_csv("taxlevel_6.csv")
abundance_df = df.set_index("taxon").iloc[:, 5:]
percentage_normalized = abundance_df.div(abundance_df.sum(axis=0), axis=1) * 100
percentage_normalized = percentage_normalized.reset_index()
percentage_normalized.to_csv("taxlevel_6_percentage_normalized.csv", index=False)

# Verify if each column (except 'taxon') sums to 100
column_sums = percentage_normalized.drop(columns="taxon").sum()
print("Column totals (should all be 100):\n", column_sums)
print("successfully completed")