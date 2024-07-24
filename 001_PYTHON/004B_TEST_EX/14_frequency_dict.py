"""
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
For example:

Test	Result
print(frequency_dict(['mela', 'banana', 'mela']))
{'mela': 2, 'banana': 1}
"""

def frequency_dict(elements: list[str]) -> dict[str,int]:
    # cancella pass e scrivi il tuo codice
    lista:dict[str,int] = {}
    
    for elemento in elements:
        if not elemento in lista:
            lista[elemento] = 1
        else:
            lista[elemento] +=1
    return lista