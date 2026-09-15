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

    print("Data saved to weather.db")