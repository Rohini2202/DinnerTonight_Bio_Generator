from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

app = Flask(__name__)
# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY_BIO")
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/generate-bio', methods=['POST'])
def generate_bio():
    try:
        data = request.get_json(force=True)
        print("Received data:", data)
        career = data.get('career','').strip()
        personality = data.get('personality','').strip()
        interests = data.get('interests','').strip()
        relationship = data.get('relationship','').strip()

        if not career or not personality or not interests:
            error_message = (
                f"Missing input data. Received values - "
                f"career: '{career}', personality: '{personality}', interests: '{interests}', relationship: {relationship}."
            )
            return jsonify({"error": error_message}), 400

    
        # AI Model Prompt
        prompt = f"I am a {career} who is {personality} and loves {interests} using {relationship}. Write a creative bio for me."
        print("Prompt:", prompt)
        # Generate Bio using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.7
        )
        print("OpenAI response:", response)
        bio = response.choices[0].text.strip()
        return jsonify({"bio": bio})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
