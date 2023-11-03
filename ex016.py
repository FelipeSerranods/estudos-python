'''
Exercício - 16
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

from math import trunc

n = float(input('Digite um numero quebrado: '))
print(f'O valor {n} arredondado será {trunc(n)}')