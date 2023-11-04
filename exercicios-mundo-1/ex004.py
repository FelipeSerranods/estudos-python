'''
Exercício - 04
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

testeVariavel = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(testeVariavel)}')
print(f'So tem espaços? {testeVariavel.isspace()}')
print(f'É um numero? {testeVariavel.isnumeric()}')
print(f'É alfabético? {testeVariavel.isalpha()}')
print(f'É alfanumérico? {testeVariavel.isalnum()}')
print(f'Está em maiúscula? {testeVariavel.isupper()}')
print(f'Está em mainúscula? {testeVariavel.islower()}')
print(f'Está capitalizada? {testeVariavel.istitle()}')




