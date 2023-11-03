n = int(input('Digite um número para ver sua tabuada: '))

for i in range(10):
    i += 1
    n * i
    print(f'{n} x {i} = {n * i}')