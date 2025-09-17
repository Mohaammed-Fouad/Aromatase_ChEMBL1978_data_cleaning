# Anticancer Activity Prediction

This project is a machine learning notebook that demonstrates how to predict the anticancer activity of chemical compounds using data from the ChEMBL database. The notebook walks through the entire process, from data retrieval and preprocessing to model building and prediction, using standard Python libraries.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Notebook Breakdown](#notebook-breakdown)
- [Acknowledgements](#acknowledgements)

---

### Project Overview

The goal of this project is to build a machine learning model that can predict the pIC50 (a measure of compound potency) for various chemical compounds based on their molecular properties. The data is sourced directly from the ChEMBL API, specifically targeting compounds with anticancer activity against a particular target (CHEMBL355).

The key steps covered in the notebook include:
- **Data Acquisition:** Fetching bioactivity data directly from the ChEMBL database.
- **Data Preprocessing:** Cleaning and preparing the data by handling missing values and standardizing compound identifiers.
- **Feature Engineering:** Calculating molecular descriptors (features) that are used as input for the machine learning model.
- **Model Training:** Training a random forest model to predict pIC50 values.
- **Prediction:** Using the trained model to predict the anticancer activity of a new compound.

---

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mohaammed-Fouad/Activity_prediction_against_aromatase_ChEMBL1978.git
    cd Activity_prediction_against_aromatase_ChEMBL1978
    ```
2.  **Install the required libraries:**
    The project relies on the following Python libraries. It's recommended to create a virtual environment first.
    
    ```bash
    pip install pandas chembl_webresource_client scikit-learn
    ```

---

### Usage

To run the notebook and replicate the analysis:

1.  Open the `anticancer_activity_prediction.ipynb` file in a Jupyter environment (e.g., Jupyter Notebook, JupyterLab, or Google Colab).
2.  Execute the cells in sequential order.

---

### Notebook Breakdown

* **Installing the Data:** Installs the `chembl_webresource_client` library to interact with the ChEMBL database.
* **Searching and Retrieving Data:** Fetches bioactivity data for the specified target.
* **Data Preparation:** Cleans the retrieved data, removes missing values, and prepares it for analysis.
* **Feature Calculation:** Computes molecular descriptors needed for the model.
* **Model Training and Prediction:** Trains a RandomForestRegressor and demonstrates how to make predictions on a new compound.

---

### Acknowledgements

This code was created with the assistance of AI and was heavily inspired by online tutorials. Special thanks to the YouTube channels "Data Professor" and "Omixium" and their creators, Dr. Chanin Nantasenamat (`@dataprofessor` on GitHub) and Dr. Pritam Cumar (`@pritampanda15` on GitHub), for providing comprehensive and insightful tutorials on this topic.
