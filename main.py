from data import EXIT_WORDS, destinations
from bot_logic import find_destinations, get_directions, correct_destinations


                 
def main():
    print("Hello! I’m your travel bot. Type 'exit', 'quit' or 'leave' to stop.")
    while True:
        try:
            user_input = input("You: ").strip()  # remove extra spaces

            if not user_input:
                print("Bot: Please type something")
                continue
            
            if any(w in user_input.lower() for w in EXIT_WORDS):
                print("Bot: Goodbye! Safe travels 🚀")
                break

            dest_key = find_destinations(user_input, destinations)
            if not dest_key:
                dest_key = correct_destinations(user_input, destinations)

            if dest_key:
                response = get_directions(dest_key)
                print("Bot:", response)
            else:
                print("Bot: Sorry :(, I don't know how to get there yet.")
        
        except Exception as e:
            print(f"Bot: Oops! Something went wrong. ({e})")


if __name__ == "__main__":
    main()

    
         
            

