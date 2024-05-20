"""
CONSEGNA
5. Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.
"""

def somma_div2_3(lista_num):

    #INIT
    somma: int = 0

    #BODY
    for number in lista_num:
        if number%2 == 0 and number % 3 == 0:
            somma += number
    
    print(f"la somma degli n divisibili per 2 eper 3 fa: {somma}")

#CALL
somma_div2_3([2,3,4,5,6,7,8,9,12,24,])