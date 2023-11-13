'''
Exercício - 81
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre: 

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
valores = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    escolha = ' '
    escolha = input('Deseja adicionar mais algum? [S/N]: ').strip().upper()
    while escolha not in 'SsNn':
        print('Digite S para continuar ou N para sair')
        escolha = input('Deseja adicionar mais algum? [S/N]: ').strip().upper()
    if escolha == 'N':
        break

print(f'\nForam adicionados {len(valores)} números na lista')
print(f'Os valores digitados em ordem crescente foram: {sorted(valores,reverse = True)}')
if 5 not in valores:
    print(f'O valor 5 não foi encontrado') 
else:
    print('O valor 5 faz parte da lista')