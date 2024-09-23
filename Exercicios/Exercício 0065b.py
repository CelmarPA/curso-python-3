# ______ Exercício 0065 ______

# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["blue"]}{"Analisador de Maior e Menor Valores":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de variaveis
opcao = 'S'
count = soma = media = maior = menor = 0

# Loop while para calculos
while opcao in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
    while opcao not in 'SsNn':
        print(f'Opção inválida. Tente novamente:')
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / count
print(f'Você digitou {cores["yellow"]}{count}{cores["reset"]} números e a média foi'
      f' {cores["green"]}{media:.2f}{cores["reset"]}.')
print(f'O maior valor foi {cores["blue"]}{maior}{cores["reset"]} e o menor foi '
      f'{cores["red"]}{menor}{cores["reset"]}.')
