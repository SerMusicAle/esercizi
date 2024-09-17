from flask import Flask, render_template, request

api = Flask(__name__, 
            static_url_path='',
            static_folder='./templates',
            template_folder='./templates'
            )

utenti:list[list[str|None]] = [
    ['mario', 'bros', 'mariobros@smanagement.it', 'password', 'OFFLINE'],
    ['luigi', 'bros', 'luigibros@smanagement.it', 'password', 'OFFLINE'],
    ['daisy', 'princess','daisyprincess@smanagement.it', 'password', 'OFFLINE'],
    ['peach', 'slave', 'peachslave@smanagement.it', 'password', 'OFFLINE'],
    ['alessandro', 'sereni', 'a.sereni@live.it', 'password', 'OFFLINE']
]

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/regok', methods=['GET'])
def regok():
    return render_template('regok.html')

@api.route('/regko', methods=['GET'])
def regko():
    return render_template('regko.html')

@api.route('/registrazione', methods=['GET'])
def registrati():
    nome:str|None = request.args.get("name")
    cognome = request.args.get("surname")
    email = request.args.get("email")
    password = request.args.get('password')
    repassword = request.args.get('repassword')
    Trovato = 0
    if password == repassword:
        for utente in utenti:
            if utente[2]== email:
                Trovato = 1
        if Trovato == 0:
            nuovo_utente:list[str|None] = []
            nuovo_utente.append(nome)
            nuovo_utente.append(cognome)
            nuovo_utente.append(email)
            nuovo_utente.append(password)
            nuovo_utente.append("0")
            utenti.append(nuovo_utente)
            return render_template('regok.html')
        
    return render_template('regko.html')

@api.route('/accesso', methods=['GET'])
def accesso():
    email = request.args.get("email")
    password = request.args.get('password')
    Trovato = 0
    for utente in utenti:
        if utente[2] == email and utente[3] == password:
            Trovato = 1
            utente[4] = "ONLINE"
            return render_template('regok.html')

"""
@api.route('/accesso', methods=['GET'])
def accesso():
    email = request.args.get("email")
    password = request.args.get('password')
    for utente in utenti:
        if email == utente[2] and password == utente[3]:
            return render_template('home.html')
        else:
            return render_template('regko.html')

"""
api.run(host="0.0.0.0",port=8085)


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
