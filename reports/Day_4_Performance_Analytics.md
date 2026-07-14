# Day 4 – Performance Analytics

## Objective

Perform performance analysis of mutual funds using historical NAV data and evaluate fund performance using financial metrics.

## Work Completed

### 1. Loaded Required Data

* Connected to the SQLite database.
* Loaded `nav_history` and `scheme_performance` tables.
* Loaded benchmark data from `10_benchmark_indices.csv`.

### 2. Daily Return Calculation

* Converted the `date` column to datetime format.
* Sorted NAV data by `amfi_code` and `date`.
* Calculated daily returns using `pct_change()`.
* Plotted the distribution of daily returns.

### 3. CAGR Comparison

* Used 1-year, 3-year and 5-year return columns from the `scheme_performance` table.
* Created a comparison table and ranked funds based on 3-year returns.

### 4. Sharpe Ratio Analysis

* Ranked all mutual funds based on Sharpe Ratio.
* Exported the ranking for further analysis.

### 5. Sortino Ratio Analysis

* Ranked all mutual funds using Sortino Ratio to evaluate downside risk-adjusted performance.

### 6. Alpha and Beta Analysis

* Analysed Alpha and Beta values for each fund.
* Exported the results as `alpha_beta.csv`.

### 7. Maximum Drawdown Analysis

* Compared all funds using Maximum Drawdown values.
* Ranked funds based on drawdown performance.

### 8. Fund Scorecard

* Created a composite score using:

  * 30% 3-Year Return Rank
  * 25% Sharpe Ratio Rank
  * 20% Alpha Rank
  * 15% Expense Ratio Rank
  * 10% Maximum Drawdown Rank
* Generated the final fund scorecard.
* Exported `fund_scorecard.csv`.

### 9. Benchmark Comparison

* Selected the Top 5 funds based on the final score.
* Rebased NAV values to 100.
* Rebased NIFTY50 and NIFTY100 benchmark values.
* Created an interactive Plotly comparison chart.
* Exported the chart as `benchmark_comparison.html`.

## Deliverables

* Performance_Analytics.ipynb
* fund_scorecard.csv
* alpha_beta.csv
* benchmark_comparison.html

## Skills Practiced

* Pandas
* SQL with SQLite
* Plotly
* Seaborn
* Financial Performance Metrics
* Ranking and Scorecard Generation
* Data Analysis using Jupyter Notebook
