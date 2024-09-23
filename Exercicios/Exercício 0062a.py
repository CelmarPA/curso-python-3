# ______ Exercício 0062 outra solução ______

# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["blue"]}{"Gerador de PA v3.0":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solicita os dados ao usuário
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

# Inicialização de variáveis
termo = primeiro
count = 1
total = 0
mais = 10

# Loop while para geração da PA
while mais != 0:
    total += mais
    while count <= total:
        print(f'{termo} → ', end='')
        termo += razao
        count += 1
    print(f'PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
