from flask import Flask, request, json
from my_json import JsonSerialize, JsonDeserialize

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    #prendi i dati della richeista
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if content_type=="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest ["codiceFiscale"]
        print ("Ricevuto " + sCodiceFiscale)

        #carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error":"000","Msg":"ok"}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error":"000","Msg":"codice fiscale già presente"}
            return json.dumps(jResponse), 200
    else:
        return "Errore, formato non riconsociuto", 401
    
api.route('/get_cittadino', methods=['GET'])

def GetCittadino():

    # prendi il codice fiscale dalla query string
    sCodiceFiscale = request.args.get('codiceFiscale')
    print("Ricevuto codice fiscale: " + sCodiceFiscale)

    if content_type=="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest ["codiceFiscale"]
        print ("Ricevuto " + sCodiceFiscale)
            
        # carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale in dAnagrafe:
            jResponse = {"Error": "000", "Msg": "ok", "Data": dAnagrafe[sCodiceFiscale]}
            return json.dumps(jResponse), 200
        else:
            jResponse = {"Error": "002", "Msg": "codice fiscale non trovato"}
            return json.dumps(jResponse), 404
        

api.run (host="127.0.0.1", port=8080)

 