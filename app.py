from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

app = Flask(__name__)
print(1)
# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
print('2')
@app.route('/')
def index():
    print('3')
    return render_template('index.html')
@app.route('/generate-bio', methods=['POST'])
def generate_bio():
    data = request.json
    career = data['career']
    personality = data['personality']
    interests = data['interests']
    relationship = data['relationship']

    # AI Model Prompt
    prompt = f"I am a {career} who is {personality} and loves {interests} using {relationship}. Write a creative bio for me."
    
    # Generate Bio using OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    print(5)
    bio = response.choices[0].text.strip()
    return jsonify({"bio": bio})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
