# 🧪 Local Setup Guide: Supabase + Media Server Project

Follow this step-by-step guide to get Supabase running locally and connect it to your media server.

---

## ✅ 1. Install Required Tools

### 🔹 Install Docker Desktop
- Download: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- Open Docker Desktop after installation.
- Check if Docker is working:
  ```bash
  docker --version
  ```
  *(Use **Terminal** on macOS or **CMD** on Windows)*

### 🔹 Install Node.js & NPM
- Download: [https://nodejs.org/en/download](https://nodejs.org/en/download)
- Choose your operating system and install the latest LTS version.
- Check if NPM is installed:
  ```bash
  npm --version
  ```

---

## ⚙️ 2. Set Up Supabase Locally

### 🔸 Install Supabase CLI
```bash
npm install supabase --save-dev
```

### 🔸 Initialize Supabase Project
```bash
npx supabase init
```

### 🔸 Start Supabase Locally
```bash
npx supabase start
```

- This will launch Supabase locally with all the services.
- Your terminal will print out **credentials** (DB URL, anon/public keys, etc).

---

## 🛠️ 3. Configure Environment Variables

1. Locate the file: `.env.local.example`
2. Rename it to: `.env.local`
3. Copy the credentials from the terminal and update the values in `.env.local`.

---

## 🗃️ 4. Access Supabase Studio

You can use the local Supabase GUI to manage your DB and storage:

👉 Open [http://127.0.0.1:54323](http://127.0.0.1:54323)

### 🪣 Create a Bucket
- Go to the **Storage** tab.
- Create a new bucket called:
  ```
  media
  ```

---

## 🐍 5. Set Up Media Server

### 🔸 Install Python & Dependencies
Make sure you have Python installed. Then run:

```bash
pip install supabase
pip install flask boto3
pip install python-dotenv
```

### 🔸 Download Project Files
Copy or clone the media server files from this repo:

🔗 [https://github.com/williammunnich/BDPA-Class-2025/tree/main/day6/media_server](https://github.com/williammunnich/BDPA-Class-2025/tree/main/day6/media_server)

### 🔸 Start the Server
Navigate to the folder in your terminal and run:

```bash
python app.py
```

- The app will prompt you to select a data source:
  - Type `1` for "Use Local Database"
  - Then type `1` again to confirm

✅ Your server should now be live at:

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧩 Done!

Your local Supabase instance is now fully connected to your media server. You can upload media via the Flask app, and it will be stored in your local Supabase bucket.
