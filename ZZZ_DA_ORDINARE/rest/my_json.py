# IMPORTAZIONI ------------------------------------------------------------------------------------------------------------------------------------------
import json  # Importa la libreria per la manipolazione dei file JSON

def JsonSerialize(data, sFile):
    # Serializza un dizionario Python e lo scrive in un file JSON
    with open(sFile, "w") as write_file:  # Apre il file in modalità scrittura
        json.dump(data, write_file, indent=4)  # Scrive il dizionario nel file con indentazione

def JsonDeserialize(sFile):
    # Legge un file JSON e restituisce un dizionario Python
    with open(sFile, "r") as read_file:  # Apre il file in modalità lettura
        return json.load(read_file)  # Carica il contenuto del file come dizionario
