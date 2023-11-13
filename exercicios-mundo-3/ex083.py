'''
Exercício - 83
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
expressao = input('Digite sua expressão: ')
par = []
for simbolo in expressao:
    if simbolo == '(':
        par.append(simbolo)
    elif simbolo == ')':
        if len(par) > 0:
            par.pop()
if len(par) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta')
    print(f'Há {len(par)} parenteses sem fechar')
        