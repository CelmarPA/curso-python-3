# ______ Exercício 00104 ______

# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["yellow"]}{"Validando Entrada de Dados em Python":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)


# Função para ler apenas um número inteiro
def leiaInt(n):
    while True:
        if n.isnumeric():
            return int(n)
        else:
            print(f'{cores["red"]}ERRO! Digite um número inteiro válido.{cores["reset"]}')
            n = str(input('Digite um número: '))


print(f'_' * 30)
n = (input('Digite um número: '))
print(f'Você acabou de digitar o número {leiaInt(n)}.')
