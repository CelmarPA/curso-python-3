# ______ Exercício 0065 outra solução ______

# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["blue"]}{"Analisador de Maior e Menor Valores":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Incialização de variáveis
resp = 'S'
media = soma = quant = maior = menor = 0

# Loop while para cálculo:
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] '))
media = soma / quant
print(f'Você digitou {quant} e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
