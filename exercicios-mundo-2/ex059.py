'''
Exercício - 59
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
print('-=-' * 20)
print('Menu de opções')
print('[ 1 ] somar')
print('[ 2 ] multiplicar')
print('[ 3 ] maior')
print('[ 4 ] novos números')
print('[ 5 ] sair do programa')
print('-=-' * 20)

while opcao != 5:
    opcao = int(input('Opção: '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}')
    elif opcao == 2:
        mult = num1 * num2
        print(f'O número {num1} x {num2} é {mult}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior valor é {num1}')
        elif num2 > num1:
            print(f'O maior valor é {num2}')
        else:
            print('Os dois números são iguais')
    elif opcao == 4:
        print('Informe novos numeros...')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(f'Os valores agora são {num1} e {num2}')
    else:
        print('Opção Invalida! Tente novamente...')
print('Saindo do Programa...')
    