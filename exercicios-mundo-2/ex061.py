'''
Exercício - 61
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 1
while cont <= 10:
    print(termo, end= ' -> ')
    termo += razao
    cont += 1
print('Acabou!')