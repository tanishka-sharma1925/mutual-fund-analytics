Dataset: 01_fund_master.csv

Shape: 40 rows × 15 columns

Observations:
- No missing values
- AMFI code appears unique
- Categories and risk classifications present
- Suitable as master dimension table

Dataset: 04_monthly_sip_inflows.csv

Issue:
- Column yoy_growth_pct contains 12 missing values

Possible Reason:
- First year records may not have a previous year available for YoY calculation.