import pandas as pd

df = pd.read_csv("weather_raw.csv")

print("Before cleaning:")
print(df.shape)

df = df.drop_duplicates()
df = df.dropna()

print("After cleaning:")
print(df.shape)

df.to_csv("weather_clean.csv", index=False)

print("Clean file saved.")