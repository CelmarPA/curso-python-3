# ______ Exercício 0091 outra solução ______

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["green"]}{"Jogo de Dados em Python":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from operator import itemgetter
from random import randint
from time import sleep

# Inicialização de dicionários e listas
jogadas = dict()
ordem = list()

print(f'Valores sorteados:')
for i in range(1, 5):
    jogadas[f'jogador{i}'] = randint(1, 6)

# Imprime valores sorteados de cada jogador
for c, k in jogadas.items():
    print(f'O {c} tirou {k} no dado.')
    sleep(1)
print(f'-=-' * 10)

# Coloca o dicionário em ordem pelos valores
ordem = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print(f'== RANKING DOS JOGADORES =='. center(30))
sleep(1)
# Imprime o resultado
for c, k in enumerate(ordem):
    print(f'{c + 1}º lugar: {k[0]} com {k[1]}.'.center(30))
    sleep(1)
