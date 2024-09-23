""" Exercício 009 - Dada uma lista de strings, crie uma nova lista contendo as strings invertidas.

    strings = ['hello', 'world', 'python'] """

# Lista de strings
strings = ['hello', 'world', 'python']

# Cria uma lista contendo as strings invertidas
invertidas = [''.join(reversed(palavra)) for palavra in strings]

print(invertidas)

# Lista de strings
strings = ['hello', 'world', 'python']
