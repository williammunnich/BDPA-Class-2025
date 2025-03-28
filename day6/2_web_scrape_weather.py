import requests
from bs4 import BeautifulSoup

url = "https://www.timeanddate.com/weather/usa/new-york"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Scraping temperature information
# temperature = soup.select_one(".h2").get_text()

# Save to file (students complete this)
# with open("weather_ny.txt", "w") as file:
#     file.write(temperature)
