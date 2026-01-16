import pandas as pd

df = pd.read_csv("outputs/cleaned_data.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Order Month"] = df["Order Date"].dt.month
df["Order Year"] = df["Order Date"].dt.year

feature_columns = ["Quantity", "Discount", "Delivery Days", "Order Month"]

X = df[feature_columns]
y = df["Sales"]

# Save datasets
X.to_csv("outputs/X.csv", index=False)
y.to_csv("outputs/y.csv", index=False)
