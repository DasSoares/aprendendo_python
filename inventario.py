
import os

# variaveis antes das funções
options = 0
estoque_array = []

#-------------------------------------------------------------------

# criação de funções antes das chamadas de funções
def printOptions():
    print('0 - Visualizar produtos')
    print('1 - Adicionar produtos')
    print('2 - Editar produto')
    print('3 - Deletar produto')
    print('4 - Sair do programa')

def getInformations():
    return int(input('Selecione uma opção: '))

#def addItemsArray(arr, product, price, description):# estoque_array.append()

def printInformation(op):

    if op != 4:
        clearSystem()

    if op == 0: # visualiza estoque_array
        print('0 - Exibir todos')
        print('1 - Selecionar por id')
        print('2 - Para voltar')

        _op = int(input('Digite a opção: '))

        if _op == 0:
            print(estoque_array)
        elif _op == 2:
            home()
        else:
            id = int(input('Digite o ID do produto: '))


    elif op == 1: # adiciona produtos
        print('OBS..: O valor do produto deve ser digitado com ponto (.) e não com vírgula (,)')
        nomeproduto = input('Digite o nome do produto: ')
        valorproduto = float(input('Digite o valor do Produto: '))


    #elif op == 2: # edita produtos
    #elif op == 3: # remove produto
    elif op == 4:
        return 0
    else:
        print('Opção não encontrada')
        clearSystem()
        home()


def clearSystem():
    name = 'cls' if os.name != 'posix' 'cls' else 'clear'
    os.system(name)

def home():
    clearSystem()
    printOptions()
    options = getInformations()
    printInformation(options)

#-------------------------------------------------------------------

# as chamadas das funções devem ser feitas depois que criamos a função
home()