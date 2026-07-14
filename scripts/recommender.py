"""
Bluestock Mutual Fund Recommender

Purpose:
Perform advanced mutual fund analytics including:
- VaR & CVaR
- Rolling Sharpe Ratio
- Cohort Analysis
- SIP Continuity Analysis
- Top 3 Mutual Fund Recommendation
- Sector HHI Report

Author: Nitan Sharma
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

NAV_FILE = os.path.join(DATA_DIR, "02_nav_history.csv")
PERFORMANCE_FILE = os.path.join(DATA_DIR, "07_scheme_performance.csv")
TRANSACTION_FILE = os.path.join(DATA_DIR, "08_investor_transactions.csv")
FUND_MASTER_FILE = os.path.join(DATA_DIR, "01_fund_master.csv")
PORTFOLIO_FILE = os.path.join(DATA_DIR, "09_portfolio_holdings.csv")


# -----------------------------
# Load Data
# -----------------------------
nav = pd.read_csv(NAV_FILE)
performance = pd.read_csv(PERFORMANCE_FILE)
transactions = pd.read_csv(TRANSACTION_FILE)
fund_master = pd.read_csv(FUND_MASTER_FILE)
portfolio = pd.read_csv(PORTFOLIO_FILE)

nav["date"] = pd.to_datetime(nav["date"])
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# -----------------------------
# Daily Returns
# -----------------------------
nav = nav.sort_values(["amfi_code", "date"])
nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

# -----------------------------
# VaR & CVaR
# -----------------------------
var95 = nav.groupby("amfi_code")["daily_return"].quantile(0.05)

cvar = nav.groupby("amfi_code").apply(
    lambda x: x.loc[
        x["daily_return"] <= x["daily_return"].quantile(0.05),
        "daily_return"
    ].mean()
)

risk_report = pd.DataFrame({
    "VaR_95": var95,
    "CVaR": cvar
}).reset_index()

risk_report.to_csv(
    os.path.join(BASE_DIR, "var_cvar_report.csv"),
    index=False
)

print("VaR/CVaR Report Generated")

# -----------------------------
# Rolling Sharpe Ratio
# -----------------------------
risk_free_daily = 0.065 / 252

nav["excess_return"] = (
    nav["daily_return"] - risk_free_daily
)


def rolling_sharpe(series):
    mean = series.rolling(90).mean()
    std = series.rolling(90).std()
    return (mean / std) * np.sqrt(252)


nav["rolling_sharpe"] = (
    nav.groupby("amfi_code")["excess_return"]
       .transform(rolling_sharpe)
)

plt.figure(figsize=(12,6))

top5 = nav["amfi_code"].drop_duplicates().head(5)

for fund in top5:

    temp = nav[nav["amfi_code"] == fund]

    plt.plot(
        temp["date"],
        temp["rolling_sharpe"],
        label=str(fund)
    )

plt.title("Rolling 90-Day Sharpe Ratio")
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.legend()
plt.grid(True)

plt.savefig(
    os.path.join(BASE_DIR, "rolling_sharpe_chart.png"),
    dpi=300
)

plt.close()

print("Rolling Sharpe Chart Saved")

# -----------------------------
# Cohort Analysis
# -----------------------------
first_year = (
    transactions.groupby("investor_id")["transaction_date"]
    .min()
    .dt.year
    .reset_index()
)

first_year.rename(
    columns={"transaction_date": "cohort_year"},
    inplace=True
)

transactions = transactions.merge(
    first_year,
    on="investor_id",
    how="left"
)

cohort = (
    transactions.groupby("cohort_year")["amount_inr"]
    .mean()
    .reset_index(name="avg_investment")
)

print("\nCohort Analysis")
print(cohort)

# -----------------------------
# SIP Continuity
# -----------------------------
sip = transactions[
    transactions["transaction_type"] == "SIP"
].copy()

sip = sip.sort_values(
    ["investor_id", "transaction_date"]
)

sip["prev_date"] = sip.groupby(
    "investor_id"
)["transaction_date"].shift(1)

sip["gap_days"] = (
    sip["transaction_date"] - sip["prev_date"]
).dt.days

eligible = (
    sip.groupby("investor_id")
    .filter(lambda x: len(x) >= 6)
)

gap_report = (
    eligible.groupby("investor_id")["gap_days"]
    .mean()
    .reset_index(name="avg_gap_days")
)

gap_report["status"] = np.where(
    gap_report["avg_gap_days"] > 35,
    "At-Risk",
    "Regular"
)

print("\nSIP Continuity Completed")

# -----------------------------
# Recommendation Engine
# -----------------------------
risk = input(
    "\nEnter Risk Appetite (Low / Moderate / High): "
)

recommended = performance[
    performance["risk_grade"].str.lower()
    == risk.lower()
]

recommended = recommended.sort_values(
    by="sharpe_ratio",
    ascending=False
)

print("\nTop 3 Recommended Funds\n")

print(
    recommended.head(3)[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)

# -----------------------------
# Sector HHI
# -----------------------------
portfolio["weight"] = (
    portfolio["weight_pct"] / 100
)

hhi = (
    portfolio.groupby("amfi_code")["weight"]
    .apply(lambda x: (x ** 2).sum())
    .reset_index(name="HHI")
)

hhi = hhi.merge(
    fund_master[
        ["amfi_code", "scheme_name"]
    ],
    on="amfi_code",
    how="left"
)

hhi = hhi.sort_values(
    by="HHI",
    ascending=False
)

hhi.to_csv(
    os.path.join(BASE_DIR, "sector_hhi_report.csv"),
    index=False
)

print("\nSector HHI Report Generated")

print("\nAdvanced Analytics Completed Successfully.")


