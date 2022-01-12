

# comentário de uma linha

"""
Comentário de várias linhas
"""

# imprimir na tela - output
print("Hello Word")

# declarações, e tipos primitivos
texto = "João da Silva Sauro"   # type -> str
inteiro = 1                     # type -> int
flutuante = 2.50                # type -> float
booleanos = True # ou False     # type -> bool
lista = []                      # type -> list

#print(type(lista))

# operadores artiméticos
soma = 1 + 1
subt = 10 - 5
mult = 5 * 3
divs = 17 / 3
exponenciacao = 4 ** 2
resto_divs = 11/4
inteiro_divs = 11//4

print(resto_divs)
print(inteiro_divs)

# conversão de tipos
# int(value) para inteiro
# float(value) para flutuantes que é float que também vale como double
# bool(value) para booleanos

## timer, deve ser importado antes
# time.sleep(1)

def tabs(s):
    qtd = len(s)%4
    _tabs = ""
    for q in range(qtd, 15):
        _tabs += "\t"

    return _tabs


def impar_par(s):
    i = len(s)
    print(type(i))
    print(i % 4)
    if i % 4 == 1:
        return i + 1
    else:
        if i / 2 == 1:
            return i
        else:
            return i


print("Mouse gamer:", impar_par("Mouse gamer"))

# print("Impar ou par: {0}".format(impar_par("canivete")))

# print(tabs("mouse gamer"))

# produtos = [
#     { "id": 1, "nome": "iPhone XR", "valor": 2700, "qtd": 1 },
#     { "id": 2, "nome": "Monitor LG 25' ultrawide screen", "valor": 680, "qtd": 1 },
#     { "id": 3, "nome": "JBL GO 3", "valor": 189, "qtd": 1 }
# ]

# for p in range(len(produtos)):
#     if produtos[p]["id"] == 1:
#         print(produtos[p]["id"])