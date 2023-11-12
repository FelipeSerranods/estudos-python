'''
Exercício - 72
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeroExtenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")


#jeito 1
while True:
    num = int(input('Digite um número de 0 a 20 para mostra-lo por extenso: '))
    while num < 0 or num > 20:
        num = int(input('Digite um número de 0 a 20, NÚMEROS NEGAVITOS OU MAIORES QUE 20 SÃO INVALIDOS: '))
    for i in range(len(numeroExtenso)):
        if num == i:
            print(f'o número {num} em extenso é {numeroExtenso[i]}')
    escolha = ' '
    escolha = input('Deseja mais algum número S para continuar e N para encerrar o programa[S/N]: ').strip().upper()
    if escolha == 'N':
        break
print('Programa encerrado....')

#jeito 2
'''
numeroExtenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input('Digite um número de 0 a 20 para mostra-lo por extenso: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeroExtenso[num]})
'''