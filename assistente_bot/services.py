from flask import Flask, request, jsonify
import spacy
import os
from transformers import pipeline


MODEL_PATH = os.path.join(os.path.dirname(__file__), "../model")
MODEL_PATH = os.path.abspath(MODEL_PATH)
nlp = spacy.load(MODEL_PATH)
generator = pipeline('text-generation', model='pierreguillou/gpt2-small-portuguese')


app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/Services", methods=["POST"])
def services():
    input_text = request.json.get("message")

    response = generator(f"Por favor, responda em português: {input_text}", max_length=100, num_return_sequences=1)

    doc = nlp(input_text)
    predictions = doc.cats
    intent = max(predictions, key=predictions.get)

    return jsonify({"Classificação":  intent , "cat": predictions, "Resposta": response[0]['generated_text']})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)










