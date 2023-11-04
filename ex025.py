'''
Exercício - 25
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome = input('Digite seu nome completo: ').upper().strip()
print(f'Analisando o nome {nome}...')
print(f'Seu nome tem o sobrenome Silva? {'SILVA' in nome}')

'''
nome = input('Digite seu nome completo: ').upper().strip()
print(f'Analisando o nome {nome}...')
if nome.find('SILVA'):
    print('Seu nome tem o sobrenome Silva')
else:
    print('Seu nome não possui o sobrenome Silva')
'''
