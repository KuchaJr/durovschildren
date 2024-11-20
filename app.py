from flask import Flask, render_template, request, jsonify
from g4f.client import Client
import openai

# Инициализация Flask-приложения
app = Flask(__name__)

client = Client()

openai.api_key = "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"

@app.route("/")
def home():
    return render_template("assistant.html")  

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=1
        )
        assistant_message = response.choices[0].message["content"]
        return jsonify({"response": assistant_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
