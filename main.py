def chatbot():
    print("Bot: Hello! I am your first rule-based AI.")
    print("Bot: Type 'exit' to quit.")

    while True:
        message = input("You: ").lower().strip()

        if message == "exit":
            print("Bot: Goodbye!")
            break

        elif "hello" in message or "hi" in message:
            print("Bot: Hello! How can I help you?")

        elif "your name" in message:
            print("Bot: I am a rule-based chatbot.")

        elif "ai" in message:
            print("Bot: AI helps computers perform tasks that seem intelligent.")

        else:
            print("Bot: I don't know how to answer that yet.")


if __name__ == "__main__":
    chatbot()