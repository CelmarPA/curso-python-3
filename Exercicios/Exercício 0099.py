# ______ Exercício 0099 ______

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["yellow"]}{"Função que Descobre o Maior":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from time import sleep


# Função que descobre o maior
def maior(num):
    print(f'-=' * 20)
    print(f'Analisando os valores passados...')
    sleep(1.5)
    if len(num) == 0:
        print(f'Foram informados {len(num)} valores.')
        print(f'O maior valor informado foi {len(num)}.')
    else:
        for i, n in enumerate(num):
            print(f'{n} ', end='')
            sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')


# Programa principal
num1 = [2, 9, 4, 5, 7, 1]
maior(num1)
num2 = [4, 7, 0]
maior(num2)
num3 = [1, 2]
maior(num3)
num4 = [6]
maior(num4)
num5 = []
maior(num5)
