valores = []

for i in range(5):
    numeros = int(input(f'Digite um valor na posição {i}: '))

    repetido = False
    for v in valores:
        if v == numeros: #se encontrar igual
            repetido = True

    if repetido == False:
        valores.append(numeros)
    else:
        print("Valor repetido, não será adicionado.")

print(valores)