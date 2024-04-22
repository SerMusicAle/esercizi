"""
dato un intero x, ritorna True se x è palindromo e False altrimenti
121 è True, -121 è False
"""
"""
def palindromo(numero:int):
    num_str = str(numero)
    if len(num_str)/2==1 and str_num[0]!="-":
        for i in range (len(num_str)/2):
            if (reverse_string(num_str))==num_str:
            True
    
    else print("non è un palindromo, deve essere di lunghezza dispari")
    
    res = palindromo(123454321)
"""
def is_palindrome(x:int) ->bool:
    s:str = str(x)
    i:int = 0
    s_lenght = len(s)
    while i < (s_lenght //2):
        j = s_lenght - (i+1)
        if = s_lenght - (i+1)
        if s[i] != s[j]:
            return False
        i +=1
    return True