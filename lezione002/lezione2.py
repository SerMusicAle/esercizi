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


