"""
CONSEGNA
12. Scrivi una funzione che 
- somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

"""

def somma (valore):

#INIT
    numeri:list = [1,2,3,4,5,6,7,8,9]
    somma = 0
#BODY
    for numero in numeri:
        if numero > valore:
            somma +=numero
    print(f"la somma dei valori superiori a {valore} è {somma}")
#INPUT
valore = int(input(f"dammi il valore interno da considerare: "))
#CALL
somma(valore)