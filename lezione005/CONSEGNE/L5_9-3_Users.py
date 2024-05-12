#DESCRIPTION
"""
9-3. Users: Make a class called User. 
Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.

9-3. Utenti: Crea una classe chiamata User. 
Crea due attributi chiamati first_name (nome) e last_name (cognome), 
e quindi crea diversi altri attributi che sono tipicamente presenti in un profilo utente. 
Crea un metodo chiamato describe_user() che stampi un riepilogo delle informazioni dell'utente. 
Crea un altro metodo chiamato greet_user() che stampi un saluto personalizzato all'utente. 
Crea diverse istanze rappresentanti utenti diversi e chiama entrambi i metodi per ciascun utente.

"""
#CLASS
class User:

    #DEC
    def __init__ (self, first_name, last_name, date, city, cf):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.date = date
        self.cf = cf

    #BODY
    #describe user
    def describe_user(self):
        print (self.first_name + " " + self.last_name + " è nato nella città di " + self.city + " il giorno " + self.date + " ed il suo codice fiscale è " + self.cf)

    #greet
    def greet_user(self):
        print (f"ciao " + self.first_name)

#ASSIGNEMENT INSTANCE
utente = User ("Alessandro", "Sereni", "14/12/1981", "Rome", "srnlsn81t14h501t")
utente2 = User ("Fernando", "Sereni", "23/03/1951", "Rome", "srnfnn51c23h501f")


#RETURN
utente.describe_user()
utente.greet_user()
utente2.describe_user()
utente2.greet_user()