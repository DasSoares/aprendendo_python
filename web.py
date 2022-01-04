
## rotas para as apis
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage(name):
    return f"Bem-vindo {name}, sua primeira página web com python"

@app.route('/get-cep/{value}')
def buscaCEP(value):
    return f'CEP: {value}'
