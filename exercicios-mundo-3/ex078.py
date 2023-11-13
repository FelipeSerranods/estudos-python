'''
Exercício - 78
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

valores = []
maior = menor = 0

for i in range(0,5):
    valores.append(int(input(f'Digite o {i}º valor: ')))
    if i == 1:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {maior} nas posições:',end=' ')

for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}....', end=' ')

print(f'\nO menor valor foi {menor} nas posições:',end=' ')

for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}....', end=' ')
