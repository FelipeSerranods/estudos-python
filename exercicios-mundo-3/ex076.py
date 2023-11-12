'''
Exercício - 76
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

prodEscolar = ('Lápis', 2.00, 'Borracha', 5.10, 'Caderno', 15.90, 'Caneta', 3.00, 'Apontador', 1.50, 'Régua', 4.30, 'Mochila', 120.00, 'Estojo', 25.00, 'Cola', 2.50)

print('-=-' * 13)
print(f'{"MATERIAL ESCOLAR 2 IRMÃOS":^35}')
print('-=-' * 13)
for item in range(0, len(prodEscolar)):
    if item % 2 == 0:
        print(f'{prodEscolar[item]:.<25}',end="")
    else:
        print(f'R${prodEscolar[item]:>10.2f}')
print('-=-' * 13)
