import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
domestic = pd.read_csv(
    "Amazon Sale Report.csv",
    low_memory=False
)

domestic["Amount"] = pd.to_numeric(
    domestic["Amount"],
    errors="coerce"
)

domestic = domestic.dropna(subset=["Amount"])

sns.set_style("whitegrid")

# Only ONE figure
plt.figure(figsize=(18,12))

# -------------------
# 1. Top States
# -------------------
plt.subplot(2,2,1)

top_states = (
    domestic.groupby("ship-state")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

sns.barplot(
    x=top_states.values,
    y=top_states.index
)

plt.title("Top 10 States by Sales")

# -------------------
# 2. Category Sales
# -------------------
plt.subplot(2,2,2)

category_sales = (
    domestic.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Category Sales")
plt.xticks(rotation=45)

# -------------------
# 3. Order Status
# -------------------
plt.subplot(2,2,3)

status_counts = domestic["Status"].value_counts().head(5)

plt.pie(
    status_counts,
    labels=status_counts.index,
    autopct="%1.1f%%"
)

plt.title("Order Status")

# -------------------
# 4. Top Cities
# -------------------
plt.subplot(2,2,4)

city_sales = (
    domestic.groupby("ship-city")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

sns.barplot(
    x=city_sales.values,
    y=city_sales.index
)

plt.title("Top Cities by Sales")

# Dashboard Title
plt.suptitle(
    "Amazon E-Commerce Sales Dashboard",
    fontsize=22,
    fontweight="bold"
)

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.show()