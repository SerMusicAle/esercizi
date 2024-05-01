#DESCRIPTION FUNCTION
"""
    6-9. Favorite Places: Make a dictionary called favorite_places. 
    Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
    To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, 
    and print each person’s name and their favorite places.
"""

#FUNCTION
def f_places():
    
    #DECLARATION LOCAL VAR!
    like = {}  

    #BODY
    while True:
        
        #INPUT - name and places, stop with end
        person_name = input("inserisci il nome del viaggiatore (o 'fine' per terminare): ").strip().lower()
        if person_name == 'fine':
            break  # Exit the loop if the user types 'end'

        place_name = input("inserisci uno dei posti preferiti per viaggiare: ")

        # Convert the name to lowercase
        person_key = person_name

        if person_key in like:
            # has already been added?
            if place_name.lower() in like[person_key]:
                # Skip if it's in the list
                pass
            else:
                # Add new place 
                like[person_key].append(place_name.lower())
        else:
            # Create a new entry
            like[person_key] = [place_name.lower()]

    # Print places 
    for person, places in sorted(like.items()):
        # Print name and  favorite places 
        print(f"\nI posti favoriti di: {person.capitalize()}:")
        for place in sorted(places):
            # Print each favorite place indented
            print(f"- {place.capitalize()}")

#CALL
f_places()
