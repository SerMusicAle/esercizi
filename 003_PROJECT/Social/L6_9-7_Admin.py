"""
9-7. Admin: An administrator is a special kind of user. 
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 
or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", 
"can delete post", "can ban user", and so on. Write a method called show_privileges() 
that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 


9-7. Amministratore: Un amministratore è un tipo speciale di utente. 
Scrivi una classe chiamata Admin che eredita dalla classe User che hai scritto nell'Esercizio 9-3 o nell'Esercizio 9-5. 
Aggiungi un attributo, privileges, che memorizza una lista di stringhe come "può aggiungere post", "può eliminare post", 
"può bannare utente", e così via. Scrivi un metodo chiamato show_privileges() che elenca l'insieme di privilegi dell'amministratore. 
Crea un'istanza di Admin e chiama il tuo metodo.


"""

#CLASS USER
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
        print (f"ciao  {self.first_name}")

#CLASS ADMIN
class Admin(User):

    #DEC
    def __init__(self, first_name:str, last_name:str, date:str, city:str, cf:str, privileges=[]):

        super().__init__ (first_name, last_name, date, city, cf)
        self.privileges = privileges

    #SHOW PRIVILEGES
    def show_privileges (self):
        print (f"{self.first_name}{self.last_name} è autorizzato a {',' .join(self.privileges)}")


#ASSIGNEMENT
amministratore = Admin ("Alessandro", "Sereni", "14//12/1981", "Roma", "srnlsn81t14h501t", ["può aggiungere post", "può eliminare post", "può bannare utente"])

#RETURN
amministratore.show_privileges()