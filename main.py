# Smarter travel chatbot with flexible exit

import random

print("Hello! I’m your travel bot. Type 'exit' or 'quit' anytime to leave.")

#dictionary with destinations and multiple possible directions
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
        "cafe":[
            "There's a cafe around the corner on 5th Street",
            "Head east for 3 minutea and you'll find a cozy cafe."
        
        ],
        "park":[
            "The park is just behind the library",
            "Go straight and you'll see the park on your left."
        ],
        "cinema":[
            "Take the subway to Central Station, then walk 5 minutes.",
            "Drive straight for 1o minutes and it's on your right."
        ]
    }
while True:
    user_input = input("You: ").lower()  # convert to lowercase

    # check if any exit word is anywhere in the input
    if any(word in user_input for word in ["exit", "quit", "leave"]):
        print("Bot: Goodbye! Safe travels 🚀")
        break
    
    # check for keywords in destinations
    found = False
    for key in destinations:
        if key in user_input:
            print("Bot:", random.choice(destinations[key]))
            found = True
            break
    if not found:
         print("Bot: Sorry, I don't know how to get there yet.")
         
            

