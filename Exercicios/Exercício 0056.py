# ______ Exercício 0056 ______

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Balança Avaliadora ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Listas dos dados
nomes = []
idades = []
sexos = []

# Inicialização de variaveis
menores = 0
media = 0

# Loop para coleta e analise de dados
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    if not nome.isalpha():
        quit(f'A nome digitado não é válido! Por favor tente novamente!')
    idade = int(input('Idade: '))
    if idade <= 0:
        quit(f'A idade digitada não é válida! Por favor tente novemante!')
    sexo = str(input('[M/F]: ')).strip().upper()
    if sexo not in 'MmFf':
        quit(f'O sexo digitado não é válido! Por favor tente novamente!')

    # Criação das listas com os dados das pessoas
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

    # Calculo da média das idades
    media = sum(idades) / i

    # Contagem de mulheres com menos de 20 anos
    if idade < 20 and sexo == 'F':
        menores += 1

# Define a maior idade e localiza o homem mais velho
maior_idade = max(idades)
mais_velho = nomes[idades.index(max(idades))]

# Imprime a análise
print(f'A média da idade do grupo é de {cores["blue"]}{media:.2f}{cores["reset"]} anos.')
print(f'O homem mais velho tem {cores["red"]}{maior_idade}{cores["reset"]} anos e se chama '
      f'{cores["yellow"]}{mais_velho}{cores["reset"]}.')
print(f'Ao todo são {cores["green"]}{menores}{cores["reset"]} mulhere(s) com menos de 20 ans.')
