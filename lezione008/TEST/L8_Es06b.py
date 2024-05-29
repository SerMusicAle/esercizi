"""
    Data una stringa s che consiste di lettere minuscole o maiuscole, 
    scrivi una funzione che 
        - restituisce la lunghezza del palindromo più lungo che può essere costruito con quelle lettere. 
        - Le lettere sono sensibili al caso, ad esempio, "Aa" non è considerato un palindromo qui.

"""

def longest_palindrome(s: str) -> int:
    conteggio = {}
    
    for lettera in s:
        if lettera in conteggio:
            conteggio[lettera] += 1
        else:
            conteggio[lettera] = 1
    
    pari = 0
    dispari = 0
    
    for val in conteggio.values():
        if val % 2 == 0:
            pari += val
        else:
            pari += val - 1
            dispari += 1
    
    if dispari > 0:
        pari += 1
    
    return pari



"""  
    for i in range(len(s)):
        for l in range (i+1, len(s)+1):
            text = s[i:l]
            if text == text[::-1]:
                lentext = len(text)
                if lentext > lenmax:
                    lenmax = lentext
    print (lenmax)

s = "abccccdd"

"""

longest_palindrome(s)


"""
1,2,3,4,5,6,7,8,9,0

12
123
1234
12345
123456
1234567
12345678
123456789
1234567890
"""