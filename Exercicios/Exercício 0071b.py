120# ______ Exercício 0071 ______

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

valor = int(input('Qual valor você quer sacar? R$'))

# Inicialização de variáveis
total = valor
ced = 50
totced = 0

# Loop while infinito
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced:.2f}!')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print(f'{cores["yellow"]}={cores["reset"]}' * 40)
print(f'Volte sempre ao {cores["red"]}BANCO CEV{cores["reset"]}! Tenha um bom dia!')
