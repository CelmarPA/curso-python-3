# ______ Exercício 0060 outra solução ______

# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["blue"]}{"Cálculo Fatorial":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

"""
from math import factorial
n = int(input('Difite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O factorial de {n} é {f}.') 
"""

num = int(input('Digite um númerop para calcular seu Fatorial: '))
count = num
fatorial = 1
print(f'Calculando {num}! = ',end='')
while count > 0:
    print(f'{count}', end='')
    print(f' x ' if count > 1 else ' = ', end='')
    fatorial *= count
    count -= 1
print(f'{fatorial}')
