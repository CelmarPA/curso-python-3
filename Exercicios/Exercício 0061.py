# ______ Exercício 0061 ______

# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
# Formula geral de uma PA: PA =  a + (tr) (onde a é o primeiro termo, t o termo e r a razão

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["blue"]}{"Gerador de PA v2.0":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

# Inicialização de variáveis
count = 0

# Loop while para cálculo da PA
while count < 10:
    PA = termo + (count * razao)
    count += 1
    print(f'{PA} {cores["red"]}→ {cores["reset"]}', end='')
print(f'{cores["red"]}FIM!{cores["reset"]}')
