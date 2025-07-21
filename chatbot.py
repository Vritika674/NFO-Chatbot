from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ NFO AI Chatbot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get("message", "").lower()

    # Introduction message
    if user_message in ["hi", "hello", "hey"]:
        reply = (
            "👋 Hello! We are from NFO.\n"
            "We’d love to assist you with your queries.\n\n"
            "📌 Menu:\n"
            "1️⃣ Guidebooks\n"
            "2️⃣ Olympiad\n"
            "3️⃣ Shipping\n"
            "4️⃣ Others\n"
            "Please type your query."
        )

    elif "guidebook" in user_message:
        reply = "📚 Guidebooks help you prepare for Olympiads. Check details here: https://nfo.org/guidebooks"

    elif "olympiad" in user_message:
        reply = "🏆 Olympiad details: https://nfo.org/olympiad"

    elif "shipping" in user_message:
        reply = "📦 Shipping usually takes 7–10 business days."

    elif "others" in user_message or "contact" in user_message:
        reply = "📞 For other queries, email us at support@nfo.org"

    else:
        reply = "🤖 Sorry, I didn’t understand. Please choose from: Guidebooks, Olympiad, Shipping, Others."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
