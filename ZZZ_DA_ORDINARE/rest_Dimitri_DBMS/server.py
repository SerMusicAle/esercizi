# server.py

# librerie
# jsonify converte dizionari in JSON
# request gestisce i dati ricevuti
from flask import Flask, jsonify, request
from my_json import JsonDeserialize, JsonSerialize

# variabile che contienete istanza flask
VAR_applicazione_api = Flask(__name__)

# percorsi json
VAR_file_path = "anagrafe.json"
VAR_users_path = "utenti.json"

# carica il contenuto json dentro la variabile
VAR_cittadini = JsonDeserialize(VAR_file_path)
VAR_users = JsonDeserialize(VAR_users_path)

@VAR_applicazione_api.route('/verifica_accesso', methods=['POST'])
def verifica_accesso():
    VAR_dati_accesso = request.json
    VAR_email = VAR_dati_accesso.get('username')
    VAR_password = VAR_dati_accesso.get('password')
    
    VAR_user = VAR_users.get(VAR_email)
    
    if VAR_user and VAR_user['password'] == VAR_password:
        return jsonify({"Esito": "000", "Msg": "Accesso consentito"}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Accesso negato"}), 401

# ROUTE - CRUD
@VAR_applicazione_api.route('/add_cittadino', methods=['POST'])
def GestisciAggiungiCittadino():
    # header torna le info relativi il tipo di contenuto da analizzare
    VAR_content_type = request.headers.get('Content-Type')
    if VAR_content_type == 'application/json':
        # prende i dati json e li inserisce
        VAR_json_richiesta = request.json
        #prende il dato nella variabile e lo assegna
        VAR_codice_fiscale = VAR_json_richiesta.get('codFiscale')
        if VAR_codice_fiscale in VAR_cittadini:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        else:
            VAR_cittadini[VAR_codice_fiscale] = VAR_json_richiesta
            #cosa registra dove
            JsonSerialize(VAR_cittadini, VAR_file_path) 
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

@VAR_applicazione_api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def leggi_cittadino(codice_fiscale):
    try:
        VAR_cittadino = VAR_cittadini.get(codice_fiscale)
        if VAR_cittadino:
            return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": VAR_cittadino}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    except Exception as e:
        # Log dell'errore
        print(f"Errore nella route /read_cittadino: {str(e)}")
        return jsonify({"Esito": "500", "Msg": "Errore del server"}), 500

@VAR_applicazione_api.route('/update_cittadino', methods=['PUT'])
def aggiorna_cittadino():
    VAR_content_type = request.headers.get('Content-Type')
    if VAR_content_type == 'application/json':
        VAR_json_richiesta = request.json
        VAR_codice_fiscale = VAR_json_richiesta.get('codFiscale')
        if VAR_codice_fiscale in VAR_cittadini:
            VAR_cittadini[VAR_codice_fiscale] = VAR_json_richiesta
            JsonSerialize(VAR_cittadini, VAR_file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

@VAR_applicazione_api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():
    VAR_content_type = request.headers.get('Content-Type')
    if VAR_content_type == 'application/json':
        VAR_codice = request.json.get('codFiscale')
        if VAR_codice in VAR_cittadini:
            del VAR_cittadini[VAR_codice]
            JsonSerialize(VAR_cittadini, VAR_file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

VAR_applicazione_api.run(host="127.0.0.1", port=8080)

"""
#librerie
#jsonify converte dizionari in JSON
#request gestice i dati ricevuti
from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize

#istanza flask
api = Flask(__name__)

#percorso json
file_path = "anagrafe.json"

#carica il contenuto json dentro la variabile
cittadini = JsonDeserialize(file_path)

#ROUTE - CRUD
@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    #header torna le info relativi il tipo di contenuto da analizzare
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        #richiesta di accesso ai dati json
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        else:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path) 
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200




@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale):
    cittadino = cittadini.get(codice_fiscale)
    if cittadino:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200






@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200






@api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        cod = request.json.get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200

api.run(host="127.0.0.1", port=8080)

"""