"""
ES_ CONTO_BANCARIO
    ACCOUNT(
        account_id: str - identificatore univoco per l'account.
        balance: float - il saldo attuale del conto.
        )
    Metodi:
        deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
        get_balance(): restituisce il saldo corrente del conto.
        
    BANK(
        accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        )
    Metodi:
        create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
        deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
        get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
    
"""

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
        
bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())
"""    
TEST
    
    bank = Bank()
    account1 = bank.create_account("123")
    print(account1.get_balance())
    0
    bank = Bank()
    account1 = bank.create_account("123")
    bank.deposit("123",100)
    print(bank.get_balance("123"))
    100
    bank = Bank()
    account2 = bank.create_account("456")
    bank.deposit("456",200)
    print(bank.get_balance("456"))
"""
        