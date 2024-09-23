# ______ Exercício 00113 ______

# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["blue"]}{"Funções Aprofundadas em Python":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except (ValueError, TypeError):
            print(f'{cores["red"]}ERRO: Por favor, digite um número inteiro válido.{cores["reset"]}')
        except KeyboardInterrupt:
            print(f'\n{cores["red"]}O usuário preferiu não digitar este número.{cores["reset"]}')
            return 0
    return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n.is_integer():
                raise ValueError
            break
        except (ValueError, TypeError):
            print(f'{cores["red"]}ERRO: Por favor, digite um número real válido.{cores["reset"]}')
        except KeyboardInterrupt:
            print(f'\n{cores["red"]}O usuário preferiu não digitar este número.{cores["reset"]}')
            return 0
    return n


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real {real}!')
