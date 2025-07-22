from flask import Flask, request, jsonify
from ai.email_guard import classify_email

app = Flask(__name__)
API_KEY = "secret123"

@app.route('/scan', methods=['POST'])
def scan():
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    text = data.get("text", "")
    return jsonify(classify_email(text))

if __name__ == '__main__':
    app.run(debug=True)
