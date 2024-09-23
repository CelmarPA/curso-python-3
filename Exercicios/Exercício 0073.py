# ______ Exercício 0073 ______

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Fortaleza.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["green"]}{"Tabela Brasileirão 2023":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Tuplaca com os 20 primeiro colocados do Brasileirão 2023
times = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Athletico-PR', 'São Paulo', 'Fluminense',
         'Bragantino', 'Fortaleza', 'Internacional', 'Cruzeiro', 'Cuiabá', 'Atlético-MG', 'Santos',
         'Corinthians', 'Goiás', 'Bahia', 'Coritiba', 'América-MG', 'Vasco da Gama')

# Imprime o enunciado do programa e as classificações
print(f'-=' * 30)
print(f'Lista dos times do Brasileirão: {times}')
print(f'-=' * 30)
print(f'Os 5 primeiros são {times[0:5]}')
print(f'-=' * 30)
print(f'Os 4 últimos são {times[-4:]}')
print(f'-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'-=' * 30)
print(f'O Fortaleza está na {times.index("Fortaleza") + 1}ª posição.')
