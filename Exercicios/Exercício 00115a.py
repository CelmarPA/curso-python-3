# ______ Exercício 00115a ______

# Vamos criar um menu em Python, usando modularização.

# Lista de cores
c = ('\033[m',  # 0 - sem cor
     '\033[0;31m',  # 1 - vermelho
     '\033[0;32m',  # 2 - verde
     '\033[0;33m',  # 3 - amarelo
     '\033[0;34m',  # 4 - azul
     '\033[0;35m',  # 5 - roxo
     '\033[7;97m'  # 6 - branco
     )

# Imprime o título do programa
print(f'{c[2]}-=-' * 20)
print(f'{c[4]}{"SISTEMA ARQUIVO v1.0":^60}')
print(f'{c[2]}-=-{c[0]}' * 20)

# Importaçãp de Módulos e Bibliotecas
from ex115.lib. interface import *
from time import sleep

# Programa principal
while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        cabecalho(f'Opção 1')
    elif opcao == 2:
        cabecalho(f'Opção 2')
    elif opcao == 3:
        cabecalho(f'Saindo do sistema... Até logo!')
        break
    else:
        print(f'{c[1]}ERRO! Digite uma opção válida!{c[0]}')
    sleep(2)


# -----------------------------------
#           MENU PRINCIPAL
# ------------------------------------
# 1 - Ver pessoas cadastradas
# 2 - Cadastrar nova Pessoa
# 3 - Sair do Sistema
# ------------------------------------
# Sua opção: 1
# -----------------------------------
#         PESSOAS CADASTRADAS
# ------------------------------------
# Celmar Pereira             33 anos
# -----------------------------------
#           MENU PRINCIPAL
# ------------------------------------
# 1 - Ver pessoas cadastradas
# 2 - Cadastrar nova Pessoa
# 3 - Sair do Sistema
# ------------------------------------
# Sua opção: 2
# -----------------------------------
#           NOVO CADASTRO
# ------------------------------------
# Nome: Zuleide Lima
# Idade: 55
# Registro de Zuleide Lima adicionado.
# -----------------------------------
#           MENU PRINCIPAL
# ------------------------------------
# 1 - Ver pessoas cadastradas
# 2 - Cadastrar nova Pessoa
# 3 - Sair do Sistema
# ------------------------------------
# Sua opção: 7
# Erro! Digite uma opção válida!
# -----------------------------------
#           MENU PRINCIPAL
# ------------------------------------
# 1 - Ver pessoas cadastradas
# 2 - Cadastrar nova Pessoa
# 3 - Sair do Sistema
# ------------------------------------
# Sua opção: 2
# -----------------------------------
#           NOVO CADASTRO
# ------------------------------------
# Nome: Pedro Pereira Paulo
# Idade: trinta
# ERRO: por favor, digite um número inteiro valido.
# Idade: trinta
