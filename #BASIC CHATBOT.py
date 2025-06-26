#BASIC CHATBOT

def chatbot():
    print("Chatbot: Hi! Type something to start a conversation (type 'exit' to end).")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        elif user_input == "exit":
            print("Chatbot: Chat ended.")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()