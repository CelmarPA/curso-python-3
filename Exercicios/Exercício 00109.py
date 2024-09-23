# ______ Exercício 00109 ______

# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["red"]}{"Formatando Moedas em Python v2.0":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Importação de Módulos
from ex109 import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 50, True)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(p, 50, True)}')
