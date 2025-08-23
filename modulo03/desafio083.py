expressao = str(input('Digite a expressão: '))
cont = 0
cont2 = 0
for simbolo in expressao:
    if simbolo == '(':
        cont += 1

for simbolo2 in expressao:    
    if simbolo2 == ')':
        cont2 += 1

if cont == cont2:
        print('Todos os parenteses tem fechamento')
if cont > cont2 or cont2 > cont:
     num_faltantes = cont - cont2

if num_faltantes < 0:
        num_faltantes*(-1)

else:
    print(f'Há {num_faltantes} parentese(s) sem fechamento')