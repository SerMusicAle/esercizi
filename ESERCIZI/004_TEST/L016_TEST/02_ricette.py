"""
    utenti
    - creare ricette, 
    - modificare ricette, 
    - cercare ricette basate sugli ingredienti. 
    
    Classe:
    - RecipeManager:
        Gestisce tutte le operazioni legate alle ricette.
        Metodi:
        - create_recipe(name, ingredients): 
            Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
        - add_ingredient(recipe_name, ingredient): 
            Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
        - remove_ingredient(recipe_name, ingredient): 
            Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
        - update_ingredient(recipe_name, old_ingredient, new_ingredient): 
            Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
        - list_recipes(): 
            Elenca tutte le ricette esistenti.
        - list_ingredients(recipe_name): 
            Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
        - search_recipe_by_ingredient(ingredient): 
            Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
"""        

class RecipeManager():
    
    def __init__ (self):
        self.recipes: dict[str, list[str]] = {}
    
    #crea nuova ricetta
    def create_recipe(self,  name:str, ingredients:list[str]):
        if name in self.recipes.keys():
            return (f"la ricetta esiste già") 
        else:
            self.recipes[name] = ingredients 
            return {name: self.recipes[name]}
        
    #aggiungi ingrediente
    def add_ingredient(self,  recipe_name:str, ingredient:str):
        if recipe_name in self.recipes:
            if ingredient in self.recipes[recipe_name]: 
                return (f"l'ingrediente è già presente")
            self.recipes[recipe_name].append(ingredient)
            return {recipe_name: self.recipes[recipe_name]}
        else:
            return (f"la ricetta non esiste")
    
    #rimuovi ingrediente
    def remove_ingredient(self, recipe_name:str, ingredient:str):
        if recipe_name in self.recipes:
            if ingredient in self.recipes[recipe_name]: 
                self.recipes[recipe_name].remove (ingredient)
            return {recipe_name: self.recipes[recipe_name]}
        else:
            return (f"la ricetta non esiste")
    
    #sostituisci ingrediente
    def update_ingredient(self, recipe_name : str, old_ingredient : str, new_ingredient:str): 
        if recipe_name in self.recipes:
            if old_ingredient in self.recipes[recipe_name]:
                index = self.recipes[recipe_name].index(old_ingredient)
                self.recipes[recipe_name][index] = new_ingredient
            return {recipe_name: self.recipes[recipe_name]}
        else:
            return (f"la ricetta non esiste")
    
    #stampa ingredienti ricetta
    def list_ingredients (self, recipe_name:str):
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        else:
            return "Ricetta non trovata"
        """
        results = ""
            results += (f"Ricetta: {name}")
            results += (f"ingredienti: \n")
            elenco_puntato = [f"- {ingredient}" for ingredient in ingredients]
            results += (f"{', '.join (elenco_puntato)}")
            
        return results.strip()
        """

    
    #stampa ricette con un ingrediente
    def search_recipe_by_ingredient(self, ingredient:str):
        for recipe_name, ingredients in self.recipes.items():
            if ingredient in ingredients:
                return {recipe_name: self.recipes[recipe_name]}
        """
        results = ""
        for recipe_name, ingredients in self.recipes.items():
            if ingredient in ingredients:
                results += (f"Ricetta: {recipe_name}")
                results += (f"ingredienti: \n")
                elenco_puntato = [f"- {ingredient}" for ingredient in ingredients]
                results += "\n".join (elenco_puntato) + "\n\n"
        return results.strip()
        """
    #elenca ricette
    def list_recipes(self):
        return list(self.recipes.keys())
    
    
#TEST
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
