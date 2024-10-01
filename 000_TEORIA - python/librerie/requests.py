import requests
from requests_oauthlib import OAuth1  # Necessaria per l'autenticazione OAuth

# 1. Richieste HTTP

# GET: Ottenere dati da un server
response = requests.get('https://api.example.com/data')
print("GET Status Code:", response.status_code)

# POST: Inviare dati a un server
response = requests.post('https://api.example.com/data', data={'key': 'value'})
print("POST Response:", response.text)

# PUT: Aggiornare dati esistenti
response = requests.put('https://api.example.com/data/1', data={'key': 'new_value'})
print("PUT Status Code:", response.status_code)

# DELETE: Eliminare dati
response = requests.delete('https://api.example.com/data/1')
print("DELETE Status Code:", response.status_code)

# PATCH: Aggiornare parzialmente i dati
response = requests.patch('https://api.example.com/data/1', data={'key': 'updated_value'})
print("PATCH Status Code:", response.status_code)

# HEAD: Ottenere solo gli header della risposta
response = requests.head('https://api.example.com/data')
print("HEAD Headers:", response.headers)

# 2. Parametri e Dati

# Parametri di query nella richiesta GET
response = requests.get('https://api.example.com/data', params={'key': 'value'})
print("GET with Params Response:", response.text)

# Dati nel corpo della richiesta POST in formato JSON
response = requests.post('https://api.example.com/data', json={'key': 'value'})
print("POST with JSON Response:", response.text)

# 3. Gestione delle Risposte

# Codice di stato della risposta
print("Response Status Code:", response.status_code)

# Contenuto della risposta (in formato stringa)
content = response.text
print("Response Content:", content)

# Header della risposta
headers = response.headers
print("Response Headers:", headers)

# 4. Gestione degli Errori

try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Solleva un'eccezione per codici di stato 4xx e 5xx
except requests.exceptions.HTTPError as err:
    print(f"Errore HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Errore di rete: {err}")

# 5. Autenticazione

# Esempio di autenticazione Basic
response = requests.get('https://api.example.com/data', auth=('username', 'password'))
print("Basic Auth Response:", response.text)

# Esempio di autenticazione OAuth
auth = OAuth1('client_key', 'client_secret', 'resource_owner_key', 'resource_owner_secret')
response = requests.get('https://api.example.com/data', auth=auth)
print("OAuth Response:", response.text)

# 6. Gestione delle Sessioni

# Creazione di una sessione
session = requests.Session()
session.get('https://api.example.com/data')  # Richiesta GET
response = session.post('https://api.example.com/data', data={'key': 'value'})  # Richiesta POST
print("Session POST Response:", response.text)

# 7. Timeout

# Impostare un timeout di 5 secondi per la richiesta
try:
    response = requests.get('https://api.example.com/data', timeout=5)
    print("Response with Timeout:", response.text)
except requests.exceptions.Timeout:
    print("La richiesta è scaduta.")

# 8. Supporto per i file

# Inviare un file in una richiesta POST
with open('file.txt', 'rb') as f:
    response = requests.post('https://api.example.com/upload', files={'file': f})
    print("File Upload Response:", response.text)

# 9. Supporto per HTTPS

# Esempio di richiesta HTTPS
response = requests.get('https://secure.api.example.com/data')
print("HTTPS Response:", response.text)

# 10. JSON

# Invio di dati in formato JSON
response = requests.post('https://api.example.com/data', json={'key': 'value'})
print("JSON POST Response:", response.json())  # Ricezione e decodifica del JSON
