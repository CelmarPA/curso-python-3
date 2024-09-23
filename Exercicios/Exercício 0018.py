# ______ Exercício 0018 ______

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, radians, sin, tan

num = float(input('Digite o ângulo que você deseja: '))

ang = radians(num)

print(f'O ângulo de {num:.1f} tem o seno de {sin(ang):.2f}.')
print(f'O ângulo de {num:.1f} tem o cosseno de {cos(ang):.2f}.')
print(f'O ângulo de {num:.1f} tem a tangente de {tan(ang):.2f}.')
