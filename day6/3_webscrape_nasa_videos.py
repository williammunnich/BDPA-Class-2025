import requests
from bs4 import BeautifulSoup

url = "https://www.nasa.gov/podcasts/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# podcast_links = soup.select("a[href$='.mp3']")  # uncomment and fix if needed

# Save links into file (students to finish)
