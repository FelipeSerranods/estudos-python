'''
Exercício - 45
Crie um programa que faça o computador jogar Jokenpô com você.
'''
print('-=-' * 20)
print('Jokenpô do Braga')

from random import randint
from time import sleep

saldoMaquina = 0
saldoUser = 0
print('Escolha de 0 a 2 para jogar')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
escolhaUser = int(input('Opcão: '))

escolhas = ('Pedra', 'Papel', 'Tesoura')
escolhaMaquina = randint(0,2)

if escolhaUser == 0 or escolhaUser == 1 or escolhaUser == 2:
    # PEDRA
    if escolhaUser == 0 and escolhaMaquina == 2:
        saldoUser += 1
    elif escolhaUser == 0 and escolhaMaquina != 0 and escolhaMaquina != 2:
        saldoMaquina += 1
    # PAPEL
    elif escolhaUser == 1 and escolhaMaquina == 0:
        saldoUser += 1
    elif escolhaUser == 1 and escolhaMaquina != 0 and escolhaMaquina != 1:
        saldoMaquina += 1
    #TESOURA
    elif escolhaUser == 2 and escolhaMaquina == 1:
        saldoUser += 1
    elif escolhaUser == 2 and escolhaMaquina != 1 and escolhaMaquina != 2:
        saldoMaquina += 1
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')

    print(f'A escolha da maquina foi {escolhas[escolhaMaquina]}')
    print(f'Sua escolha foi {escolhas[escolhaUser]}')
    print()    
    print('Pontos Totais')
    print(f'Pontos da CPU: {saldoMaquina}')
    print(f'Pontos do usúario: {saldoUser}')
    print('-=-' * 20)
else:
    print('Opção Invalida!, tente novamente...')

