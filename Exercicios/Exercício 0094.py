# ______ Exercício 0094 ______

# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["green"]}{"Unindo Dicionários e Listas":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Incialização de dicionários
pessoa = dict()

# Inicialização de listas
cadastros = list()

# Inicialização de variáveis
soma = 0

# Loop infinito para obtenção dos dados
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print(f'Opção inválida. Tente novamente! Por favor, digite apenas M ou F')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    # Condição para continuar ou sair do loop
    if opcao == 'S':
        cadastros.append(pessoa.copy())
        pessoa.clear()
    elif opcao == 'N':
        cadastros.append(pessoa.copy())
        pessoa.clear()
        break
    else:
        print(f'Opção inválida. Tente novamente! Responda apenas M OU F.')
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

# Loop for para soma as idades
for pessoa in cadastros:
    soma += pessoa['idade']

# Cálculo da média das idades
media = soma / len(cadastros)

# Imprime os resultados
print(f'-=-' * 20)
print(f' - O grupo tem {len(cadastros)} pessoa(s).\n'
      f' - A média de idade é de {media:.2f} anos.')
print(f' - As mulheres cadastradas foram: ',end='')

for pessoa in cadastros:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]} ', end='')
print(f'')
print(f' - Lista das pessoas que estão acima da média da idade:')
for pessoa in cadastros:
    if pessoa['idade'] > media:
        print(f'   nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]};')
print(f' << ENCERRADO >>')
