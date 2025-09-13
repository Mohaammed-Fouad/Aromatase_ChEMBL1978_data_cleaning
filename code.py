# Install ChEMBL client (uncomment if running in Colab/Jupyter)
# !pip install chembl_webresource_client

# Import libraries
import pandas as pd
from chembl_webresource_client.new_client import new_client

# -----------------------------
# Step 1: Query target (Aromatase)
# -----------------------------
target = new_client.target
target_query = target.search('aromatase')

# Convert to DataFrame
targets = pd.DataFrame.from_dict(target_query)

# Select the first target from the search
selected_target = targets.target_chembl_id[0]

# -----------------------------
# Step 2: Get bioactivity data (IC50)
# -----------------------------
activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")

df = pd.DataFrame.from_dict(res)

# -----------------------------
# Step 3: Data cleaning
# -----------------------------
# Drop rows without IC50 values
df.dropna(subset=['standard_value'], inplace=True)

# Check available units
print("Unique units:", df.standard_units.unique())

# Count occurrences of main units
unit_counts = df['standard_units'].value_counts()
print("Counts of standard_units:")
print(unit_counts[['nM', 'mg kg-1', 'ug.mL-1']])

# Keep only nanomolar (nM) values
df = df[~df['standard_units'].isin(['mg kg-1', 'ug.mL-1'])]

# Convert IC50 values to numeric
df['standard_value'] = pd.to_numeric(df['standard_value'], errors='coerce')

# -----------------------------
# Step 4: Classify bioactivity
# -----------------------------
# Active (0–1000 nM), Intermediate (1000–10,000 nM), Inactive (10,000–1,000,000 nM)
df['activity'] = pd.cut(
    df.standard_value,
    bins=[0, 1000, 10000, 1000000],
    labels=['active', 'intermediate', 'inactive'],
    right=False
)

# -----------------------------
# Step 5: Create final dataset
# -----------------------------
# Keep only relevant columns
df2 = df[['molecule_chembl_id', 'canonical_smiles', 'standard_value', 'activity']].copy()

# Rename columns
df2.rename(
    columns={
        'canonical_smiles': 'SMILES',
        'standard_value': 'IC50 nM',
        'molecule_chembl_id': 'ChEMBL'
    },
    inplace=True
)

# Preview
print(df2.head())

# Save to CSV
df2.to_csv('anticancer_activity_data.csv', index=False)
print("Bioactivity data saved to 'bioactivity_data.csv'")
