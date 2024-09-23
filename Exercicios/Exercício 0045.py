# ______ Exercício 0045 ______

# Crie um programa que faça o computador jogar Jokenpô com você.

# Importação de bibliotecas
from random import randint
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Joken Pyhton ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Imprime as opções do jogador
print(f'''Suas opões:
[ {cores["red"]}0{cores["reset"]} ] {cores["red"]}PEDRA{cores["reset"]}
[ {cores["green"]}1{cores["reset"]} ] {cores["green"]}PAPEL{cores["reset"]}
[ {cores["blue"]}2{cores["reset"]} ] {cores["blue"]}TESOURA{cores["reset"]}''')

# Solicita a jogada do jogador
jog = int(input('Qual é a sua jogada? '))

# Computador sorteia sua jogada
comp = randint(0, 2)

# Inicializar variaveis
vencedor = ''

# Lista de jogadas
jogadas = {0: 'Pedra', 1: 'Papel', 2: 'Tesoura'}

print(f'{cores["yellow"]}JO{cores["reset"]}')
sleep(0)
print(f'{cores["yellow"]}KEN{cores["reset"]}')
sleep(0)
print(f'{cores["yellow"]}PO!!!{cores["reset"]}')

# Analisar quem
if (jog == 0 and comp == 2) or (jog == 1 and comp == 0) or (jog == 2 and comp == 1):
    vencedor = 'JOGADOR'
    print(f'{cores["yellow"]}-={cores["reset"]}' * 15)
    print(f'Computador jogou {jogadas[comp]}')
    print(f'Jogador jogou {jogadas[jog]}')
    print(f'{cores["yellow"]}-={cores["reset"]}' * 15)
    print(f'{cores["blue"]}{vencedor}{cores["reset"]} VENCE!!!')
elif (comp == 0 and jog == 2) or (comp == 1 and jog == 0) or (comp == 2 and jog == 1):
    vencedor = 'COMPUTADOR'
    print(f'{cores["yellow"]}-={cores["reset"]}' * 15)
    print(f'Computador jogou {jogadas[comp]}')
    print(f'Jogador jogou {jogadas[jog]}')
    print(f'{cores["yellow"]}-={cores["reset"]}' * 15)
    print(f'{cores["blue"]}{vencedor}{cores["reset"]} VENCE!!!')
elif jog == comp:
    print(f'{cores["yellow"]}-={cores["reset"]}' * 15)
    print(f'Computador jogou {jogadas[comp]}')
    print(f'Jogador jogou {jogadas[jog]}')
    print(f'{cores["yellow"]}-={cores["reset"]}' * 15)
    print(f'{cores["blue"]}EMPATE{cores["reset"]}!!!')
else:
    print(f'{cores["red"]}Jogada invalida, tente novamente!{cores["reset"]}')
