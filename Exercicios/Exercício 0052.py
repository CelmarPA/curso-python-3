# ______ Exercício 0052 ______

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Classificador de Número Primos ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solicita um número ao usúario
num = int(input(f'Digite um número: '))

# Inicialização de variáveis
count = 0

# Loop para classificação dos números primos
for i in range(1, num + 1):
    if num % i == 0 and num / 1 == num:
        count += 1
        print(f'{cores["yellow"]}', end='')
    else:
        print(f'{cores["red"]}', end='')
    print(f'{i}{cores["reset"]}', end=' ')
print(f'\nO número {cores["blue"]}{num}{cores["reset"]} foi divisível {cores["yellow"]}{count}{cores["reset"]} vezes.')
if count == 2:
    print(f'Por isso ele é {cores["green"]}PRIMO{cores["reset"]}!')
else:
    print(f'Por isso ele {cores["red"]}NÃO É PRIMO{cores["reset"]}!')
