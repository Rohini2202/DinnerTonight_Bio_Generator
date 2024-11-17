from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

app = Flask(__name__)

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-bio', methods=['POST'])
def generate_bio():
    data = request.json
    career = data['career']
    personality = data['personality']
    interests = data['interests']

    # AI Model Prompt
    prompt = f"I am a {career} who is {personality} and loves {interests}. Write a creative bio for me."
    
    # Generate Bio using OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    bio = response.choices[0].text.strip()
    return jsonify({"bio": bio})

if __name__ == '__main__':
    app.run(debug=True)
