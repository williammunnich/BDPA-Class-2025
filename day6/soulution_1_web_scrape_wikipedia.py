import requests
from bs4 import BeautifulSoup
import csv
import os

url = "https://simple.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Scraping first paragraph text
paragraphs = soup.select('p')
text_content = paragraphs[0].get_text()

# Saving to text file
with open("python_info.txt", "w") as file:
    file.write(text_content)

# Changing TXT → CSV
with open("python_info.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Info"])
    writer.writerow([text_content])

# Deleting TXT file
os.remove("python_info.txt")
