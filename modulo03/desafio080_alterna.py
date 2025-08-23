lista = []

for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
# append(): Adiciona um elemento apenas ao final da lista.
#extend(): Adiciona vários elementos de um iterável ao final da lista.
#insert() é fundamental quando a ordem dos elementos é importante e você precisa adicionar um item em uma posição intermediária da lista. 
    else:
        posicao = 0
        while posicao < len(lista):
            if n < lista[posicao]:
                lista.insert(posicao, n)
                print(f'O numero foi add a posição {posicao} da lista')
                break
        posicao += 1

        print('_'*30)
        print(f'Os valores digitados em ordem foram {lista}')
