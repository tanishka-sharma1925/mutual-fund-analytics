import pandas as pd
from sqlalchemy import create_engine

print("Creating SQLite Database...")

# Create database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load datasets
fund_df = pd.read_csv("data/raw/01_fund_master.csv")

nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

perf_df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

txn_df = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

# Load into SQLite
fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")
print("Database File: bluestock_mf.db")