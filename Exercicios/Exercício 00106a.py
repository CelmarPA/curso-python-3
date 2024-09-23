# ______ Exercício 00106 outra solução ______

# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

# Lista de cores
cores = {'reset': '\033[m', 'redb': '\033[30;41m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m', 'greenb': '\033[97;42m',
         'blueb': '\033[97;44m', 'whiteb': '\033[30;107m', 'redw': '\033[97;41m'}

c = ('\033[m',  # 0 - sem cor
     '\033[0;97;41m',  # 1 - vermelho
     '\033[0;97;42m',  # 2 - verde
     '\033[0;97;43m',  # 3 - amarelo
     '\033[0;97;44m',  # 4 - azul
     '\033[0;97;45m',  # 5 - roxo
     '\033[7;97m'  # 6 - branco
     )

# Importação de bibliotecas
from time import sleep

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Analisando e gerando Dicionários":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=2):
    tam = len(msg) + 4
    print(c[cor], end='')
    print(f'~' * tam)
    print(f'  {msg}')
    print(f'~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA Pyhelp')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
