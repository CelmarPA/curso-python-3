# ______ Exercício 0038 ______

# Escreva um programa que leia dois número interos e compare-os, mostrando na tela uma mensagem:
# -> O primeiro valor é maior
# -> O segundo valor é maior
# -> Não existe valor maior, os dois são iguais

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{"Comparador de Números":^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Solicita os números ao usuário
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

if n1 > n2:
    print(f'O {cores["red"]}PRIMEIRO{cores["reset"]} número é maior!')
elif n2 > n1:
    print(f'O {cores["red"]}SEGUNDO{cores["reset"]} número é maior!')
else:
    print(f'Os dois números são {cores["blue"]}IGUAIS{cores["reset"]}!')
