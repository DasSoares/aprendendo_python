food = input('Digite sua comida preferida: ')
isCondition = bool(input('deseja usar a condição if? Use 1 para sim e 0 para não: '))

print(isCondition)

"""
comparações
== igual
!= diferente
> maior
< menor
>= maior ou igual
<= menor ou igual
=== parecido
!=== não parecido
"""

if isCondition:
    if food == 'pizza':
        print(f'{food} Possui muitas calorias')
    elif food == 'macarrão':
        print(f'{food} possui muitas calorias')
    elif food == '':
        print(f'{food} possui muitos beneficions e é muito saudavel')
    else:
        print(f'desconheço as calorias desta comida: {food}')

else:
    match food:
        case 'pizza':
            print(f'{food} possui muitas calorias')
        case 'macarrão':
            print(f'{food} possui muitas calorias')
        case 'salada':
            print(f'{food} possui muitos beneficios e é muito saudavel')
        # não sei como usar o default case

# b = bool(0)
#
# b = if bool(isCondition)
#
# print(f'{ if isCondition == ""}')