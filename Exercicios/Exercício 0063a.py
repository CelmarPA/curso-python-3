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

# Solicita um número ao usuário
num = int(input('Quantos termos você quer mostrar? '))

# Incialização de variaveis
t1 = 0
t2 = 1
count = 3

print(f'~' * 60)
print(f'{t1} → {t2} → ', end='')

# Loop while para cálculo de Fibonacci
while count <= num:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    count += 1
print(f'FIM!')
print(f'~' * 60)
