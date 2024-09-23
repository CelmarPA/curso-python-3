# ______ Exercício 0060 ______

# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["blue"]}{"Cálculo Fatorial":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solita um número ao usuário
num = int(input('Digite um número: '))

print(f'Calulando {num}! = ', end='')

# Inicialização de variáveis
fatorial = 1
count = num

# Loop while para calcular fatorial
while count > 0:
    print(f'{count}', end='')
    fatorial *= count
    count -= 1
    print(f' x ' if count > 1 else ' = ', end='')

print(f'{fatorial}')

"""
while i != 1:
    print(f'Calculando {num}! = ', end='')
    for i in range(num, 0, -1):
        fatorial = fatorial * i
        print(f'{i}', end='')
        print(f' x ' if i > 1 else ' = ', end='')
print(f'{fatorial}')

f = 1
for i in range(num, 0, -1):
    f *= i
    print(f'{i}', end='')
    print(f' x ' if i > 1 else ' = ', end='')
print(f'{f}')
"""