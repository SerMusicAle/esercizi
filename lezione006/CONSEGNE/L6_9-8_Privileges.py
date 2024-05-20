"""
9-8. Privileges: Write a separate Privileges class. 
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.

9-8. Privilegi: Scrivi una classe separata chiamata Privileges. 
La classe dovrebbe avere un attributo, privileges, che memorizza una lista di stringhe come descritto nell'Esercizio 9-7. 
Sposta il metodo show_privileges() in questa classe. Crea un'istanza di Privileges come attributo nella classe Admin. 
Crea una nuova istanza di Admin e utilizza il tuo metodo per mostrare i suoi privilegi.

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

    #USER - describe
    def describe_user(self):
        print (f"{self.first_name} {self.last_name} è nato nella città di {self.city} il giorno {self.date} ed il suo codice fiscale è {self.cf}")

    #USER - greet
    def greet_user(self):
        print (f"ciao  {self.first_name}")


class Privileges:
    
    #DEC
    def __init__ (self, privileges=None):
        if privileges is None:
            self.privileges =[]
        else:
            self.privileges = privileges

    #PRIVILEGES - show
    def show_privileges (self, admin):
        print (f"{admin.first_name} {admin.last_name} è autorizzato a: ")
        for privilege in self.privileges:
            print (f"- {privilege} \n")

class Admin(User):

    #DEC
    def __init__(self, first_name:str, last_name:str, date:str, city:str, cf:str, privileges=None):

        super().__init__ (first_name, last_name, date, city, cf)
        self.privileges = Privileges(privileges)



#INPUT
admin_privileges = [" aggiungere post", " eliminare post", " bannare utente"]

#RETURN
amministratore = Admin("Alessandro", "Sereni", "14//12/1981", "Roma", "srnlsn81t14h501t", admin_privileges)
amministratore.privileges.show_privileges(amministratore)

