'''
Exercício - 41
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM

Até 14 anos: INFANTIL

Até 19 anos: JÚNIOR

Até 25 anos: SÊNIOR

Acima de 25 anos: MASTER
'''
from datetime import datetime
anoNascimento = int(input('Informe em que ano você nasceu: '))

anoAtual = datetime.now().year

idade = anoAtual - anoNascimento

if idade > 25:
    print(f'A idade do atleta é {idade} anos sua categoria será MASTER')
elif idade > 19 and idade <= 25:
    print(f'A idade do atleta é {idade} anos sua categoria será SÊNIOR')
elif idade > 14 and idade <=19:
    print(f'A idade do atleta é {idade} anos sua categoria será JÚNIOR')
elif idade > 9 and idade <= 14:
    print(f'A idade do atleta é {idade} anos sua categoria será INFANTIL')
elif idade > 3 or idade <= 9:
    print(f'A idade do atleta é {idade} anos sua categoria será MIRIM')
