# ______ Exercício 00101 ______

# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["red"]}{"Função Para Votação":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)


def voto(ano):
    """
    -> Função para verificação de obrigatoriedade de voto.
    :param ano: O ano do nascimento.
    :return: Retorna a avaliação do voto.
    """
    # Importação de biblioteca
    from datetime import datetime
    # Calculo da idade
    atual = datetime.now().year
    idade = atual - ano
    # Analise do voto
    print(f'Com {idade} anos: ', end='')
    if 16 <= idade < 18 or idade >= 65:
        return 'VOTO FACULTATIVO!'
    elif 18 <= idade < 65:
        return 'VOTO OBRIGATORIO!'
    else:
        return 'NÃO VOTA!'


# Programa principal
print(f'_' * 30)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
