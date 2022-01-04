
## pega os dados de um CEP

import requests
import os

os.system('clear')

cep = input('digite o cep: ')
request = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))


os.system('clear')

dados = request.json()

print() # pula uma linha
print(dados) # retorno dos dados do cep informado.