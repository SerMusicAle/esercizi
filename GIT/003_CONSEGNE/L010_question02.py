"""
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

"""


def f_transform(x: int) -> int:
    if x%2 == 0:
        x//=2
    else:
        x = x*3-1
    print (x)

f_transform(10)