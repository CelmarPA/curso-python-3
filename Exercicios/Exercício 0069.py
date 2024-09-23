# ______ Exercício 0069 ______

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["green"]}{"Analisador de Dados do Grupo":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáceis
maior_18 = menor_20 = count_homem = 0

# Loop while infinito para solicitação dos dados
while True:
    print(f'-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print(f'-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]  # Também pode ser sexo = ''
    while sexo not in 'MF':  # Loop while para validação do sexo
        print(f'Opção inválidade. Tente novamente!')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Também pode ser opcao = ''
    while opcao not in 'SN':  # Loop while para validação da opção
        print(f'Opção inválidade. Tente novamente!')
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:  # Contador para pessoas com mais de 18 anos cadastradas
        maior_18 += 1
    if sexo == 'M':  # Contador de homens cadastrados
        count_homem += 1
    if sexo == 'F' and idade < 20:  # Contador de mulheres com menos de 20 anos cadastradas
        menor_20 += 1
    if opcao == 'N':  # Condição para saida do loop
        break
# Imprime o resultado da análise
print(f'=' * 45)
print(f'O total de pessoas com mais de 18 anos: {maior_18}\n'
      f'Ao todo temos {count_homem} homem(s) cadastrado(s).\n'
      f'E temos {menor_20} mulher(s) com menos de 20 anos.')
print(f'=' * 45)
