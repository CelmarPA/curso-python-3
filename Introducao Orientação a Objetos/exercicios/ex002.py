""" Exercício 002 - Refaça o exercício 001, melhorando o código acrescentando getters e setters e input de dados: """

# Importação de pacotes e classes
from exercicios.ex002.lib. classes import *

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["lilas"]}{"Sistema de Gerenciamento de Funcionários":^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Programa principal

# Funcionário Normal
funcionario_normal = FuncionarioNormal('João', 33, 123456)
funcionario_normal.apresentar()

# Gerente
gerente = Gerente('Maria', 30, 654321, 15)
gerente.apresentar()
