# ☁️ Create a Supabase Project and Connect It to the Media Server

This guide walks you through setting up your own Supabase account, creating a database and bucket, and connecting everything to William’s media server.

---

## ✅ 1. Create a Supabase Account

1. Go to [https://supabase.com/](https://supabase.com/)
2. Click **Start your project** or **Sign in** using GitHub or email.
3. After logging in, you’ll land on the Supabase **dashboard**.

---

## 🛠️ 2. Create a New Project

1. Click the green **New project** button.
2. Fill in the required fields:
   - **Project name** (any name is fine)
   - **Database password** → Choose a strong password (save it somewhere!)
3. Choose a region close to you.
4. Click **Create project**.

> 🕐 Wait a minute or two for your database to finish provisioning.

---

## 📦 3. Create a Storage Bucket

1. In your project dashboard, go to the **Storage** tab.
2. Click **Create a new bucket**.
3. Name the bucket:
   ```
   media
   ```
4. Leave “Public bucket” **unchecked** (for private access).
5. Click **Create**.

---

## 🔑 4. Get Your Supabase Credentials

Go to the **Project Settings** → **API** tab, and copy the following:

- **Project URL**
- **anon public key**

You’ll also need:
- The **bucket name** → should be `media`
- Your **database password** (from step 2)

---

## 📂 5. Configure Your Environment File

1. In the `media_server` folder, locate the file:
   ```
   .env.cloud.example
   ```

2. Rename it to:
   ```
   .env.cloud
   ```

3. Fill in the variables using the values you got from Supabase:

```
SUPABASE_URL=your-project-url
SUPABASE_KEY=your-anon-key
SUPABASE_BUCKET=media
SUPABASE_PASSWORD=your-db-password
```

---

## 🐍 6. Install Dependencies & Run the Server

### 📦 Install Python packages:
```bash
pip install flask python-dotenv boto3 requests supabase
```

### ▶️ Run the Server
```bash
cd media_server
python app.py
```

- When prompted:
  - Type `2` to use a cloud database
  - Then type `2` again to confirm

✅ The terminal will show you the local server URL (usually [http://127.0.0.1:5000](http://127.0.0.1:5000)).

Open it in your browser to access the app!

---

## 🎉 You’re Now Connected to Your Own Supabase Project!

Your Flask media server is now hooked into your personal Supabase database and bucket — you're in full control of your own media storage.