'''
Exercício - 53
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos
'''
print('=' * 20)
print('TESTE DE PALÍNDROMO')
print('=' * 20)
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
fraseInvertida = frase[::-1]

print(f'O inverso de {frase} é {fraseInvertida}')
if fraseInvertida == frase:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')