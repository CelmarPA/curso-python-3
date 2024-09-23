""" Exercício 008 - Dada uma lista de números, crie uma nova lista contendo apenas os números divisíveis por
    3 e 5.

    numbers = [15, 30, 7, 45, 60, 21, 10] """

# Lista de números
numbers = [15, 30, 7, 45, 60, 21, 10]

# Cria lista com número divisíveis por 3 e 5
divisiveis = [numeros for numeros in numbers if numeros % 5 == 0 and numeros % 3 == 0]

print(divisiveis)
