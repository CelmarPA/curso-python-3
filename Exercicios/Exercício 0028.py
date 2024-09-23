# ______ Exercício 0028 ______

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Importação das bibliotecas
from colorama import Fore
from random import randint
from time import sleep

# Imprime o enunciado do programa
print(Fore.YELLOW + f'-=-' * 20)
print(Fore.BLUE + f'Vou pensar em um número entre 0 e 5. Tente adivinha...')
print(Fore.YELLOW + f'-=-' * 20)

num = int(input('Em que número eu pensei? '))  # Pedi o usuário um número

print(Fore.RED + 'PROCESSANDO...')

sleep(2)
pc = randint(0, 5)  # Faz o programa sortear um número de 0 a 5

# Condição para vitoria e derrota do jogador
if num == pc:
    print(Fore.GREEN + f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(Fore.RED + f'GANHEI! Eu pensei no número {pc} e não no {num}!')
