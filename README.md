# Transaction Portfolio Data ETL

An end-to-end Python ETL pipeline for cleaning, validating, enriching, and exporting transaction portfolio data from a raw CSV source into analysis-ready datasets.

This project was designed around a realistic financial transaction workflow:
- explore a raw transaction dataset
- clean and standardize inconsistent values
- engineer business-oriented features
- export final deliverables for downstream analysis and reporting

## Project objectives

The pipeline transforms a raw transactional dataset into a structured and documented final output by:

- diagnosing data quality issues
- removing duplicate transactions
- standardizing mixed date and numeric formats
- handling missing values
- detecting anomalous transactions
- creating analytical and risk-oriented features
- exporting clean intermediate and final files
- documenting all cleaning decisions

## Workflow

The project is organized as a multi-step ETL pipeline:

1. **Exploration**
   - inspect dataset shape, columns, data types, missing values, and duplicates
   - identify problematic fields before transformation

2. **Cleaning**
   - remove duplicate records
   - standardize dates
   - convert numeric-like text fields into numeric columns
   - normalize text columns
   - handle missing values
   - drop unusable columns when necessary

3. **Feature engineering**
   - create time-based variables
   - verify converted EUR values
   - create a risk category from credit score
   - flag anomalies
   - compute customer- and agency-level indicators

4. **Final export**
   - validate final structure
   - export deliverables
   - generate a cleaning decision log

## Project structure

```text
Transaction-Portfolio-Data-ETL/
│
├── bank_transactions.csv              # Raw input dataset
├── main.py                            # Runs the full pipeline
├── step1_exploration.py               # Exploration and diagnostics
├── step2_cleaning.py                  # Data cleaning
├── step3_features_export.py           # Feature engineering
├── step4_export.py                    # Final export and documentation
├── utils.py                           # Shared utility functions
│
├── financecore_step1_clean.csv        # Cleaned intermediate dataset
├── financecore_step2_enriched.csv     # Enriched intermediate dataset
├── financecore_clean.csv              # Final exported dataset
├── DECISIONS.md                       # Cleaning decisions
│
├── exploration.log                    # Logs from exploration step
├── cleaning.log                       # Logs from cleaning step
├── feature_engineering.log            # Logs from feature step
└── export.log                         # Logs from final export
