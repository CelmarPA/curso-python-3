# ______ Exercício 0083 ______

# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["red"]}{"Validando expressões Matemáticas":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Inicialização de variáveis
paren_aberto = 0
paren_fechado = 0

# Solicita a expressão ao usúario
expressao = str(input('Digite a expressão: '))

# Loop for para verificar a quantidade dos parenteses
for v in expressao:
    if v == '(':
        paren_aberto += 1
    if v == ')':
        paren_fechado += 1
if paren_aberto == paren_fechado:
    print(f'Sua expressão é válida!')
else:
    print(f'Sua expressão está errada!')
