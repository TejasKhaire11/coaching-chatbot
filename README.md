# 🎓 EduBot — AI Chatbot for Coaching Institutes

> A production-ready AI chatbot that handles student & parent queries 24/7 — automatically, in Hindi, English & Hinglish.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-red?style=flat-square&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLaMA3-orange?style=flat-square)


---

## 🚀 Features

- ⚡ Instant AI replies powered by **Groq + LLaMA 3** (fastest free AI API)
- 🌐 Supports **Hindi, English & Hinglish** automatically
- 🔘 One-click **quick question buttons** for common queries
- 🎨 Beautiful, **mobile-friendly UI**
- 🔧 **10-minute customization** for any institute
- ☁️ **Free deployment** on Streamlit Cloud

---

## 🛠️ Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/TejasKhaire11/coaching-chatbot.git
cd coaching-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your FREE Groq API key

### 4. Add your API key
Create the file `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your-groq-key-here"
```
> ⚠️ Never upload this file to GitHub 

### 5. Customize for your client


### 6. Run locally
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## ☁️ Deploy for Free (Streamlit Cloud)

1. Push this repo to GitHub (without `secrets.toml`)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo → select `app.py`
4. Go to **Advanced Settings → Secrets** and paste:
```toml
GROQ_API_KEY = "your-groq-key-here"
```
5. Click **Deploy** — live URL ready in 2 minutes! 🎉

---

## 📁 Project Structure

```
coaching-chatbot/
├── app.py               ← Main chatbot application
├── requirements.txt     ← Python dependencies
├── .gitignore           ← Keeps secrets safe
├── .streamlit/
│   └── secrets.toml    ← API key (never push this!)
└── README.md
```

---

## 👨‍💻 Built by

**Tejas Khaire** — AIML Engineering Student (3rd Year) |  AI Developer

📧 tejaskhaire2005@gmail.com | 🔗 [LinkedIn](https://www.linkedin.com/in/tejas-khaire-168b61276/) | 🐙 [GitHub](https://github.com/TejasKhaire11)

---

