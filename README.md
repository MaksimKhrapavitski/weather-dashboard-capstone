# Weather Dashboard Capstone

This project collects weather data from the Weather Around The World website using Selenium.

## Features

- Web scraping with Selenium
- Data cleaning with Pandas
- CSV export
- SQLite database (coming soon)
- Streamlit dashboard (coming soon)

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python scrape_weather.py
python clean_weather.py
```
## Data Cleaning

The raw weather data is cleaned using pandas in `clean_weather.py`.

## Database Storage

The cleaned dataset is stored in a SQLite database (`weather.db`) using `weather_database.py`.

The script:
- Loads the cleaned CSV file
- Saves the data into a SQLite table named `weather_data`
- Reads the first 5 rows back from the database to verify the import
