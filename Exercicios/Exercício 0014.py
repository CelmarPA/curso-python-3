# ______ Exercício 0014 ______

# Escreva um programa que converta uma temperatura digitada em °C para °F.

t = float(input('Informe a temperatura em °C: '))

far = (t * (9 / 5)) + 32

print(f'A temperatura de {t:.2f}°C corresponde a {far:.2f}°F.')
