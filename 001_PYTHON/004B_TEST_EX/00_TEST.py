###BANK###

class Account():
#INIT
    def __init__(self, account_id:str, balance:float = 0):
        self.account_id = account_id
        self.balance = balance
    
#BODY
    def deposit(self,amount:float):
        self.balance += amount
    
    def get_balance(self):
        return self.balance
    
class Bank():
#INIT
    def __init__(self):
        self.accounts:dict[str, Account] ={}
#BODY
    def create_account(self, account_id:str):
        if account_id not in self.accounts:
            self.accounts[account_id]= Account(account_id)
            return Account(account_id)
        else:
            #return (f"l'account esiste già")
            raise ValueError ("Account with this ID already exists")
        
    def deposit(self, account_id:str, amount:float):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        else:
            raise ValueError(f"Account not found")      
        
    def get_balance(self, account_id:str):
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        else:
            raise ValueError("Account not found")

###CHECK###
def check_access(username: str, password: int, status: bool) -> str:
    conferma:str = "Accesso consentito" 
    negato: str = "Accesso negato"
    if username == "admin" and password == "12345" and status== True:
        return conferma
    else:
        return negato
    
###RECIPE###
class RecipeManager():
#INIT
    def __init__(self):
        self.ricettario:dict[str, list[str]] = {}
    
    def create_recipe(self, name:str, ingredients:list[str]):
        if name not in self.ricettario:
           self.ricettario[name] = ingredients 
           return self.ricettario
        else:
            return "ERR F.CREATE RECIPE - esiste già"
        
    def add_ingredient(self, recipe_name:str, ingredient:str): 
        
        if recipe_name in self.ricettario:
            if ingredient not in self.ricettario[recipe_name]:
                self.ricettario[recipe_name].append(ingredient)
                ingredienti = self.ricettario[recipe_name]
                return {recipe_name: ingredienti}
            else:
                print ("ERRORE - ingrediente già presente")
        else:
            print ("ERR F.ADD INGREDIENT - ricetta non esistente")
    
    def remove_ingredient(self, recipe_name:str, ingredient:str): 
        if recipe_name in self.ricettario:
            if ingredient in self.ricettario[recipe_name]:
                self.ricettario[recipe_name].remove(ingredient)
                ingredienti = self.ricettario[recipe_name]
                return {recipe_name: ingredienti}
            else:
                print ("ERR REMOVE - l'ingrediente non esiste")
        else:
            print ("ERR F.REMOVE - la ricetta non esiste")  
            
    def update_ingredient(self, recipe_name:str, old_ingredient:str, new_ingredient:str): 
        if recipe_name in self.ricettario:
            if old_ingredient in self.ricettario[recipe_name]:
                indice = self.ricettario[recipe_name].index(old_ingredient)
                self.ricettario[recipe_name][indice] = new_ingredient
                ingredienti = self.ricettario[recipe_name]
                return {recipe_name: ingredienti}
            else:
                print ("ERR F.REMOVE - l'ingrediente non esiste")
        else:
            print ("ERR F.REMOVE - la ricetta non esiste")  
    
    def list_recipes(self):
        return list(self.ricettario.keys() )
        
    def list_ingredients(self, recipe_name:str): 
        if recipe_name in self.ricettario:
            return self.ricettario[recipe_name]
        else:
            print("ERR F.LIST INGREDIENTS- la ricetta non esiste")
    
    def search_recipe_by_ingredient(self, ingredient: str):
        ricette_con_ingrediente: dict[str, list[str]] = {}
        
        for nome, ingredienti in self.ricettario.items():
            if ingredient in ingredienti:
                ricette_con_ingrediente[nome] = ingredienti
        if ricette_con_ingrediente:
            return ricette_con_ingrediente
        else:
            return f"F. SEARCH RECIPE - Nessuna ricetta contiene l'ingrediente."

###PRINT_SEQ###
def print_seq(): 
    
    print("Sequenza a):")
    # SCRIVI QUI IL TUO CICLO
    num:int = 1
    for i in range(7):
        print (num)
        num+=1

    print("\nSequenza b):")
    # SCRIVI QUI IL TUO CICLO
    num:int = 3
    for i in range(5):
        print(num)
        num+=5

    print("\nSequenza c):")
    # SCRIVI QUI IL TUO CICLO
    num:int = 20
    for i in range(6):
        print(num)
        num-=6

    print("\nSequenza d):")
    # SCRIVI QUI IL TUO CICLO
    num:int = 19
    for i in range(5):
        print(num)
        num+=8
        
###MOVIE###
class Movie():
#INIT
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self):
        if self.is_rented == False:
            self.is_rented = True
        else:
            print (f"Il film {repr(self.title)} è già noleggiato.")
    
    def return_movie(self):
        if self.is_rented == True:
            self.is_rented = False
        else:
            print (f"Il film {repr(self.title)} non è attualmente noleggiato.")

class Customer():
#INIT
    def __init__(self, customer_id: str, name: str):
        self.custumoer_id = customer_id
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie: Movie):
        if not movie.is_rented:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print (f"Il film {repr(movie.title)} è già noleggiato.")

    def return_movie(self, movie: Movie): 
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            print (f"Il film {repr(movie.title)} non è stato noleggiato da questo cliente.")
            
class VideoRentalStore():
#INIT
    def __init__(self):
        self.movies: dict [str,Movie] = {}
        self.customers: dict [str, Customer] = {}
        
    def add_movie(self, movie_id: str, title: str, director: str): 
        if movie_id not in self.movies: 
            self.movies[movie_id] = Movie (movie_id, title, director) 
        else:
            print (f"Il film con ID {movie_id} esiste già.")
            
    def register_customer(self, customer_id: str, name: str): 
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer (customer_id, name)
        else:
            print (f"Il cliente con ID {customer_id} è già registrato.")
            
    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies: 
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print (f"Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str): 
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print (f"Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str): 
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies 
        else:
            print (f"Cliente non trovato.")
            return []
        
###CHIAVE_VALORE###
from typing import Any
def trova_chiave_per_valore(dizionario: dict[Any, Any], valore: int) -> str:
    # cancella pass e scrivi il tuo codice
    for chiave,val in dizionario.items():
        if val == valore:
            return chiave
        
###VEICOLI###

class Veicolo():
#INIT
    def __init__(self, marca:str, modello:str, anno:int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
#BODY
    def descrivi_veicolo(self):
        print (f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
        
class Auto(Veicolo):
#INIT
    def __init__(self, marca: str, modello: str, anno: int, numero_porte:int):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
 
    def descrivi_veicolo(self):
        print (f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")
        

class Moto(Veicolo):
#INIT
    def __init__(self, marca: str, modello: str, anno: int, tipo:str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
        
    def descrivi_veicolo(self): 
        print (f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")

###TRASHOLD###
def sum_above_threshold(numbers: list[int], trashold:int) -> int:
    # prima cancella ... e definisci parametro e tipo per il dato mancante
    # successivamente cancella pass e scrivi il tuo codice
    somma:int = 0
    for i in numbers:
        if i > trashold:
            somma += i
    return somma

###TRANSFORM###
def transform(x: int) -> int:
    # cancella pass e scrivi il tuo codice
    if x%2 ==0:
        x//=2
    else:
        x = (x*3)-1
    return x

###CHECK_COMBINATION###
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    ok: str = "Operazione permessa"
    no:str = "Operazione negata"
    if conditionA or (conditionB and conditionC):
        return ok
    else:
        return no
    
###LISTA_TO_DICT###
def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codie
    dizionario:dict [str,list[int]] = {}
    for chiave, valore in tuples:
        if chiave not in dizionario:     
            dizionario[chiave] = [valore]
        else:
            dizionario[chiave].append(valore)
    return dizionario

###FILTRA_MAPPA###
def filtra_e_mappa(prodotti: dict[str,float]) -> dict[str,float]:
    # cancella pass e scrivi il tuo codice
    nuovodic:dict[str,float] = {}
    for prodotto in prodotti:
        if prodotti[prodotto] > 20:
            nuovodic[prodotto] = prodotti[prodotto] * 0.9
    return nuovodic

###MERGE_DICTIONARIES###
def merge_dictionaries(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    dictunico: dict[str, int] = {}
    
    # Aggiungi tutte le coppie chiave-valore da dict1 a dictunico
    for chiave1, valore1 in dict1.items():
        dictunico[chiave1] = valore1
    
    # Aggiorna dictunico con le coppie chiave-valore di dict2
    for chiave2, valore2 in dict2.items():
        if chiave2 in dictunico:
            dictunico[chiave2] += valore2
        else:
            dictunico[chiave2] = valore2
    
    return dictunico


###FREQUENCY###
def frequency_dict(elements: list[str]) -> dict[str,int]:
    # cancella pass e scrivi il tuo codice
    lista:dict[str,int] = {}
    
    for elemento in elements:
        if not elemento in lista:
            lista[elemento] = 1
        else:
            lista[elemento] +=1
    return lista

###LIBRARY###
from typing import Any
class Book():
#INIT
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool = False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
#BODY
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
        else:
            raise ValueError("Book is already borrowed")
        
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            raise ValueError(f"Il libro '{self.title}' non è attualmente in prestito.")
        
class Member():
#INIT
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []
#BODY        
    def borrow_book(self, book: Book) -> None:
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print (f"Book is already borrowed")
            
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise ValueError("Book not borrowed by this member")
               
class Library:
#INIT
    def __init__ (self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
        
    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id not in self.books:
            self.books[book_id] = Book (book_id, title, author)
        else:
            raise ValueError(f"Il libro con ID '{book_id}' esiste già nella biblioteca.")
            
    def register_member(self, member_id:str, name: str):
        if member_id not in self.members:
            self.members[member_id] = Member (member_id, name)
        else:
            raise ValueError(f"Il membro con ID '{member_id}' esiste già nella biblioteca.")
        
    def borrow_book(self, member_id: str, book_id: str): 
        if member_id in self.members:
            if book_id in self.books:
                self.members[member_id].borrow_book(self.books[book_id])
            else:
                raise ValueError (f"Book not found")
        else:
            raise ValueError("Member not found")
        
    def return_book(self, member_id: str, book_id: str):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError(f"Book with ID '{book_id}' not found")
        
        self.members[member_id].return_book(self.books[book_id])
    
    def get_borrowed_books(self, member_id:str) -> list[str]:
        if member_id not in self.members:
            raise ValueError("Member not found")
        
        return [book.title for book in self.members[member_id].borrowed_books]
    
    ###CLASSIFICA_NUMERI###
    def classifica_numeri(lista: int) -> dict[str,list[int]]:
    # cancella pass e scrivi il tuo codice
    pari:list[int] = []
    dispari:list[int] = []
    numeri:dict[str,list[int]] = {"pari":pari, "dispari": dispari}
    for i in lista:
        if i%2==0:
            pari.append(i)
        else:
            dispari.append(i)
    return numeri

