'''
Exercício - 34
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('É possivel formar um triângulo')
else:
    print('Não é possivel formar um triângulo')

