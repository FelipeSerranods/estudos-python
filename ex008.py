'''
Exercício - 08
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

valorMetros = float(input('Digite o valor em metros para convertelo a outras medidas: '))
valorCentimetros = valorMetros * 100
valorMilimetros = valorCentimetros * 10

print(f'O valor de {valorMetros} metros corrosponde:')
print(f'Valor em centímetros: {valorCentimetros}cm')
print(f'Valor em milímetros: {valorMilimetros}mm')
