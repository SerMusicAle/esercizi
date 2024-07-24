"""
    Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
For example:

Test	Result
print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
{'a': [1, 3], 'b': [2]}
print(lista_a_dizionario([]))
{}
    
    """

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codie
    dizionario:dict [str,list[int]] = {}
    for chiave, valore in tuples:
        if chiave not in dizionario:     
            dizionario[chiave] = [valore]
        else:
            dizionario[chiave].append(valore)
    return dizionario