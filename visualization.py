import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Category-wise spending
category_summary = data.groupby("category")["amount"].sum()

# Plot bar chart
category_summary.plot(kind="bar", color="skyblue")

plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Total Spending")

plt.tight_layout()
plt.savefig("images/category_spending.png")

plt.show()