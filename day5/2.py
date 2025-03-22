import csv

def main():
    # 👇 Change this to the name of YOUR text file from the last exercise
    input_file = "your_text_file.txt"  # ← Change this!
    
    # 👇 This will be the name of the CSV file that gets created
    csv_file = "video_links.csv"

    # 📥 Step 1: Read video links from the text file line by line
    # 🧠 Ask ChatGPT or your teacher:
    # - What does `with open(...)` do here?
    # - Why use `.strip()`?
    with open(input_file, "r") as infile:
        video_links = [line.strip() for line in infile if line.strip()]

    # 📤 Step 2: Save the links to a CSV file
    # 🧠 Ask ChatGPT or your teacher:
    # - What does `csv.writer()` do?
    # - Why do we write a header row?
    try:
        with open(csv_file, "w", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["video_links"])  # 👈 Adds a header row

            # 👇 Write each video link as a new row
            for link in video_links:
                writer.writerow([link])

        print("✅ Rows saved successfully to CSV.")
    
    # 🚨 Error handling
    # 🧠 Ask ChatGPT or your teacher:
    # - What is a try/except block for?
    # - What might go wrong in this block of code?
    except Exception as e:
        print(f"❌ Failed to save rows to CSV: {e}")

# ✅ Only run main() if this file is executed directly
if __name__ == "__main__":
    main()