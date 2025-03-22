# Import required libraries
import re
from bs4 import BeautifulSoup

# Open and read the HTML file
with open("coding_youtube_vreative_commons.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# TODO: What does BeautifulSoup do here?
soup = BeautifulSoup(html_content, "html.parser")

# TODO: What does this pattern find?
pattern = re.compile(r"watch\?v=([^\s\\&]{11})")

# TODO: What does .findall do?
matches = pattern.findall(soup.prettify())

print("Matched video links:")
for video_id in matches:
    # TODO: What is this URL pointing to?
    print("https://youtube.com/watch?v="+video_id)
    
# TODO: Save all the printed URLs to a text file which you create