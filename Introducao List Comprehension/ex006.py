""" Exercício 006 - Dada uma lista de strings, crie uma nova lista contendo todas as letras maiúsculas das palavras.
    strings = ['hello', 'world', 'python'] """

# Lista de palavras
strings = ['hello', 'world', 'python']

# Cria uma lista contendo todas as letras maiúsculas das palavras
maiusculas = [letra.upper() for palavra in strings for letra in palavra]

print(maiusculas)
