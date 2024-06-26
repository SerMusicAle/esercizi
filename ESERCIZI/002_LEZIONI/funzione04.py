def print_numbers(numeri:list):
    for n in numeri:
        print (n)
res = print_numbers([1,2,3,4,5,9,7,])

#versione 2
def print_numbers(numeri:list):
    for i in range(len(numeri)):
        print (f"il numero in posizione {i}, è {numeri[i]}")
res = print_numbers([1,2,3,4,5,9,7,])
