import os
from dotenv import load_dotenv

def choose_env():
    print("🌐 Choose environment:")
    print("1. Local")
    print("2. Cloud")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        load_dotenv(".env.local")
    elif choice == "2":
        load_dotenv(".env.cloud")
    else:
        print("Invalid choice. Defaulting to local.")
        load_dotenv(".env.local")

choose_env()

# Legacy S3 values (still used for listing/downloading/streaming)
S3_ENDPOINT = os.getenv("S3_ENDPOINT")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# New: Supabase REST upload config
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
# You can store or use `env_choice` however you want here

