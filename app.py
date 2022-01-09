import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://www.heritageislesgolf.com/tee-times/")
print(html_text)