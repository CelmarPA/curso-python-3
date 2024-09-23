""" Exercício 004 - Dada uma lista de palavras, crie uma nova lista contendo o comprimento de cada palavra.
    words = ['python', 'programming', 'is', 'fun'] """

# Lista de palavras
words = ['python', 'programming', 'is', 'fun']

# Cria uma lista com o comprimento de cada lavra
comprimento = [len(palavra) for palavra in words]

print(comprimento)
