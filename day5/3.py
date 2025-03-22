import csv
import sqlite3
import os

# File and table setup
CSV_FILE = 'video_links.csv'
DB_FILE = 'video_links.db'
TABLE_NAME = 'video_links'

# 🧠 Ask ChatGPT or your teacher:
# - What does this function do?
# - Why use `CREATE TABLE IF NOT EXISTS`?
def setup_database(conn):
    with conn:
        conn.execute(f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT NOT NULL UNIQUE
            )
        ''')

def main():
    # 🧠 Ask ChatGPT or your teacher:
    # - What does os.path.exists() check for?
    # - Why is it important before opening a file?
    if not os.path.exists(CSV_FILE):
        print(f"CSV file '{CSV_FILE}' not found.")
        return

    # 🧠 Ask ChatGPT or your teacher:
    # - What does sqlite3.connect() do?
    # - What kind of database does this create?
    conn = sqlite3.connect(DB_FILE)
    setup_database(conn)

    # 🧠 Ask ChatGPT or your teacher:
    # - What is csv.reader doing here?
    # - Why do we check `if row:`?
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                link = row[0]

                # 🧠 Ask ChatGPT or your teacher:
                # - What does the `?` in the SQL statement mean?
                # - Why use try/except here?
                try:
                    conn.execute(f"INSERT INTO {TABLE_NAME} (link) VALUES (?)", (link,))
                    conn.commit()
                    print(f"Link '{link}' has been written successfully.")

                # 🧠 Ask: What is an IntegrityError?
                except sqlite3.IntegrityError:
                    print(f"Link '{link}' is a duplicate and was not written.")

                # 🧠 Ask: What other exceptions might happen here?
                except Exception as e:
                    print(f"Link '{link}' has been written unsuccessfully: {e}")

    # Always close the connection
    conn.close()

if __name__ == "__main__":
    main()