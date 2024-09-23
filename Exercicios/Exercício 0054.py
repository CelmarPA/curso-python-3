# ______ Exercício 0054 ______

# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores. Maioridade 21 anos.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Avaliador de Maioridade ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from datetime import datetime

# Inicialização de variáveis
atual = datetime.today().year
maior = 0
menor = 0

# Loop para avaliar as idade
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if ano < atual:
        idade = atual - ano
        if idade >= 21:
            maior += 1
        else:
            menor += 1
    else:
        quit(f'Data inserida inválida" Tente novamente!')

# Imprime o resultado
print(f'Ao todo tivemos {cores["yellow"]}{maior}{cores["reset"]} pessoas {cores["blue"]}maiores{cores["reset"]} '
      f'de idade.')
print(f'E também tivemos {cores["yellow"]}{menor}{cores["reset"]} pessoas {cores["green"]}menores{cores["reset"]}'
      f' de idade.')
