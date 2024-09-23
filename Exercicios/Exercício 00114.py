# ______ Exercício 00114 ______
import requests

# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Site Está Acessível?":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


def status(url):
    from requests import get
    try:
        resp = get(url)
        if resp.status_code == 200:
            print(f'Consegui acessar o site \"{url}\" com sucesso!')
        else:
            print(f'O site \"{url}\" não está acessível no momento.')
    except requests.ConnectionError:
        print(f'Não foi possível conectar ao site {url}!')


site = "https://www.pudim.com.br"
status(site)
