# ______ Exercício 0097 ______

# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["green"]}{"Um Print Especial":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)


# Função escreva
def escreva(txt):
    i = len(txt) + 4
    print(f'~' * i)
    print(txt.center(i))
    print(f'~' * i)


# Programa principal
texto = str(input('Escreva uma frase: '))
escreva(texto)
