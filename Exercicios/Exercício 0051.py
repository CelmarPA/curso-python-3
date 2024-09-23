# ______ Exercício 0051 ______

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}={cores["reset"]}' * 40)
print(f'{cores["blue"]}{" 10 TERMOS DE UMA PA ":^40}{cores["reset"]}')
print(f'{cores["green"]}={cores["reset"]}' * 40)

# Solicita os dados ao usuário
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

# Formula geral de uma PA: PA =  a + (tr) (onde a é o primeiro termo, t o termo e r a razão

# Loop para calcula da PA
for i in range(0, 10):
    PA = termo + (i * razao)
    print(f'{PA} {cores["yellow"]}\u2192{cores["reset"]} ', end='')
print(f'{cores["red"]}ACABOU!{cores["reset"]}')
