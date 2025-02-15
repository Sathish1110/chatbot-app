# import google.generativeai as ai

# API_KEY="Your api key"
# ai.configure(api_key=API_KEY)
# mod=ai.GenerativeModel("gemini-pro")
# chat=mod.start_chat()
# while True:
#     user_input=input("You: ")
#     if user_input.lower()=="exit":
#         print("Bot: Goodbye!")
#         break
#     response=chat.send_message(user_input)
#     print("Bot: "+response.text)
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as ai
from fastapi.middleware.cors import CORSMiddleware

# Configure API Key
API_KEY = "AIzaSyBdq7Ca4BioiVZFjLseDvYJ_qu3hgccIAY"
ai.configure(api_key=API_KEY)

# Initialize Chat Model
mod = ai.GenerativeModel("gemini-pro")
chat = mod.start_chat()

# FastAPI App
app = FastAPI()

# Enable CORS for Flutter Integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your Flutter app's domain if deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(message: Message):
    user_input = message.message
    response = chat.send_message(user_input)
    return {"response": response.text}

# Run the server using: uvicorn backend:app --host 0.0.0.0 --port 8000
