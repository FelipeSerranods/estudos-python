'''
Exercício - 31
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

distanciaViagem = float(input('Para calcular o valor da passagem, informe a distância em Km de sua viagem: '))

if distanciaViagem <= 200:
    valorViagem = distanciaViagem * 0.5
else:
    valorViagem = distanciaViagem * 0.45
print(f'A passagem de sua viagem com distância de {distanciaViagem}Km será de R${valorViagem:.2f}')