def lenght_of_last_word(frase:str) -> int:

    """
    data una stringa con parole e spazi 
    restituire la lunghezz adell'ultima parola.
    """

 """
 versione mia

    count: int = 0
    for i in range (len(frase)-1, 0, -1):
        if i == " ":
            for l in range (i+1,i==" ",+1):
                count+=1
            continue
    print (f"la lunghezza dell'ultima parola è {count}")
lenght_of_last_word ("questa è la frase")

"""

"""
l:ist[str] = s.split()
return len(l[-1])
"""


s:str = "".join(reversed(s))
i: int = 0
curr_len: int = 0
while i < len (s):
    if s[i] != "":
        curr_len +=1
    else:
        break
    i +=1
return curr_len
