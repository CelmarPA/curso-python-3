# ______ Exercício 0075 ______

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["red"]}{"Análise de Dados em Uma Tupla":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Solicita os número ao usuário
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

# Transforma a listas dos números em uma tupla
numeros = (n1, n2, n3, n4)

# Imprime os resultados
print(f'Você digitou os valores {numeros}.')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 not in numeros:
    print(f'O valor 3 não foi digitado em nehuma posição.')
else:
    print(f'O valor 3 apareceu {numeros.index(3) + 1}ª posição.')
print(f'Os valores pares digitados foram: ')
for p in range(len(numeros)):
    if numeros[p] % 2 == 0:
        print(f'{numeros[p]} ', end='')


# ______ Exercício 0075 ______

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)}.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nehuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
