# ______ Exercício 0071 ______

# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Simulador de Caixa Eletrônico":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Imprime o enunciado do programa
print(f'{cores["yellow"]}=' * 40)
print(f'{cores["red"]}{"BANCO CEV":^40}')
print(f'{cores["yellow"]}={cores["reset"]}' * 40)

# Loop while infinito
while True:
    valor = int(input('Qual valor você quer sacar? R$'))
    if valor <= 0:
        print(f'Valor inválido! Tente novamente!')
        valor = int(input('Qual valor você quer sacar? R$'))
    if valor >= 50:
        total = valor // 50
        rest = valor % 50
        print(f'Total de {total} células de R$50.00!')
        if rest != 0:
            valor -= (total * 50)
        else:
            break
    if valor >= 20:
        total = valor // 20
        rest = valor % 20
        print(f'Total de {total} células de R$20.00!')
        if rest != 0:
            valor -= total * 20
        else:
            break
    if valor >= 10:
        total = valor // 10
        rest = valor % 10
        print(f'Total de {total} células de R$10.00!')
        if rest != 0:
            valor -= total * 10
        else:
            break
    if valor >= 1:
        total = valor // 1
        rest = valor % 1
        print(f'Total de {total} células de R$1.00!')
        if rest != 0:
            valor -= total * 1
        else:
            break
print(f'{cores["yellow"]}={cores["reset"]}' * 40)
print(f'Volte sempre ao {cores["red"]}BANCO CEV{cores["reset"]}! Tenha um bom dia!')
