# ______ Exercício 0088 ______

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

# Importação de bibliotecas
from random import randrange
from time import sleep

# Inicializalção de listas
jogos = list()
numeros = list()

# Solicita a quantidade de jogos ao usuário
quant = int(input('Quantos jogos você quer que eu sorteie? '))

# Imprime o cabeçalho do programa
print(f'=+=' * 3, f'SORTEANDO {quant} JOGOS', f'=+=' * 3)

# Loop for para obteção do números sorteados
for j in range(0, quant):  # Intera a quantidade de jogos informados
    for n in range(0, 6):
        l = numeros.append(randrange(1, 61))  # Randrange escolhe numeros aleatóriamente em um lista
        while l in numeros:  # Se tiver algum número repetido nos jogos seram sorteados novamente
            numeros.append(randrange(1, 61))
    jogos.append(numeros[:])
    numeros.clear()
    jogos[j].sort()
    sleep(1)
    print(f'Jogo {j + 1}: {jogos[j]}')  # Imprime os jogos

print(f'=+=' * 3, f'< BOA SORTE! >', f'=+=' * 3)
