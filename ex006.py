'''
Exercício - 06
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

n = float(input('Digite  um valor: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f'O dobro de {n} é {dobro}')
print(f'O triplo de {n} é {triplo}')
print(f'A raiz quadrada de {n} é {raiz:.2}')