import random
from data import destinations

#bot logic and functions all stored here.

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