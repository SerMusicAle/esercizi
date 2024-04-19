def check_each(numeri:list):
    for i in range(len(numeri)):
        if numeri[i]==5:
            print (f"il numero {numeri[i]}, è uguale a 5")
        elif numeri[i]<5:
            print (f"il numero {numeri[i]}, è minore di 5")
        else:
            print (f"il numero {numeri[i]}, è maggiore di 5") 
res = check_each([1,2,3,4,5,9,7,])
