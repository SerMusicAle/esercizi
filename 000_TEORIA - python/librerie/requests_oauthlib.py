from requests_oauthlib import OAuth1Session, OAuth2Session

# 1. Autenticazione OAuth 1.0

# Creare una sessione OAuth1
oauth1 = OAuth1Session(
    client_key='your_client_key',
    client_secret='your_client_secret',
    resource_owner_key='your_resource_owner_key',
    resource_owner_secret='your_resource_owner_secret'
)

# Eseguire una richiesta GET con OAuth1
response = oauth1.get('https://api.example.com/data')
print("OAuth1 GET Response:", response.json())

# 2. Autenticazione OAuth 2.0

# Creare una sessione OAuth2
oauth2 = OAuth2Session(
    client_id='your_client_id',
    token={'access_token': 'your_access_token', 'token_type': 'Bearer'}
)

# Eseguire una richiesta GET con OAuth2
response = oauth2.get('https://api.example.com/data')
print("OAuth2 GET Response:", response.json())

# 3. Flussi di Autenticazione (OAuth 2.0)

# Esempio di autorizzazione tramite Authorization Code Grant
authorization_url, state = oauth2.authorization_url('https://provider.com/oauth/authorize')

# Stampa l'URL di autorizzazione da visitare
print("Visita questo URL per autorizzare:", authorization_url)

# Supponiamo di ricevere il 'code' dal redirect
# code = 'authorization_code_received_after_redirect'
# token = oauth2.fetch_token('https://provider.com/oauth/token', authorization_response=redirect_response)

# Eseguire una richiesta dopo aver ottenuto il token
# response = oauth2.get('https://api.example.com/data')
# print("Authorized OAuth2 GET Response:", response.json())

# 4. Aggiornamento del Token

# Esempio di refresh del token
# new_token = oauth2.refresh_token('https://provider.com/oauth/token', refresh_token='your_refresh_token')
# oauth2.token = new_token
# response = oauth2.get('https://api.example.com/data')
# print("Refreshed OAuth2 GET Response:", response.json())

# 5. Gestione degli Errori

try:
    response = oauth1.get('https://api.example.com/data')
    response.raise_for_status()  # Solleva un'eccezione per codici di stato 4xx e 5xx
except requests.exceptions.HTTPError as err:
    print(f"Errore HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Errore di rete: {err}")
