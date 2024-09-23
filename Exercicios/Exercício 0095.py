# ______ Exercício 0095 ______

# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Cadastro de Jogadores v2.0":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Incialização de dicionários e listas
cadastros = list()
jogador = dict()
partidas = list()

# Loop infinito para obtenção dos dados
while True:
    print(f'-' * 30)
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    quantidade = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(1, quantidade + 1):
        partidas.append(int(input(f'Quantos gols na {i}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas[:])
    cadastros.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print(f'Opção inválida. Digite apenas S ou N!')
    if opcao == 'N':
        break
    jogador.clear()
    partidas.clear()
print(f'-=-' * 20)
print(f'{"Cod.":<5}{"Nome":<10}{"Gols":<20}{"Total":<15}')
print(f'-' * 40)

# Loop for para imprimir dos dados so jogador
for i, k in enumerate(cadastros):
    print(f'{i:<5}{k["nome"]:<10}', f'{k["gols"]}'.ljust(20), f'{k["total"]:<15}')
print(f'-' * 40)
while True:
    pesq = int(input('Mostrar dados de qual jogador (digite 999 para encerrar)? '))
    if pesq == 999:
        break
    for i, k in enumerate(cadastros):
        if pesq < 0 or pesq > len(cadastros):
            print(f'Valor informado é invalido. Informe o número de um jogador da lista!')
        else:
            print(f'-- LEVANTAMENTO DO JOGADOR {k["nome"]}:')
            for j, g in enumerate(cadastros[pesq]['gols']):
                print(f'No jogo {j} fez {g} gols.'.center(40))
print(f'<< VOLTE SEMPRE! >>'.center(40))
