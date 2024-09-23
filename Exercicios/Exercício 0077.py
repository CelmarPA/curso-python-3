# ______ Exercício 0077 ______

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Contador de Vogais em Tupla":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Tupla com as palavras
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

# Loop for para analisar as vogais
for palavra in palavras:  # Pega cada palavra dentro da tupla
    print(f'Na palavra {palavra.upper()} temos ', end='')  # Imprime as palavras
    for letras in palavra:  # Pegas as letras de cada palabvra
        if letras in 'aeiou':  # Verifica se as letrar sao vogais se foram, as imprime
            print(letras, end=' ', )
    print(f'')
