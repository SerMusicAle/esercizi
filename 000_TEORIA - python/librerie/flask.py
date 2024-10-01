from flask import Flask, request, jsonify, render_template

# 1. Creazione di un'Applicazione Flask

# Creare un'istanza dell'applicazione Flask
app = Flask(__name__)

# 2. Definire una Route

# Route per la homepage
@app.route('/')
def home():
    return render_template('index.html')  # Renderizza un template HTML

# 3. Route per un'API REST

# Route per un endpoint API che restituisce dati
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello, World!', 'status': 'success'}
    return jsonify(data)  # Restituisce i dati in formato JSON

# 4. Gestire le Richieste POST

# Route per gestire le richieste POST
@app.route('/api/data', methods=['POST'])
def post_data():
    content = request.json  # Ottieni i dati JSON dal corpo della richiesta
    response = {'received': content, 'status': 'success'}
    return jsonify(response)  # Restituisce la risposta in formato JSON

# 5. Gestire gli Errori

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# 6. Avvio dell'Applicazione

if __name__ == '__main__':
    app.run(debug=True)  # Avvia l'app in modalità debug
