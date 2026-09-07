# Task 3: Simple Chatbot
# Create a simple chatbot that responds to at least four different messages such as hello, how are you, what is AI, and bye.

message = input("You: ").lower()

if message == "hello":
    print("Bot: Hello! How can I help you?")
elif message == "how are you":
    print("Bot: I am fine, thank you!")
elif message == "what is ai":
    print("Bot: AI stands for Artificial Intelligence.")
elif message == "bye":
    print("Bot: Goodbye!")
else:
    print("Bot: Sorry, I don't understand.")