import random

#dictionary with destinations and multiple possible directions

EXIT_WORDS = ["exit", "quit", "leave"]

destinations = { 
        "library" : [
            "go straight and turn left at the first street." ,
            "Take the second right and walk 5 minutes."
        ],
        "supermarket": [
            "The supermarket is 2 blocks north from here.",
            "walk straight for 3 minutes and you will see it on your right."
        
        ],
        "train station": [
            "walk down Main Street for 10 minutes and you'll see the train station.",
            "Take the bus to Central Ave and walk 2 minutes."
        ],
        "cafe":{
            "walking": ["There's a cafe around the corner on 5th Street"],
            "driving": ["Head east for 3 minutea and you'll find a cozy cafe."]
        
        },
        "park":{
            "walking": [
            "The park is just behind the library",
            "Go straight and you'll see the park on your left."
            ],
            "driving": [
                "Drive straight for 2 minutes and paek nearby.",
                "Take Main Street, it's about 3 minutes by car."
            ]
        },
        
        "cinema":[
            "Take the subway to Central Station, then walk 5 minutes.",
            "Drive straight for 1o minutes and it's on your right."
        ]
    }

def find_destinations(user_input, destinations):
    """
    return a destination key form destinations that mattches user input
    (substring match) or none if no destination found.
    """
    ui = user_input.lower()
    for key in destinations:
        if key in ui:
            return key
    return None

def get_directions(dest_key, mode=None):
    directions = destinations[dest_key]
    if isinstance(directions,dict):
        if mode is None:
            mode = input("Bot:Do you want walking or driving directions? ").lower()
        if mode in directions :
            return random.choice(directions["walking"])
        first_list = next(iter(directions.values()))
        return random.choice(first_list)
    return random.choice(directions)

                 
def main():
    
    print("Hello! I’m your travel bot. Type 'exit' or 'quit' anytime to leave.")


    while True:
     user_input = input("You: ").lower()  # convert to lowercase
     if any(w in user_input.lower() for w in EXIT_WORDS):
         print("Bot: Goodbye! safe Travels")
         break
     dest_key = find_destinations(user_input,destinations)
     if dest_key:
         response = get_directions(dest_key)
         print("Bot:", response)
     else:
        print("Bot: Sorry :(, I don't know how to get there yet.")
        
        
if __name__ == "__main__":
    main()
           
    
         
            

