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


