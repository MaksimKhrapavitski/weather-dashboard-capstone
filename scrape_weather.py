from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Launch Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

try:
    # Open website
    driver.get("https://www.timeanddate.com/weather/")

    # Wait for table to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "table tbody tr")
        )
    )

    # Get all table rows
    rows = driver.find_elements(
        By.CSS_SELECTOR,
        "table tbody tr"
    )

    print("Rows found:", len(rows))

    results = []

    for row in rows:
        try:
            text = row.text

            print("-----")
            print(text)
            print("LEN:", len(text.split("\n")))

            if not text:
                continue

            parts = text.split("\n")

            if len(parts) >= 4:
                results.append({
                    "City": parts[0],
                    "Temperature": parts[1],
                    "Wind": parts[2],
                    "Local Time": parts[3]
                })

        except Exception as e:
            print("Skipping row:", e)

    # Create DataFrame
    df = pd.DataFrame(results)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    # Save raw data
    df.to_csv("weather_raw.csv", index=False)

    print("\nweather_raw.csv saved successfully!")

finally:
    driver.quit()