# ______ Exercício 0081 ______

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Extraindo Dados de Uma Lista":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
numeros = list()

# Inicialização de variáveis
count = 0

# Loop infinito para solicitação do valores
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    opcao = str(input('Quer continuar? [S/N] ')).strip()[0]
    while opcao not in 'SsNn':  # Loop while para validação da opção
        print(f'Opção inválida. Tenta novamente!')
        opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break
numeros.sort(reverse=True)  # Organiza a lista em ordem descrescente

# Imprime os resultados
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print(f'O valor 5  faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
