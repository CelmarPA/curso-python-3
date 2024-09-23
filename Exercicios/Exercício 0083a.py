# ______ Exercício 0083 outra solução ______

# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["red"]}{"Validando expressões Matemáticas":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

expr = str(input('Digite a expressão: '))

pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expressão está válida!')
else:
    print(f'Sua expressão está errada!')
