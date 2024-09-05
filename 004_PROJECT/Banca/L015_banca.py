class ContoBancario:

    total_accounts = 0
    definizione: str = "classe contobancario" 

    def __init__(self, iban, saldo, nome):
        self.iban = iban
        self.saldo = saldo
        self.nome = nome

        ContoBancario.total_accounts += 1
    
    def deposito(self, importo):
        self.saldo += importo
        print(f"{importo} depositato. Il nuovo saldo è {self.saldo}")
        
    def prelievo(self, importo):
        self.saldo -= importo
        print(f"{importo} prelevato. Il nuovo saldo è {self.saldo}")

    @classmethod
    def get_total_accounts(cls):
        print(f"Account totali creati: {cls.total_accounts}")

    @staticmethod
    def valida_account(iban):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print("IBAN valido")
            return True
        else:
            print("IBAN non valido")
            return False

# Creazione degli account
account1 = ContoBancario(1234567890, 0, "Alice")
account2 = ContoBancario(8765432109, 1000, "Bob")

# Operazioni sui conti
account1.deposito(6500)
account1.prelievo(3000)

account2.deposito(300)
account2.prelievo(300)

# Visualizzazione del numero totale di account
ContoBancario.get_total_accounts()

# Validazione degli IBAN
ContoBancario.valida_account(1234567890)
ContoBancario.valida_account("1234GGH")
