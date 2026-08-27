from flask import Flask, render_template, request, jsonify
import re
import os

app = Flask(__name__)

SPAM_KEYWORDS = {
    "free": 2,
    "win": 2,
    "cash": 2,
    "money": 2,
    "urgent": 1,
    "offer": 1,
    "credit": 2,
    "loan": 2,
    "prize": 2,
    "click": 1,
    "buy": 1,
    "cheap": 1
}

THRESHOLD = 3


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text


def analyze(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    score = 0
    matched = []

    for word in words:
        if word in SPAM_KEYWORDS:
            score += SPAM_KEYWORDS[word]
            matched.append(word)

    result = "SPAM" if score >= THRESHOLD else "NOT SPAM"

    return {
        "score": score,
        "matched": matched,
        "result": result
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({
                "error": "No text provided"
            }), 400

        text = data["text"]

        if not isinstance(text, str) or not text.strip():
            return jsonify({
                "error": "Please enter some text"
            }), 400

        return jsonify(analyze(text))

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
