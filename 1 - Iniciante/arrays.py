import os

# start::funções
def printOptions():
    # os.system('cls')
    print('0 - Exibir lista')
    print('1 - Inserir na lista')
    print('2 - Editar item da lista')
    print('3 - Remover da lista')
    print('4 - Exibir a quantidade de itens da lista')
    print('9 - Sair do programa')


def insertToList(value):
    arr.append(value)
    # arr.insert(position, value)

def removeOfList(value):
    bEncontrou = False

    for r in range(len(arr)):
        if arr[r] == value:
            bEncontrou = True
            break

    if bEncontrou:
        arr.remove(value)


def printList():
    print(f'lista = {arr}')


def getOptions():
    id = int(input("Informe a opção: "))
    selectOptions(id)


def editList(old, new):
    bEncontrou = False

    for i in range(len(arr)):
        if arr[i].lower() == old.lower():
            bEncontrou = True
            arr[i] = new

    if bEncontrou:
        print('Item não encontrado')


def selectOptions(id):
    if id == 0:
        if len(arr) > 0:
            printList()
        else:
            print('\nNão há registros na lista\n')
    elif id == 1:
        value = input('Digite algo para adicionar a lista: ')
        insertToList(value)
    elif id == 2:
        oldvalue = input('Digite o nome do item que deseja alterar: ')
        new_value = input('Digite o nome para alterar: ')
        editList(oldvalue, new_value)
    elif id == 3:
        if len(arr) > 0:
            value = input('Digite o nome do campo que deseja remover: ')
            removeOfList(value)
        else:
            print('\nNão há registros para remover\n')
    elif id == 4:
        print(f'\nquantidade: {len(arr)}\n')
    elif id == 9:
        return 0
    else:
        print('\nOpção não encontrada.')
        print('selecione outra opção abaixo\n')
        printOptions()
        getOptions()

    print()
    home()

def isNumeric(value):
    return value.isnumeric()

def home():
    printOptions()
    getOptions()


# end::functions

# start::variables
arr = []

# end::variables

# start::calls
home()
# end::calls
