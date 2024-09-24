import json
from flask import Flask, render_template, request

api = Flask(__name__, 
            static_url_path='',
            static_folder='./templates',
            template_folder='./templates'
            )

#utenti
def load_utenti():
    with open('utenti.json', 'r') as f:
        return json.load(f)

def save_utenti(utenti):
    with open('utenti.json', 'w') as f:
        json.dump(utenti, f)

#pagine
@api.route('/', methods=['GET'])
def index():
    return render_template('pages/index.html')

@api.route('/regok', methods=['GET'])
def regok():
    return render_template('regok.html')

@api.route('/regko', methods=['GET'])
def regko():
    return render_template('regko.html')

@api.route('/registrazione', methods=['GET'])  

#SIGNIN
def registrati():
    utenti = load_utenti()
    nome:str|None = request.args.get("name")
    cognome = request.args.get("surname")
    email = request.args.get("email")
    password = request.args.get('password')
    repassword = request.args.get('repassword')

    if password == repassword:
        for utente in utenti:
            if utente["email"]== email:
                return render_template('regko.html')  # Utente già registrato
                break
            
        nuovo_utente:list[str] = {
            "nome": nome,
            "cognome": cognome,
            "email": email,
            "password": password,
            "logged": "0"
        }
        utenti.append(nuovo_utente)
        save_utenti(utenti)  # Salva nel file JSON
        return render_template('regok.html')
        
    return render_template('regko.html')

#LOGIN
@api.route('/login', methods=['GET'])
def login():
    email = request.args.get("email")
    password = request.args.get('password')
    
    for utente in utenti:
#verifica corrispondenza
        if utente[2] == email and utente[3] == password:

#verifica log precedente            
            if utente[4] == '1':
                print("L'utente è già loggato")
                return render_template('regko.html')
            else:
                utente[4] = "1"
                return render_template('pages/home.html')
    print("Utente non trovato")
    return render_template('regko.html')
        

#LOGOUT
@api.route('/logout', methods=['GET'])
def logout():
    email = request.args.get("email")
    for utente in utenti:
        if utente[2] == email:
            utente[4] = '0'
            return render_template('regok.html')
    return render_template('regko.html')

#api
api.run(host="0.0.0.0",port=8085)

#TIMEOUT


"""
@api.route('/registrazione', methods=['GET'])
def registrati():
    nome = request.args.get("name")
    cognome = request.args.get("surname")
    email = request.args.get("email")
    password = request.args.get('password')
    repassword = request.args.get('repassword')
    if password == repassword:
        password = request.args.get("password")
        for utente in utenti:
            if email != utente[2] : 
                new_user=[]
                new_user.append(nome)
                #= [nome, cognome, email, password, "0"]
                utenti.append(new_user)
                return render_template('regok.html')
            else:
                return render_template('regko.html')
    else:
        return render_template('regko.html')
"""
