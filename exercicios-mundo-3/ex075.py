'''
Exercício - 75
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

tupla = ()
par = ()
for i in range(1,5):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        par += (num,)
    tupla += (num,)
print(f'Os valores digitados foram: {tupla}')
print(f'O número 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 aparece na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')
print(f'E apareceu estes números pares {par}')
