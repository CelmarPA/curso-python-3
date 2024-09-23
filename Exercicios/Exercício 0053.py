# ______ Exercício 0053 ______

# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{" Detector de Palíndromo ":=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

frase = str(input('Digite uma frase: ')).replace(' ', '').strip().upper()

inverso = frase[::-1]

print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('Temos um palíndromo!')
else:
    print(f'A frase digitada não é um palíndromo!')

# ______ Exercício 0053 outra solução ______

frase = str(input(f'Digite uma frase: ')).strip().upper()

palavras = frase.split()  # Separa a frase em palavras
junto = ''.join(palavras)  # Junto as palabras sem os espaços
inverso = ''  # inicializa a variável inverso

for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print(f'O inverso da frase {junto} é {inverso}')

if junto == inverso:
    print(f'Temos um palíndromo!')
else:
    print(f'A frase digitada não é um palíndromo!')
