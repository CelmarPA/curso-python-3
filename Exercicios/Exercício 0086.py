# ______ Exercício 0086 ______

# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre
# a matriz na tela, com a formatação correta.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["blue"]}{"Matriz em Python":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
matriz = [[], [], []]

# Loop para obtenção do dados e geração da lista que será a matriz
for n in range(len(matriz)):
    for i in range(0, 3):
        num = int(input(f'Digite um valor para [{n}, {i}]: '))
        matriz[n].insert(i, num)
print(f'-=-' * 20)
# Loop para imprimir a matriz no formato
for r in range(len(matriz)):
    for t in range(len(matriz)):
        print(f'[{matriz[r][t]:^5}]', end='')
    print(f'')
print(f'-=-' * 20)