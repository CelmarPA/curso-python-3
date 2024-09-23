# ______ Exercício 0017 ______

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotensa.

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print(f'A hipotenusa vai medir {hypot(co, ca):.2f}.')

# ______ Exercício 0017 outra solução ______

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'A hipotenusa vai medir {hi:.2f}.')
