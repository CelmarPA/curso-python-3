# ______ Exercício 0088 outra solução ______

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Palpites Para a Mega Sena":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

print(f'-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print(f'-' * 30)

from random import randint
from time import sleep

lista = list()
jogos = list()
count = 0

quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

# Imprime o cabeçalho do programa
print(f'=+=' * 3, f'SORTEANDO {quant} JOGOS', f'=+=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print(f'=+=' * 3, f'< BOA SORTE! >', f'=+=' * 3)
