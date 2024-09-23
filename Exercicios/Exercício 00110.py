# ______ Exercício 00110 ______

# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Reduzindo Ainda Mais o Seu Programa":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Importação de Módulos
from ex110 import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p)
