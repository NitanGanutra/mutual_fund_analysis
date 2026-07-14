"""
Bluestock Mutual Fund Analytics

File: load_to_sqlite.py

Purpose:
Load cleaned mutual fund datasets into
SQLite database.

Author: Nitan Sharma
"""
import pandas as pd
from sqlalchemy import create_engine

# SQLite database
engine = create_engine("sqlite:///mutual_fund.db")

# Load cleaned files
nav = pd.read_csv("data/processed/nav_history_clean.csv")
txn = pd.read_csv("data/processed/investor_transactions_clean.csv")
perf = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Save tables
nav.to_sql("nav_history", engine, if_exists="replace", index=False)
txn.to_sql("investor_transactions", engine, if_exists="replace", index=False)
perf.to_sql("scheme_performance", engine, if_exists="replace", index=False)

print("Database Created Successfully!")