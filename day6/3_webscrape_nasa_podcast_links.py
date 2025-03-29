import requests
from bs4 import BeautifulSoup

# Get NASA podcasts page
url = "https://www.nasa.gov/podcasts/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#podcast_links = [link['href'] for link in soup.select("a[href^='https://www.nasa.gov/podcasts/']")] # uncomment and fix if needed

# Save links into file (for students to finish)
