""" Exercício 003 - Dada uma lista de números, crie uma nova lista contendo apenas os números pares.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] """

# Lista de número
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cria uma lista contendo apenas os números pares
pares = [numero for numero in numbers if numero % 2 == 0]

print(pares)
