# ______ Exercício 0066 ______

# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["red"]}{"Calculada de Soma com Flag":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
soma = count = 0

# Loop shile infinito com condição break
while True:
    num = int(input(f'Digite um valor ({cores["red"]}999{cores["reset"]} para parar): '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'A soma dos {cores["green"]}{count}{cores["reset"]} valores foi {cores["blue"]}{soma}{cores["reset"]}!')
