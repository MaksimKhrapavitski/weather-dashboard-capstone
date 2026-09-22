import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("weather_clean.csv")

print(df.head())

# Connect to SQLite database
conn = sqlite3.connect("weather.db")

# Save dataframe to database
df.to_sql(
    "weather_data",
    conn,
    if_exists="replace",
    index=False
)

# Verify
result = pd.read_sql_query(
    "SELECT * FROM weather_data LIMIT 5",
    conn
)

print("\nFirst 5 rows from database:")
print(result)

conn.close()

print("\nweather.db updated successfully!")