import pandas as pd

# Load raw data
df = pd.read_csv("weather_raw.csv")

print("Before cleaning:")
print(df.shape)
print(df.head())

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Clean text columns
df["City"] = df["City"].str.strip()
df["Temperature"] = df["Temperature"].str.strip()
df["Wind"] = df["Wind"].str.strip()
df["Local Time"] = df["Local Time"].str.strip()

print("\nAfter cleaning:")
print(df.shape)
print(df.head())

# Save cleaned file
df.to_csv("weather_clean.csv", index=False)

print("\nweather_clean.csv saved successfully!")