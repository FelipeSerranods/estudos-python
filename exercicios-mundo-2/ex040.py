'''
Exercício - 40
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

Média abaixo de 5.0: REPROVADO

Média entre 5.0 e 6.9: RECUPERAÇÃO

Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Digite a primera nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media >= 7.0:
    print(f'Aluno aprovado, média de: {media}')
elif media >= 5.0:
    print(f'Aluno em recuperação, média de: {media}')
else:
    print(f'Aluno reprovado, média de: {media}')