# IMPORTAZIONI ------------------------------------------------------------------------------------------------------------------------------------------ 
from flask import Flask, request, json  # Importa il framework Flask e i moduli necessari per gestire le richieste HTTP e le risposte JSON.
                                            # Flask è un micro-framework per Python che facilita la creazione di applicazioni web.

from my_json import JsonSerialize, JsonDeserialize  # Importa funzioni personalizzate per gestire la serializzazione e deserializzazione dei dati JSON.
                                                     # Queste funzioni consentono di convertire oggetti Python in formato JSON e viceversa.

# percorso json
sFileAnagrafe = "./anagrafe.json"  # Definisce il percorso del file JSON che contiene i dati anagrafici.
                                      # Questo file verrà utilizzato per salvare e recuperare le informazioni sui cittadini.

# crea un'istanza del framework Flask per la configurazione HTTP
api = Flask(__name__)  # Crea un'applicazione Flask, che gestirà le richieste HTTP in entrata.

# DECORATORE CHE IMPOSTA RISPOSTE ALLA CHIAMATA CLIENT 
@api.route('/add_cittadino', methods=['POST'])  # Definisce una rotta (endpoint) per aggiungere un cittadino, utilizzando il metodo HTTP POST.
def GestisciAddCittadino():
    # Funzione per gestire la richiesta di aggiunta di un cittadino.
    
    # estrai i dati della richiesta HTTP
    content_type = request.headers.get('Content-Type')  # Ottiene il tipo di contenuto dalla richiesta (header).
    print("Ricevuta chiamata " + content_type)  # Stampa il tipo di contenuto ricevuto per il debug.

    # verifica se il tipo è json
    if content_type == "application/json":  # Controlla se il tipo di contenuto è JSON.
        try:
            # conversione in dizionario 
            jRequest = request.json  # Converte il corpo della richiesta in un dizionario Python.
            # ottiene codice fiscale dal dizionario
            sCodiceFiscale = jRequest["codiceFiscale"]  # Estrae il codice fiscale dal dizionario.
            print("Ricevuto " + sCodiceFiscale)  # Stampa il codice fiscale ricevuto.

            # carichiamo l'anagrafe, dizionario ottenuto dalla conversione del file json
            dAnagrafe = JsonDeserialize(sFileAnagrafe)  # Deserializza il file JSON in un dizionario Python.
            if sCodiceFiscale not in dAnagrafe:  # Controlla se il codice fiscale non è già presente nel dizionario.
                dAnagrafe[sCodiceFiscale] = jRequest  # Aggiunge il cittadino al dizionario usando il codice fiscale come chiave.
                JsonSerialize(dAnagrafe, sFileAnagrafe)  # Serializza il dizionario aggiornato nel file JSON.
                jResponse = {"Error": "000", "Msg": "ok"}  # Crea una risposta di successo.
                return json.dumps(jResponse), 200  # Restituisce la risposta con codice di stato 200 (OK).
            else:
                jResponse = {"Error": "001", "Msg": "codice fiscale già presente"}  # Risposta di errore se il codice fiscale è già presente.
                return json.dumps(jResponse), 400  # Restituisce la risposta con codice di stato 400 (Bad Request).
        except Exception as e:
            # Gestione degli errori in caso di eccezioni.
            return json.dumps({"Error": "003", "Msg": str(e)}), 400  # Restituisce un messaggio di errore con codice 400.
    else:
        return "Errore, formato non riconosciuto", 401  # Risposta per formato non supportato, con codice 401 (Unauthorized).

# DECORATORE PER RECUPERARE I DATI DEL CITTADINO
@api.route('/get_cittadino', methods=['GET'])  # Definisce una rotta per ottenere i dati di un cittadino, utilizzando il metodo HTTP GET.
def GetCittadino():
    # Funzione per gestire la richiesta di recupero dei dati di un cittadino.
    
    # prendi il codice fiscale dalla query string
    sCodiceFiscale = request.args.get('codiceFiscale')  # Ottiene il codice fiscale dalla query string della richiesta GET.
    print("Ricevuto codice fiscale: " + sCodiceFiscale)  # Stampa il codice fiscale ricevuto.

    # carichiamo l'anagrafe
    dAnagrafe = JsonDeserialize(sFileAnagrafe)  # Deserializza il file JSON in un dizionario Python.
    if sCodiceFiscale in dAnagrafe:  # Se il codice fiscale è presente nel dizionario.
        jResponse = {"Error": "000", "Msg": "ok", "Data": dAnagrafe[sCodiceFiscale]}  # Crea una risposta di successo con i dati del cittadino.
        return json.dumps(jResponse), 200  # Restituisce la risposta con codice di stato 200 (OK).
    else:
        jResponse = {"Error": "002", "Msg": "codice fiscale non trovato"}  # Risposta di errore se il codice fiscale non è trovato.
        return json.dumps(jResponse), 404  # Restituisce la risposta con codice di stato 404 (Not Found).

@api.route('/read_cittadion/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale)
    cittadino = cittadini.get(codice_fiscale)
    if cittadion:
        return jsonify({"Esito":"200","Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito":"404", "Msg": "Cittadino no trovato"}), 404
    
@api.route('/update_cittadino',methods=['POST'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        
        jsonReq = request.jsoncodice_fiscale = jsonReq.get ('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq.get

# AVVIO DELL'APPLICAZIONE
api.run(host="127.0.0.1", port=8080)  # Avvia il server Flask sull'indirizzo locale (localhost) e sulla porta 8080.
