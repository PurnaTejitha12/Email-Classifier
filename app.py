from flask import Flask, render_template, request, jsonify
import re

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
    text = clean_text(text)
    words = text.split()

    score = 0
    matched = []

    for w in words:
        if w in SPAM_KEYWORDS:
            score += SPAM_KEYWORDS[w]
            matched.append(w)

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
    data = request.json["text"]
    return jsonify(analyze(data))


if __name__ == "__main__":
    app.run(debug=True)