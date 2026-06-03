-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Highest 1-Year Return
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 4. Lowest Expense Ratio
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC
LIMIT 5;

-- 5. Fund Count by Category
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- 6. Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 7. Total Transaction Amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- 8. KYC Status Distribution
SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;

-- 9. Average AUM
SELECT AVG(aum_crore)
FROM fact_performance;

-- 10. Highest Sharpe Ratio
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;