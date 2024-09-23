# ______ Exercício 0062 ______

# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["blue"]}{"Gerador de PA v3.0":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solicita os dados ao usuário:
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

# Inicialização de variáveis
count = 0

# Loop while para geração da PA
while count < 10:
    pa = termo + (count * razao)
    count += 1
    print(f'{pa} {cores["blue"]}→ {cores["reset"]}', end='')
    if count == 10:
        print(f'{cores["red"]}PAUSE!{cores["reset"]}')
        termo = int(input('Quantos termos você quer mostrar a mais? '))
        while termo > 0:
            while termo != 0:
                pa += razao
                termo -= 1
                count += 1
                print(f'{pa} {cores["blue"]}→ {cores["reset"]}', end='')
            print(f'{cores["red"]}PAUSE!{cores["reset"]}')
            termo = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {cores["yellow"]}{count}{cores["reset"]} termos mostrados.')
