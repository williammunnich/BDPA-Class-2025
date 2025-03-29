import requests
from bs4 import BeautifulSoup

# Get NASA podcasts page
url = "https://www.nasa.gov/podcasts/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find podcast links using CSS selector - links starting with NASA podcasts URL
podcast_links = [link['href'] for link in soup.select("a[href^='https://www.nasa.gov/podcasts/']")]

# Save the links to a file
with open("nasa_podcasts.txt", "w") as file:
    for href in podcast_links:
        file.write(href + "\n")
        print(f"Saved link: {href}")

print(f"Found {len(podcast_links)} NASA podcast links")