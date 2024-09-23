# ______ Exercício 00106 ______

# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

# Lista de cores
cores = {'reset': '\033[m', 'redb': '\033[30;41m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m', 'greenb': '\033[97;42m',
         'blueb': '\033[97;44m', 'whiteb': '\033[30;107m', 'redw': '\033[97;41m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Analisando e gerando Dicionários":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


# Função help
def ajuda(msg):
    from time import sleep
    print(f'{cores["blueb"]}~' * 40)
    print(f'Acessando o manual do comando {msg}'.center(40))
    print(f'~' * 40)
    sleep(1.0)
    print(f'{cores["whiteb"]}')
    return help(msg)


# Programa principal
while True:
    print(f'{cores["greenb"]}~' * 30)
    print(f'SISTEMA DE AJUDA PyHELP'.center(30))
    print(f'~' * 30)
    pesq = ''
    pesq = str(input(f'{cores["reset"]}Função ou Biblioteca > ')).strip().lower()
    if pesq == 'fim':
        print(f'{cores["redw"]}~' * 15)
        print(f'ATÉ LOGO!'.center(15))
        print(f'~' * 15)
        break
    elif not pesq.isalpha():
        print(f'{cores["redb"]}ERRO! Opção inválida, tente novamente!{cores["reset"]}')
        pesq = str(input(f'Função ou Biblioteca > '))
    print(ajuda(pesq))
