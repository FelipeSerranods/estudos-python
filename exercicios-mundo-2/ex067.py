'''
Exercício - 67
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

cont = 0
while True:
    cont = 1
    num = int(input('Quer ver a tabuada de qual valor?: '))
    if num < 0:
        break
    print('-' *20)
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
    print('-' *20)
print('Progama encerrado...')    

