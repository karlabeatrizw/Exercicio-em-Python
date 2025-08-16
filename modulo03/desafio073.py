#exibir os times em ordem alfabéticas
#exibir o top 5
#exibir os ultimos 4 colocados
#fornecer a posição do time que o usuário deseja saber

tabela = ('flamengo','cruzeiro','palmeiras','bahia','botafogo',
          'mirassol','sao paulo','red bull bragantino','fluminense',
          'atletico mineiro','internacional','ceara','corinthians',
          'santos','gremio','vitoria','vasco da gama','fortaleza',
          'juventude','sport recife')

ordem_alfab = (sorted(tabela))

print('-------------------------------------------------')
#Por padrão, sorted() ordena em ordem crescente (de menor para maior).
print('Essa é a lista de times em ordem alfabética')
print('-------------------------------------------------')
for cont, posicao in enumerate(ordem_alfab, start=1):
    print(f'{cont} - {posicao}')

print('-------------------------------------------------')
print('Top 5 colocados do Brasileirão')

print('-------------------------------------------------')
#enumerate
for posicao, time in enumerate(tabela[:5], start=1):
    print(f'{posicao}º colocado: {time}')

print('-------------------------------------------------')

print('Os 4 últimos colocados do Brasileirão')
print('-------------------------------------------------')
#tabela com numero 15 pois os termos sao de 0 a 19
for posicao, time in enumerate(tabela[15:], start=17):
    print(f'{posicao}º colocado: {time}')

print('-------------------------------------------------')

while True:
    escolha = str(input('Escolha um time dentro da lista que você deseja saber\na posição no Campeonato Brasileiro de Futebol: ')).lower()

    if escolha in tabela:
        posicao = tabela.index(escolha) + 1
        # +1 porque o índice começa em 0
        print(f'o time {escolha} está na posição {posicao}')
        break

    else:
        print('Dígito Invàlido')