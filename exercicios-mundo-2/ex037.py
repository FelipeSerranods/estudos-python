'''
Exercício - 37
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''
num = int(input('Digite um número inteiro: '))

print('Escolha uma base para conversão: ')
print('-=-' * 20)
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

escolha = int(input('Opção: '))

if escolha == 1:
    binario = format(num, 'b')
    print(f'O valor {num} em decimal para binário é {binario}')
elif escolha == 2:
    octal = format(num, 'o')
    print(f'O valor {num} em decimal para octal é {octal}')
elif escolha == 3:
    hexadecimal = format(num, 'x')
    print(f'O valor {num} em decimal para hexadecimal é {hexadecimal}')
else:
    print('Opção inválida. Tente novamente.')
