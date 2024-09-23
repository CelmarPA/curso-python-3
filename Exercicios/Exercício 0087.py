# ______ Exercício 0087 ______

# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["blue"]}{"Matriz em Python v2.0":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Inicialização de variáveis
soma_par = soma_c3 = maior_l2 = 0

# Loop for para gerar matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        soma_c3 += matriz[l][2]
        if l == 1:
            maior_l2 = 0
        else:
            if matriz[1][c] > maior_l2:
                maior_l2 = matriz[1][c]
# Loop para imprimir a matriz
print(f'-=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print(f'')
print(f'-=-' * 20)
print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_c3}.')
print(f'O maior valor da segunda linha é {maior_l2}.')
print(f'-=-' * 20)
