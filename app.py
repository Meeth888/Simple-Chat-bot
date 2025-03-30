from flask import Flask, request, jsonify
#flask- A Light weight web framework for creating web applications.
#request - used to handle upcoming HTTP request.
#jsonify - converts python dictionaries into json response.

app = Flask(__name__)
#Intializes flask web application

def chatbot_user(input):
    input = input.lower()

    if "hello" in input:
        return "Hi there! How can I help you today?"
    elif "how are you" in input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in input:
        return "I'm a simple chatbot created with Python!"
    elif "bye" in input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you try asking something else?"

@app.route("/chat", methods=["POST"])
##This defines an API route (/chat) that listens for POST requests.
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = chatbot_user(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    #This ensures the script runs only when executed directly, not when imported.
    app.run(host="0.0.0.0", port=8080)
#Starts the Flask web server on port 8080.

### Summary
'''
The Flask app starts and waits for requests at /chat.

When a POST request is received with a message:

The chatbot processes it using if-elif-else logic.

Returns an appropriate response in JSON format.

The server runs on port 8080, ready to be accessed locally or deployed to the cloud.
'''