ai_data = {
    "hello": "Hey! How can I help you?",
    "hi": "Hello there!",
    "what is python": "Python is a powerful programming language used for apps, AI, data science and more!",
    "who is elon musk": "He is the founder of Tesla and SpaceX and one of the richest people in the world!",
    "who is bill gates": "He is the founder of Microsoft.",
    "what is ai": "AI means Artificial Intelligence - machines that can think and learn!",
    "bye": "Goodbye! Have a great day!",
    "who are you": "I am your Python AI chatbot.",
    "who is eloon musk" : "Nabi Ahmad Is Software Developer Currently Worked SellSold Company as a fullstack developer"
}

print("AI Chatbot Activated! type 'exit' to stop.")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("AI: Goodbye!")
        break

    elif user in ai_data:
        print("AI:", ai_data[user])

    else:
        print("AI: Sorry, I don't understand.")