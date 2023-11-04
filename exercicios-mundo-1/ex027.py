'''
Exercício - 27
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''
nome = input('Digite seu nome completo: ').strip().title()
separador = nome.split()

print(separador)
print('Analisando o seu nome. . .')
print(f'Seu primeiro nome é {separador[0]}')
print(f'Seu último nome é {separador[-1]}')