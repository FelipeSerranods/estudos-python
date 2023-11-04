'''
Exercício - 28
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint

numeroSorte = randint(0,5)

numeroEscolhido = int(input('Digite um número de 0 a 5 e teste sua sorte para ganhar!: '))

if numeroEscolhido == numeroSorte:
    print(f'Você acertou meus parabéns')
else:
    print(f'Você errou o número era {numeroSorte}')
