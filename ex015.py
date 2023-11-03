'''
Exercício - 15
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

diasAlugado = int(input('Digite quantos dias ele foi alugado: '))
kmPercorridos = float(input('Digite a quantidade de km percorridos: '))

valorPagar = (60 * diasAlugado) + (0.15 * kmPercorridos)

print(f'O valor a pagar será de R${valorPagar:.2f}')