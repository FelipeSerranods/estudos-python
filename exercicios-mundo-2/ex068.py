'''
Exercício - 68
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 20)


from random import randint

vitoriaUser = vitoriaMaquina = 0
escolhaUser = ''
while vitoriaMaquina < 1:
    
    numUser = int(input('Diga um valor: '))
    numMaquina = randint(1,10)
    escolhaUser = input('Par ou Ímpar? digite P ou I: ').strip().upper()
    while escolhaUser != 'P' and escolhaUser != 'I':
        escolhaUser = input('Por favor tente novamente escolha P ou I: ').strip().upper()
    total = numUser + numMaquina

    #Guarda se o valor é par ou impar
    if total % 2 == 0:
        resp = 'par'
    else:
        resp = 'impar'
    print(f'Você escolheu {numUser} e o computador {numMaquina}. Total deu {total} e deu {resp}')
    print('-=-' * 20)
    if escolhaUser == 'P' and resp == 'par':
        vitoriaUser += 1
        print('Voce ganhou!')
        print('Vamos jogar novamente...')
    elif escolhaUser == 'P' and resp == 'impar':
        vitoriaMaquina += 1
    elif escolhaUser == 'I' and resp == 'impar':
        vitoriaUser += 1
        print('Voce ganhou!')
        print('Vamos jogar novamente...')
    elif escolhaUser == 'I' and resp == 'par':
        vitoriaMaquina += 1
print('Voce Perdeu')
print('-=-' * 20)
print(f'GAME OVER! Você venceu {vitoriaUser} vezes')