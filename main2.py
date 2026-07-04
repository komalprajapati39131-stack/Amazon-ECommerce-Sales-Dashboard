import pandas as pd
import matplotlib.pyplot as plt

domestic = pd.read_csv(
    "Amazon Sale Report.csv",
    low_memory=False
)

international = pd.read_csv(
    "International sale Report.csv"
)

# Convert to numeric
domestic["Amount"] = pd.to_numeric(
    domestic["Amount"],
    errors="coerce"
)

international["GROSS AMT"] = pd.to_numeric(
    international["GROSS AMT"],
    errors="coerce"
)

# Revenue
domestic_revenue = domestic["Amount"].sum()
international_revenue = international["GROSS AMT"].sum()

print("Domestic Revenue =", domestic_revenue)
print("International Revenue =", international_revenue)

# Plot
labels = ["Domestic", "International"]
revenue = [domestic_revenue, international_revenue]

plt.figure(figsize=(8,5))
plt.bar(labels, revenue)

plt.title("Domestic vs International Revenue")
plt.xlabel("Market")
plt.ylabel("Revenue")

plt.show()


top_customers = (
    international.groupby("CUSTOMER")["GROSS AMT"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)

top_customers.plot(
    kind="bar",
    figsize=(12,5)
)

plt.title("Top 10 International Customers")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.show()


top_products = (
    international.groupby("SKU")["GROSS AMT"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

top_products.plot(
    kind="bar",
    figsize=(12,5)
)

plt.title("Top 10 International Products")
plt.xlabel("SKU")
plt.ylabel("Revenue")
plt.show()



print("Total International Revenue:",
      international["GROSS AMT"].sum())

print("Total International Orders:",
      len(international))

print("Average Revenue Per Order:",
      international["GROSS AMT"].mean())