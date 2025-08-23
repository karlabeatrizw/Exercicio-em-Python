#valores = list(range(1,11))
# Programa que mostre os valores da lista e seus respectivos indices
# Exiba também o maior e o menor valor
valores = []

for i in range(5):
    numeros = int(input(f'Digite um valor na posição {i}: '))
    valores.append(numeros)

maior = max(valores)
menor = min(valores)

pos_menor = []
pos_maior = []

for indice, valor in enumerate(valores):
    if valor == menor:
        pos_menor.append(indice)
    if valor == maior:
        pos_maior.append(indice)

print(f'os valores digitados foram {valores} o menor valor da lista é {menor} na posicão {pos_menor}  e o maior valor é {maior} na posição {pos_maior}')

