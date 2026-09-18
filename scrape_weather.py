from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

try:
    url = "https://www.timeanddate.com/weather/"
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "table tbody tr")
        )
    )

    cities = driver.find_elements(
        By.CSS_SELECTOR,
        "table tbody tr"
    )

    results = []

    for city in cities:
        results.append({"Data": city.text})

    df = pd.DataFrame(results)

    print(df.head())

    df.to_csv("weather_raw.csv", index=False)

finally:
    driver.quit()