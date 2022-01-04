"""
    Estrutura de repetição -> For
"""
# imprime de 0 a 4 range(5)
for i in range(1, 11): # (inicia, termina)
    print(i)

print()

# imprime cada letra do texto
name = "batman"
for j in range(len(name)):
    print(name[j])


"""
    Estrutura de repetição -> While
    interrupção do while -> break
"""

contador = 0
while contador < 10:
    contador += 1
    if contador == 7:
        print('Bateu a média')
    print(f"contador: {contador}")
