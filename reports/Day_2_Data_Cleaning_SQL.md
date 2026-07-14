# Day 2 – Data Cleaning & SQLite Database Design

## Objective

Clean the raw mutual fund datasets, validate data quality, design a SQLite database, and load the cleaned data for analysis.

## Work Completed

### 1. Data Cleaning

#### NAV History

* Converted the `date` column to datetime format.
* Sorted data by `amfi_code` and `date`.
* Removed duplicate records.
* Forward-filled missing NAV values for holidays and weekends.
* Validated that all NAV values are greater than zero.

#### Investor Transactions

* Standardized transaction types (`SIP`, `Lumpsum`, `Redemption`).
* Converted transaction dates into a consistent format.
* Removed invalid transaction amounts.
* Verified KYC status values.

#### Scheme Performance

* Checked that return columns contain numeric values.
* Validated expense ratio values.
* Identified and handled abnormal or missing values.

---

## SQLite Database Design

Created a SQLite database (`bluestock_mf.db`) using a star schema.

Tables created:

* dim_fund
* dim_date
* fact_nav
* fact_transactions
* fact_performance
* fact_aum

Primary keys and foreign keys were defined to maintain relationships between tables.

---

## Data Loading

* Connected to SQLite using SQLAlchemy.
* Loaded cleaned datasets using `df.to_sql()`.
* Verified row counts after loading.

---

## SQL Analysis

Created analytical SQL queries including:

* Top 5 funds by AUM
* Average monthly NAV
* Year-over-Year SIP growth
* Transactions by state
* Funds with expense ratio below 1%
* Additional analytical business queries

---

## Data Dictionary

Created a Markdown data dictionary containing:

* Column names
* Data types
* Business definitions
* Source dataset information

---

## Deliverables

* Cleaned CSV files
* bluestock_mf.db
* schema.sql
* analysis_queries.sql
* data_dictionary.md

## Skills Practiced

* Pandas Data Cleaning
* SQLAlchemy
* SQLite Database Design
* SQL Queries
* Data Validation
* Data Documentation
