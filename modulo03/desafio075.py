# Programa que vai ler 4 numeros
# a) O programa deve dizer quantas vezes aparece o numero 9
# b) O programa devera dizer qual a posição do primeiro numero 3
# c) Quais foram os numeros pares

n = 0
valores = []
pares = []

while n < 4:
    numero = int(input('Digite um numero: '))
    valores.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    n += 1

print('\n-------------------------------------------------\n')

t = tuple(valores) # converte a lista para tupla
print("A tupla gerada foi")
print(t)

print('\n-------------------------------------------------\n')

nove = valores.count(9)
print(f"O numero 9 apareceu {nove} vez(es)")

print('\n-------------------------------------------------\n')

if 3 in valores:
    tres = valores.index(3)
    print(f"O numero três apareceu na posição de digitação {tres+1} ")
else:
    print("O número 3 não apareceu na digitação.")

print('\n-------------------------------------------------\n')

print(f"Os numeros pares foram {pares}")