#DESCRIPTION FUNCTION
"""
    5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
    • If the alien is green, print a message that the player earned 5 points.
    • If the alien is yellow, print a message that the player earned 10 points.
    • If the alien is red, print a message that the player earned 15 points.
    • Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
#FUNCTION
def f_alien_colors_v3():

    #DECLARATION LOCAL VAR - INPUT requests
    alien_color = input(f"PARTITA 1 - di quale colore è l'alieno? green o red?")

    #BODY
    # Test if-elif-else per gestire il colore dell'alieno (verde)
    if alien_color == 'green':
        print("Il giocatore ha appena guadagnato 5 punti per aver sparato all'alieno.")
    elif alien_color == 'yellow':
        print("Il giocatore ha appena guadagnato 10 punti per aver sparato all'alieno.")
    else:
        print("Il giocatore ha appena guadagnato 15 punti per aver sparato all'alieno.")

#CALL
f_alien_colors_v3()
