import pandas as pd

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    print("\n" + "=" * 60)
    print(f"DATASET: {file}")
    print("=" * 60)

    df = pd.read_csv(f"data/raw/{file}")

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\n")
print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].value_counts())

print("\n")
print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print(f"Total AMFI Codes in Fund Master: {len(master_codes)}")
print(f"Total AMFI Codes in NAV History: {len(nav_codes)}")

print("\nMissing Codes:")
print(missing_codes)

print(f"\nNumber of Missing Codes: {len(missing_codes)}")