# ______ Exercício 0050 ______

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{" Calculadora de Pares ":=^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
soma = 0
count = 0

# Loop para soma dos número pares
for i in range(1, 7):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        count += 1
        soma += num

print(f'Você informou {cores["blue"]}{count} {cores["red"]}PARES{cores["reset"]} e a soma foi'
      f' {cores["green"]}{soma}{cores["reset"]}.')
