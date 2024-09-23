# ______ Exercício 0076 ______

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Lista de Preços com Tupla":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Tupla com lista de compras
listagem = ('Leite', 4.50, 'Pão de Forma', 3, 'Ovos (Dúzia)', 6.50, 'Arroz (5Kg)', 10, 'Feijão (1Kg)', 5.50,
            'Frango (1Kg)', 15, 'Tomate (1Kg)', 3.50, 'Cenoura (1Kg)', 2, 'Maçã (1Kg)', 4, 'Refrigerante (2L)', 5)
print(f'-' * 60)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print(f'-' * 60)

for i in range(0, len(listagem), 2):
    produto = listagem[i]
    valor = listagem[i + 1]
    if isinstance(valor, str):
        print(f'{produto:.<50}{valor}')
    else:
        print(f'{produto:.<50}R$ {valor:>6.2f}')  # Alinha a direita o valores
print(f'-' * 60)

# ______ Exercício 0076 outra solução ______

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Lista de Preços com Tupla":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Tupla com lista de compras
listagem = ('Leite', 4.50, 'Pão de Forma', 3, 'Ovos (Dúzia)', 6.50, 'Arroz (5Kg)', 10, 'Feijão (1Kg)', 5.50,
            'Frango (1Kg)', 15, 'Tomate (1Kg)', 3.50, 'Cenoura (1Kg)', 2, 'Maçã (1Kg)', 4, 'Refrigerante (2L)', 5)
print(f'-' * 60)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print(f'-' * 60)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<50}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')
print(f'-' * 60)