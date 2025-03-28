import requests
from bs4 import BeautifulSoup

# URL of NASA podcasts page
url = "https://www.nasa.gov/podcasts/"

# Fetch the webpage content
response = requests.get(url)

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape all links that end with .mp3
podcast_links = soup.select("a[href$='.mp3']")

# Open a file and save all podcast links into it
with open("nasa_podcasts.txt", "w") as file:
    for link in podcast_links:
        href = link.get('href')
        file.write(href + "\n")
        print(f"Saved link: {href}")
