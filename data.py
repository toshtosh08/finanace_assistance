import pandas as pd

# Mock transaction data
data = {
    "Date": ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05"],
    "Description": ["Starbucks", "Walmart", "Netflix", "Shell Gas", "McDonald's"],
    "Amount": [5.50, 120.00, 15.99, 45.00, 10.00],
    "Category": ["Food & Beverage", "Shopping", "Entertainment", "Transport", "Food & Beverage"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("transactions.csv", index=False)
print("Mock dataset created!")