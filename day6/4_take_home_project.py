#Websites hat you can scrape from:
#Wikipdia: wikipdia.org
#NASA: NASA.gov
#Yahoo Finance Stock Data: https://finance.yahoo.com/
#Weather data from webpage: https://weather.com/


import requests
from bs4 import BeautifulSoup

url = "PUT_YOUR_LINK_HERE"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# YOUR SCRAPING CODE HERE

# SAVE SCRAPED CONTENT HERE
