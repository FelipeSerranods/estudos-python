'''
Exercício - 62
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
mais = 10
total = 0
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end= ' -> ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Acabou!')  
print(f'Ao total foram informados {total} termos')
        