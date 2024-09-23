# ______ Exercício 0078 outra solução ______

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["green"]}{"Maior e Menor Valores na Lista":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

listnum = []
maior = 0
menor = 0

for c in range(0, 5):
    listnum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listnum[c]
    else:
        if listnum[c] > maior:
            maior = listnum[c]
        if listnum[c] < menor:
            menor = listnum[c]

print(f'-=-' * 20)
print(f'Você digitou os valores {listnum}')  # Imprime a lista
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listnum):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listnum):
    if v == menor:
        print(f'{i}... ', end='')
