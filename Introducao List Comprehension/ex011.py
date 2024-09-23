""" Exercício 011 - Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que são palíndromas
    (iguais quando lidas de trás para frente).

    words = ['radar', 'level', 'python', 'civic', 'language'] """

# Lista de palavras
words = ['radar', 'level', 'python', 'civic', 'language']

# Cria uma lista contendo apenas as palavras palíndromas
palindromas = [palavra for palavra in words if ''.join(reversed(palavra)) == palavra]

print(palindromas)
