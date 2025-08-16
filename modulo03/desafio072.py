#Programa que mostra o numero de 0 a 20 por estenso em português
# tuplas são imutáveis

num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    escolha = int(input('choose a number from 0 to 20 to be displayed in Portuguese: '))

    if 0 <= escolha <= 20:
        print(f'the number chosen was {num[escolha]}.')
        break
    else:
        print('invalid digit')