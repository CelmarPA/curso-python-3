# ______ Exercício 0045 ______

# Crie um programa que faça o computador jogar Jokenpô com você.

# Importação de biblioteca
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
print(f'''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOUSA''')
jogador = int(input('Qual é a sua jogada? '))
print(f'JO')
sleep(1)
print(f'KEN')
sleep(1)
print(f'PO')
print(f'-=' * 12)
print(f'Computador jogou {itens[computador]}.')
print(f'Jogador jogou {itens[computador]}.')
print(f'-=' * 12)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:  # Jogador jogou PEDRA
        print(f'EMPATE!')
    elif jogador == 1:  # Jogador jogou PAPEL
        print(f'JOGADOR VENCE!')
    elif jogador == 2:  # Jogador jogou TESOURA
        print(f'COMPUTADOR VENCE!')
    else:
        print(f'JOGADA INVÁLIDA!')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:  # Jogador jogou PEDRA
        print(f'COMPUTADOR VENCE!')
    elif jogador == 1:  # Jogador jogou PAPEL
        print(f'EMPATE!')
    elif jogador == 2:  # Jogador jogou TESOUSA
        print('JOGADOR VENCE!')
    else:
        print(f'JOGADA INVÁLIDA!')
elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:  # Jogador jogou PEDRA
        print(f'JOGADOR VENCE!')
    elif jogador == 1:  # Jogador jogou PAPEL
        print(f'COMPUTADOR VENCE!')
    elif jogador == 2:  # Jogador jogou TESOUSA
        print(f'EMPATE!')
    else:
        print(f'JOGADA INVÁLIDA!')
