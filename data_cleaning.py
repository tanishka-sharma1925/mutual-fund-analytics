import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Dataset Loaded")
print("Rows:", len(df))

# ==================================
# Convert return columns to numeric
# ==================================

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ==================================
# Check missing numeric values
# ==================================

print("\nMissing Values:")
print(df[return_cols].isnull().sum())

# ==================================
# Expense Ratio Validation
# ==================================

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nFunds with Invalid Expense Ratio:")
print(len(invalid_expense))

if len(invalid_expense) > 0:
    print(invalid_expense[
        ["scheme_name", "expense_ratio_pct"]
    ])

# ==================================
# Check duplicates
# ==================================

before_rows = len(df)

df = df.drop_duplicates()

after_rows = len(df)

print("\nDuplicates Removed:")
print(before_rows - after_rows)

# ==================================
# Save cleaned file
# ==================================

output_file = (
    "data/processed/"
    "07_scheme_performance_cleaned.csv"
)

df.to_csv(output_file, index=False)

print("\nSaved Successfully:")
print(output_file)

print("\n========== SUMMARY ==========")
print("Rows:", len(df))
print("Invalid Expense Ratios:", len(invalid_expense))
print("Duplicates Removed:", before_rows - after_rows)
print("=============================")