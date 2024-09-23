# ______ Exercício 0089 ______

# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Boletim com Listas Compostas":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from time import sleep

# Inicialização de listas
historicos = list()

# Loop infinito para obtenção dos dados e cálculo da média
while True:
    aluno = str(input('Nome: ')).strip()  # Solicita o nome do aluno
    while not aluno.isalpha():  # Loop while para validação do nome
        print(f'Digite um nome válido!')
        aluno = str(input('Nome: ')).strip()
    while True:
        try:
            nota1 = float(input('Nota 1: '))  # Solicita a primeira nota
            break
        except ValueError:
            print('Digite uma nota válida!')
    while True:
        try:
            nota2 = float(input('Nota 2: '))  # Solicita a segunga nota
            break
        except ValueError:
            print('Digite uma nota válida!')
    media = (nota1 + nota2) / 2  # Calcula a média
    historicos.append([aluno, [nota1, nota2], media])  # Inseri os dados na lista historicos
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Pergunta se o usuário deseja continuar
    while opcao not in 'SN':  # Loop while para validação da opção
        print(f'Opção inválida. Tente novamente!')
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
# Imprime o cabeçalho do histórico
print(f'{cores["grey"]}{"+-+"}' * 8)
print(f'{cores["yellow"]}{"Nº":^2}', f'{"NOME":>6}', f'{"MÉDIA":>10}{cores["reset"]}')
print(f'{cores["grey"]}{"+-+"}{cores["reset"]}' * 8)
for i, boletim in enumerate(historicos):
    print(f'{i:^2} {boletim[0]:>8} {boletim[2]:>7}')
print('-' * 30)
# Loop infinito para perguntar qual nota mostrar
while True:
    notas = int(input(f'Mostrar notas de qual aluno? ({cores["red"]}{999}{cores["reset"]} para finalizar): '))
    if notas == 999:
        break
    for i, boletim in enumerate(historicos):
        if notas == i:
            print(f'Notas de {cores["blue"]}{boletim[0]}{cores["reset"]} são '
                  f'{cores["green"]}{boletim[1]}{cores["reset"]}')
        elif notas != i:  # Valida o aluno escolhido, caso não esteja na lita historico
            print(f'{cores["red"]}Aluno não encontrado no banco de dados. Tente novamente!{cores["reset"]}')
print(f'{cores["red"]}{"FINALIZANDO..."}{cores["reset"]}')
sleep(2)
print(f'{cores["blue"]}{"<< < VOLTE SEMPRE >> >"}{cores["reset"]}')
