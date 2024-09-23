# ______ Exercício 0096 ______

#  Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
#  comprimento) e mostre a área do terreno.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["blue"]}{"Função que Calcula Área":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)


# Função para cálculo de área
def area(l, c):
    a = l * c
    print(f'A área de uma terroa de {l}x{c} é de {a}m².')


# Programa principal
print(f'Controle de Terrenos')
print(f'-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
