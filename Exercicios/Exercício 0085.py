# ______ Exercício 0085 ______

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["green"]}{"Lista de Pares e Ímpares":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
numeros = list()
pares = list()
impares = list()

# Loop for para obtençãos dos valores
for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}º valor: '))
    if num % 2 == 0:  # Seleciona os valores pares
        pares.append(num)  # Adiciona o valores pares a lista temporária pares
    if num % 2 == 1:  # Seleciona os valores ímpares
        impares.append(num)  # Adiciona os valores ímpares a lista temporária impares

# Adicionar os valores pares e impares na lista numeros
numeros.insert(0, pares[:])
numeros.insert(1, impares[:])

# Limpa as listas temporárias pares e impares
pares.clear()
impares.clear()

# Ordena os valores em ordem crescente
numeros[0].sort()
numeros[1].sort()

# Imprime as lista em ordem crescente
print(f'-=-' * 20)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
