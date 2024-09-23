# ______ Exercício 0063 ______

# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Gerador de Sequência de Fibonacci":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Incialização de listas
t = {0: 0, 1: 1}

# Incialização de variáveis
i = 2

# Solicita um número ao usuário
num = int(input('Quantos termos você que sejam mostrados? '))

print(f'~' * 60)
print(f'{t[0]} → {t[1]} → ', end='')

# Loop while para calculo de Fibonacci
while i < num:
    t[i] = t[i - 1] + t[i - 2]
    print(f'{t[i]} → ', end='')
    i += 1
print(f'FIM!')
print(f'~' * 60)
