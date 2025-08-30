# Criar uma tupla unica com os nomes dos produtos e seus respectivos preços na sequencia
# mostrar uma listagem de preços
# Organizado de forma tubular

prod_preco = (
    'janela de madeira', 'janela de alumínio', 'porta de quarto',
    'porta de entrada madeira', 'porta de entrada aluminio',
    'vaso sanitário', 'tambor 200L', 'escada caracol',
    'porta balcão de madeira', 'fogão',
    700.00, 400.00, 300.00, 700.00, 400.00,
    200.00, 120.00, 1300.00, 1200.00, 250.00
)

produtos = prod_preco[:10]

preco = prod_preco[10:]

# zip() combina elementos de duas ou mais sequências (como listas, tuplas, etc.) em iterações, criando pares ou tuplas de elementos correspondentes.

dados_combinados = zip(produtos, preco)

print('Tabela de Produtos e seus Valores')
print('_'*30)
print(f'{"Produto":<37} {"Preço"}')
print('_'*30)

for produto, preco in dados_combinados:
    print(f'{produto:<35} R$ {preco:.2f}')

