import pandas as pd
import random

# Categories and example descriptions
categories = {
    "Food & Beverage": ["Starbucks", "McDonald's", "Pizza Hut", "Burger King", "Dunkin' Donuts"],
    "Shopping": ["Walmart", "Target", "Amazon", "Best Buy", "Costco"],
    "Entertainment": ["Netflix", "Spotify", "Cinema", "Concert", "Theme Park"],
    "Transport": ["Shell Gas", "Exxon", "Uber", "Lyft", "Public Transport"],
    "Utilities": ["Electric Bill", "Water Bill", "Internet Bill", "Phone Bill"],
    "Healthcare": ["Pharmacy", "Doctor Visit", "Hospital", "Health Insurance"],
    "Travel": ["Airline Ticket", "Hotel Booking", "Car Rental", "Travel Insurance"]
}

# Generate mock data
data = {
    "Date": [],
    "Description": [],
    "Amount": [],
    "Category": []
}

for _ in range(1000):  # Generate 1000 transactions
    category = random.choice(list(categories.keys()))
    description = random.choice(categories[category])
    amount = round(random.uniform(1, 200), 2)  # Random amount between $1 and $200
    date = pd.date_range(start="2023-01-01", end="2023-10-31", freq="D")[random.randint(0, 300)]

    data["Date"].append(date)
    data["Description"].append(description)
    data["Amount"].append(amount)
    data["Category"].append(category)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("transactions.csv", index=False)
print("Expanded mock dataset created!")