# Definizione della classe base
class BaseClass:
    def __init__(self, base_attribute):
        # Inizializza l'attributo base_attribute
        self.base_attribute = base_attribute

    def base_method(self):
        # Metodo della classe base che stampa l'attributo base_attribute
        print(f"Base method called. Base attribute: {self.base_attribute}")

    def method_to_override(self):
        # Metodo che può essere sovrascritto nelle classi derivate
        print("Method in BaseClass")

# Definizione della prima classe derivata che eredita da BaseClass
class DerivedClass1(BaseClass):
    def __init__(self, base_attribute, derived1_attribute):
        # Inizializza la parte della classe base
        super().__init__(base_attribute)
        # Inizializza l'attributo specifico di DerivedClass1
        self.derived1_attribute = derived1_attribute

    def derived1_method(self):
        # Metodo specifico di DerivedClass1
        print(f"Derived1 method called. Derived1 attribute: {self.derived1_attribute}")

    # Sovrascrive method_to_override della classe base
    def method_to_override(self):
        print("Method overridden in DerivedClass1")

# Definizione della seconda classe derivata che eredita da BaseClass
class DerivedClass2(BaseClass):
    def __init__(self, base_attribute, derived2_attribute):
        # Inizializza la parte della classe base
        super().__init__(base_attribute)
        # Inizializza l'attributo specifico di DerivedClass2
        self.derived2_attribute = derived2_attribute

    def derived2_method(self):
        # Metodo specifico di DerivedClass2
        print(f"Derived2 method called. Derived2 attribute: {self.derived2_attribute}")

    # Sovrascrive method_to_override della classe base
    def method_to_override(self):
        print("Method overridden in DerivedClass2")

# Esempio di utilizzo delle classi
if __name__ == "__main__":
    # Creazione di un'istanza della classe base
    base = BaseClass("Base Attribute")
    base.base_method()  # Chiamata del metodo base_method della classe base
    base.method_to_override()  # Chiamata del metodo method_to_override della classe base

    # Creazione di un'istanza della classe derivata 1
    derived1 = DerivedClass1("Base Attribute", "Derived1 Attribute")
    derived1.base_method()  # Chiamata del metodo base_method ereditato dalla classe base
    derived1.derived1_method()  # Chiamata del metodo specifico di DerivedClass1
    derived1.method_to_override()  # Chiamata del metodo method_to_override sovrascritto in DerivedClass1

    # Creazione di un'istanza della classe derivata 2
    derived2 = DerivedClass2("Base Attribute", "Derived2 Attribute")
    derived2.base_method()  # Chiamata del metodo base_method ereditato dalla classe base
    derived2.derived2_method()  # Chiamata del metodo specifico di DerivedClass2
    derived2.method_to_override()  # Chiamata del metodo method_to_override sovrascritto in DerivedClass2
