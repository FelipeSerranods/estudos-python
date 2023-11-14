'''
Exercício - 84
Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

listaPessoas = []
dados = []

while True:
    dados.append(str(input('Digite seu nome: ')).strip().title())
    dados.append(float(input('Informe seu peso: ')))
    listaPessoas.append(dados[:])
    dados.clear()
    escolha = ' '
    escolha = str(input('Cadastrar mais uma pessoa? [S/N]: ')).strip().upper()
    while escolha not in 'SN':
        escolha = str(input('Cadastrar mais uma pessoa? [S/N]: ')).strip().upper()
    if escolha == 'N':
        break

for peso in listaPessoas:
    maiorPeso = menorPeso = listaPessoas[0][1]
    if peso[1] > maiorPeso:
        maiorPeso = peso[1]
    if peso[1] < menorPeso:
        menorPeso = peso[1]


print(f'Foram cadastradas {len(listaPessoas)} usuários')
print(f'O maior peso foi {maiorPeso}.Peso de ',end=' ')
for pessoa in listaPessoas:
    if pessoa[1] == maiorPeso:
        print(f'[{pessoa[0]}]',end='')
print(f'\nO menor peso foi {menorPeso}.Peso de ',end=' ')
for pessoa in listaPessoas:
    if pessoa[1] == menorPeso:
        print(f'[{pessoa[0]}]',end='')