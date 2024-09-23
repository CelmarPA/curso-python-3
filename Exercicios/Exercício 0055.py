# ______ Exercício 0055 ______

# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Balança Avaliadora ":=^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização das variáveis
count = 0
pesos = []  # Lista vazia

# Loop para avaliar os pesos
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa em Kg: '))
    pesos.append(peso)

print(f'O maior peso lido foi de {cores["red"]}{max(pesos)}{cores["reset"]}Kg.')
print(f'O menor peso lido foi de {cores["green"]}{min(pesos)}{cores["reset"]}Kg.')

# ______ Exercício 0055 outra solução______
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')
