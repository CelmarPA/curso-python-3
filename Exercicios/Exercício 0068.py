# ______ Exercício 0068 ______

# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["red"]}{"Jogo do Par ou Ímpar":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Imprime a apresentação do jogo
print(f'{cores["green"]}=-=' * 10)
print(f'{cores["yellow"]}{"VAMOS JOGAR PAR OU ÍMPAR":^30}')
print(f'{cores["green"]}=-={cores["reset"]}' * 10)

# Importação de bibliotecas
from random import randint

# Inicialização de variáveis
vitorias = 0

# Loop while infinito, verifica o número a opção, e gera o resultado
while True:
    num = int(input('Digite um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I] ')).strip()[0]  # Solicita o opção ao usuário
    while opcao not in 'PpIi':  # Loop while para validação da opção
        print(f'Opção inválida! Tente novamente!')
        opcao = str(input('Par ou Ímpar? [P/I] ')).strip()[0]
    if opcao in 'Pp':
        opcao = 'PAR'
    else:
        opcao = 'ÍMPAR'
    comp = randint(0, 9)  # Gera a escolha do computador aleatoriamente
    soma = num + comp  # Soma o valor do jogador com o valor do computador
    if soma % 2 == 0:  # Defini se a soma é PAR ou ÍMPAR
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    print(f'-' * 60)
    print(f'Você jogou {num} e o computador jogou {comp}. Total de {soma} deu {result}!')
    print(f'-' * 60)
    if result != opcao:  # Se o resultado for diferente da opção i computador vence e o jogo encerra
        jogador = f'{cores["red"]}PERDEU{cores["reset"]}'
        break
    else:  # Caso o jogador vença o programa continua e aumenta o contador de vitórias
        jogador = f'{cores["green"]}VENCEU{cores["reset"]}'
        vitorias += 1
    print(f'Você {jogador}!')
    print(f'Vamos jogar novamente...')
    print(f'=-=' * 10)
    # Imprime a derrota e a quantidade de vitórias
print(f'Voce {jogador}!')
print(f'=-=' * 10)
print(f'{cores["red"]}GAME OVER!{cores["reset"]} Você venceu {cores["blue"]}{vitorias}{cores["reset"]} vezes.')
