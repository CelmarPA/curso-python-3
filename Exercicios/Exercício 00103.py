# ______ Exercício 00103 ______

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Ficha do Jogador":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)


# Função ficha do jogador
def ficha(j='', g=0):
    if not j:
        j = '<desconhecido>'
    return f'O jogador {j} fez {g} gol(s) no campeonato.'


# Programa principal
print(f'_' * 30)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Total de gols: '))

if not gols or gols.isalpha():
    gols = 0
else:
    gols = int(gols)

print(ficha(nome, gols))

# _________________________________
# Nome do jogador: Romário
# Total de Gols: 33
# O jogadaor Romário fez 33 gol(s) no campeonato.

# _________________________________
# Nome do jogador:
# Total de Gols: 2
# O jogadaor <desconhecido> fez 2 gol(s) no campeonato.

# _________________________________
# Nome do jogador:
# Total de Gols:
# O jogadaor <desconhecido> fez 0 gol(s) no campeonato.
