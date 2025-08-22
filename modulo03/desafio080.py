valores = []

for inserir in range(5):
    numeros = int(input(f'Digite um valor: '))
    valores.append(numeros)


for i in range(len(valores)): #garante que fazemos várias “passadas” pela lista
    for compara in range(len(valores)-1): #faz a comparação e troca os números adjacentes.

        if valores[compara] > valores[compara+1]:
            valores[compara], valores[compara+1] = valores[compara+1], valores[compara]

print("Lista ordenada:", valores)
