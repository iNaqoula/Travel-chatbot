import random
import difflib
from data import destinations, destination_synonyms, EXIT_WORDS


class TravelBot:
    def __init__(self):
        self.destinations = destinations
        self.synonyms = destination_synonyms
    
        self.synonym_map = {}
        for key, synonyms in self.synonyms.items():
            for s in synonyms:
             self.synonym_map[s] = key
        
        for key in self.destinations:
         self.synonym_map[key]= key
    
        self.all_keywords = list(self.synonym_map.keys())
        
    def find_destinations(self, user_input):
   
        ui = user_input.lower()
        for key in self.destinations:
            if key in ui:
             return key
        
        for main_key, synonyms in self.synonyms.items():
            if any(word in ui for word in synonyms):
                return main_key
        
        return None
    
    def correct_destinations(self,user_input):
        words = user_input.lower().split()
        for word in words:
            close = difflib.get_close_matches(word, self.destinations.keys(), n=1, cutoff=0.7)
            if close:
             return close[0]
        return None
    
    def get_directions(self,dest_key, mode=None):
         
        # function to get the destinations both if defined or not
        
        directions = self.destinations[dest_key]
        
        if isinstance(directions,dict):
            if mode is None:
                mode = input("Bot:Do you want walking or driving directions? ").lower()
        
            if mode in directions :
                return random.choice(directions[mode])
       
        
           
            if "walking" in directions:
                print("Bot: I can't do that yet, but here's the walking directions: ")
                return random.choice(directions["walking"])
           
            else:
                 first_list = next(iter(directions.values()))
                 print("Bot: I can't do that yet, here's the closest option I found")
                 return random.choice(first_list)
        else:
            return random.choice(directions)
    
    def run(self):
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

            dest_key = self.find_destinations(user_input)
            if not dest_key:
                dest_key = self.correct_destinations(user_input, destinations)

            if dest_key:
                response = self.get_directions(dest_key)
                print("Bot:", response)
            else:
                print("Bot: Sorry :(, I don't know how to get there yet.")
        
          except Exception as e:
            print(f"Bot: Oops! Something went wrong. ({e})")
    
    