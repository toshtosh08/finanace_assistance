import pandas as pd

# Load the dataset
df = pd.read_csv("transactions.csv")

# Display the first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Save preprocessed data
df.to_csv("processed_transactions.csv", index=False)
print("Data preprocessed and saved!")