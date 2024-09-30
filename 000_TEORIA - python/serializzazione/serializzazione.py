# ==================== 1. Serializzazione e Deserializzazione con `pickle` (binario) ====================
import pickle

# Oggetto complesso da serializzare
my_data = {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# Serializzazione con `pickle` (in formato binario)
with open('data.pkl', 'wb') as file:
    pickle.dump(my_data, file)

# Deserializzazione con `pickle`
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
# Output: {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# ==================== 2. Serializzazione e Deserializzazione con `json` (testuale) ====================
import json

# Oggetto complesso da serializzare
my_data = {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# Serializzazione con `json` (in formato testuale)
with open('data.json', 'w') as file:
    json.dump(my_data, file)

# Deserializzazione con `json`
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)
# Output: {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# ==================== 3. Serializzazione e Deserializzazione con `marshal` (binario) ====================
import marshal

# Oggetto Python semplice
my_data = {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# Serializzazione con `marshal` (in formato binario)
with open('data.marshal', 'wb') as file:
    marshal.dump(my_data, file)

# Deserializzazione con `marshal`
with open('data.marshal', 'rb') as file:
    loaded_data = marshal.load(file)

print(loaded_data)
# Output: {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# ==================== 4. Serializzazione e Deserializzazione con `yaml` (testuale leggibile) ====================
import yaml

# Oggetto Python complesso
my_data = {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# Serializzazione con `yaml` (in formato testuale)
with open('data.yaml', 'w') as file:
    yaml.dump(my_data, file)

# Deserializzazione con `yaml`
with open('data.yaml', 'r') as file:
    loaded_data = yaml.load(file, Loader=yaml.FullLoader)

print(loaded_data)
# Output: {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# ==================== 5. Serializzazione e Deserializzazione con `pickle` su rete (socket) ====================

# -------- Server (riceve l'oggetto serializzato) --------
import pickle
import socket

# Configurazione del server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)

conn, addr = server_socket.accept()

# Ricezione dell'oggetto serializzato
data = conn.recv(4096)
obj = pickle.loads(data)  # Deserializzazione
print(obj)  # Output: Mostra l'oggetto ricevuto

conn.close()

# -------- Client (invia l'oggetto serializzato) --------
import pickle
import socket

# Oggetto complesso da inviare
my_data = {'nome': 'Mario', 'eta': 30, 'hobby': ['calcio', 'lettura', 'cucina']}

# Serializzazione dell'oggetto
data = pickle.dumps(my_data)

# Connessione al server e invio dei dati serializzati
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))
client_socket.sendall(data)

client_socket.close()
