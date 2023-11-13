'''
Exercício - 79
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valores = []
while True:
    num = int(input('Digite um valor: '))
    while num in valores:
        print('Valor duplicado! Tente novamente...')
        num = int(input('Digite um valor: '))
    print('O valor foi adicionado com sucesso...')
    valores.append(num)
    escolha = ' '
    escolha = input('Deseja adicionar mais algum? [S/N]: ').strip().upper()
    while escolha not in 'SsNn':
        print('Digite S para continuar ou N para sair')
        escolha = input('Deseja adicionar mais algum? [S/N]: ').strip().upper()
    if escolha == 'N':
        break

print(f'\nOs valores digitados em ordem crescente foram: {sorted(valores)}')    