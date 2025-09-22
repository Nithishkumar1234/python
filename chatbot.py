import os
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GRPC_TRACE"] = ""

from dotenv import load_dotenv
import google.generativeai as genai


import os
from dotenv import load_dotenv
import google.generativeai as genai

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
# Step 3: Terminal Chat Function
# -----------------------------
def terminal_chat():
    print("\n🤖 Gemini Chatbot (Terminal Mode). Type 'exit' to quit.\n")
    chat = model.start_chat(history=[])

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye 👋")
            break

        response = chat.send_message(user_input)
        print("Chatbot:", response.text)

# -----------------------------
# Step 4: Main Execution
# -----------------------------
if __name__ == "__main__":
    terminal_chat()



