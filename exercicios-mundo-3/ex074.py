'''
Exercício - 74
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

#jeito 1 - sem Tupla
'''
from random import randint

maior = menor = 0
for i in range(1,6):
    num = randint(1,10)
    if i == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    t1 = num
    print(t1, end=' ')
print()
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
'''

#jeito 2 - com tupla
from random import randint

maior = menor = 0
numeroSorteado = (randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10))

print('Os valores sorteados foram: ', end='')
for num in numeroSorteado:
    print(num, end=' ')
print(f'\nO maior valor sorteado foi {max(numeroSorteado)}')
print(f'O menor valor sorteado foi {min(numeroSorteado)}')

