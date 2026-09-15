import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("weather_clean.csv")

# Connect to database
with sqlite3.connect("weather.db") as conn:

    # Save DataFrame to SQLite
    df.to_sql(
        "weather_data",
        conn,
        if_exists="replace",
        index=False
    )

    # Verify data was written
    result = pd.read_sql_query(
        "SELECT * FROM weather_data LIMIT 5",
        conn
    )

    print("First 5 rows from SQLite database:")
    print(result)

print("Data saved to weather.db")