import random
# Progrma que gera 5 numeros aleatórios e coloca em tuplas
# mostrar a lista desses numeros
# indicar maior e menor valor da tupla

# gera uma lista vazia (opcional)
cinco_numeros = ()
#[ ... for _ in range(5)] → é como dizer: “faça isso 5 vezes
cinco_numeros = [random.randint(1,50) for _ in range(5)]

maior_valor = max(cinco_numeros)
menor_valor = min(cinco_numeros)

print(f"Os números gerados foram: {cinco_numeros}")
print(f"O MAIOR valor gerado foi {maior_valor} e o MENOR valor gerado foi {menor_valor}")

