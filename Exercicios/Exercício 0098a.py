# ______ Exercício 0098 outra solução ______

# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["yellow"]}{"Função de Contador":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from time import sleep


# Função de contador
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2.5)
    if i < f:
        count = i
        while count <= f:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count += p
        print(f'FIM!')
    else:
        count = i
        while count >= f:
            print(f'{count} ', end='', flush=True)
            sleep(0.5)
            count -= p
        print(f'FIM!')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

# Solicita os dados ao usuário

print(f'Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
