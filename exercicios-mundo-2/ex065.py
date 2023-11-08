'''
Exercício - 65
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

escolha = 'S'
cont = soma = 0
while escolha == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num 
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = input('Deseja continuar? [S/N]: ')
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles é {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

