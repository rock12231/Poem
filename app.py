from flask import Flask, render_template, request
from google.api_core import client_options
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = Flask(__name__)
load_dotenv() 

genai.configure(api_key=os.environ["API"])

# Set the generation config for aldult content

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 8192
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_text = ""

    if request.method == 'POST':
        keywords = request.form['keywords']
        language = request.form['language']
        prompt = f"Write a short poem or story using these words: {keywords}, make it interesting, engaging and rhyming. Not more than 70 words in {language}."

        # Use generate_content()
        response = model.generate_content(prompt) 
        generated_text = response.text  # Access the generated text

    return render_template('index.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True) 