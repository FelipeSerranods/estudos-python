'''
Exercício - 34
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

salarioAtual = float(input('Informe seu salário atual para reajuste salárial: '))
if salarioAtual > 1250:
    salarioNovo = salarioAtual * 1.1
    print(f'Seu salário era de {salarioAtual} e após o reajuste será de {salarioNovo}')
elif salarioAtual <= 1250:
    salarioNovo = salarioAtual * 1.15
    print(f'Seu salário era de {salarioAtual} e após o reajuste será de {salarioNovo}')
