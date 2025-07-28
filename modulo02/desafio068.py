"""Jogo em que o usuario dgita um numero e soma com um numero sorteado pelo computador. No final o usuario precisa falar se essa soma é impar ou par. Caso o jogador perca o jogo finaliza, mas se ele ganhar o jogo continua."""

import random
contador = 0
while True:
    n1 = random.randint(1, 10)
    n2 = int(input("Enter a number: "))
    resultado = n1 + n2

    p = str(input("Par ou Impar[P/I]: ")).upper()


    if resultado % 2 == 0 and p == 'P':
        print(f"voce jogou {n2} e computador {n1}. total de {resultado} deu PAR")
        print("Voce VENCEU\nJOGAR NOVAMENTE...")


    if resultado % 2 != 0 and p == 'P':
        print(f"voce jogou {n2} e computador {n1}. total de {resultado} deu IMPAR")
        print("Voce PERDEU\nJOGAR NOVAMENTE...")
        break

    if resultado % 2 == 0 and p == 'I':
        print(f"voce jogou {n2} e computador {n1}. total de {resultado} deu PAR")
        print("Voce PERDEU\nJOGAR NOVAMENTE...")
        break

    if resultado % 2 != 0 and p == 'I':
        print(f"voce jogou {n2} e computador {n1}. total de {resultado} deu IMPAR")
        print("Voce VENCEU\nJOGAR NOVAMENTE...")

    contador += 1


print(f"a quantidade de vezes que vc ganhou foram {contador}")
