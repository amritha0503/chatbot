import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up API key from environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def chatbot(user_input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    reply = chatbot(user_input)
    print("Bot:", reply)