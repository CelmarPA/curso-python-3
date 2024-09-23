# ______ Exercício 0074 ______

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["yellow"]}{"Maior e Menor Valores em Tupla":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from random import randint
from random import sample

numeros = tuple(sample(range(10), 5))

print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')


# ______ Exercício 0074 outra solução ______

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
