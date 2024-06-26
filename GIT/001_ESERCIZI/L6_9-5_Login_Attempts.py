"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


9-5. Tentativi di Accesso: 
Aggiungi un attributo chiamato login_attempts alla tua classe User dall'Esercizio 9-3. 
Scrivi un metodo chiamato increment_login_attempts() che incrementa il valore di login_attempts di 1. 
Scrivi un altro metodo chiamato reset_login_attempts() che reimposta il valore di login_attempts a 0. 
Crea un'istanza della classe User e chiama increment_login_attempts() diverse volte. 
Stampa il valore di login_attempts per assicurarti che sia stato incrementato correttamente, e poi chiama reset_login_attempts(). 
Stampa di nuovo login_attempts per assicurarti che sia stato reimpostato a 0.


"""

#CLASS
class User:

    #DEC
    def __init__ (self, first_name, last_name, date, city, cf, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.date = date
        self.cf = cf
        self.login_attempts = login_attempts

    #BODY
    #describe user
    def describe_user(self):
        print (self.first_name + " " + self.last_name + " è nato nella città di " + self.city + " il giorno " + self.date + " ed il suo codice fiscale è " + self.cf)

    #greet
    def greet_user(self):
        print (f"ciao " + self.first_name)

    def increment_login_attempts(self):
        self.login_attempts +=1
        print (f"il numero di accesso di questo utente è: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print (f"il numero di accesso di questo utente è: {self.login_attempts}")


#ASSIGNEMENT INSTANCE
utente = User ("Alessandro", "Sereni", "14/12/1981", "Rome", "srnlsn81t14h501t")
utente2 = User ("Fernando", "Sereni", "23/03/1951", "Rome", "srnfnn51c23h501f")

#RETURN
utente.describe_user()
utente.greet_user()
utente2.describe_user()
utente2.greet_user() 
utente.increment_login_attempts()
utente.increment_login_attempts()
utente.increment_login_attempts()
utente.increment_login_attempts()
utente.reset_login_attempts()