produtos = []
precos = []
contador1 = 0
contador2 = 0

while True:
    prod = str(input("Qual produto: "))
    valor = float(input("Qual o valor do produto: "))

    produtos.append(prod) #adiciona os itens digitados a lista vazia de produtos
    precos.append(valor) #adiciona os valores de cada produto a lista vazia de precos

    contador2 += valor #faz a soma de todos os valores

    if valor > 1000: #conta os itens de valor superior a 1000
        contador1 += 1

    barato = min(precos) #identifica o item da lista de menor valor
    indice = precos.index(barato) #encontra a posição do item de menor valor
    nome_menor = produtos[indice] #pega o indice que estava em precos e usa para achar o nome do produto na lista de produtos

    interronpe = int(input("[1] CONTINUAR\n[0] ENCERRAR"))

    if interronpe == 0: #quando o usuario digitar zero o while interrompe
        break

print(f"A soma de todos os valores é {contador2}")
print(f"o menor valor é {barato} e pertence a {nome_menor}")
print(f"a quantidade de produtos menos de 1000 é {contador1}")
