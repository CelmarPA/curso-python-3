# ______ Exercício 0072 ______

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Número por Extenso":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Tupla com os números por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Solicita um número ao usuário
num = int(input('Digite um número entre 0 e 20: '))

# Loop while para validação do número solicitado ao usuario
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
# Imprimi o número por extenso
print(f'Você digitou o número {numeros[num]}!')


# ______ Exercício 0072 ______

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Tupla com os números por extenso
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Loop while para validação do número solicitado ao usuario
while True:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
# Imprimi o número por extenso
print(f'Você digitou o número {numeros[num]}!')