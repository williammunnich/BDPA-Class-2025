import requests
from bs4 import BeautifulSoup

# STEP 1: Enter your webpage URL here
url = "PUT_YOUR_LINK_HERE"

# STEP 2: Request the webpage content
response = requests.get(url)

# STEP 3: Parse the webpage content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# STEP 4: Scrape content you want by customizing this selector
# Example CSS selector: "h2", ".class-name", "#id-name", "a[href$='.mp3']"
scraped_elements = soup.select("YOUR_CSS_SELECTOR_HERE")

# STEP 5: Process and save the scraped content
with open("scraped_content.txt", "w") as file:
    for element in scraped_elements:
        # Customize what content to save (e.g., text, href links, src, etc.)
        content = element.get_text(strip=True)  # or element['href'], element['src']
        file.write(content + "\n")
        print(f"Saved: {content}")
