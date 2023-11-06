'''
Exercício - 43
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

IMC abaixo de 18,5: Abaixo do Peso

Entre 18,5 e 25: Peso Ideal

25 até 30: Sobrepeso

30 até 40: Obesidade

Acima de 40: Obesidade Mórbida
'''

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / pow(altura, 2)
print('-' * 20)
print('Tabela IMC')
print('IMC abaixo de 18,5: Abaixo do Peso')
print('IMC entre 18,5 e 25: Peso Ideal')
print('IMC de 25 até 30: Sobrepeso')
print('IMC de 30 até 40: Obesidade')
print('IMC acima de 40: Obesidade Mórbida')
print('-' * 20)

if imc > 40:
    print(f'Seu imc é {imc:.2f}, você está com obesidade mórbida')
elif imc > 30 and imc <= 40:
    print(f'Seu imc é {imc:.2f}, você está com obesidade')
elif imc > 25 and imc <= 30:
    print(f'Seu imc é {imc:.2f}, você está com sobrepeso')
elif imc > 18.5 and imc <= 25:
    print(f'Seu imc é {imc:.2f}, você está com o peso ideal')
else:
    print(f'Seu imc é {imc:.2f}, você está abaixo do peso')

