from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import re
import logging

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

# Load the JSON dataset
try:
    with open('intents.json', 'r') as f:
        data = json.load(f)
        intents = data.get('intents', [])
        if not intents:
            logging.error("No 'intents' key found in the JSON file or it's empty.")
            raise ValueError("Invalid JSON structure: Missing 'intents'.")
except Exception as e:
    logging.error(f"Failed to load JSON dataset: {e}")
    intents = []

# Debugging: Print loaded intents to confirm structure
logging.debug(f"Loaded intents: {json.dumps(intents, indent=4)}")

def get_bot_response(user_message):
    """
    Match the user message against patterns in the dataset and return a response.
    """
    user_message = user_message.lower()
    logging.info(f"User message: {user_message}")

    for intent in intents:
        tag = intent.get('tag', 'unknown')
        patterns = intent.get('patterns', [])
        responses = intent.get('responses', [])

        for pattern in patterns:
            # Use regex for partial matching (case-insensitive)
            if re.search(re.escape(pattern.lower()), user_message, re.IGNORECASE):
                response = random.choice(responses)
                logging.info(f"Matched intent: {tag}, Pattern: {pattern}, Response: {response}")
                return response

    # Default response if no match
    logging.info("No matching pattern found.")
    return "I'm sorry, I didn't understand you. Could you rephrase?"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'response': "Please provide a message."}), 400

    response = get_bot_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)



