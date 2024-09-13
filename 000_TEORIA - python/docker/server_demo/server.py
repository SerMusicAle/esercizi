from flask import Flask, render_template, request

api = Flask(__name__, 
            static_url_path='',
            static_folder='./templates',
            template_folder='./templates'
            )

utenti = [
    ['mario', 'bros', 'M', '0'],
    ['luigi', 'bros', 'M', '0'],
    ['daisy', 'princess', 'F', '0'],
    ['peach', 'slave', 'F', '0']
]

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/regok', methods=['GET'])
def regok():
    return render_template('/regok.html')

@api.route('/regko', methods=['GET'])
def regko():
    return render_template('/regko.html')


@api.route('/registrati', methods=['GET'])
def registrati():
    nome = request.args.get("name")
    print("Nome inserito:" + nome)

    password = request.args.get("cognome")

    return render_template('/index.html')


api.run(host="0.0.0.0",port=8085)


