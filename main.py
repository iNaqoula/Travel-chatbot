# Smarter travel chatbot with flexible exit

print("Hello! I’m your travel bot. Type 'exit' or 'quit' anytime to leave.")

while True:
    user_input = input("You: ").lower()  # convert to lowercase

    # check if any exit word is anywhere in the input
    if any(word in user_input for word in ["exit", "quit"]):
        print("Bot: Goodbye! Safe travels 🚀")
        break

    if "library" in user_input:
        print("Bot: To reach the library, go straight and turn left at the first street.")
    elif "supermarket" in user_input:
        print("Bot: The supermarket is 2 blocks north from here.")
    elif "train station" in user_input:
        print("Bot: Walk down Main Street for 10 minutes and you’ll see the train station.")
    else:
        print("Bot: Sorry, I don’t know how to get there yet.")
