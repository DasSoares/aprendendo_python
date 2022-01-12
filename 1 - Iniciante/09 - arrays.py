lista = [
    {"id": 1, "nome": "danilo"},
    {"id": 2, "nome": "monique"}
]

products = []

#print(lista)
#print("index: {0}".format(lista[0].index))

def getIndex(arr, search, value):
    for i in range(len(arr)):
        index = i
        if arr[i][search] == value:
            break

    return index

#print("Index: {0}".format(getIndex(lista, "id", 1)))
print(lista)
lista.pop(1)
print(lista)

# adiciona na lista
# lista.append("Leegoal")
# print(lista)
# adiciona valor em uma posição
# lista.insert(0, "madeira")
# print(lista)
# pega o indice
# print(lista.index("leegoal", 0, 1))

def insertProduct(name, price, quantity):
    id = len(products) + 1
    products.append(
        {"id": id, "nome": name, "price": price, "quantity": quantity}
    )
insertProduct("iPhone XR", 2700, 1)
insertProduct("Fone de ouvido", 140, 2)


print(products)

#print(len(products))