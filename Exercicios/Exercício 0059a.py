# ______ Exercício 0059 outra solução ______

# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Calculadora com Menu de Opões":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

