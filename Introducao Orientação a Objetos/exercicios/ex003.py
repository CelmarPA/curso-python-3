""" Exercício: Sistema de Biblioteca - Crie uma classe chamada Livro que representará um livro na biblioteca. O livro
    deve ter os seguintes atributos:

        - Título
        - Autor
        - Ano de Publicação
        - Número de Páginas

    A classe Livro também deve ter os seguintes métodos:
    1. informacoes_livro(): Imprime as informações do livro, incluindo título, autor, ano de publicação e número
    de páginas.
    2. verificar_clasico(): Retorna True se o livro for considerado um "clássico" com base em um critério de sua
    escolha (por exemplo, se tiver mais de 50 anos desde a publicação), e False caso contrário.

    Crie instâncias da classe Livro e teste os métodos para diferentes livros."""

# Importação de pacotes
from exercicios.ex003.lib. classes import *

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[033m', 'blue': '\033[34m',
         'lilas': '\033[1;35m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{"Sistema de Biblioteca":^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização da lista livros
livros_cadastrados = []

# Solicita as informações de cada livro ao usuário
while True:
    titulo = str(input('Digite o título do livro: ')).strip().capitalize()
    auto = str(input('Digite o autor do livro: ')).strip().capitalize()
    publicacao = int(input('Digite o ano de publicação do livro: '))
    paginas = int(input('Digite o número de paginas do livro: '))

    # Cria uma instância do livro e adiciona à lista
    livro = Livro(titulo, auto, publicacao, paginas)
    livros_cadastrados.append(livro)
    opc = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if opc == "N":
        print(f'-' * 45)
        break

# Exibe as informações dos livros adicionados a lista
for livro in livros_cadastrados:
    livro.informacoes_livro()
    livro.verificar_classico()
    print('-' * 45)
print(f'Obrigado por usar nosso sistema. Volte sempre!')
