from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

url = "https://www.timeanddate.com/weather/"

driver.get(url)

cities = driver.find_elements(
    By.CSS_SELECTOR,
    "table tbody tr"
)

results = []

for city in cities:
    try:
        data = city.text
        results.append({"Data": data})
    except:
        continue

df = pd.DataFrame(results)

print(df.head())

df.to_csv("weather_raw.csv", index=False)

driver.quit()