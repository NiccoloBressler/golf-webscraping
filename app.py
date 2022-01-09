from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get('https://www.golfnow.com/tee-times/facility/3130-heritage-isles-golf-country-club/search?gclid=Cj0KCQiAieWOBhCYARIsANcOw0yLI2fS6gmlsfUgjxe0gNZdSVw6Oai3mix-0OMXosonYEnjm8sqr54aAoCSEALw_wcB#sortby=Date&view=Grouping&holes=3&timeperiod=3&timemax=42&timemin=10&players=0&pricemax=10000&pricemin=0')

# Adds all available tee-times to a list
tee_times = []
for item in driver.find_elements(By.CLASS_NAME,"time-meridian"):
    tee_times.append(item.text)

# Adds all available tee-time's prices/status to a list
statuses = []
for item in driver.find_elements(By.XPATH,"//*[@class='zone-price' or @class='price']"):
    statuses.append(item.text)

# Merges tee-times and prices/status into a single dictionary
print(dict(zip(tee_times, statuses)))



# Gets prices

# Holes

# Players