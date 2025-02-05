# Basic Chatbot in Python with extended responses

def chatbot_response(user_input):
    # Extended responses dictionary
    responses = {
        "hi": "Hello! How can I help you today?",
        "wagwan":"nara watsap g",
        "nothing":"wats the plan for today?",
        "you good":"always pham",
        "hello": "Hi there! What’s on your mind?",
        "how are you": "I'm just a bunch of code, but thanks for asking! How are you?",
        "what's your name": "I'm your friendly neighborhood chatbot.",
        "bye": "Goodbye! Have a great day!",
        "what's the weather like": "I can't check the weather, but you can check it online!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "exit": "Goodbye! See you soon!",
        "amen": "praise Jesus",
        "ok": "alright then, anything else you need, please hala at me",
        "what is your purpose": "well, just to serve you my master!"
    }

    # Process user input
    user_input = user_input.lower()

    # Check if input is in responses
    response = responses.get(user_input, "Sorry, I didn’t quite get that. Can you say it another way?")
    return response


# Main interaction loop
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")

    if user_input.lower() == "exit":
        break