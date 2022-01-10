import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

print("Fetching tee-times...")

# Suppresses unnecessary selenium error messages
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Allows for script to run without opening browser
options.add_argument('headless')

driver = webdriver.Chrome(options=options)
driver.get('https://www.golfnow.com/tee-times/facility/3130-heritage-isles-golf-country-club/search?gclid=Cj0KCQiAieWOBhCYARIsANcOw0yLI2fS6gmlsfUgjxe0gNZdSVw6Oai3mix-0OMXosonYEnjm8sqr54aAoCSEALw_wcB#sortby=Date&view=Grouping&holes=3&timeperiod=3&timemax=42&timemin=10&players=0&pricemax=10000&pricemin=0')

# Adds all available tee-times to a list
tee_times = []
for item in driver.find_elements(By.CLASS_NAME, "time-meridian"):
    tee_times.append(item.text)

# Adds all available tee-time's prices/status to a list
statuses = []
for item in driver.find_elements(By.CLASS_NAME, "zone-price"):
    statuses.append(item.text)
for item in driver.find_elements(By.CLASS_NAME, "price"):
    statuses.append(item.text)

# Removes tee-time if it has already been sold, then prints.
available_tee_times = dict(zip(tee_times, statuses))
available_tee_times = {key:val for key, val in available_tee_times.items() if val != "SOLD"}

# Inserts decimal point into cost of slot.
for key, value in available_tee_times.items():
    available_tee_times[key] = value[:3] + '.' + value[3:]

# Holes
holes = []
for item in driver.find_elements(By.CLASS_NAME, "holes"):
    holes.append(item.text)

# Prevents holes from showing up on wrong tee-times due to unavailable slots.
while '' in holes:
    holes.remove('')

# Players
players = []
for item in driver.find_elements(By.CLASS_NAME, "golfers-available"):
    players.append(item.text)

# Takes dictionary and turns keys and values into lists.
times = list(available_tee_times.keys())
prices = list(available_tee_times.values())

zipped = list(zip(times, prices, holes, players))

# Creates a dataframe from all four lists.
df = pd.DataFrame(zipped, columns=['Time', 'Price', 'Holes', 'Players'])

print(driver.title)
print(f"There are currently {len(df)} tee-times available at this location.")
print(df)
time.sleep(5)
driver.quit()

