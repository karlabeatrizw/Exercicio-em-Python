valores = []

pares = []

impares = []

while True:
    numeros = int(input(f'Digite um valor: '))

    continuar = str(input(f'Deseja continuar S/N:')).lower

    if continuar == 'n':
        print('Você finalizou a lista')
        break
    
    valores.append(numeros)
    
    if numeros % 2 == 0:
        pares.append(numeros)

    if numeros % 2 != 0:
        impares.append(numeros)



