import pandas as pd

df = pd.read_csv("data/superstore.csv")

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


print("Initial shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# Drop rows with missing critical values
df = df.dropna(subset=["Sales", "Profit"])

# Remove duplicate rows
df = df.drop_duplicates()

# Create new feature: delivery time in days
df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Save cleaned dataset
df.to_csv("outputs/cleaned_data.csv", index=False)

print("\nCleaned shape:", df.shape)