#valores = list(range(1,11))
# Programa que mostre os valores da lista e seus respectivos indices
# Exiba também o maior e o menor valor
valores = [2, 1, 8, 5, 4]
maior = max(valores)
menor = min(valores)
for c, v in enumerate(valores):
    print(f'No índice {c} o valor é {v}')


print(f'O menor valor da lista é {menor} e o maior valor é {maior}')

