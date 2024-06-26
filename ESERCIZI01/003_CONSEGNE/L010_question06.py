"""
Definire una funzione chiamata hypotenuse 
- che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. 
- che deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) 
- che deve restituire l'ipotenusa come un float.

Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

"""
import math

def f_hypotenuse(lato1:float, lato2:float):

#INIT
    ipotenusa:float = 0.0
#BODY
    ipotenusa = math.sqrt(lato1 ** 2 + lato2 ** 2)
#RETURN
    print (ipotenusa)

#INPUT

lato1 = 3.0
lato2 = 4.0

#CALL
f_hypotenuse(lato1, lato2)