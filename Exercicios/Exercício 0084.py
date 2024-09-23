# ______ Exercício 0084 ______

# Faça um programa que leia nome e peso de várias pessoas,  guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Lista Composta e Análise de Dados":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de listas
pessoas = list()
dados = list()

# Inicialização de variáveis
maior = 0
menor = 0

# Loop infinito para obtenção dos dados
while True:
    nome = str(input('Nome: ')).strip()
    dados.append(nome)
    peso = float(input('Peso: '))
    dados.append(peso)
    # Define maior e menor pesos
    if len(pessoas) == 0:  # E o tamanho da lista pessoas for 0
        maior = menor = dados[1]
    else:  # Caso contrário fará serão feitas as seguintes verificações
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])  # Cria copia dos dados dentro da lista pessoas
    dados.clear()  # Limpas a lista temporaria de dados
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
# Imprime os resultados
print(f'-=-' * 20)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior:.1f}Kg. Peso de ', end='')
for p in pessoas:  # Interação para obter nome dos mais pesados
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi {menor:.1f}Kg. Peso de ', end='')
for p in pessoas:  # Interação para obter nome dos mias leves
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print(f'')
print(f'-=-' * 20)
