#valores = list(range(1,11))
# Programa que mostre os valores da lista e seus respectivos indices
# Exiba também o maior e o menor valor
valores = []

for i in range(5):
    numeros = int(input(f'Digite um valor na posição {i}: '))
    valores.append(numeros)

maior = max(valores)
menor = min(valores)

print(f'O menor valor da lista é {menor} e o maior valor é {maior}')

