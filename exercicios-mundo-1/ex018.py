'''
Exercício - 18
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo: '))
anguloRadiano = radians(angulo)

seno = sin(anguloRadiano)
cosseno  = cos(anguloRadiano)
tangente  = tan(anguloRadiano)


print(f'O ângulo em radianos é {anguloRadiano:.2f}.')
print(f'O seno do ângulo é {seno:.2f}.')
print(f'O cosseno do ângulo é {cosseno:.2f}.')
print(f'A tangente do ângulo é {tangente:.2f}.')