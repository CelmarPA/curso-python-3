# ______ Exercício 0040 ______

# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:
# -> Média abaixo de 5.0: REPROVADO
# -> Média entre 5.0 e 6.9: RECUPERAÇÂO
# -> Média 7.0 ou superior: APROVADO

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["yellow"]}{"Calculadora de Média":^60}{cores["reset"]}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solicita as notas ao usuário
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

# Calculo da média
media = (n1 + n2) / 2

# Avaliação da média
if media < 5:
    status = f'{cores["red"]}REPROVADO{cores["reset"]}'
elif 5 <= media < 7:
    status = f'{cores["yellow"]}RECUPERAÇÃO{cores["reset"]}'
else:
    status = f'{cores["green"]}APROVADO{cores["reset"]}'

# Imprime média e o resultado
print(f'Tirando {cores["blue"]}{n1}{cores["reset"]} e {cores["blue"]}{n2}{cores["reset"]}, a média do aluno'
      f' é {cores["blue"]}{media}{cores["reset"]}.')
print(f'O aluno está {status}!')
