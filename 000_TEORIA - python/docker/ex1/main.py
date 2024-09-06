import os
from file_search import cerca_stringa_in_file_system
from utilities import verifica_directory

# IMMISSIONE DEI PARAMETRI
sRoot = input("Inserisci la root directory: ")
sStringaDaCercare = input("Inserisci la stringa da cercare: ")
sOutDir = input("Inserisci la dir di output: ")

# Verifica se la directory di input esiste
if not os.path.isdir(sRoot):
    print("La directory specificata non esiste.")
    exit()

# Verifica e crea directory di output
verifica_directory(sOutDir)

# Avvia la ricerca della stringa nei file
cerca_stringa_in_file_system(sRoot, sStringaDaCercare, sOutDir)
