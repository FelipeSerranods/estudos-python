'''
Exercício - 09
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
'''

n = int(input('Digite um número para ver sua tabuada: '))

for i in range(1,11):
    print(f'{n} x {i} = {n * i}')