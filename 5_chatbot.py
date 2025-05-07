# Define simple responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! How can I help you?",
    "help": "Sure! You can ask me about our products, prices, or support.",
    "products": "We offer a variety of products, including laptops, phones, and accessories.",
    "price": "Our products range from $50 to $2000 depending on the type and features.",
    "thanks": "You're welcome! Feel free to ask if you need more help.",
    "bye": "Goodbye! Have a great day!"
}

# Function to handle user input and provide a response
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # Get user input and convert to lowercase
        
        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            print("Chatbot: I'm sorry, I don't understand that. Type 'help' for assistance.")
        
        if user_input == "bye":
            break

# Run the chatbot
chatbot()
