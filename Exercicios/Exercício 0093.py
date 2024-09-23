# ______ Exercício 0093 ______

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["red"]}{"Cadastro de Jogador de Futebol":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização de dicionários
jogador = dict()
gols = list()

# Inicialização de variáveis
total = 0

# Solicita os dados ao usuários
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# Loop while para validar quantidade de partidas
while partidas <= 0:
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# Loop for para quantidade de gols por partidas
for i in range(1, partidas + 1):
    quantidade = int(input(f'Quantos gols na {i}ª partida? '))
    gols.append(quantidade)  # Adiciona os gols a lista
    total += quantidade  # Calcula o total de gols

# Adiciona a lista gols ao dicionário e total de gols
jogador['gols'] = gols[:]
jogador['total'] = total

# Imprime os resultados
print(f'-=-' * 35)
print(f' O nome do jogador é {jogador["nome"]} ele marcou {jogador["gols"]} gols nas {partidas} partidas,'
      f' obtendo um total de {jogador["total"]} gols.'.center(105))
print(f'-=-' * 35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.'.center(105))
print((f'-=-' * 30).center(105))
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.'.center(105))
for i in range(0, partidas):
    print(f'=> Na {i + 1}ª partida, fez {jogador["gols"][i]} gols.'.center(105))
print(f'Foi um total de {jogador["total"]} gols.'.center(105))
