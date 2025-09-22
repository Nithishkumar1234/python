# chatbot_web.py
import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# -----------------------------
# Step 1: Load .env and API Key
# -----------------------------
project_folder = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(project_folder, ".env"))

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found. Check your .env file.")
else:
    print("✅ Loaded GOOGLE_API_KEY successfully (starts with):", api_key[:6], "*****")

# -----------------------------
# Step 2: Configure Gemini API
# -----------------------------
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# Step 3: Streamlit Web UI
# -----------------------------
st.set_page_config(page_title="AskNithish", page_icon="🤖")
st.title("🤖 AskNithish ")

# Initialize chat session in Streamlit state
if "chat" not in st.session_state:
    st.session_state["chat"] = model.start_chat(history=[])

# Display chat history
for msg in st.session_state.chat.history:
    role = "user" if msg.role == "user" else "assistant"
    st.chat_message(role).markdown(msg.parts[0].text)

# Chat input box
if prompt := st.chat_input("Type your message here..."):
    # Display user message
    st.chat_message("user").markdown(prompt)

    # Send message to Gemini API
    response = st.session_state.chat.send_message(prompt)

    # Display AI response
    st.chat_message("assistant").markdown(response.text)
