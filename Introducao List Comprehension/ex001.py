""" Exercício 001 - Dada uma lista de números, crie uma nova lista contendo o quadrado de cada número.

    numbers = [1, 2, 3, 4, 5]"""

# Lista de números
numbers = [1, 2, 3, 4, 5]

# Cria uma lista com os quadrados de cada número de numbers
quadrados = [num**2 for num in numbers]

print(quadrados)
