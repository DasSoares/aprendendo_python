
input = input('digite um numero: ')
valor = 0

# retorna inteiro
def returnInt(value):
    if type(value) != 'str' and value.isnumeric():
        return print(f'{value}, tipo:{type(int(value))}')

# retorna flutuante
def returnFloat(value):
    if type(value) != 'str' and value.isnumeric():
        return print(f'{value}, tipo:{type(float(value))}')

# retorna string
def returnString(value):
    if type(value) == 'str':
        return print(f'{value}, tipo:{type(value)}')

# não retorna nada, apenas faz o que for preciso
def soma(value):
    valor = value
    print(f'O valor inserido pelo usuário: {valor}')


returnInt(input)
returnString(input)
returnFloat(input)
soma(input)