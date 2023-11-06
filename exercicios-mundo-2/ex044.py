'''
Exercício - 44
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

à vista dinheiro/cheque: 10% de desconto

à vista no cartão: 5% de desconto

em até 2x no cartão: preço formal 

3x ou mais no cartão: 20% de juros
'''
valorProduto = float(input('Informe o valor do produto: '))

print(f'Sua compra deu R${valorProduto:.2f} qual a forma de pagamento?')
print('[ 1 ] à vista dinheiro/cheque: 10% de desconto')
print('[ 2 ] à vista no cartão: 5% de desconto')
print('[ 3 ] em até 2x no cartão: preço formal ')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
formaPag = int((input('Opcão: ')))

if formaPag == 1:
    desconto = valorProduto * 0.9
    print(f'O valor R${valorProduto:.2f} com desconto de 10% ficará R${desconto:.2f}')
elif formaPag == 2:
    desconto = valorProduto * 0.95
    print(f'O valor R${valorProduto:.2f} com desconto de 5% ficará R${desconto:.2f}')
elif formaPag == 3:
    valorPag = valorProduto / 2
    print(f'O valor R${valorProduto:.2f} em 2x no cartão será de R${valorPag:.2f}')
elif formaPag == 4:
    vezesCartao = int(input('Em quantas vezes?: '))
    juros = valorProduto * 1.2
    valorPag = juros / vezesCartao
    print(f'O valor R${valorProduto:.2f} em {vezesCartao} vezes no cartão será de R${valorPag:.2f}')
else:
    print('Escolha incorreta, por favor escolha de 1 a 4 para forma de pagamento')