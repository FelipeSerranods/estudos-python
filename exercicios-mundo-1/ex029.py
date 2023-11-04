'''
Exercício - 29
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidadeCarro = int(input('Qual a velocidade do veículo ao passar pelo pardal?: '))

kilometroPermitido = 80

multa = 7.00 * (velocidadeCarro - kilometroPermitido)
if velocidadeCarro >  kilometroPermitido:
    print(f'Você será multado no valor de R${multa:.2f}')
    print(f'Sua velocidade ao passar pelo pardal foi de {velocidadeCarro}Km/h a velocidade maxíma era de {kilometroPermitido}Km/h')
else:
    print(f'Sua velocidade ao passar pelo pardal foi de {velocidadeCarro}Km/h')
    print('Como você respeitou as leis não leverá multa')
