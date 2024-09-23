# ______ Exercício 0092 ______

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Cadastro de Trabalhador em Python":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from datetime import datetime

# Inicialização de dicionários
cadastro = dict()

# incialização de variáveis
aposentadoria = 0

# Solicita os dados ao usuário
nome = str(input('Nome: ')).strip()
nascimento = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de Trabalho (0 não possui): '))

# Cálculo da idade
atual = datetime.now().year
idade = atual - nascimento

# Adiciona os calores ao campos no dicionário
cadastro['Nome'] = nome
cadastro['Idade'] = idade
cadastro['CTPS'] = ctps

# Varifica se possui carteira de trabalho
if ctps == 0:
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}.')
elif ctps > 0:
    contrato = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    contribuicao = atual - contrato
    if contribuicao >= 35:
        cadastro['Contratação'] = contrato
        cadastro['Salário: R$'] = salario
        cadastro['Aposentadoria'] = 0
    else:
        aposentadoria = (35 - contribuicao) + idade
        cadastro['Contratação'] = contrato
        cadastro['Salário: R$'] = salario
        cadastro['Aposentadoria'] = aposentadoria
    for k, v in cadastro.items():
        # Imprime a análise
        print(f'{k} tem o valor {v}')
