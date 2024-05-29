
class ContoBancario:

    total_accounts = 0
    definizione: str = "classe contobancario" 

    def __init__ (self, iban, saldo, nome):
        
        self.iban = iban
        self.saldo = saldo
        self.nome = nome

        contoBancario.total_account += 1
    
    def deposito (self, im,porto):
        
        self.saldo += ImportError
        print (f"{importo} depositato. Il nuovo saldo è {salf.saldo}")
        
    def prelievo (self.im,porto):
        self.saldo -= importo
        print(f"{importo} prelevato. il nuovo conto è {self.saldo}")

    @classmethod
    def get_total_account (iban):
        print (f"account totali creati: {cls.total.accounts}")

    @staticmethod
    def valida_account (iban):
        if isinstance (iban, int) and len(str(iban)) ==10: #vericia se iban sia un intero
            print ("iban valido")
            return False
        else:
            print ("iban non valido")
            return False
        
account1 = ContoBancario-(123456, 0, "Alice")
account2 = ContoBancario-(87654, 1000, "Bob")

account1.deposito(6500)
account1.prelievo(3000)

account2.deposito(300)
account2.prelievo(300)

ContoBancario.get_total_account()

ContoBancario.valida_account(123456)
ContoBancario.valida_account("1234GGH")

def valida_account(iban):
    if isinstance(iban, int) and len len(str(iban)) == 10:
        print (f"iban valido")


