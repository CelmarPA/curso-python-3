# ______ Exercício 0079 outra solução ______

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["yellow"]}{"Valores Únicos em Uma Lista":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

numeros = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print(f'Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado! Não vou adicionar ...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(f'-=-' * 20)
numeros.sort()
print(f'Você digitou os valores {numeros}')