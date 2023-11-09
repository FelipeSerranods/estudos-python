'''
Exercício - 70
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

print('-=-' * 20)
print('CARRINHO DE COMPRAS')
print('-=-' * 20)

total = altoValor = cont = 0
baixoValor = ''
while True:
    nomeProduto = input('Nome do produto: ').strip().title()
    valorProduto = float(input('Valor: R$'))
    if valorProduto > 1000:
        altoValor += 1
    cont += 1
    if cont == 1 or valorProduto < menorValor:
        menorValor = valorProduto
        baixoValor = nomeProduto
    total += valorProduto
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja adicionar mais produtos? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram adicionados {cont} produtos ao carrinho e o total da compra deu R${total:.2f}')
print(f'Foram adicionados {altoValor} produtos acima de R$1.000 ao carrinho')
print(f'O produto de menor valor foi {baixoValor} que custou R${menorValor:.2f}')

