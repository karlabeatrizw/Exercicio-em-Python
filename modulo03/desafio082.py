valores = []

pares = []

impares = []

while True:
    numeros = int(input(f'Digite um valor: '))
    valores.append(numeros)
    
    continuar = str(input(f'Deseja continuar S/N:')).lower()

    if continuar == 'n':
        print('Você finalizou a lista')
        break
    

    if numeros % 2 == 0:
        pares.append(numeros)

    if numeros % 2 != 0:
        impares.append(numeros)

print('_'*35)
print(f'A lista gerada foi {valores}')
print('_'*35)
print(f'Os numeros pares foram {pares}')
print('_'*35)
print(f'Os numeros impares foram {impares}')




