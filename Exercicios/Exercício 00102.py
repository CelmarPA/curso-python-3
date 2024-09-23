# ______ Exercício 00102 ______

# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["yellow"]}{"Função Para Fatorial":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)


def fatorial(num, show=False):
    """
    -> Função para calcular fatorial de número.
    :param num: O número que deseja calcular o fatorial.
    :param show: (opcional) Para mostrar ou não o processo de cálculo do fatorial.
    :return: Returna o fatorial calculado de um número.
    """
    print(f'_' * 30)
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show is True:
            print(f'{c}', end='')
            print(f' x ' if c > 1 else ' = ', end='')
    return f


# Programa principal
print(fatorial(5, True))
help(fatorial)
