"""
Bluestock Mutual Fund Analytics

File: day2_cleaning.py

Purpose:
Clean raw mutual fund datasets by handling
missing values, duplicates, and formatting.

Author: Nitan Sharma
"""
import pandas as pd

# Load transactions dataset
txn = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Rows:", len(txn))

# Convert date
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

# Remove duplicate rows
txn = txn.drop_duplicates()

# Keep only positive amounts
txn = txn[txn["amount_inr"] > 0]

# Valid KYC values
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

print("Cleaned Rows:", len(txn))

# Save cleaned file
txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("File Saved Successfully!")
# SCHEME PERFORMANCE CLEANING

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\nPerformance Original Rows:", len(perf))

cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf = perf.drop_duplicates()

perf = perf[
    (perf["return_1yr_pct"] >= -100)
    &
    (perf["return_1yr_pct"] <= 100)
]

perf = perf[
    (perf["expense_ratio_pct"] >= 0)
    &
    (perf["expense_ratio_pct"] <= 5)
]

print("Performance Cleaned Rows:", len(perf))

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("scheme_performance_clean.csv saved")