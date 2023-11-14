'''
Exercício - 85
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
listaNum = [ [], [] ]
for i in range(1,8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        listaNum[0].append(num)
    else:
        listaNum[1].append(num)

listaNum[0].sort()
listaNum[1].sort()

print(f'Os valores digitados foram: {listaNum}')
print(f'Os valores pares ordenados são {listaNum[0]}')
print(f'Os valores impares ordenados são {listaNum[1]}')