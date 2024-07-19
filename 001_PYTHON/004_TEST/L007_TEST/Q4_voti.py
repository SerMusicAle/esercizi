"""
Q4
    Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
    e aggrega i voti per studente in un nuovo dizionario.
    For example:

    expected: 
    {'Alice': [90, 85], 'Bob': [75]}
    print(aggrega_voti([])) 
"""
from typing import Union
def aggrega_voti(voti:list[dict[str, Union[str , int]]]):
    
    nuova_lista: dict [Union[str, int], list[Union[int, str]]]= {}
    
    for i in voti:
        nome:Union[str, int] = i["nome"]
        voto:Union[str, int] = i["voto"]

        if nome not in nuova_lista:
            nuova_lista[nome] = []
        nuova_lista[nome].append(voto)            
    
    return nuova_lista
    
#EXE
voti: list[dict[str,str | int]] = [{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]
print (aggrega_voti(voti))
