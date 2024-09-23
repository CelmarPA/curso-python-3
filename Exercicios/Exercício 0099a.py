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
def maior(* num):
    count = maior = 0
    print(f'-=' * 30)
    print(f'Analisando os valores passados...')
    sleep(1.0)
    for valor in num:
        print(f'{valor} ', end="")
        sleep(0.3)
        if count == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        count += 1
    print(f'Foram informados {count} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
