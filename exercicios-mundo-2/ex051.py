'''
Exercício - 51
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

# Primeíra Maneira de fazer

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
for i in range(10):
    print(termo,end=' -> ')
    termo += razao
print('ACABOU')


#Segunda Maneira
'''
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo + razao, razao):
    print(i, end=' -> ')
print('ACABOU')
'''