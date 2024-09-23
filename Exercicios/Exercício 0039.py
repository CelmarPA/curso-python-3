# ______ Exercício 0039 ______

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -> Se ele ainda vai se alistar ao serviço militar.
# -> Se é a hora de se alistar.
# -> Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Importação de bibliotecas
from datetime import datetime

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{"Analisador de Alistamento Militar":^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Solicita ao usuário o ano do nascimento
ano = int(input('Ano de nascimento: '))

# Calculo da idade
atual = datetime.today().year
idade = atual - ano

print(f'Quem nasceu no ano de {cores["yellow"]}{ano}{cores["reset"]} tem {cores["green"]}{idade}{cores["reset"]} anos '
      f'em {cores["blue"]}{atual}{cores["reset"]}.')

# Analise do alistamento
if idade == 18:
    print(f'Você tem que se alistar {cores["red"]}IMEDIATAMENTE{cores["reset"]}!')
elif idade < 18:
    print(f'Ainda faltam {cores["green"]}{18 - idade}{cores["reset"]} anos para o alistamento.')
    print(f'Seu alistamento será em {cores["blue"]}{atual + (18 - idade)}{cores["reset"]}.')
else:
    print(f'Você já deveria ter se alistado há {cores["red"]}{idade - 18}{cores["reset"]} ano(s).')
    print(f'Seu alistamento era para ter sido feito {cores["red"]}{atual - (idade - 18)}{cores["reset"]}.',)
