import os

# start::variaveis
products = list()
last_ids = list()
_index = 0

products = [
    { "id": 1, "nome": "iphone xr", "valor": 2700, "qtd": 1 },
    { "id": 2, "nome": "Mouse gamer", "valor": 87.98, "qtd": 1 },
    { "id": 3, "nome": "Canivete", "valor": 58.23, "qtd": 1 },
    { "id": 4, "nome": "Lápis", "valor": 0.80, "qtd": 2 },
    { "id": 5, "nome": "Teclado", "valor": 109.80, "qtd": 4 }
]

last_ids = [
    { "lastid": 1 },
    { "lastid": 2 },
    { "lastid": 3 },
    { "lastid": 4 },
    { "lastid": 5 }
]


# end::variaveis


# start::functions
def imprimirOpcoes():
    print('1 - Produtos')
    print('2 - Inserir produto')
    print('3 - Editar produto')
    print('4 - Remover Produto')
    print('0 - Sair do programa')
    print()
    selecionarOpcao(input('Insira a opção: '))


def inserirProduto(nome, valor, qtd):
    id = 0;

    if len(last_ids) > 0:
        id = len(last_ids) + 1
    else:
        id = len(products) + 1

    products.append(
        {
            "id": id,
            "nome": nome,
            "valor": valor,
            "qtd": qtd
        }
    )

    last_ids.append(
        {
            "lastid": id
        }
    )


# na opção mostrar todos, está printando um produto de cada vez
def produtos():
    print('\n1 - Visualizar produto desejado')
    print('2 - Visualizar todos produto')
    op = input('Selecione a opção: ')

    if op == '1':
        op2 = input('Insira o id: ')

        for p in range(len(products)):
            if products[p]["id"] == int(op2):
                print("id: {0}, produto: {1}, valor: {2}, quantidade: {3}".format(
                    products[p]["id"], products[p]["nome"], products[p]["valor"], products[p]["qtd"])
                )
    else:
        print("\nTabela de produtos")
        print("id\t\t\t|produto\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|valor\t\t\t\t\t|quantidade")
        for p in range(len(products)):
            print("{0}\t\t\t|{1}{2}|{3}\t\t\t\t\t|{4}".format(
                products[p]["id"], products[p]["nome"], tabs(products[p]["nome"]), products[p]["valor"],
                products[p]["qtd"])
            )
    print()


# estou com problema de editar o item
def editarProduto(id):
    _index = IndexOf(products, "id", int(id))

    if _index >= 0:
        print('1 - editar nome')
        print('2 - editar valor')
        print('3 - editar quantidade')
        v = input('Insira a opção que deseja editar: ')

        if v.isnumeric():
            b = False
            if v == '1':
                nome = input('Insira o nome do produto: ')
                if products[_index]["nome"] != nome:
                    b = True
                products[_index]["nome"] = nome
            elif v == '2':
                valor = input('Insira o valor do produto: ')
                if products[_index]["valor"] != valor:
                    b = True
                products[_index]["valor"] = valor
            elif v == '3':
                qtd = input('Insira a quantidade do produto: ')
                if products[_index]["qtd"] != qtd:
                    b = True
                products[_index]["qtd"] = qtd

    if b:
        print('Registro alterado com sucesso!')

    home()


def removerProduto(id):
    id = int(id)
    for r in range(len(products)):
        if products[r]["id"] == id:
            products.pop(IndexOf(products, "id", id))
            break


def IndexOf(arr, search, value):
    for i in range(len(arr)):
        if arr[i][search] == value:
            index = i
            break

    return index


def selecionarOpcao(id):
    os.system("cls")

    if id == '1':
        produtos()
    elif id == '2':
        nome = input('Insira o nome do produto: ')
        valor = input('Insira o valor do produto: ')
        qtd = input('Insira a quantidade do produto: ')
        inserirProduto(nome, valor, qtd)
    elif id == '3':
        idp = input('Informe o id que deseja alterar: ')
        editarProduto(idp)
    elif id == '4':
        print()
        idp = input('Insira o id do produto que deseja remover: ')
        removerProduto(idp)
    elif id == 0:
        return 0

    home()


def tabs(s):
    qtd = len(s) / 4
    qtd = round(qtd)
    if qtd % 4 == 1:
        qtd - 1
    else:
        qtd + 1

    _tabs = ""
    for q in range(qtd, 17):
        _tabs += "\t"

    return _tabs


def home():
    imprimirOpcoes()


# end::functions


home()
