'''
Exercício - 77
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
frases = ('Prato', 'Mouse', 'Teclado', 'Monitor', 'Cadeira', 'Mesa', 'Livro', 'Caneta')

for palavra in frases:
    print(f'\nNa palavra {palavra} temos: ',end='')
    for vogal in palavra:
        if vogal.lower() in 'a,e,i,o,u':
            print(vogal,end=' ')
    