import random
import difflib
from data import destinations, destination_synonyms

#bot logic and functions all stored here.


synonym_map = {}
for key, synonyms in destination_synonyms.items():
    for s in synonyms:
        synonym_map[s] = key
        
for key in destinations:
    synonym_map[key]= key
    
all_keywords = list(synonym_map.keys())


def find_destinations(user_input, destinations):
    """
    return a destination key form destinations that mattches user input
    (substring match) or none if no destination found.
    """
    ui = user_input.lower()
    for key in destinations:
        if key in ui:
            return key
        
    for main_key, synonyms in destination_synonyms.items():
        if any(word in ui for word in synonyms):
            return main_key
        
    return None

def correct_destinations(user_input):
    #find the closest destination key to the user's input
    ui = user_input.lower()
    keys = list(destinations.keys())
    #get the closest match
    closest = difflib.get_close_matches(ui, all_keywords, n=1 , cutoff=0.6)
    if closest:
        return synonym_map[closest[0]]
    return None

def get_directions(dest_key, mode=None):
    # function to get the destinations both if defined or not
    directions = destinations[dest_key]
    if isinstance(directions,dict):
        if mode is None:
            mode = input("Bot:Do you want walking or driving directions? ").lower()
        if mode in directions :
            return random.choice(directions["walking"])
        first_list = next(iter(directions.values()))
        return random.choice(first_list)
    return random.choice(directions)