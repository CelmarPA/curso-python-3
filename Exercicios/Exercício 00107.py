# ______ ex107 ______

# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
# também um programa que importe esse módulo e use algumas dessas funções.

# Lista de cores
cores = {'reset': '\033[m', 'redb': '\033[30;41m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m', 'greenb': '\033[97;42m',
         'blueb': '\033[97;44m', 'whiteb': '\033[30;107m', 'redw': '\033[97;41m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["green"]}{"Exercitando Módulos em Python":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Importação de módulos
from ex107 import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {p} é {moeda.metade(p)}.')
print(f'O dobro de {p} é {moeda.dobro(p)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}.')
print(f'Reduzindo 15%, temos {moeda.diminuir(p, 15)}.')
