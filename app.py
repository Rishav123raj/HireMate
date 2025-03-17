import streamlit as st
import time
from question_generator import generate_questions  # Importing from question_generator.py

# Set Streamlit page config
st.set_page_config(page_title="HireMate AI", page_icon="🤖", layout="wide")

# Custom Styling for an elegant and interactive UI
st.markdown("""
    <style>
        body { background-color: #1a1a2e; color: #e0e0e0; }
        .stTextInput input, .stNumberInput input, .stTextArea textarea {
            background-color: #16213e !important;
            color: white !important;
            border: 2px solid #00f5d4 !important;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton > button {
            background: linear-gradient(45deg, #ff0066, #00f5d4);
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 12px;
            font-size: 18px;
            transition: 0.3s;
            box-shadow: 0 4px 15px rgba(0, 245, 212, 0.4);
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, #00f5d4, #ff0066);
            transform: scale(1.05);
        }
        .title { text-align: center; color: #00f5d4; font-size: 40px; font-weight: bold; }
        .subtitle { text-align: center; color: #ff0066; font-size: 24px; margin-bottom: 20px; }
        .chat-container {
            background: rgba(0, 0, 0, 0.5);
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='title'>🚀 HireMate - AI Hiring Assistant 🤖</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Helping you hire the best tech talent with AI! 💡</h3>", unsafe_allow_html=True)

# Animated Loading
with st.spinner("🤖 AI is getting ready to assist you..."):
    time.sleep(1.5)
st.success("Let's get started!")

# Sidebar with branding and user guide
st.sidebar.image("hiremate.webp", use_container_width=True)
st.sidebar.markdown("## 🌟 About HireMate AI")
st.sidebar.info("This AI-powered chatbot screens candidates by collecting information and generating relevant technical questions based on their tech stack.")

# Candidate Information Form
st.markdown("## 📝 Candidate Details")
full_name = st.text_input("👤 Full Name")
email = st.text_input("📧 Email Address")
phone = st.text_input("📞 Phone Number")
experience = st.number_input("🛠 Years of Experience", min_value=0, max_value=50, step=1)
position = st.text_input("🎯 Desired Position")
location = st.text_input("🌍 Current Location")
tech_stack = st.text_area("💻 Tech Stack (comma-separated)", help="Mention technologies like Python, React, MongoDB")

st.write("---")

# Button to Generate Questions
if st.button("🎯 Generate Technical Questions"):
    if not all([full_name, email, phone, position, tech_stack]):
        st.warning("⚠ Please fill in all required fields before proceeding.")
    else:
        with st.spinner("🔍 Generating tailored questions..."):
            time.sleep(2)
            questions = generate_questions(experience, tech_stack)  # Calls the function from question_generator.py
        
        st.subheader("🤔 Your Technical Questions")
        if isinstance(questions, list):  # Ensure it's a list before displaying
            for i, q in enumerate(questions, 1):
                st.markdown(f"**{i}. {q}**")
        else:
            st.error("⚠ An error occurred while fetching questions.")

st.write("---")

# Chatbot Conversation Simulation
st.markdown("## 💬 Chat with the AI")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💡 Type your response here...")

if st.button("📩 Send"):
    if user_input:
        st.session_state.chat_history.append(f"👤 Candidate: {user_input}")
        bot_response = generate_questions(experience, tech_stack)[0]  # Gets the first response from AI
        st.session_state.chat_history.append(f"🤖 Bot: {bot_response}")

        st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
        for message in st.session_state.chat_history:
            st.write(message)
        st.markdown("</div>", unsafe_allow_html=True)

st.write("---")
st.success("🎉 Thank you for using HireMate AI! Our team will reach out to you soon.")
