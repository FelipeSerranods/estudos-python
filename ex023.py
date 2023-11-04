'''
Exercício - 23
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''


numero = input('Digite um número de 0 a 9999: ')
unidade = numero[-1]
dezena = numero[-2] if len(numero) >= 2 else 0
centena = numero[-3] if len(numero) >= 3 else 0
milhar = numero[-4] if len(numero) >= 4 else 0

print(f'Analisando o número {numero}...')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

'''
Outro jeito de estar realizando o exercício
numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
'''
