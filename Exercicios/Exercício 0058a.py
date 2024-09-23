# ______ Exercício 0058 outra solução ______

# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Jogo da Adivinhação v2.0":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from random import randint

# Inicialização de variáveis
acertou = False
palpites = 0

# Imprime mensagem do computador
print(f'Sou seu computador... \n'
      f'Acabei de pensar em um número entre 0 e 10. \n'
      f'Será que você consegui adivinhar qual foi?')

# Palpite do computador
comp = randint(0, 10)

# Loop while com condições para verificação de acerto
while not acertou:
    # Solicita palpite ao usuário
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print(f'Mais... Tente mais uma vez.')
        elif jogador > comp:
            print(f'Menos... Tente mais uma vez.')
print(f'Acertou com {cores["yellow"]}{palpites}{cores["reset"]} tentativas. {cores["red"]}Parabéns{cores["reset"]}!')
