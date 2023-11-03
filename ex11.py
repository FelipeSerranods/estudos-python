'''
Exercício - 11
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

larguraParede = float(input('Digite a largura da parede em metros: '))
alturaParede = float(input('Digite a altura da parede em metros: '))

area = larguraParede * alturaParede

tinta = area / 2

print("A área total a ser pintada é de", area, "metros quadrados.")
print("Você precisará de", tinta, "litros de tinta.")