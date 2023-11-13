'''
Exercício - 82
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
valores = []
valoresImpar = []
valoresPar = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    escolha = ' '
    escolha = input('Deseja adicionar mais algum? [S/N]: ').strip().upper()
    while escolha not in 'SsNn':
        print('Digite S para continuar ou N para sair')
        escolha = input('Deseja adicionar mais algum? [S/N]: ').strip().upper()
    if escolha == 'N':
        break
print(valores)
for n in valores:
    if n % 2 == 0:
        valoresPar.append(n)
    else:
        valoresImpar.append(n)

print(valoresPar)
print(valoresImpar)