# ______ Exercício 0078 ______

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["green"]}{"Maior e Menor Valores na Lista":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
numeros = list()

# Loop while para solicitar os números
for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {i}: ')))

# Define o maior e o menor valor
maior = max(numeros)
menor = min(numeros)

print(f'-=-' * 20)
print(f'Você digitou os valores {numeros}')  # Imprime a lista
print(f'O maior valor digitado foi {maior} nas posições ', end='')  # Imprime o maior valor e a posição

# Loop para indice do maior valor
for index, m in enumerate(numeros):
    if m == maior:
        print(f'{index}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')

for index, n in enumerate(numeros):
    if n == menor:
        print(f'{index}... ', end='')

# Digite um valor para a Posição {0}: 7
# Digite um valor para a Posição {1}: 2
# Digite um valor para a Posição {2}: 9
# Digite um valor para a Posição {3}: 8
# Digite um valor para a Posição {4}: 3

# -=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=-
# Você digitou os valores [7, 2, 9, 8, 3]
# O maior valor digitado foi 9 nas posições 2...
# O menor valor digitado foi 2 nas posições 1...
