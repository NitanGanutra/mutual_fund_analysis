-- Total NAV Records
SELECT COUNT(*) FROM nav_history;

-- Total Transactions
SELECT COUNT(*) FROM investor_transactions;

-- Total Schemes
SELECT COUNT(*) FROM scheme_performance;

-- Average 3 Year Return
SELECT AVG(return_3yr_pct)
FROM scheme_performance;

-- Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Transaction Type Distribution
SELECT transaction_type,
       COUNT(*) AS total
FROM investor_transactions
GROUP BY transaction_type;

