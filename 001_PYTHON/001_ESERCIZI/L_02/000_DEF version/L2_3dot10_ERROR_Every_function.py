"""
    3-10. Every Function: Think of things you could store in a list. 
    For example, you could make a list of mountains, rivers, countries, cities, languages, 
    or anything else you’d like. Write a program that creates a list containing these items and then uses 
    each function introduced in this chapter at least once.
"""

def f_all ():
    random_things = [42, "banana", True, 3.14, "python", [1, 2, 3], {'name': 'John', 'age': 30}, None, (1, 2, 3), "apple"]
    print (f"la lista originale era {random_things}")

    #pop
    random_things.pop(0)
    print (f"eseguo il pop {random_things}")
    print(f"\n")

    #sorted
    sortable_items = [item for item in random_things if isinstance(item, (int, float, str))]

    # Ordina gli elementi ordinabili
    sorted_items = sorted(sortable_items)

    print(sorted_items)
    #insert
    random_things.insert(0, "elemento nuovo")
    print (f"eseguo insert {random_things}")
    print(f"\n")

    #reverse
    random_things.reverse()
    print (f"eseguo il reverse {random_things}")
    print(f"\n")
    
    #append
    random_things.append("ultimo appeso")
    print (f"eseguo append {random_things}")
    print(f"\n")

    #len
    lunghezza = len(random_things)
    print (f"eseguo il len: lunghezza di {len(random_things)}")
    print(f"\n")

    #remove
    random_things.remove(1)
    print (f"eseguo il remove {random_things}")
    print(f"\n")

    #suffix, #lower, #upper, #capitalize, suffisso
    random_things = [42, "banana", True, 3.14, "python", [1, 2, 3], {'name': 'John', 'age': 30}, None, (1, 2, 3), "apple"]

    for i, item in enumerate(random_things):
        # Controlla se l'elemento è una stringa
        if isinstance(item, str):  
            print (f"la versione con suffisso di {item}, è: ")
            random_things[i] = item + "_suffissoaggiunto"
            print(f"\n")
            print (f"la versione upper di {item}, è: ")
            random_things[i] = item.upper()
            print(f"\n")
            print (f"la versione lower di {item}, è: ")
            random_things[i] = item.lower()
            print(f"\n")
            print (f"la versione capitalize di {item}, è: ")
            random_things[i] = item.capitalize()
            print (f"la versione senza suffisso di {item}, è: ")
            print(f"\n")
            random_things[i] = item.removesuffix("aggiunto")
            print(f"\n")
            
    #del
    del random_things[0]
    print (f"eseguo il del {random_things}")
    print(f"\n")

#CALL
f_all()