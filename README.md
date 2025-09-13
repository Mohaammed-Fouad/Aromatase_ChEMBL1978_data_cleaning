# Aromatase Inhibitor Bioactivity Data

This repository contains a Python script that uses the **ChEMBL** database to retrieve, clean, and classify bioactivity data for **aromatase inhibitors**. The final output is a clean CSV file containing key information about the molecules and their activity.

### How It Works

The script automates a multi-step process for data retrieval and preparation:

1.  **Target Query:** It searches the ChEMBL database for the target protein "Aromatase" and selects the relevant ChEMBL ID.
2.  **Bioactivity Retrieval:** It retrieves all bioactivity data, specifically **IC50** values, associated with the selected aromatase target.
3.  **Data Cleaning:** The raw data is cleaned by removing entries without an IC50 value and filtering for only **nanomolar (nM)** units to ensure consistency.
4.  **Activity Classification:** The molecules are classified into three categories based on their IC50 value:
      * **Active:** $\< 1000 \\text{ nM}$
      * **Intermediate:** $1000 - 10,000 \\text{ nM}$
      * **Inactive:** $\> 10,000 \\text{ nM}$
5.  **Final Dataset Creation:** A final dataset is created with key columns—molecule ChEMBL ID, canonical SMILES, IC50 value, and the new activity classification—and saved to a CSV file.

-----

### Getting Started

#### Prerequisites

To run this script, you'll need the `pandas` library and the `chembl_webresource_client`.

You can install them using pip:

```bash
pip install pandas chembl_webresource_client
```

#### Running the Script

1.  Save the code as a Python file (e.g., `get_aromatase_data.py`).
2.  Run the script from your terminal:

<!-- end list -->

```bash
python get_aromatase_data.py
```

After execution, a file named `anticancer_activity_data.csv` will be saved in the same directory.

### Output

The final `anticancer_activity_data.csv` file will have the following columns:

  * **ChEMBL:** The unique identifier for the molecule in the ChEMBL database.
  * **SMILES:** The canonical SMILES string representing the molecule's structure.
  * **IC50 nM:** The IC50 value in nanomolars.
  * **activity:** The bioactivity class (`active`, `intermediate`, or `inactive`).

### Example Output

```
   ChEMBL                       SMILES  IC50 nM      activity
0  CHEMBL108605  O=C(O)c1ccc(c(Cl)c1)C#N   1.0000  intermediate
1  CHEMBL135606  CC(C)CC(NC(C)C)C(=O)O    3.4000        active
2  CHEMBL37409   Cc1cc(C)c2ccccc2c1       5.6000        active
3  CHEMBL136976  C[C@@H](C)CC(=O)O        8.5000        active
4  CHEMBL59317   C[C@H](O)C(=O)c1ccccc1   10.0000        active
```
