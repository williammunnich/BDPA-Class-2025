import sqlite3
import yt_dlp

# 🧠 Ask ChatGPT or your teacher:
# - What does sqlite3.connect() do?
# - What is a "cursor" in a database?
# Connect to the SQLite database
conn = sqlite3.connect('video_links.db')
cursor = conn.cursor()

# 🧠 Ask:
# - What does the SELECT statement do here?
# - What does .fetchall() return?
# Retrieve all video links from the database
cursor.execute("SELECT link FROM video_links")
videos = cursor.fetchall()

# 🎥 Step 1: Print out all video links to be downloaded
print("Videos to download:")
for video in videos:
    print(video[0])  # Each video is a tuple, and the link is at index 0

# 🧠 Ask:
# - What is yt-dlp?
# - What does 'format': 'mp4' mean in this context?
# Set up yt-dlp options to download in MP4 format
ydl_opts = {
    'format': 'mp4'
}

# 🧠 Ask:
# - What does `with yt_dlp.YoutubeDL(...)` do?
# - Why is the try/except block useful here?
# Step 2: Download each video using yt-dlp
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for video in videos:
        url = video[0]
        try:
            # Attempt to download the video
            ydl.download([url])
            print("✅ File was downloaded successfully")
        except Exception as e:
            # Print an error message if the download fails
            print(f"❌ Failed to download {url}: {e}")

# 🧠 Ask:
# - Why is it important to close the database connection at the end?
# Close the database connection
conn.close()
