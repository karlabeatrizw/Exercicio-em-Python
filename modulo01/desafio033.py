num1 = int(input('enter a number:\n'))
num2 = int(input('enter another number:\n'))
num3 = int(input('enter another number:\n'))

lista = [num1, num2, num3]
print(lista)

if num1 > num2 :
    num1, num2 = num2, num1

if num1 > num3 :
    num1, num3 = num3, num1
    lista2 = [num1, num2, num3]
    print(lista2)

if num2 > num3:
    num2, num3 = num3, num2
    lista3 = [num1, num2, num3]
    print(lista3)