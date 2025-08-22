valores = []
contagem = 0
while True:
    numeros = int(input(f'Digite um valor, se quiser finalizar digite 0: '))

    if numeros == 5:
        contagem +=1

    if numeros == 0:
        print('Você finalizou.')
        break
    valores.append(numeros)

for i in range(len(valores)):
    for j in range(len(valores)-1):
        if valores[j] > valores[j+1]:
            valores[j], valores[j+1] = valores[j+1], valores[j]

ordem_desc = valores[:]
ordem_desc.sort(reverse=True)
quantidade = len(valores)

print('---------------------------------------------------------------------')

print(f'Esses são os valores ordenados {ordem_desc}')
print('---------------------------------------------------------------------')

print(f'A quantidade de numeros digitados foram {quantidade}')

print('---------------------------------------------------------------------')

print(f'A quantidade de vezes que o numero 5 apareceu foi {contagem}')







