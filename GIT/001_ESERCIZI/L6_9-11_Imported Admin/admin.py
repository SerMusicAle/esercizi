"""
9-11. Imported Admin: Start with your work from Exercise 9-8. 
Store the classes User, Privileges, and Admin in one module. 
Create a separate file, make an Admin instance, and call show_privileges() 
to show that everything is working correctly.


9-11. Amministratore Importato: Parti dal lavoro svolto nell'Esercizio 9-8. 
Memorizza le classi User, Privileges e Admin in un unico modulo. 
Crea un file separato, crea un'istanza di Admin e chiama show_privileges() 
per mostrare che tutto funziona correttamente.


"""


# my_module.py

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print("Privilegi:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("Nessun privilegio assegnato.")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()
