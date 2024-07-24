"""
Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
For example:

Test	Result
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
b
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))
None
"""
from typing import Any
def trova_chiave_per_valore(dizionario: dict[Any, Any], valore: int) -> str:
    # cancella pass e scrivi il tuo codice
    for chiave,val in dizionario.items():
        if val == valore:
            return chiave

        