import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.title("🌤 Weather Dashboard")

st.write(
    "Explore weather information by city and temperature range."
)

# --------------------
# Load Database
# --------------------

conn = sqlite3.connect("weather.db")

df = pd.read_sql(
    "SELECT * FROM weather_data",
    conn
)

conn.close()

# --------------------
# Clean Temperature Data
# --------------------

df["Temp_Num"] = (
    df["Temperature"]
    .str.replace("°F", "", regex=False)
    .str.strip()
)

df["Temp_Num"] = pd.to_numeric(
    df["Temp_Num"],
    errors="coerce"
)

df = df.dropna(subset=["Temp_Num"])

# --------------------
# Weather Summary
# --------------------

st.subheader("Weather Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Cities",
    df["City"].nunique()
)

col2.metric(
    "Average Temp",
    round(df["Temp_Num"].mean(), 1)
)

col3.metric(
    "Max Temp",
    round(df["Temp_Num"].max(), 1)
)

# --------------------
# Filters
# --------------------

st.sidebar.header("Filters")

city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df["City"].unique().tolist())
)

min_temp = int(df["Temp_Num"].min())
max_temp = int(df["Temp_Num"].max())

temp_range = st.sidebar.slider(
    "Temperature Range (°F)",
    min_temp,
    max_temp,
    (min_temp, max_temp)
)

filtered_df = df[
    (df["Temp_Num"] >= temp_range[0]) &
    (df["Temp_Num"] <= temp_range[1])
]

if city != "All":
    filtered_df = filtered_df[
        filtered_df["City"] == city
    ]

# --------------------
# Show Data
# --------------------

st.subheader("Filtered Weather Data")

st.dataframe(filtered_df)

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

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

st.subheader("Top Warmest Cities")

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

ax.set_title("Top Warmest Cities")
ax.set_xlabel("City")
ax.set_ylabel("Temperature (°F)")

plt.xticks(rotation=45)

st.pyplot(fig)

# --------------------
# Visualization 3
# --------------------

st.subheader("Temperature by City")

chart_df = (
    filtered_df
    .sort_values("Temp_Num")
)

st.line_chart(
    chart_df.set_index("City")["Temp_Num"]
)

# --------------------
# Extra Visualization
# --------------------

st.subheader("Average Temperature")

avg_temp = (
    filtered_df["Temp_Num"]
    .mean()
)

fig, ax = plt.subplots()

ax.bar(
    ["Average"],
    [avg_temp]
)

ax.set_ylabel("Temperature (°F)")
ax.set_title("Average Temperature")

st.pyplot(fig)