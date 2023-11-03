diasAlugado = int(input('Digite quantos dias ele foi alugado: '))
kmPercorridos = float(input('Digite a quantidade de km percorridos: '))

valorPagar = (60 * diasAlugado) + (0.15 * kmPercorridos)

print(f'O valor a pagar será de R${valorPagar:.2f}')