"""
CONSEGNA
11. Scrivi una funzione che 
- converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro. 
- Utilizza il concetto di parametri opzionali.
"""

def conversione ():

#INIT
    cel_in_far = 0
    far_in_cel = 0

#INPUT
    temp = float (input(f"quanti gradi devo convertire?"))
    tipo = int (input(f"devo convertire da 1. celsius a fahrenheit, 2. da fahrenheit a celsius: "))

#BODY
    if tipo == 1:
        cel_in_far = (temp * 9/5) + 32
        print(f"{temp} gradi Celsius corrispondono a {cel_in_far} gradi Fahrenheit")
    elif tipo == 2:
        far_in_cel = (temp - 32) * 5/9
        print(f"{temp} gradi Fahrenheit corrispondono a {far_in_cel} gradi Celsius")
    else:
        print (f"hai inserito una selezione non valida")

#INPUT

#CALL
conversione()