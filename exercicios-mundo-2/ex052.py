'''
Exercício - 52
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um número: '))
cont = 0
for i in range(1,num + 1):
    if num % i == 0:
        cont += 1
        print(f"\033[1;33m{i}\033[0m", end=' ')
    else:
        print(f"\033[1;31m{i}\033[0m", end=' ')
print()
if cont > 2:
    print(f'O numero {num} não é primo, ele foi divisível por {cont} números')
else:
    print(f'O numero {num} é primo, ele foi divisível por {cont} números ')
