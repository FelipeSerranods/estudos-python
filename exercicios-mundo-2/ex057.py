'''
Exercício - 57
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
if sexo == 'M' or sexo == 'F':
    print('Sexo confirmado')
else:
    while sexo != 'M' and sexo != 'F':
        print('Opção inválida, digite M para masculino e F para feminino')
        sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
    print('Sexo confirmado')
