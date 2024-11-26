from flask import Flask, request, jsonify
import spacy
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../model")
MODEL_PATH = os.path.abspath(MODEL_PATH)
nlp = spacy.load(MODEL_PATH)

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/Services", methods=["POST"])
def services():
    input_text = request.json.get("message")

    doc = nlp(input_text)
    predictions = doc.cats
    intent = max(predictions, key=predictions.get)

    return jsonify({"Classificação":  intent , "cat": predictions})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)










