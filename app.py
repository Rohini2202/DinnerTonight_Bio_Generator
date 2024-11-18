from flask import Flask, render_template, request, jsonify
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import os
import torch

# Initialize Flask app
app = Flask(__name__)

# Load GPT-Neo model and tokenizer from Hugging Face
model_name = "EleutherAI/gpt-neo-1.3B"  # GPT-Neo model (1.3B parameters)
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Route to home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate bio
@app.route('/generate-bio', methods=['POST'])
def generate_bio():
    try:
        data = request.get_json(force=True)
        career = data.get('career', '').strip()
        personality = data.get('personality', '').strip()
        interests = data.get('interests', '').strip()
        relationship = data.get('relationship', '').strip()

        if not career or not personality or not interests:
            error_message = (
                f"Missing input data. Received values - "
                f"career: '{career}', personality: '{personality}', interests: '{interests}'."
            )
            return jsonify({"error": error_message}), 400

        # Create prompt based on user input
        prompt = (
            f"I am a {career} who is {personality} and loves {interests}. "
            f"My relationship goal is {relationship}. Write a creative bio for me."
        )

        # Tokenize the prompt
        inputs = tokenizer(prompt, return_tensors="pt")

        # Generate output
        output = model.generate(
            inputs['input_ids'], 
            max_length=150,  # Adjust the length of the generated response
            num_return_sequences=1, 
            no_repeat_ngram_size=2,  # Avoid repetition in text
            temperature=0.7,  # Adjust creativity (higher = more creative)
            top_k=50,  # Sampling for more diverse results
            top_p=0.95  # Nucleus sampling for creativity
        )

        # Decode the output
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        
        # Return the generated bio as a JSON response
        return jsonify({"bio": generated_text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
