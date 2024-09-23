# ______ Exercício 0090 ______

# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela. Se a média for 7 aprovado abaixo disso reprovado.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["red"]}{"Dicionário em Python":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização de dicionários
boletim = {'Nome': '', 'Média': 0, 'Situação': ''}

# Solicita os dados ao usuário
nome = str(input('Nome: ')).strip()
media = float(input(f'Média: '))

# Condição para verificação de aprovado ou reprovado
if media >= 7:
    situacao = 'Aprovado'
elif 5 <= media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

# Anexa os dados no respectivos campos no dicionário
boletim['Nome'] = nome
boletim['Média'] = media
boletim['Situação'] = situacao

# Loop para impressão dos resultados
print(f'-=-' * 20)
for c, k in boletim.items():
    print(f'{c} é igual a {k}')
