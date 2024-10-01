# IMPORTAZIONI ------------------------------------------------------------------------------------------------------------------------------------------ 
import json  # Importa la libreria per la manipolazione dei file JSON (JavaScript Object Notation), un formato per lo scambio di dati.
import requests  # Importa la libreria per effettuare richieste HTTP, consentendo al programma di comunicare con server web.

# URL ------------------------------------------------------------------------------------------------------------------------------------------ 
base_url = "http://127.0.0.1:8080"  # Imposta l'URL base per le richieste al server locale (127.0.0.1 è l'indirizzo IP per il computer locale).

# FUNZIONI ------------------------------------------------------------------------------------------------------------------------------------------ 

def RichiediDatiCittadino():
    # Richiesta dei dati del cittadino all'utente
    nome = input("inserisci nome cittadino: ")  # Chiede il nome del cittadino
    cognome = input("inserisci cognome cittadino: ")  # Chiede il cognome del cittadino
    dataNascita = input("inserisci la data di nascita del cittadino: ")  # Chiede la data di nascita
    codFiscale = input("inserisci il codice fiscale: ")  # Chiede il codice fiscale
    
    # Creazione di un dizionario con i dati inseriti
    jRequest = {
        "nome": nome,  # Aggiunge il nome al dizionario
        "cognome": cognome,  # Aggiunge il cognome al dizionario
        "dataNascita": dataNascita,  # Aggiunge la data di nascita al dizionario
        "codiceFiscale": codFiscale  # Aggiunge il codice fiscale al dizionario
    }
    return jRequest  # Restituisce il dizionario creato

def CaricaDatiCittadino():
    # Richiesta del codice fiscale per caricare i dati del cittadino
    codFiscale = input("inserisci il codice fiscale: ")  # Chiede il codice fiscale

    try:
        # Invia una richiesta GET per ottenere i dati del cittadino
        response = requests.get(base_url + "/get_cittadino", params={"codiceFiscale": codFiscale})  # Effettua la richiesta GET

        # Verifica se la risposta ha avuto successo
        if response.status_code == 200:  # 200 indica che la richiesta è andata a buon fine
            djson = response.json()  # Converte la risposta JSON in un dizionario
            print("I dati dell'utente sono:")  # Messaggio di output
            print(f"Nome: {djson['Data']['nome']}, Cognome: {djson['Data']['cognome']}, Data di Nascita: {djson['Data']['dataNascita']}, Codice Fiscale: {djson['Data']['codiceFiscale']}")
        else:
            print("Nessun cittadino trovato con il codice fiscale fornito.")  # Messaggio di errore
    except requests.exceptions.RequestException as e:
        # Gestione degli errori di comunicazione con il server
        print("Problemi di comunicazione con il server:", e)

def ModificaDatiCittadino():
    # Richiesta del codice fiscale per modificare i dati del cittadino
    codFiscale = input("inserisci il codice fiscale del cittadino da modificare: ")  # Chiede il codice fiscale

    try:
        # Carica i dati correnti
        response = requests.get(base_url + "/get_cittadino", params={"codiceFiscale": codFiscale})  # Effettua la richiesta GET
        if response.status_code == 200:  # Se la risposta è OK
            djson = response.json()['Data']  # Ottiene i dati attuali
            print("Dati attuali:")  # Messaggio di output
            print(f"Nome: {djson['nome']}, Cognome: {djson['cognome']}, Data di Nascita: {djson['dataNascita']}, Codice Fiscale: {djson['codiceFiscale']}")

            # Richiesta dei nuovi dati
            nome = input("Nuovo nome (premi invio per mantenere attuale): ")  # Chiede un nuovo nome
            cognome = input("Nuovo cognome (premi invio per mantenere attuale): ")  # Chiede un nuovo cognome
            dataNascita = input("Nuova data di nascita (premi invio per mantenere attuale): ")  # Chiede una nuova data di nascita

            # Aggiorna solo i campi forniti
            if nome:  # Se è stato fornito un nuovo nome
                djson['nome'] = nome  # Aggiorna il nome
            if cognome:  # Se è stato fornito un nuovo cognome
                djson['cognome'] = cognome  # Aggiorna il cognome
            if dataNascita:  # Se è stata fornita una nuova data di nascita
                djson['dataNascita'] = dataNascita  # Aggiorna la data di nascita
            
            # Invia la richiesta di modifica al server
            response = requests.post(base_url + "/update_cittadino", json=djson)  # Invia i dati modificati
            if response.status_code == 200:  # Se la modifica è andata a buon fine
                print("Dati modificati con successo.")  # Messaggio di conferma
            else:
                print("Errore nella modifica dei dati:", response.json())  # Messaggio di errore
        else:
            print("Nessun cittadino trovato con il codice fiscale fornito.")  # Messaggio di errore
    except requests.exceptions.RequestException as e:
        print("Problemi di comunicazione con il server:", e)  # Gestione degli errori

def EliminaCittadino():
    # Richiesta del codice fiscale per eliminare il cittadino
    codFiscale = input("inserisci il codice fiscale del cittadino da eliminare: ")  # Chiede il codice fiscale

    try:
        # Invia una richiesta DELETE al server
        response = requests.delete(base_url + "/delete_cittadino", json={"codiceFiscale": codFiscale})  # Effettua la richiesta DELETE

        # Verifica la risposta
        if response.status_code == 200:  # Se la cancellazione è andata a buon fine
            print("Cittadino eliminato con successo.")  # Messaggio di conferma
        else:
            print("Errore nell'eliminazione del cittadino:", response.json())  # Messaggio di errore
    except requests.exceptions.RequestException as e:
        print("Problemi di comunicazione con il server:", e)  # Gestione degli errori

def CreaInterfaccia():
    # Visualizzazione delle operazioni disponibili
    print("operazioni disponibili:")  # Messaggio di output
    print("1. inserisci cittadino")  # Opzione per inserire un cittadino
    print("2. richiedi dati cittadino")  # Opzione per richiedere dati di un cittadino
    print("3. modifica dati cittadino")  # Opzione per modificare i dati di un cittadino
    print("4. elimina cittadino")  # Opzione per eliminare un cittadino
    print("- exit")  # Opzione per uscire

# CHIAMATA FUNZIONE A TERMINALE ------------------------------------------------------------------------------------------------------------------------------------------ 
CreaInterfaccia()  # Mostra le operazioni disponibili

# RICHIESTA INPUT DA TERMINALE ------------------------------------------------------------------------------------------------------------------------------------------ 
sOper = input("Seleziona operazione: ")  # Chiede all'utente quale operazione eseguire
while sOper != "exit":  # Continua finché l'utente non decide di uscire
    if sOper == "1":  # Se l'utente sceglie di inserire un cittadino
        jsonDataRequest = RichiediDatiCittadino()  # Richiama la funzione per ottenere i dati del cittadino
        api_url = base_url + "/add_cittadino"  # Imposta l'URL per aggiungere un cittadino
        try:
            response = requests.post(api_url, json=jsonDataRequest)  # Invia i dati al server
            
            # Elaborazione della risposta
            print(response.status_code)  # Stampa il codice di stato della risposta dal server
            print(response.headers["Content-type"])  # Stampa il tipo di contenuto della risposta
            data1 = response.json()  # Converte la risposta JSON in un dizionario
            print(data1)  # Stampa i dati ricevuti
        except requests.exceptions.RequestException as e:
            print("Problemi di comunicazione con il server:", e)  # Gestione degli errori

    elif sOper == "2":  # Se l'utente sceglie di richiedere i dati di un cittadino
        codiceFiscaleCittadino = input("inserisci il codice fiscale: ")  # Chiede il codice fiscale
        api_url = base_url + "/get_cittadino"  # Imposta l'URL per ottenere i dati
        try:
            # Invia dati al server per ottenere i dati del cittadino
            response = requests.get(api_url, params={"codiceFiscale": codiceFiscaleCittadino})  # Effettua la richiesta
            
            # Elaborazione della risposta
            if response.status_code == 200:  # Se la risposta è OK
                djson = response.json()  # Converte la risposta JSON in un dizionario
                print("I dati dell'utente sono:")  # Messaggio di output
                print(f"Nome: {djson['Data']['nome']}, Cognome: {djson['Data']['cognome']}, Data di Nascita: {djson['Data']['dataNascita']}, Codice Fiscale: {djson['Data']['codiceFiscale']}")
            else:
                print("Nessun cittadino trovato con il codice fiscale fornito.")  # Messaggio di errore
        except requests.exceptions.RequestException as e:
            print("Problemi di comunicazione con il server:", e)  # Gestione degli errori

    elif sOper == "3":  # Se l'utente sceglie di modificare i dati di un cittadino
        ModificaDatiCittadino()  # Richiama la funzione per modificare i dati

    elif sOper == "4":  # Se l'utente sceglie di eliminare un cittadino
        EliminaCittadino()  # Richiama la funzione per eliminare il cittadino

    # RICHIAMATA INTERFACCIA
    CreaInterfaccia()  # Mostra di nuovo le operazioni disponibili
    sOper = input("Seleziona operazione: ")  # Richiede di nuovo l'input all'utente
