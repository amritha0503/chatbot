from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI()  # This will automatically use OPENAI_API_KEY from environment

@app.route("/chat", methods=["POST"])
def chat():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "Message field is required"}), 400

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",  # Changed from gpt-4.0 to gpt-3.5-turbo for better compatibility
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = completion.choices[0].message.content
        return jsonify({"response": reply})

    except Exception as e:
        print(f"Error: {str(e)}")  # Add this for debugging
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

if __name__ == "__main__":
    app.run(debug=True)