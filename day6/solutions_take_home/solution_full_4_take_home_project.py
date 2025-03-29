import requests
from bs4 import BeautifulSoup

# STEP 1: Enter your webpage URL here
url = "https://simple.wikipedia.org/wiki/Python_(programming_language)"

# STEP 2: Request the webpage content
response = requests.get(url)

# STEP 3: Parse the webpage content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# STEP 4: Scrape all paragraphs (p tags) from the Wikipedia page
scraped_elements = soup.select("p")

# STEP 5: Process and save the scraped headings into a file
with open("scraped_pragaraphs.txt", "w") as file:
    for element in scraped_elements:
        # Extract and save text content from each heading
        content = element.get_text(strip=True)
        file.write(content + "\n")
        print(f"Saved paragraphs: {content}")
