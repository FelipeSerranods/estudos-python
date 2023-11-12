'''
Exercício - 73
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Fluminense.
'''

timesBrasileirao = ("Botafogo", "Palmeiras", "Bragantino", "Grêmio", "Flamengo", "Atlético-MG", "Athletico-PR", "Fluminense", "São Paulo", "Fortaleza", "Internacional", "Cuiabá", "Corinthians", "Santos", "Bahia", "Vasco", "Cruzeiro", "Goiás", "Coritiba", "América-MG")

print('-=-' * 20)
print(f'Lista de times do Brasileirão: {timesBrasileirao}')
print('-=-' * 20)
print(f'Os 5 primeiros são: {timesBrasileirao[:5]}')
print('-=-' * 20)
print(f'Os 4 últimos são: {timesBrasileirao[-4:]}')
print('-=-' * 20)
print(f'Times em ordem alfabética: {sorted(timesBrasileirao)}')
print('-=-' * 20)
print(f'O Fluminense está na {timesBrasileirao.index("Fluminense") +1 }ª posição')
