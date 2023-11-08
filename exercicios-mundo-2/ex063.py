"""
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 - 1 - 1 - 2 - 3 - 5 - 8
"""

print('=' * 20)
print('Sequência de Fibonacci')
print('=' * 20)

termo = int(input('Quantos termos você quer mostar?: '))
print('=' * 20)
a = 0
b = 1
cont = 3
print(a, end=" -> ")
print(b, end=" -> ") 

while cont <= termo:
    c = b + a
    a = b
    b = c
    print(b , end=" -> ")
    cont += 1
print('Acabou')