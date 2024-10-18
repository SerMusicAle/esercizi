# client.py

# LIBRERIE PER COMUNICARE CON LE API CON RICHIESTE GET POST PUT E DELETE
import requests, json, sys

# VARIABILE
VAR_base_url = "http://127.0.0.1:8080"

# RICHIESTA DATI CITTADINO DA UTENTE E CREAZIONE DEL DIZIONARIO
def GetDatiCittadino():
    VAR_nome = input("Inserisci il nome: ")
    VAR_cognome = input("Inserisci il cognome: ")
    VAR_data_nascita = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    VAR_cod_fiscale = input("Inserisci il codice fiscale: ")
    VAR_dati_cittadino = {
        "nome": VAR_nome, 
        "cognome": VAR_cognome, 
        "dataNascita": VAR_data_nascita, 
        "codFiscale": VAR_cod_fiscale
    }
    return VAR_dati_cittadino

# RICHIESTA CODICE FISCALE
def GetCodiceFiscale():
    VAR_codice_fiscale = input('Inserisci codice fiscale: ')
    return {"codFiscale": VAR_codice_fiscale}

def dati_utente():
    VAR_user = input("inserisci username")
    VAR_psw = input("inserisci password")
    return {"username": VAR_user, "password": VAR_psw}

def verifica_accesso(dati):
    VAR_accesso = requests.post(VAR_base_url + "/verifica_accesso", json=dati)
    return VAR_accesso.status_code == 200

def EseguiOperazione(VAR_i_operazione, VAR_servizio, VAR_dati_da_inviare):
    VAR_response = None
    
    try:
        if VAR_i_operazione == 1:
            VAR_response = requests.post(VAR_servizio, json=VAR_dati_da_inviare)
        elif VAR_i_operazione == 2:
            VAR_response = requests.get(VAR_servizio)
        elif VAR_i_operazione == 3:
            VAR_response = requests.put(VAR_servizio, json=VAR_dati_da_inviare)
        elif VAR_i_operazione == 4:
            VAR_response = requests.delete(VAR_servizio, json=VAR_dati_da_inviare)

        else:
            print("Operazione non valida.")
            return
        
        # Sapendo che il 200 è positivo
        if VAR_response.status_code == 200:
            print(VAR_response.json())
        else:
            print("Attenzione, errore " + str(VAR_response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova più tardi.")


while True:
    # Richiesta di accesso
    print("Accedi al sistema.")
    credenziali = dati_utente()

    if not verifica_accesso(credenziali):
        print("Accesso negato! Riprova.")
        continue

    print("Accesso consentito!")

    while True:
        print("\nOperazioni disponibili:")
        print("1. Inserisci cittadino")
        print("2. Richiesta cittadino")
        print("3. Modifica cittadino")
        print("4. Elimina cittadino")
        print("5. Esci")

        try:
            VAR_i_operazione = int(input("Cosa vuoi fare? "))
        except ValueError:
            print("Inserisci un numero valido!")
            continue

        if VAR_i_operazione == 1:
            print("Aggiunta cittadino")
            VAR_api_url = VAR_base_url + "/add_cittadino"
            VAR_json_data_request = GetDatiCittadino()
            EseguiOperazione(1, VAR_api_url, VAR_json_data_request)

        elif VAR_i_operazione == 2:
            print("Richiesta dati cittadino")
            VAR_api_url = VAR_base_url + "/read_cittadino"
            VAR_json_data_request = GetCodiceFiscale()
            EseguiOperazione(2, VAR_api_url + "/" + VAR_json_data_request['codFiscale'], None)

        elif VAR_i_operazione == 3:
            print("Modifica cittadino")
            VAR_api_url = VAR_base_url + "/update_cittadino"
            VAR_json_data_request = GetDatiCittadino()
            EseguiOperazione(3, VAR_api_url, VAR_json_data_request)

        elif VAR_i_operazione == 4:
            print("Eliminazione cittadino")
            VAR_api_url = VAR_base_url + "/elimina_cittadino"
            VAR_json_data_request = GetCodiceFiscale()
            EseguiOperazione(4, VAR_api_url, VAR_json_data_request)

        elif VAR_i_operazione == 5:
            print("Buona giornata!")
            sys.exit()

        else:
            print("Operazione non disponibile, riprova.")

"""
#LIBRERIE PER COMUNICARE CON LE API CON RICHIESTE GET POST PUT E DELETE
import requests, json, sys

#VARIABILE
base_url = "http://127.0.0.1:8080"

#RICHIESTA DATI CITTADINO DA UTENTE E CREAZIONE DEL DIZIONARIO
def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF
    }
    return datiCittadino

#RICHIESTA CODICE FISCALE
def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codFiscale": cod}


def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)
#sapendo che il 200 è positivo
        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova più tardi.")


while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        print("Aggiunta cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        EseguiOperazione(1, api_url, jsonDataRequest)

    # Richiesta dati cittadino
    elif iOper == 2:
        print("Richiesta dati cittadino")
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = GetCodicefiscale()
        EseguiOperazione(2, api_url + "/" + jsonDataRequest['codFiscale'],None)

    elif iOper == 3:
        print("Modifica cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = GetDatiCittadino()
        EseguiOperazione(3, api_url, jsonDataRequest)


    elif iOper == 4:
        print("Eliminazione cittadino")
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = GetCodicefiscale()
        EseguiOperazione(4, api_url, jsonDataRequest)

    elif iOper == 5:
        print("Buona giornata!")
        sys.exit()

    else:
        print("Operazione non disponibile, riprova.")


"""