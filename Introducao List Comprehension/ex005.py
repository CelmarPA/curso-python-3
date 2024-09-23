""" Exercício 005 - Dada uma lista de números, crie uma nova lista contendo apenas os números maiores que 5.
    numbers = [3, 8, 1, 6, 4, 9, 2, 7] """

# Lista de números
numbers = [3, 8, 1, 6, 4, 9, 2, 7]

# Cria uma lista contendo apenas os números maiores que 5
maiores = [maior for maior in numbers if maior > 5]

print(maiores)
