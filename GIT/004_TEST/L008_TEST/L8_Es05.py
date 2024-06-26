"""
Data una stringa s contenente solo i caratteri '(', ')', '{', '}', '[' e ']', 

scrivi se la stringa di input è valida. lo è se:
    - Le parentesi aperte devono essere chiuse dallo stesso tipo di parentesi.
    - Le parentesi aperte devono essere chiuse nell'ordine corretto.
    - Ogni parentesi chiusa ha una parentesi aperta corrispondente dello stesso tipo.

"""
"""
def is_valid_parentheses(s: str) -> bool:

#INIT
    confronto = {')': '(', '}': '{', ']': '['}
    aperte = []
    
#BODY
    for i in s:

        if i in confronto:
            last = aperte.pop()

            if confronto[i] != last:
                return False

        else:
            aperte.append(i)
    
    return not aperte

"""

def is_valid_parentheses(s: str) -> bool:
    # Dizionario per tenere traccia delle corrispondenze delle parentesi
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    # Inizializziamo l'indice del primo carattere
    start = 0
    # Inizializziamo l'indice dell'ultimo carattere
    end = len(s) - 1
    
    # Iteriamo finché non raggiungiamo l'intera stringa
    while start < end:
        # Controlliamo se il primo e l'ultimo carattere corrispondono
        if s[start] in matching_parentheses and s[end] == matching_parentheses[s[start]]:
            # Rimuoviamo il primo e l'ultimo carattere corrispondenti
            s = s[:start] + s[start+1:end] + s[end+1:]
            # Aggiorniamo l'indice dell'ultimo carattere
            end -= 2
        else:
            # Se i caratteri non corrispondono, la stringa non è valida
            return False
    # Alla fine, se la stringa è stata ridotta a vuota, tutte le parentesi sono state chiuse correttamente
    return s == ''


# Esempi di utilizzo
print(is_valid_parentheses("()"))        # Output: True
print(is_valid_parentheses("()[]{}"))    # Output: True
print(is_valid_parentheses("(]"))        # Output: False
print(is_valid_parentheses("([)]"))      # Output: False
print(is_valid_parentheses("{[]}"))      # Output: True
