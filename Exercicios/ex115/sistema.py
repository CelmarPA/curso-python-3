# Importação de Módulos e Bibliotecas
from time import sleep
from ex115.lib. interface import *
from ex115.lib. arquivo import *

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

# Programa principal
arquivo = 'dados.txt'

# Caso o arquivo não exista vai criar um arquivo
if not localizar_arquivo(arquivo):
    gerar_arquivo(arquivo)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        # Opção de listar o conteúdo de um arquivo
        ler_arquivo(arquivo)
    elif opcao == 2:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif opcao == 3:
        cabecalho(f'Saindo do sistema... Até logo!')
        break
    else:
        print(f'{c[1]}ERRO! Digite uma opção válida!{c[0]}')
    sleep(2)
