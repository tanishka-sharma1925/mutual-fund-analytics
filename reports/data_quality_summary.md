# Day 1 Data Quality Summary

## Dataset Overview

| Dataset | Rows | Columns |
|----------|----------|----------|
| 01_fund_master.csv | 40 | 15 |
| 02_nav_history.csv | 46000 | 3 |
| 08_investor_transactions.csv | 32778 | 13 |

## Data Quality Checks

### Missing Values

- 01_fund_master.csv → No missing values
- 02_nav_history.csv → No missing values observed
- 04_monthly_sip_inflows.csv → 12 missing values in yoy_growth_pct

### Duplicate Records

- No duplicate rows found in inspected datasets

## Fund Master Analysis

### Fund Houses

Total Fund Houses: 10

- SBI Mutual Fund
- HDFC Mutual Fund
- ICICI Prudential MF
- Nippon India MF
- Kotak Mahindra MF
- Axis Mutual Fund
- Aditya Birla Sun Life MF
- UTI Mutual Fund
- Mirae Asset MF
- DSP Mutual Fund

### Categories

- Equity
- Debt

### Risk Categories

- Moderate: 16
- High: 8
- Very High: 6
- Low: 6
- Moderately High: 4

## AMFI Validation

Total AMFI Codes in Fund Master: 40

Total AMFI Codes in NAV History: 40

Missing Codes: 0

Result:
All AMFI scheme codes are present in NAV history.

## Live NAV Fetch

Successfully fetched NAV data from MFAPI and exported NAV history CSV files for multiple schemes.

Status: Successful