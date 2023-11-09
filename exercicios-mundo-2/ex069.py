'''
Exercício - 69
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

escolha = sexo = ''
homens = mulheres = cont = 0
while escolha != 'N':
    print('-' * 20)
    print('Cadastre uma pessoa')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()
    while sexo not in 'MF':
        print('Opção Invalida! tente novamente')
        sexo = input('Sexo: [M/F] ').strip().upper()
    if idade > 18:
        cont +=1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 18:
        mulheres += 1
    print('-' * 20)
    escolha = input('Quer continuar a cadastrar?: [S/N] ').strip().upper()
    while escolha not in 'SN':
        print('Opção Invalida! tente novamente')
        escolha = input('Quer continuar a cadastrar?: [S/N] ').strip().upper()
print('-' * 20)
print(f'O total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
