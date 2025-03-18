from flask import Flask, request, jsonify, render_template
from waitress import serve  # Importe o Waitress

app = Flask(__name__)

@app.route('/', endpoint='index')
def home():
    return render_template('index.html')

@app.route('/authentication')
def authentication():
    return render_template('lics-authentication.html')

if __name__ == '__main__':
    # Rodando a aplicação com o Waitress, não com o Flask
    serve(app, host='0.0.0.0', port=5000)
