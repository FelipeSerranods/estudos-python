'''
Exercício - 54
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import datetime
maior = 0
menor = 0
anoAtual = datetime.today().year
for i in range(1,8):
    anoNascimento = int(input(f'Em que ano a {i}ª peesoa nasceu?: '))
    idade = anoAtual - anoNascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print()
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')