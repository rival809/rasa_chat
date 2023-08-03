# app.py
from flask import Flask, request
import rasa

# Import your Rasa agent here
# Example: from rasa.core.agent import Agent

app = Flask(__name__)

# Initialize your Rasa agent here
# Example: agent = Agent.load(...)

@app.route('/webhook', methods=['POST'])
def rasa_webhook():
    input_json = request.get_json()
    agent = rasa.core.agent.Agent("my_model.yml", "endpoints.yml")
    response = agent.handle_message(input_json)
    return {'responses': response}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
