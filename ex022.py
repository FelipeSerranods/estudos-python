'''
Exercício - 22
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nomeCompleto = str(input('Digite seu nome: ')).strip()
nomeSemEspaco = nomeCompleto.replace(' ','')
primeiroNome = nomeCompleto.split()
print('Analisando seu nome...')
print(f'Seu nome em maiscúlas fica: {nomeCompleto.upper()}')
print(f'Seu nome em minúsculas fica: {nomeCompleto.lower()}')
print(f'Seu nome tem {len(nomeSemEspaco)} letras')
print(f'Seu primeiro nome tem {len(primeiroNome[0])} letras')
