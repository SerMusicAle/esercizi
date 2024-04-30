#DESCRIPTION FUNCTION
"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, 
and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) 
to insert a blank line between each word-meaning pair in your output.
"""

#FUNCTION
def f_glossary():
    
    #DECLARATION LOCAL VAR
    glossary = {
        'Variabile': 'Una variabile è un\'entità che può memorizzare un valore o un insieme di valori in un programma. Ogni variabile ha un nome univoco e un tipo di dato associato.',
        'Funzione': 'Una funzione è un blocco di codice riutilizzabile che esegue un\'azione specifica quando chiamato. Le funzioni sono utilizzate per organizzare il codice e facilitare la modularità e il riuso.',
        'Condizione': 'Una condizione è un\'espressione logica che determina il flusso del programma. Se una condizione è vera, il programma esegue un blocco di istruzioni specifico; altrimenti, può eseguire un altro blocco di istruzioni.',
        'Ciclo': 'Un ciclo è una struttura di controllo che consente di ripetere un blocco di istruzioni più volte. I cicli sono utilizzati per automatizzare compiti ripetitivi e iterare su una sequenza di elementi.',
        'Dizionario': 'Un dizionario è una struttura dati in Python che associa chiavi (generalmente stringhe) a valori. Ogni elemento nel dizionario è una coppia chiave-valore, che consente un\'indicizzazione efficiente e rapida ricerca dei dati.'
    }

    #BODY
    for word, meaning in glossary.items():
        print(f"{word.capitalize()}:\n {meaning}\n")
    
#CALL FUNCTION
f_glossary()












