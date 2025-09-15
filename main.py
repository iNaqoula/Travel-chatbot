from data import EXIT_WORDS, destinations
from bot_logic import find_destinations, get_directions, correct_destinations


                 
def main():
    
    print("Hello! I’m your travel bot. Type 'exit' or 'quit' anytime to leave.")


    while True:
     user_input = input("You: ").lower()  # convert to lowercase
     if any(w in user_input.lower() for w in EXIT_WORDS):
         print("Bot: Goodbye! safe Travels")
         break
     dest_key = find_destinations(user_input,destinations)
     if not dest_key:
         dest_key = correct_destinations(user_input)
     if dest_key:
         response = get_directions(dest_key)
         print("Bot:", response)
     else:
        print("Bot: Sorry :(, I don't know how to get there yet.")
        
        
if __name__ == "__main__":
    main()
           
    
         
            

