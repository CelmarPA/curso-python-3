# ______ Exercício 00112 ______

# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
# valores que seja monetários.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["blue"]}{"Entrada de Dados Monetários":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Importação de Módulos
from utilidadescev import moeda, dado

p = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
