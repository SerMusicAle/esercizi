from flask import Flask, render_template, request

api = Flask(__name__, 
            static_url_path='',
            static_folder='./templates',
            template_folder='./templates'
            )

utenti = [
    ['mario', 'bros', 'mariobros@smanagement.it', 'password', '0'],
    ['luigi', 'bros', 'luigibros@smanagement.it', 'password', '0'],
    ['daisy', 'princess','daisyprincess@smanagement.it', 'password', '0'],
    ['peach', 'slave', 'peachslave@smanagement.it', 'password', '0']
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


@api.route('/registrati', methods=['GET'])
def registrati():
    nome = request.args.get("name")
    cognome = request.args.get("surname")
    email = request.args.get("email")
    password = request.args.get('password')
    repassword = request.args.get('repassword')
    if password == repassword:
        password = request.args.get("password")
    else:
        return render_template('regko.html')

    for utente in utenti:
        if email == utente[2] :
            return render_template('home.html')    

    new:list[str] = [nome, cognome, email, password, "0"]
    utenti.append(new)
    return render_template('regko.html')



api.run(host="0.0.0.0",port=8085)


