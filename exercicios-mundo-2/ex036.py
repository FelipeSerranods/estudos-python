'''
Exercício - 36
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valorCasa = float(input('Qual o valor da casa que deseja comprar?: '))
salarioComprador = float(input('Informe o seu salário atual: '))
anosPag = int(input('Quantos anos de financiamento? : '))

valorFinanciamento = valorCasa / (anosPag * 12)

if valorFinanciamento > salarioComprador - (salarioComprador * 0.7):
    print(f'Infelizmente seu pedido de financiamento foi recusado, \n O valor do financiamento mensal será de R${valorFinanciamento:.2f} excedendo os 30% de seu salário')
else:
    print('Emprestimo confirmado!')
    print(f'O valor do financiamento mensal será de R${valorFinanciamento:.2f} que será pago pelos proxímos {anosPag} anos conforme solicitado.')


