# ______ Exercício 00114 ______

# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Site Está Acessível?":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

import urllib.request
import urllib.error
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print(f'O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')

print(site.read())
