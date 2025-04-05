# 🌐 Connect to William’s Cloud Media Server (HTTP)

This guide walks you through accessing a hosted media server by using provided credentials. After setup, you'll be able to view uploaded media directly in your browser!

---

## ✅ 1. Get the Project Files

You can either **clone the full repo** or just download the `media_server` folder:

🔗 [https://github.com/williammunnich/BDPA-Class-2025/tree/main/day6/media_server](https://github.com/williammunnich/BDPA-Class-2025/tree/main/day6/media_server)

---

## 🔐 2. Set Up Your Credentials

1. Get the cloud credentials from William via this TinyURL link:
   > 📎 Example: `https://tinyurl.com/YOUR-CREDENTIAL-LINK`  
   *(Replace this with the actual TinyURL William provides)*

2. Inside the `media_server` folder:
   - Rename `.env.cloud.example` to `.env.cloud`
   - Paste the credentials from the TinyURL into `.env.cloud`

✅ This file gives you access to the cloud-hosted database and media.

---

## 🐍 3. Install Python Dependencies

In your terminal (Mac: Terminal, Windows: CMD or PowerShell):

```bash
pip install flask python-dotenv boto3 requests supabase
```

---

## 🚀 4. Run the Media Server

1. Navigate into the `media_server` directory:
   ```bash
   cd media_server
   ```

2. Start the app:
   ```bash
   python app.py
   ```

3. When prompted:
   - Type `2` → to use the cloud database
   - Then type `2` again → to confirm

---

## 🌍 5. View the Media Server

Once it's running, it will print an address like:

```bash
Server running at http://127.0.0.1:5000
```

➡️ Open that link in your browser.

You’ll be connected to the **live cloud database** and will be able to:
- Browse existing media files
- View uploaded content

---

## ✅ You’re All Set!

Let me know if you’d like this as a `.txt` or `.md` file so you can include it in your repo or send it to others!