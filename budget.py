import pandas as pd

# Load transactions
df = pd.read_csv("processed_transactions.csv")

# Define a budget
budget = {
    "Food & Beverage": 200,
    "Shopping": 300,
    "Entertainment": 50,
    "Transport": 100
}

# Calculate total spending per category
spending = df.groupby('Category')['Amount'].sum()

# Compare with budget
for category, amount in spending.items():
    if category in budget:
        print(f"{category}: Spent {amount} / Budget {budget[category]}")
        if amount > budget[category]:
            print("Warning: Budget exceeded!")