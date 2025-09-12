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
while True:
    user_input = input("You: ").lower()  # convert to lowercase

    # check if any exit word is anywhere in the input
    if any(word in user_input for word in ["exit", "quit", "leave"]):
        print("Bot: Goodbye! Safe travels 🚀")
        break
    found = False
    for key in destinations:
        if key in user_input:
            directions = destinations[key]
    
        # Check if the destination has walking/driving options
    if isinstance(directions, dict):
         mode = input("Bot: Do you want walking or driving directions? ").lower()
         if mode in directions:
            print("Bot:", random.choice(directions[mode]))
         else:
             print("Bot: Sorry, I can only give walking or driving directions.")
    else:
        # Simple list, no walking/driving distinction
         print("Bot:", random.choice(directions))
            
    found = True
    break

if not found:
     print("Bot: Sorry, I don’t know how to get there yet.")
         
            

