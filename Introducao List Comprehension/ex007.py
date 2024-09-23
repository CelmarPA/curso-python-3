""" Exercício 007 - Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que têm mais de três
    letras e começam com a letra 'a'.

    words = ['apple', 'banana', 'orange', 'avocado', 'kiwi', 'grape'] """

# Lista de palabras
words = ['apple', 'banana', 'orange', 'avocado', 'kiwi', 'grape']

# Cria a lista que contem apenas as palavras que tem mais de 3 letras e começam com a letra 'a'
lista = [palavras for palavras in words if len(palavras) > 3 and palavras[0] == 'a']

print(lista)
