from flask import Flask, render_template, request, jsonify
import re
import os

app = Flask(__name__)

# 🚨 Spam keywords and their scores
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

# 🎯 Minimum score required to classify as spam
THRESHOLD = 3


# 🧹 Clean the input text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text


# 🔍 Analyze the email
def analyze(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    score = 0
    matched = []

    for word in words:
        if word in SPAM_KEYWORDS:
            score += SPAM_KEYWORDS[word]
            matched.append(word)

    # 🚨 Determine result
    if score >= THRESHOLD:
        result = "SPAM"
    else:
        result = "NOT SPAM"

    return {
        "score": score,
        "matched": matched,
        "result": result
    }


# 🏠 Home page
@app.route("/")
def home():
    return render_template("index.html")


# 🔮 Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        # Check if data exists
        if not data:
            return jsonify({
                "error": "No data received"
            }), 400

        # Check if text exists
        if "text" not in data:
            return jsonify({
                "error": "Text field is required"
            }), 400

        text = data["text"]

        # Check empty text
        if not isinstance(text, str) or not text.strip():
            return jsonify({
                "error": "Please enter some text"
            }), 400

        # Analyze the email
        result = analyze(text)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ❤️ Health check
@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "message": "Spam Classifier Backend is working!"
    })


# 🚀 Run Flask
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
