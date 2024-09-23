"""  Exercício 002 - Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que começam com
    a letra 'a'.

    words = ['apple', 'banana', 'orange', 'avocado', 'kiwi'] """

# Lista de palavras
words = ['apple', 'banana', 'orange', 'avocado', 'kiwi']

# Cria uma lista contendo apenas as palavras iniciadas com a letra 'a'
inicia_a = [palavra for palavra in words if palavra[0] == 'a']

print(inicia_a)
