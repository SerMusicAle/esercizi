"""
    Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. 
    Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.
    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - list_recipes(): Elenca tutte le ricette esistenti.
    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
For example:

Test	Result
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
"""    

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

For example:

Test	Result
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
    
