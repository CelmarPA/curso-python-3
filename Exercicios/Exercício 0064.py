# ______ Exercício 0064 ______

# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["green"]}{"Tratando varios valores v1.0":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Solicita um número ao usúario
num = int(input('Digite um número [999 para para]: '))

# Inicialização de variáveis
soma = count = 0

# Loop while para soma
while num != 999:
    soma += num
    count += 1
    num = int(input('Digite um número [999 para para]: '))  # Assim a variável soma não recebe o flag 999
print(f'Você digitou {count} números e a soma estre eles foi {soma}.')
