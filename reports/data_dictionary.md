# Mutual Fund Analytics Data Dictionary

## 01_fund_master.csv

| Column | Description |
|----------|----------|
| amfi_code | Unique AMFI scheme code |
| fund_house | Fund provider |
| scheme_name | Scheme name |
| category | Fund category |
| sub_category | Fund subtype |
| plan | Direct/Regular |
| risk_category | Risk classification |

---

## 02_nav_history.csv

| Column | Description |
|----------|----------|
| amfi_code | Fund identifier |
| date | NAV date |
| nav | Net Asset Value |

---

## 07_scheme_performance.csv

| Column | Description |
|----------|----------|
| return_1yr_pct | 1 Year Return |
| return_3yr_pct | 3 Year Return |
| return_5yr_pct | 5 Year Return |
| sharpe_ratio | Risk adjusted return |
| alpha | Excess return |
| beta | Market sensitivity |
| aum_crore | Assets Under Management |
| expense_ratio_pct | Expense ratio |

---

## 08_investor_transactions.csv

| Column | Description |
|----------|----------|
| investor_id | Investor identifier |
| transaction_date | Transaction date |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |
| kyc_status | KYC verification status |