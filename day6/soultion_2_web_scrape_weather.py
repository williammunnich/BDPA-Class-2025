import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.timeanddate.com/weather/usa/minneapolis"

# Request the webpage content
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.text, 'html.parser')

# Scraping temperature information (uncommented and working)
temperature = soup.select_one(".h2").get_text()

# Display scraped temperature (optional)
print(f"Current temperature in New York: {temperature}")

# Save the scraped temperature to a file
with open("weather_minneapolis.txt", "w") as file:
    file.write(f"Current temperature in Minneapolis: {temperature}")

