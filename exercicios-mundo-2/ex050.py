'''
Exercício - 50
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
cont = 0
for numeros in range(1,7):
    num = int(input(f'Digite o {numeros} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
    if cont > 0 and cont == 1:
        plural = 'numero par e a soma é igual a'
    else:
        plural = 'números pares e a soma entre eles é igual a'

print(f'Você informou {cont} {plural} {soma}')
