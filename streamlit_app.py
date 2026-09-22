import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.title("🌤 Weather Dashboard")

st.write(
    "Select a city to explore weather data."
)

# Load database
conn = sqlite3.connect("weather.db")

df = pd.read_sql(
    "SELECT * FROM weather_data",
    conn
)

conn.close()

st.subheader("Weather Data")

st.dataframe(df)

# Convert temperature column

df["Temp_Num"] = (
    df["Temperature"]
    .str.replace("°F", "", regex=False)
    .str.strip()
    .astype(float)
)

st.subheader("Weather Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Cities",
    len(df)
)

col2.metric(
    "Average Temp",
    round(df["Temp_Num"].mean(), 1)
)

col3.metric(
    "Max Temp",
    df["Temp_Num"].max()
)

# --------------------
# User filter
# --------------------

city = st.selectbox(
    "Select a city",
    ["All"] + sorted(df["City"].unique().tolist())
)

if city != "All":
    filtered_df = df[df["City"] == city]
else:
    filtered_df = df

st.subheader("Filtered Data")

st.dataframe(filtered_df)

# --------------------
# Visualization 1
# --------------------

st.subheader("Temperature Distribution")

fig, ax = plt.subplots()

ax.hist(
    filtered_df["Temp_Num"],
    bins=10
)

ax.set_title("Temperature Distribution")
ax.set_xlabel("Temperature (°F)")
ax.set_ylabel("Count")

st.pyplot(fig)

# --------------------
# Visualization 2
# --------------------

st.subheader("Top 10 Warmest Cities")

top10 = (
    filtered_df
    .sort_values(
        "Temp_Num",
        ascending=False
    )
    .head(10)
)

fig, ax = plt.subplots()

ax.bar(
    top10["City"],
    top10["Temp_Num"]
)

ax.set_title("Top 10 Warmest Cities")
ax.set_ylabel("Temperature (°F)")

plt.xticks(rotation=45)

st.pyplot(fig)

# --------------------
# Visualization 3
# --------------------

st.subheader("Temperature by City")

st.line_chart(
    filtered_df.set_index("City")["Temp_Num"]
)