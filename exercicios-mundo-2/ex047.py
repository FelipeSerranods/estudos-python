'''
Exercício - 47
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
#Mais trabalhoso
for i in range (0, 51):
    if i % 2 == 0:
        print(i,end=" ")

print()
print('-=-' * 20)

#Jeito mais simples
for c in range (0, 51, 2):
    print(c,end=" ")
    