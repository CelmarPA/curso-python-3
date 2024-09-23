# ______ Exercício 0059 ______

# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Calculadora com Menu de Opões":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Importação de bibliotecas
from time import sleep

# Incialização de variáveis
opcao = 0

# Solicita ao usuário dois valores
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

# Loop para menu
while not opcao == 5:
    print(f' ' * 3, f'[ 1 ] somar')
    print(f' ' * 3, f'[ 2 ] multiplicar')
    print(f' ' * 3, f'[ 3 ] maior')
    print(f' ' * 3, f'[ 4 ] novos números')
    print(f' ' * 3, f'[ 5 ] sair do programa')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}.')
        print(f'=-=' * 10)
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}.')
        print(f'=-=' * 10)
    elif opcao == 3:
        print(f'Entre 5 e 8 o maior valor é {max(n1, n2)}.')
        print(f'=-=' * 10)
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print(f'Finalizando...')
    else:
        print(f'Opção inválida. Tente novamente!')
        print(f'=-=' * 10)
    sleep(3)
print(f'=-=' * 10)
print(f'Fim do programa! Volte sempre!')
