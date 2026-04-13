# End-to-End Sales Data Pipeline with AI Anomaly Detection

## Overview
A complete ETL pipeline engineered to process raw sales data, validate schemas, identify statistical anomalies using machine learning, and load the refined datasets into a relational database for visualization. 

This project demonstrates core data engineering principles: data extraction, programmatic cleaning, machine learning integration, and SQL database loading.

## Architecture & Workflow
1. **Extraction:** Python scripts locate and ingest raw CSV data.
2. **Transformation:** Standardizes column schemas, enforces strict datetime formatting, and drops corrupted or incomplete records.
3. **Machine Learning (AI Layer):** Implements an Isolation Forest algorithm (`scikit-learn`) to scan transaction histories and flag the top 2% most anomalous sales records (e.g., extreme spikes or drops).
4. **Loading:** Automatically creates an SQLite database (`sales_database.db`) and securely loads clean data and AI-flagged records into distinct SQL tables.
5. **Visualization:** Power BI connects directly to the SQLite database to visualize daily sales trends and isolate regional anomalies for business stakeholders.

## Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas
* **Machine Learning:** Scikit-Learn (Isolation Forest)
* **Database:** SQLite
* **Visualization:** Power BI

## Repository Structure
```text
ai-data-pipeline-sales/
├── data/
│   ├── raw/               # Original CSV files
│   └── processed/         # Cleaned CSVs and SQLite database
├── scripts/
│   ├── data_cleaning.py       # ETL extraction and transformation logic
│   ├── anomaly_detection.py   # ML Isolation Forest implementation
│   └── load_to_sql.py         # Database connection and table creation
├── outputs/               # Generated anomaly reports
├── dashboard/             # Power BI (.pbix) file
└── README.md