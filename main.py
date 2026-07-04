import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)

print("Dataset Loaded Successfully")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:", df.shape)

# -----------------------------
# Data Cleaning
# -----------------------------
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

# Remove rows where Amount is missing
df = df.dropna(subset=["Amount"])

# Remove duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

print("New Shape:", df.shape)

# -----------------------------
# Dataset Summary
# -----------------------------
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumerical Summary:")
print(df.describe())

# -----------------------------
# KPI Metrics
# -----------------------------
print("\n===== KPI METRICS =====")

total_revenue = df["Amount"].sum()
average_order_value = df["Amount"].mean()
total_orders = len(df)

print("Total Revenue:", round(total_revenue, 2))
print("Average Order Value:", round(average_order_value, 2))
print("Total Orders:", total_orders)

# -----------------------------
# Cancellation Rate
# -----------------------------
cancelled = df["Status"].str.contains(
    "cancelled",
    case=False,
    na=False
)

cancel_rate = cancelled.sum() / len(df) * 100

print(f"Cancellation Rate: {cancel_rate:.2f}%")

# -----------------------------
# Category Wise Sales
# -----------------------------
category_sales = (
    df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory Sales:")
print(category_sales)

# -----------------------------
# Top Selling Products
# -----------------------------
top_products = (
    df.groupby("SKU")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products:")
print(top_products)

# -----------------------------
# Top States by Sales
# -----------------------------
state_sales = (
    df.groupby("ship-state")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop States:")
print(state_sales)

# -----------------------------
# Top Cities by Sales
# -----------------------------
city_sales = (
    df.groupby("ship-city")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Cities:")
print(city_sales)

# -----------------------------
# Order Status
# -----------------------------
status_counts = df["Status"].value_counts().head(5)

print("\nOrder Status:")
print(status_counts)

# -----------------------------
# Monthly Sales Trend
# -----------------------------
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

monthly_sales = (
    df.groupby(df["Date"].dt.month)["Amount"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)