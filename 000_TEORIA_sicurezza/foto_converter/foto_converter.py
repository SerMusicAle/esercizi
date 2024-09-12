def png_to_binary(file_path):
    
    # Apri il file PNG in modalità binaria (rb = read binary)
    with open(file_path, 'rb') as file:
        # Leggi tutto il contenuto del file
        binary_data = file.read()
        
    # Converti i dati binari in una stringa binaria (0 e 1)
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    
    return binary_string

# Esempio di utilizzo
file_path = 'roma.png'  # Inserisci qui il percorso del tuo file PNG
binary_output = png_to_binary(file_path)
print(binary_output)
