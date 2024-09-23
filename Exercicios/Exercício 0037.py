# ______ Exercício 0037 ______

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -> 1 para binário
# -> 2 para octal
# -> 3 para hexadecimal

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'cyan': '\033[36m'}

# Título do programa
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]} {"Conversor de Bases Númericas":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solicita ao usuário um número
num = int(input('Digite um número inteiro: '))

# Solicita ao usuário a base
print(f'''Escolha uma das bases para conversão:
 [ {cores["green"]}1{cores["reset"]} ] converter para {cores["green"]}BINÁRIO{cores["reset"]}
 [ {cores["yellow"]}2{cores["reset"]} ] converter para {cores["yellow"]}OCTAL{cores["reset"]}
 [ {cores["blue"]}3{cores["reset"]} ] converter para {cores["blue"]}HEXADECIMAL{cores["reset"]}''')
base = int(input('Sua opção: '))

# Inicializando variável para evitar que sejam indefinidas
convertido = None
classe = ''

# Condição para conversão
if base == 1:
    convertido = bin(num)[2:]
    classe = f'{cores["green"]}BINÁRIO{cores["reset"]}'
elif base == 2:
    convertido = oct(num)[2:]
    classe = 'OCTAL'
elif base == 3:
    convertido = hex(num)[2:]
    classe = 'HEXADECIMAL'
else:
    print(f'Opção inválida! Tente novamente.')
    quit()

print(f'O número {cores["red"]}{num}{cores["reset"]} convertido para {classe} é igual '
      f'a {cores["cyan"]}{convertido}{cores["reset"]} !')
