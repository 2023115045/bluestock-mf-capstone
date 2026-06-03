SELECT * FROM nav_history
LIMIT 10;
SELECT COUNT(*) FROM nav_history;

SELECT MAX(nav) FROM nav_history;

SELECT MIN(nav) FROM nav_history;

SELECT AVG(nav) FROM nav_history;

SELECT COUNT(*) AS Total_Records
FROM nav_history;

SELECT MAX(nav) AS Maximum_NAV
FROM nav_history;

SELECT MIN(nav) AS Minimum_NAV
FROM nav_history;

SELECT AVG(nav) AS Average_NAV
FROM nav_history;

-- Top 5 funds by AUM
SELECT scheme_name, aum
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV per month
SELECT strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- Funds with low expense ratio
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;