# 🎓 EduBot — AI Chatbot for Coaching Institutes

A ready-to-deploy AI chatbot built with Python + Streamlit + OpenAI GPT.  
Designed for coaching institutes to handle student/parent queries 24/7 — automatically.

---

## 🚀 Features
- Instant answers about courses, fees, timings, admissions
- Quick-question buttons for common queries  
- Supports Hindi, English, and Hinglish
- Fully customizable for any institute
- Beautiful, mobile-friendly UI

---

## 🛠️ Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/coaching-chatbot.git
cd coaching-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key
Create the file `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "sk-your-key-here"
```
> Get a free API key at https://platform.openai.com

### 4. Customize the institute info
Open `app.py` and edit the `INSTITUTE_INFO` block with your client's details:
- Institute name, address, phone
- Courses and fees
- Batch timings
- Admission process

### 5. Run locally
```bash
streamlit run app.py
```

---

## ☁️ Deploy for Free (Streamlit Cloud)

1. Push this repo to GitHub (without the secrets.toml file!)
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Add your `OPENAI_API_KEY` in the Streamlit Cloud secrets panel
5. Click Deploy — your chatbot is live in 2 minutes! 🎉

---

## 💰 How to Sell This

**Pricing suggestion:**
- Setup fee: ₹3,000 – ₹5,000 (one time)
- Monthly maintenance: ₹1,000/month
- API costs (OpenAI): ~₹200–₹500/month (client pays or you include it)

**Target clients in Nashik:**
- Coaching institutes (JEE/NEET/MHT-CET)
- Schools with admission queries
- Private tutors with many students
- Any business with repetitive customer questions

---

## 📁 Project Structure
```
coaching-chatbot/
├── app.py              ← Main chatbot application
├── requirements.txt    ← Python dependencies
├── .streamlit/
│   └── secrets.toml   ← API key (DO NOT upload to GitHub)
└── README.md
```

---

## 👨‍💻 Built by
[Your Name] — AIML Engineering Student | Freelance AI Developer  
📧 your@email.com | 🔗 linkedin.com/in/yourprofile
