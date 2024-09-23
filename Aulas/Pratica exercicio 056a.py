# ______ Exercício 0056 ______

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Balança Avaliadora ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
soma_idade = 0
media = 0
maior_idade = 0
menores = 0
nome_maior = ''

for i in range(1, 5):
    print(f'----- {i}ª PESSO -----')
    nome = str(input('Nome: ')).strip()
    if nome.isalpha() == False:
        print(f'O {cores["red"]}nome{cores["reset"]} digitado não é válido! Tente novamente!')
        quit(1)
    idade = int(input(f'Idade: '))
    if idade <= 0:
        print(f'A {cores["red"]}idade{cores["reset"]} digitada não é válida! Tente novamente!')
        quit(1)
    sexo = str(input(f'Sexo [M/F]: ')).strip()
    if sexo not in 'MnFf':
        print(f'O sexo {cores["red"]}sexo{cores["reset"]} digitado não é válido! Tente novamente!')
        quit(1)
    # Cálculo da média das idades
    soma_idade += idade
    media = soma_idade / i
    # Definição do homem mais velho
    if i == 1 and idade > maior_idade:
        maior_idade = idade
        nome_maior = nome
    if sexo in 'Mn' and idade > maior_idade:
        maior_idade = idade
        nome_maior = nome
    # Definição da quantidade de mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        menores += 1

# Imprime a analise
print(f'A média da idade do grupo é de {cores["blue"]}{media}{cores["reset"]} anos.')
print(f'O homem mais velho tem {cores["red"]}{maior_idade}{cores["reset"]} anos e se chama '
      f'{cores["yellow"]}{nome_maior}{cores["reset"]}.')
print(f'Ao todo são {cores["green"]}{menores}{cores["reset"]} mulhere(s) com menos de 20 anos.')
