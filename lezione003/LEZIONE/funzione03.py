def check_lenght(frase:str):
    if len(frase)==10:
        print (f"la lunghezza del testo {frase}, è 10")
    elif len(frase)<10:
        print (f"la lunghezza del testo {frase}, è minore 10")
    else:
        print (f"la lunghezza del testo {frase}, è maggiore di 10")
res = check_lenght("1234567890")