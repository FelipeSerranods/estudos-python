'''
Exercício - 26
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = input('Digite uma frase: ').strip().lower()
print(f'A letra A aparaceu {frase.count('a')} vezes na frase')
print(f'A primeira letra A aparaceu na posição {frase.find('a') + 1}')
print(f'A última letra A aparaceu na posição {frase.rfind('a') + 1}')

