import streamlit as st
from groq import Groq

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="EduBot – Coaching Assistant",
    page_icon="🎓",
    layout="centered"
)

# ─────────────────────────────────────────────
# INSTITUTE DATA — Edit this for each client!
# ─────────────────────────────────────────────
INSTITUTE_INFO = """
You are EduBot, the friendly AI assistant for "Bright Future Coaching Classes" in Nashik, Maharashtra.

INSTITUTE DETAILS:
- Name: Bright Future Coaching Classes
- Location: Near CBS Chowk, Nashik, Maharashtra
- Phone: +91 98765 43210
- Email: info@brightfuture.in
- Website: www.brightfuture.in

COURSES OFFERED:
1. JEE Mains & Advanced (Class 11-12) — ₹45,000/year
2. NEET Preparation (Class 11-12) — ₹42,000/year
3. MHT-CET (Class 11-12) — ₹30,000/year
4. Foundation Batch (Class 8-10) — ₹20,000/year
5. SSC Board (Class 10) — ₹18,000/year

TIMINGS:
- Morning Batch: 7:00 AM – 10:00 AM
- Afternoon Batch: 12:00 PM – 3:00 PM
- Evening Batch: 5:00 PM – 8:00 PM
- Sunday: Doubt sessions only (10 AM – 1 PM)

ADMISSION PROCESS:
1. Fill the inquiry form at the institute or WhatsApp us
2. Appear for a free diagnostic test
3. Choose your batch and pay fees
4. Admissions open: April–June every year

FACULTY:
- 12+ experienced teachers
- IIT/NIT alumni for JEE
- MBBS doctors for NEET Biology

FACILITIES:
- AC classrooms
- Online test series (free with admission)
- Doubt clearing sessions daily
- Study material included in fees
- Parent-teacher meetings every month

RULES:
- Attendance minimum 75% required
- Fees can be paid in 2 installments
- No refund after 15 days of admission
- Scholarship available for meritorious students (up to 50% fee waiver)

IMPORTANT:
- Always be friendly, warm, and helpful
- If a question is outside your knowledge, say "Please call us at +91 98765 43210 for more details"
- Respond in the same language the user writes in (Hindi or English or Hinglish)
- Keep answers concise and clear
"""

# ─────────────────────────────────────────────
# STYLING
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    .header-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 24px;
        color: white;
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .header-title { font-size: 24px; font-weight: 700; margin: 0; color: white; }
    .header-sub { font-size: 13px; color: #a0b4d6; margin: 4px 0 0 0; }
    .online-dot {
        display: inline-block; width: 8px; height: 8px;
        background: #4ade80; border-radius: 50%; margin-right: 6px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-box">
    <div style="font-size: 48px;">🎓</div>
    <div>
        <p class="header-title">EduBot — Bright Future Coaching</p>
        <p class="header-sub"><span class="online-dot"></span>Online · Nashik, Maharashtra · Replies instantly</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# GROQ SETUP
# ─────────────────────────────────────────────
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ─────────────────────────────────────────────
# HELPER — call Groq with full history
# ─────────────────────────────────────────────
def get_reply(user_message):
    messages = [{"role": "system", "content": INSTITUTE_INFO}]
    for m in st.session_state.messages:
        messages.append({"role": m["role"], "content": m["content"]})
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message.content

# ─────────────────────────────────────────────
# QUICK QUESTION BUTTONS
# ─────────────────────────────────────────────
st.markdown("**Quick questions:**")
quick_questions = [
    "📚 Courses & Fees",
    "⏰ Batch Timings",
    "🎓 Admission Process",
    "🏫 Facilities",
    "🏆 Scholarships",
    "📞 Contact Info"
]
cols = st.columns(3)
quick_input = None
for i, q in enumerate(quick_questions):
    if cols[i % 3].button(q, use_container_width=True):
        quick_input = q

# ─────────────────────────────────────────────
# CHAT HISTORY INIT
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Namaste! I'm EduBot, your assistant for **Bright Future Coaching Classes**.\n\nI can help you with course details, fees, timings, admissions, and more!\n\nAap kya jaanna chahte hain? 😊"
    })

# ─────────────────────────────────────────────
# DISPLAY CHAT HISTORY
# ─────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ─────────────────────────────────────────────
# HANDLE QUICK BUTTON CLICK
# ─────────────────────────────────────────────
if quick_input:
    st.session_state.messages.append({"role": "user", "content": quick_input})
    with st.chat_message("user"):
        st.markdown(quick_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_reply(quick_input)
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

# ─────────────────────────────────────────────
# HANDLE TYPED INPUT
# ─────────────────────────────────────────────
if prompt := st.chat_input("Ask anything about our courses, fees, or admissions..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_reply(prompt)
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})