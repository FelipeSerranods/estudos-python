'''
Exercício - 39
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import datetime
anoNascimento = int(input('Informe em que ano você nasceu: '))

anoAtual = datetime.now().year

idade = anoAtual - anoNascimento
alistamento = 18
difIdade = alistamento - idade
difAlistamento = difIdade + anoAtual


print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}')

if idade == alistamento:
    print('Está na hora de preparar para o alistamento militar, entre no site gov.com e faça sua inscrição e boa sorte.')
elif idade > alistamento: 
    print('Você já passou dos 18 anos tenha certeza de ter já se alistado, caso não tenha se alistado compareça imediatamente ao um forte militar que estaremos te orientando.')
else:
    print(f'Ainda faltam {difIdade} anos para o seu alistamento militar')
    print(f'Seu alistameto militar será apenas em {difAlistamento}')
