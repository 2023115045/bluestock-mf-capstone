# Data Dictionary

## 1. fund_master

| Column Name | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI mutual fund code |
| fund_house | TEXT | Name of fund house |
| scheme_name | TEXT | Mutual fund scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Direct or Regular plan |
| launch_date | DATE | Fund launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | FLOAT | Expense ratio percentage |
| exit_load_pct | FLOAT | Exit load percentage |
| min_sip_amount | FLOAT | Minimum SIP investment |
| min_lumpsum_amount | FLOAT | Minimum lumpsum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk level |
| sebi_category_code | TEXT | SEBI category code |

---

## 2. nav_history

| Column Name | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Mutual fund AMFI code |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value |

---

## 3. investor_transactions

| Column Name | Data Type | Description |
|---|---|---|
| investor_id | INTEGER | Unique investor ID |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Mutual fund AMFI code |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | FLOAT | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification |
| age_group | TEXT | Investor age category |
| gender | TEXT | Investor gender |
| annual_income_lakh | FLOAT | Annual income |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

## 4. scheme_performance

| Column Name | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Mutual fund AMFI code |
| scheme_name | TEXT | Mutual fund scheme |
| fund_house | TEXT | Fund company |
| category | TEXT | Scheme category |
| plan | TEXT | Plan type |
| return_1yr_pct | FLOAT | 1-year return percentage |
| return_3yr_pct | FLOAT | 3-year return percentage |
| return_5yr_pct | FLOAT | 5-year return percentage |
| benchmark_3yr_pct | FLOAT | Benchmark return |
| alpha | FLOAT | Alpha metric |
| beta | FLOAT | Beta metric |
| sharpe_ratio | FLOAT | Sharpe ratio |
| sortino_ratio | FLOAT | Sortino ratio |
| std_dev_ann_pct | FLOAT | Annual standard deviation |
| max_drawdown_pct | FLOAT | Maximum drawdown |
| aum_crore | FLOAT | Assets under management |
| expense_ratio_pct | FLOAT | Expense ratio |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk grade |