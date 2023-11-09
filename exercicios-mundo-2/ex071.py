'''
Exercício - 71
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('='* 20)
print('BANCO FS')
print('='* 20)
valorSaque = int(input('Qual valor você deseja sacar?: R$'))
saque = valorSaque
totalCedula = 0
cedula = 50
while True:
    if saque >= cedula:
        saque -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédula de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if saque == 0:
            break
print('='* 20)
print('Volte Sempre!')

