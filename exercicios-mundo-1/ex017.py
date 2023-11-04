'''
Exercício - 17
Faça um programa que leia o comprimento do cateto oposto e do cateto ajascente de um triangûlo retângulo, calcule e mmostre o comprimento da hipotenusa
'''

catetoOpo = float(input('Digite o valor do cateto oposto: '))
catetoAdja = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (catetoOpo ** 2) + (catetoAdja ** 2) 
hipotenusa = hipotenusa ** (1/2)

print(f'O valor da hipotenusa é: {hipotenusa:.2f}')

'''
Mesmo exercício porem utilizando a biblioteca math para calcular a hipotenusa
import math

co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}.')

'''