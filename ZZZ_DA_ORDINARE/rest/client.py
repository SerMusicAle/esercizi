import json
import requests

#URL ------------------------------------------------------------------------------------------------------------------------------------------
base_url = "http://127.0.0.1:8080"


#FUNZIONI ------------------------------------------------------------------------------------------------------------------------------------------
def RichiediDatiCittadino():
    nome = input("inserisci nome cittadino: ")
    cognome = input("inserisci cognome cittadino: ")
    dataNascita = input("inserisci la data di nascita del cittadino: ")
    codFiscale = input("inserisci il codice fiscale: ")
    jRequest = {"nome": nome, "cognome": cognome, "dataNascita": dataNascita, "codiceFiscale": codFiscale}
    return jRequest

def CaricaDatiCittadino():
    codFiscale = input("inserisci il codice fiscale: ")


    try:
        response = requests.get(api_url, params={"codiceFiscale": codFiscale})
        if response.status_code == 200:
            djson = response.json()
            print("I dati dell'utente sono:")
            print(f"Nome: {djson['nome']}, Cognome: {djson['cognome']}, Data di Nascita: {djson['dataNascita']}, Codice Fiscale: {djson['codiceFiscale']}")
        else:
            print("Nessun cittadino trovato con il codice fiscale fornito.")
    except requests.exceptions.RequestException as e:
        print("Problemi di comunicazione con il server:", e)

def CreaInterfaccia():
    print("operazioni disponibili:")
    print("1. inserisci cittadino")
    print("2. richiedi dati cittadino")
    print("3. modifica dati cittadino")
    print("4. Elimina cittadino")
    print("- exit")


#CHIAMATE ------------------------------------------------------------------------------------------------------------------------------------------
CreaInterfaccia()
sOper = input("Seleziona operazione: ")
while sOper != "exit":
    if sOper == "1":
        jsonDataRequest = RichiediDatiCittadino()
        api_url = base_url + "/add_cittadino"
        try:
            #invio dati alserver
            response = requests.post(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-type"])
            data1 = response.json()
            print(data1)
        except requests.exceptions.RequestException as e:
            print("Problemi di comunicazione con il server:", e)

    if sOper == "2":
        CaricaDatiCittadino()


#MAIN ------------------------------------------------------------------------------------------------------------------------------------------
    CreaInterfaccia()
    sOper = input("Seleziona operazione: ")
