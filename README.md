# SWYNEX Task 1 – Data Cleaning & Preparation

## Project

Online Retail Dataset – Data Cleaning and Preparation

## Objective

Clean and prepare a raw online retail dataset by identifying data quality issues and applying suitable cleaning steps to make the data more reliable for further analysis.

## Dataset

- Rows in raw dataset: 20,000
- Columns: 8
- Source: Kaggle – Online Retail Dataset
- Raw file: `Online_Retail_Raw.csv`

## Data Quality Issues Identified

### 1. Missing Values

- Missing `Description` values were identified and removed.
- Missing `CustomerID` values were identified and retained.

### 2. Duplicate Records

- Duplicate records were identified in the raw dataset.
- Exact duplicate rows were removed.

### 3. Zero Unit Price

- Records with `UnitPrice` equal to zero were identified and removed.

### 4. Negative Quantity

- Negative `Quantity` values were inspected and retained because they may represent returns or cancellations.

### 5. Data Type

- `InvoiceDate` was converted to datetime format for proper date handling.

## Cleaning Steps

1. Loaded the raw dataset using Pandas.
2. Inspected the dataset structure, data types, missing values, and duplicates.
3. Removed rows with missing `Description`.
4. Removed duplicate records.
5. Converted `InvoiceDate` to datetime format.
6. Removed records with zero `UnitPrice`.
7. Inspected negative `Quantity` values and retained them.
8. Checked for negative `UnitPrice` values.
9. Exported the cleaned dataset.
10. Generated a data quality report and quality summary.

## Final Dataset

- Final rows: 19,549
- Columns: 8
- Duplicate rows: 0
- Missing `CustomerID` values: 6,517
- Missing values in other columns: 0
- Negative `Quantity` records retained: 261
- Zero `UnitPrice` records: 0

## Files

- `Online_Retail_Raw.csv` – Original raw dataset
- `Online_Retail_Cleaned.csv` – Cleaned dataset
- `Online-Retail-Data-Cleaning.py` – Python cleaning script
- `Data Cleaning.ipynb` – Jupyter Notebook with the cleaning process
- `data_quality_report.csv` – Column-wise missing-value and data-type report for the cleaned dataset
- `Quality_Summary.txt` – Summary of dataset cleaning results
- `README.md` – Project documentation

## Tools Used

- Python
- Pandas
- Jupyter Notebook
- VS Code
- CSV

## Conclusion

The dataset was cleaned by removing rows with missing descriptions, duplicate records, and zero unit-price entries. The invoice date was converted to datetime format, and negative quantity records were retained for possible return or cancellation analysis.

The final dataset contains 19,549 rows and 8 columns, with no duplicate rows. A total of 6,517 `CustomerID` values remain missing, while the other columns have no missing values. The cleaned dataset and supporting files are prepared for further analysis.
