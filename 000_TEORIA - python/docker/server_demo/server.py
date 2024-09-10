from flask import Flask, render_template

api = Flask(__name__, 
            static_url_path='',
            static_folder='./templates',
            template_folder='./templates'
            )

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/pages/milano.html', methods=['GET'])
def index2():
    return render_template('/pages/milano.html')

api.run(host="0.0.0.0",port=8085)