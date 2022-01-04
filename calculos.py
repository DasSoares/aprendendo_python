
operation = ''
valueA = 0
valueB = 0
valueResult = 0

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(operation, a, b):
    if a.isnumeric():
        if a.index('.') == -1:
            a = int(a)
        elif type(a) == 'float':
            a = float(a)
        else:
            options("Digite números inteiros ou Reais (flutuantes ex: 2.59)!")

    if operation == '+':
        valueResult = somar(a, b)
    elif operation == '-':
        valueResult = subtrair(a, b)
    elif operation == '*':
        valueResult = multiplicar(a, b)
    elif operation == '/':
        valueResult = dividir(a, b)
    else:
        print('não existe calculo para este tipo de operação, tente novamente')
        options("")
        calcular(operation, valueA, valueB)

    print(valueResult)


def options(message):
    if len(message) > 0:
        print(message)
    print("exemplo de operações: + - * /")
    operation = input('Digite o a operação: ')
    valueA = input('Digite o valor: ')
    valueB = input('Digite outro valor: ')
    print(valueA.index('.'))
    calcular(operation, valueA, valueB)


options("")