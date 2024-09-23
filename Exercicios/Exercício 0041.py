# ______ Exercício 0041 ______

# A Confederação  Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# -> Até 9 anos: MIRIM
# -> Até 14 anos: INFANTIL
# -> Até 19 anos: JUNIOR
# -> Até 25 anos: SÊNIOR
# -> Acima : MASTER

# Importação de bibliotecas
from datetime import datetime

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'black': '\033[30m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{"Classificador de Atletas":^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Solicita o ano de nascimento ao usuário
ano = int(input('Ano de nascimento: '))

# Cálculo da idade
atual = datetime.today().year
idade = atual - ano

if idade <= 9:
    categoria = f'{cores["green"]}MIRIM{cores["reset"]}'
elif idade <= 14:
    categoria = f'{cores["blue"]}INFANTIL{cores["reset"]}'
elif idade <= 19:
    categoria = f'{cores["yellow"]}JUNIOR{cores["reset"]}'
elif idade <= 25:
    categoria = f'{cores["red"]}SÊNIOR{cores["reset"]}'
else:
    categoria = f'{cores["black"]}MASTER{cores["reset"]}'

# Imprime o resultado avaliação
print(f'O atleta tem {cores["blue"]}{idade}{cores["reset"]} anos.')
print(f"Classificação: {categoria}")
