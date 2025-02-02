from flask import Flask, request, jsonify
from gemini_chat import generate_response
from mysql_connection import get_db_connection, store_chat_history

app = Flask(__name__)

@app.route("/chat", methods=["POST"])

def chat():
    data = request.get_json()
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "Query is required!"}), 400

    response = generate_response(user_query)

    # Convert response to string
    if isinstance(response, str):
        final_response = response
    else:
        final_response = response.text  # Extract text from response object

    # Store chat history in MySQL database
    store_chat_history(user_query, final_response)

    return jsonify({"query": user_query, "response": final_response})


if __name__ == "__main__":
    app.run(debug=True)