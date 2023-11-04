'''
Exercício - 12
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

valorInicial = float(input('Digite o valor que leverá um desconto de 5%: '))
valorNovo = valorInicial * 0.95

print(f'O produto x com valor de {valorInicial} reais após o desconto de 5% ficará {valorNovo} reais')