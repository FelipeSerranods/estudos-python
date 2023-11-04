'''
Exercício - 32
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from datetime import datetime
anoAtual = ''
ano = int(input('Informe algum ano e descubra se ele é bissexto, caso queira testar o ano atual digite 0: '))

if ano == 0:
    anoAtual = datetime.now().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {anoAtual} é bissexto')
    else:
        print(f'O ano {anoAtual} não é bissexto')
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')