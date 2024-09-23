# ______ Exercício 00111 ______

# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as
# funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Transformando Módulos em Pacotes":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


# Importação de Módulos
from utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)
