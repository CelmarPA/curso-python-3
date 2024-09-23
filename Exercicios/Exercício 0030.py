# ______ Exercício 0030 ______

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Importar biblioteca
from colorama import Fore

# Solicita um número ao usuário
num = int(input(Fore.MAGENTA + 'Me diga um número qualquer: '))

# Verificar se é par ou impar
if num % 2 == 0:
    print(f'O número {num} é', Fore.BLUE + f'PAR', Fore.RESET + f'!')
else:
    print(f'O número {num} é', Fore.BLUE + f'ÍMPAR', Fore. RESET + f'!')
