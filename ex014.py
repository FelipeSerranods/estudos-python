'''
Exercício - 14
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
celcius = float(input('Digite a temperatura em °C: '))

fahrenheit = (celcius * 1.8) + 32

print(f'A temperatura de {celcius}°C convertida para fahrenheit é {fahrenheit}°F')