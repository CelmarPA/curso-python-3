# ______ Exercício 0082 ______

#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
#  conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
#  listas geradas.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Dividindo Valores em Várias Listas":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas:
numeros = list()
pares = list()
impares = list()

# Loop infinito para solicitar os valores
while True:
    numeros.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N] ')).strip()[0]
    while opcao not in 'SsNn':
        print(f'Opção inválida! Tente novamente!')  # Loop while para validação da opção
        opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break
for num in numeros:  # Intera na lista numeros e pegando os números e verificando se são pares ou impares
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Imprime as listas separadas
print(f'-=-' * 20)
print(f'A lista completa é {numeros}\n'
      f'A lista de pares é {pares}\n'
      f'A lista de impares é {impares}')
