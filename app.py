from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Individual golf course websites being scraped
heritage_isles = "https://www.heritageislesgolf.com/tee-times/"

# Gets tee-times
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Passes in website being scraped and searched for all tee-times.
    driver.get(heritage_isles)
    tee_times = driver.find_element(By.XPATH,'//p[@class="jss503"]')
    tee_times_list = []
    for time in range(len(tee_times)):
        tee_times_list.append(tee_times[time].text)
except NoSuchElementException:
    print("No available tee times.")

# Gets prices

# Holes

# Players