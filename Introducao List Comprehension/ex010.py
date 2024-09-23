""" Exercício 010 - Dada uma lista de números, crie uma nova lista contendo apenas os números que são quadrados
    perfeitos.

    numbers = [1, 4, 9, 16, 25, 36, 49, 64] """

#  Importação de bibliotecas
from math import isqrt

# Lista de números
numbers = [1, 4, 9, 16, 25, 36, 49, 64]

# Cria uma lista com os quadrados perfeitos
perfeitos = [num for num in numbers if isqrt(num)**2 == num]

# perfeitos = [num for num in numbers if int(num**0.5)**2 == num]

print(perfeitos)
