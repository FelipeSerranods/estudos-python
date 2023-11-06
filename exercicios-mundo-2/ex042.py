'''
Exercício - 42
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo seráformado:
EQUILÁTERO: todos os lados iguais

ISÓSCELES: dois lados iguais, um diferente

ESCALENO: todos os lados diferente
'''

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('É possivel formar um triângulo')
    if a == b == c:
        print('Com os segmentos informados é possivel formar um triângulo equilátero')
    elif a == b and b != c or a != b and b == c:
        print('Com os segmentos informados é possivel formar um triângulo isósceles')
    else:
        print('Com os segmentos informados é possivel formar um triângulo escaleno')
else:
    print('Não é possivel formar um triângulo')
