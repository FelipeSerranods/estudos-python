'''
Exercício - 56
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
texto = 'MEDIAS DO GRUPO'
totalIdade = 0
contIdade = 0 
contHomem = 0
contMulher = 0
for i in range(1,5):
    print(f'---------{i}ª PESSOA ---------')
    nome = input(f'Nome: ')
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo [M/F]: ').strip().upper()
    print()
    totalIdade += idade
    mediaIdade = totalIdade / 4

    if sexo == 'M':
        contHomem += 1
        if i == 1:
            maiorIdade = idade
            nomeVelho = nome
        else:
            if idade > maiorIdade:
                maiorIdade = idade
                nomeVelho = nome
        
    if sexo == 'F':
        contMulher += 1
        if i == 1:
            idadeMulher = idade
        else: 
            if idade < 20:
                idadeMulher = idade
                contIdade += 1
print()
print('-=-' * 20)
print(texto.center(60, ' '))
print('-=-' * 20)


print(f'Ao todo temos {contHomem} homens e {contMulher} mulheres')
print(f'A média de idade do grupo é de {mediaIdade} anos')
print(f'O homem mais velho se chama {nomeVelho}')
print(f'E também temos {contIdade} mulheres abaixo dos 20 anos')

