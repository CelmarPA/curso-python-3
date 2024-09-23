# ______ Exercício 0070 outra solução ______

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["yellow"]}{"Analisador de Estatísticas de Produtos":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Imprime o enunciado do programa
print(f'=' * 30)
print(f'{"LOJAS SUPER BARATÃO":^30}')
print(f'=' * 30)

# Inicialização de variáveis
total = count = count_1000 = menor_valor = 0
mais_barato = ''

# Loop while para obtenção do dados
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    count += 1
    while preco <= 0:  # Enquanto preço digitado não for maior que 0 vai continua a pedir um preço
        print(f'Valor digitado inválido! Preço não pode ser igual ou menor que zero.\n'
              f'Insira o valor novamente!')
        preco = float(input('Preço: R$'))
    if count == 1 or preco < menor_valor:  # Defini o produto mais barato
        menor_valor = preco
        mais_barato = produto
    total += preco  # Calula o total da compra
    if preco > 1000:  # Regista a quantidade de produtos que custaram mais de R$1000,00
        count_1000 += 1
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Solicita ao usuário se quer continuar ou não
    if opcao not in 'SN':  # Enquando digitar um opção inválida irá continuar solicitando a opção
        print(f'Opção inválida! Tente novamente!')
        opcao = str(input('Quer continuar? [S/N] '))
    if opcao == 'N':  # Condição para sair do loop infinito
        break
# Imprime os resultados
print(f'-' * 15, f' FIM DO PROGRAMA ', f'-' * 15)
print(f'O total da compra foi de R${cores["blue"]}{total:.2f}{cores["reset"]}.\n'
      f'Temos {cores["red"]}{count_1000}{cores["reset"]} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {cores["green"]}{mais_barato}{cores["reset"]} e '
      f'custa R${cores["green"]}{menor_valor:.2f}{cores["reset"]}.')
