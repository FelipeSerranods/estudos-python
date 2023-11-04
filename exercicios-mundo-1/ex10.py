'''
Exercício - 10
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''

dinheiroCarteira = float(input('Quanto dinheiro você tem na sua carteria? '))
dinheiroDolar = dinheiroCarteira / 4.89

print(f'Com {dinheiroCarteira} reais você consegue trocar para {dinheiroDolar:.3} doláres')