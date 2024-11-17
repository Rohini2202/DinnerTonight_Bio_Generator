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
    try:
        data = request.json
        print("Received data:", data)
        career = data.get('carrer','')
        personality = data.get('personality','')
        interests = data.get('interests','')
        relationship = data.get('relationship','')

        if not (career and personality and interests and relationship):
            return jsonify({"error": "Missing input data"}), 400
    
        # AI Model Prompt
        prompt = f"I am a {career} who is {personality} and loves {interests} using {relationship}. Write a creative bio for me."
        print("Prompt:", prompt)
        # Generate Bio using OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
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
