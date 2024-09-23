# ______ Exercício 0057 ______

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["red"]}{"Validação de Dados":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Solicita o sexo ao usuário
sexo = str(input('Informe seu sexo?: [M/F] ')).strip().upper()[0]

# Loop while para verificação dados
while sexo not in 'MF':
    sexo = str(input('Dados, inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {cores["blue"]}{sexo}{cores["reset"]} registrado com sucesso!')
