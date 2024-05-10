"""
    ENTRO LE 23.59 del 16 05 2024
    
    ZOO
    
    RECINTI
    OK area float, 
    OK temperatura float
    OK habitat stringa
    lista di animali che puo contenere
    -- describe_zoo come __str__ 
    OK    stampa tutti gli zookeeper, 
    OK    stampa caratteristiche di ogni recinto, con animali
    OK habitat è una stringa
    OK add_animal inserisce un animale nel recinto che rispetta l'habitat e le necessità come le dimensioni
    lo spazio deve esser sufficiente
    OK remove_animal. se sta nel recinto. si ripristina l'area rimasta

    ANIMALE
    OK animale ha caratteristiche, habitat preferito, stato salute
       finire alla terza cifra per la salute
        
    GUARDIANI
    OK nome, surname, id, 
    OK ID è una stringa
    -- nutrire:
        salute incrementa di 1% ad ogni nutrimento
        dimensioni dell'animale incrementano del 2% ad ogni nutrimento. 
        verifica se lo spazio è sufficiente a farlo mangiara 
    -- pulire
        torna un float come tempo necessario a pulire
        l'area occupata / area rimasta
    ?? svolgere compiti



    CONSEGNA
    file zip (nome e cognome), contenente il file zoo.py
    compilare come con code runner, senza dati in input
    describe zoo è l'unico print. gli altri sono tutti controlli
"""

#CLASS ANIMAL
class Animal:
    pass

    #INIT
    def __init__(self, name, species, age, height, width, preffered_habitat):
        
        #DEC
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preffered_habitat = preffered_habitat
        self.health = round(100 * (1/age), 3)

        #BODY
        self.volume = self.height*self.width

#CLASS FENCE
class Fence:
    pass

    #INIT
    def __init__(self, area:float, temperature: float, habitat:str, animals=None):
        
        self.area = area
        self. temperature = temperature
        self.habitat = habitat
        self.area_cleaned = area

        if animals is None:
            self.animals = []
        else:
            self.animals = animals
    
    #ADD ANIMAL


####### inserisci condizione di spazio
    
    def add_animal(self, animal: Animal):
        if self.area_cleaned >= animal.volume and animal.preffered_habitat == self.habitat:
            self.animals.append(animal)
            self.area_cleaned -= animal.volume

    #REMOVE ANIMAL

###inserisci agiornamento spazio

    def remove_animal(self, animal:Animal):
        
        if animal in self.animals:
            self.animals.remove(animal)
            self.area -= animal.volume



#CLASS ZOOKEEPER
class Zookeeper:
    
    #INIT
    def __init__(self, name, surname, id:str):
        self.name = name
        self.surname = surname
        self.id = id

############################################ da finire ###################################
    #SOMETHING TO EAT
    def feed(self, animal:Animal):
        for fence in Zoo.fences:
            for animal in Fence.animals:
                height = animal.height * 1.02
                width = animal.width * 1.02
                volume = height * width
 
                if Fence.area >= volume:
                    animal.height = height
                    animal.width = width
                    animal.volume= volume

                fence.

            

    #CLEAN ENCLOSURE
    def clean(self, fence):
        tempo = (fence.area - fence.area_cleaned) /fence.area_cleaned


#CLASS ZOO
class Zoo:

    #INIT
    def __init__(self, fences=None, zoo_keepers=None ):

        #verify the presence of zoo_keepers        
        if zoo_keepers is None:
            self.zoo_keepers = []
        else:
            self.zoo_keepers = zoo_keepers

        #verify the presence of fences
        if fences is None:
            self.fences = []
        else:
            self.fences = fences
        
        #add new fence
        def add_fence(self, fence):
            self.fence.append(fence)
        
        #remove some fence
        def remove_fence(self, fence):
            if fence in self.fence:
                self.fence.remove(fence)
        
        #così.... tanto per ribadire...
        #add zoo_keeper
        def add_zoo_keeper(self, zoo_keeper):
            self.zoo_keepers.add(zoo_keeper)
        
        #remove zoo_keeper
        def remove_zoo_keeper(self, zoo_keeper):
            if zoo_keeper in self.zoo_keepers:
                self.zoo_keepers.remove(zoo_keeper)


    #DESCRIBE
    def describe_zoo(self):
        zookeepers_info = "\n".join(str(keeper) for keeper in self.zoo_keepers)
        fences_info = "\n\n".join(str(fence) for fence in self.fences)
        animals_info = "\n\n".join(str(animal) for animal in self.animals)
        return f"lo Zoo è composto da: \n\n i seguenti guardiani: \n {zookeepers_info} \n  
                che controllano i seguenti recinti: \n {fences_info} \
                che contengono i seguenti animali: \n {animals_info}"


