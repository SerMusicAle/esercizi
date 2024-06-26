#DESCRIPTION FUNCTION
"""
    # Definizione della funzione make_shirt() con valori predefiniti
    def make_shirt(size="L", message="I love Python"):
        print(f"Creo una maglietta di taglia {size} con il messaggio: {message}")

    # Creazione di una maglietta grande (default) con messaggio predefinito
    make_shirt()

    # Creazione di una maglietta media (default) con messaggio predefinito
    make_shirt(size="M")

    # Creazione di una maglietta di qualsiasi taglia con un messaggio diverso
    make_shirt(size="S", message="Keep calm and code on!")

"""

#FUNCTION
# default setup
def f_large_shirt(size="L", message="I love Python"):

    #BODY
    print(f"Creo una maglietta di taglia {size} con il messaggio: {message}")

# CALL and create default shirt 
f_large_shirt()

# CALL and create M version
f_large_shirt(size="M")

# CALL and create new version
f_large_shirt(size="S", message="Keep calm and code on!")
