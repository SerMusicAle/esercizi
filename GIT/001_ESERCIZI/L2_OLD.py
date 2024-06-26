#Alessandro Sereniù
#2024 04 18

#ex. prova
print ("Hello Word")

"""
ex.2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
"""
#variabile nome
name: str = "Alessandro"

#variabile mesaggio
messaggio: str = f"ciao {name}, proviamo a stampare"

print (messaggio)

"""
ex. 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in 
lowercase, uppercase, and title case.
"""
#la variabile nome viene modificata nei 3 stili
#metodo1
print (name.upper(), name.lower(), name.title())

#metodo2
print (f"{name}, {name.upper()}, {name.lower()}")

#metodo3
name_lower: str =name.lower()
name_upper: str = name.upper()
print (f"{name}, {name.upper()}, {name.lower()}")


"""
ex. 2-5. Famous Quote: Find a quote from a famous person you admire. 
Print the quote and the name of its author. Your output should look something like the following, 
including the quotation marks: Albert Einstein once said, “A person who never made a mistake 
never tried anything new.”
"""
#elementi citazioni del dizionario
vip_q: dict = {'Einstein':'la vita è come una bicicletta', 'Mandela':'La istruzione è arma più potente', 'Jobs':'Stay hungry, stay foolish'}

#faccio inserire dall'utente il vip
print ('chi preferisci tra Einstein, Mandela e Jobs?')
vip: str =  input()

#verifico la corrispondenza e cito il personaggio
if vip_q[vip]:
    print(f"{vip} una volta disse:, {vip_q[vip]}")

"""
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() 
method to display the filename without the file extension, like some file browsers do.
"""

#creo dizionario con unica chiave valore
files: dict = {'file1':'python notes.txt'}

print (f"{files}")


"""
        3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
    • Store the locations in a list. Make sure the list is not in alphabetical order.
    • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
    • Use sorted() to print your list in alphabetical order without modifying the actual list.
    • Show that your list is still in its original order by printing it.
    • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
    • Show that your list is still in its original order by printing it again.
    • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
    • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
    • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
    • Use sort() to change your list so it’s stored in reverse-alphabetical order.
    Print the list to show that its order has changed.
"""
def f_places (places):
    print(f"la lista originale è {places}")
    
    #verifico se la lista è ordinata alfabeticamente
    for i in range (len (places)-1):
        if places[i] < places[i+1]:
            print(f"la lista è ordinata alfabeticamente")
        else: 
            print(f"la lista non è ordinata alfabeticamente")

    #stampa lista originale e in ordine inverso
    print(f" l'ordine della lista originale è: ")
    for i in places:
        print(i)
    places2 = places[::-1]
    print(f"il nuovo ordine della lista è inverso: ")
    for i in places2:
        print(i)        
    places.sort()
    places3 = places[::-1]
    print(f"l'ordine della lista originale era: ")
    for i in places3:
        print(i)

f_places (["roma", "londra", "madrid", "parigi", "lisbona"])


"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.
"""
ospiti: list = (["marco", "luigi", "mario"])

def len_ospiti(ospiti):
    