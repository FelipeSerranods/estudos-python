'''
Exercício - 58
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
from time import sleep
tentar = 'S'
texto = 'Vamos Jogar'
print('-=-' * 20)
print(texto.center(60, ' '))
print('-=-' * 20)
numeroSorte = randint(0,10)
print('Pensando...')
sleep(1)
print('Acabei de pensar em um número de 0 a 10 será que você congue adivinhar?')

while tentar != 'N':
    numeroEscolhido = int(input('Digite um número de 0 a 10 e teste sua sorte para ganhar!: '))
    
    if numeroEscolhido != numeroSorte:
        if numeroSorte > numeroEscolhido:
            print('Hmm,mais...')
        else:
            print('Hmm,menos...')
        tentar = input(('Deseja continuar ? [S/N]: ')).strip().upper()
    else:
        print(f'Você acertou meus parabéns')
        tentar = input(('Outro jogo ? [S/N]: ')).strip().upper()
        numeroSorte = randint(0,10)
print('Obrigado por jogar!')
