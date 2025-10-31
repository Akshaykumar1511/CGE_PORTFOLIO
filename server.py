from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# ✅ Replace this with your *new* API key safely
client = OpenAI(api_key="")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        # Get AI response
        response = client.responses.create(
            model="gpt-4o-mini",  # small, fast, and ideal for chatbot
            input=user_input
        )

        reply = response.output[0].content[0].text
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"reply": f"⚠️ Server error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
