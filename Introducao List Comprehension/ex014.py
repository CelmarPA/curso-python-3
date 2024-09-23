""" Exercício 014 - Você tem uma lista de palavras. Sua tarefa é criar uma nova lista contendo as palavras que são
    anagramas de pelo menos outra palavra na lista. Um anagrama é uma palavra ou frase formada pela reorganização
    das letras de outra palavra, ou frase.

    words = ['listen', 'silent', 'enlist', 'heart', 'earth', 'night', 'thing', 'python', 'typhon', 'game', 'mega']

    Crie uma nova lista chamada 'anagrams' contendo as palavras que são anagramas de pelo menos outra palavra na
    lista. Lembre-se de que um anagrama precisa ter as mesmas letras, mas em uma ordem diferente. """

# Lista de palavras
words = ['listen', 'silent', 'enlist', 'heart', 'earth', 'night', 'thing', 'python', 'typhon', 'game',
         'mega', 'casa', 'mapa']


# Função para verificar anagramas
def anagramas(palavra1, palavra2):
    return set(palavra1) == set(palavra2) and len(palavra1) == len(palavra2)


# Cria a lista com os anagramas
anagrams = [palavra for palavra in words if any(anagramas(palavra,  outra) for outra in words if outra != palavra)]

print(anagrams)
