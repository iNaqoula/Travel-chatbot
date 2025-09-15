EXIT_WORDS = ["exit", "quit", "leave"]
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
# dictionary with synonyms for multiple destinations
destination_synonyms = {
    "train station" : ["station", "train", "railway"],
    "supermarket" : ["market", "grocery store","grocery"],
    "library" : ["bookshop", "reading room"],
    "cafe": ["coffee shop"]
}