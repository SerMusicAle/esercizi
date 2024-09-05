import os

# Modifica questa stringa con il codice di connessione che vuoi cercare
search_strings = [
    'ib.connect(',
    'IB_HOST',
    'IB_PORT',
    'IB_CLIENT_ID'
]

def search_files_for_code(directory, search_strings):
    results = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    contents = f.read()
                    if any(search_string in contents for search_string in search_strings):
                        results.append(file_path)
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")
    
    return results

if __name__ == "__main__":
    root_directory = os.getcwd()  # Usa la cartella corrente
    matching_files = search_files_for_code(root_directory, search_strings)
    
    if matching_files:
        print("Found connection code in the following files:")
        for file in matching_files:
            print(file)
    else:
        print("No connection code found.")
