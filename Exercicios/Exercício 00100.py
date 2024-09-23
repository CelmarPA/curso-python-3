# ______ Exercício 00100 ______

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Função que Descobre o Maior":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from random import randint
from time import sleep

# Inicialização de listas
numeros = list()


# Função de sorteio
def sorteia(lista):
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(f'Sorteando {len(lista)} valores da lista: ', end='')
    for i, v in enumerate(lista):
        print(f'{v} ', end='')
        sleep(0.5)
    print(f'PRONTO!')
    sleep(0.5)


# Função de soma dos valores pares
def somapar(lista):
    soma = 0
    for i, v in enumerate(lista):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}.')


# Programa principal
sorteia(numeros)
somapar(numeros)
