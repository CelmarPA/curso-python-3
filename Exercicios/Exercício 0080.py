# ______ Exercício 0080 ______

# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["green"]}{"Lista Ordenada Sem Repetições":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Incialização de listas
valores = list()

# Loop for para obtenção do valores e organização dos números
for i in range(0, 5):
    valor = int(input('Digite um valor: '))  # Solicita os números ao usuário
    if i == 0:  # Adiciona o primeiro valor da lista
        valores.append(valor)
        print(f'Adicionado ao final da lista...')
    if i == 1:  # Adiciona o segundo valor da lista
        if valor > valores[0]:
            valores.insert(1, valor)
            print(f'Adicionado ao final da lista...')
        else:
            valores.insert(0, valor)
            print(f'Adicionado na posição 0 da lista...')
    if i == 2:  # Adiciona o terceiro valor da lista
        if valor > valores[0] or valor < valores[1]:
            valores.insert(1, valor)
            print(f'Adicionado na posição 1 da lista...')
        elif valor < valores[0]:
            valores.insert(0, valor)
            print(f'Adicionado na posição 0 da lista...')
        else:
            valores.append(valor)
            print(f'Adicionado ao final da lista...')
    if i == 3: # Adiciona o quarto valor da lista
        if valores[0] < valor < valores[1]:
            valores.insert(1, valor)
            print(f'Adicionado na posição 1 da lista...')
        elif valores[1] < valor < valores[2]:
            valores.insert(2, valor)
            print(f'Adicionado na posição 2 da lista...')
        elif valor < valores[0]:
            valores.insert(0, valor)
            print(f'Adicionado na posição 0 da lista...')
        else:
            valores.append(valor)
            print(f'Adicionado ao final da lista...')
    if i == 4:  # Adiciona o último valor da lista
        if valores[0] < valor < valores[1]:
            valores.insert(1, valor)
            print(f'Adicionado na posição 1 da lista...')
        elif valores[1] < valor < valores[2]:
            valores.insert(2, valor)
            print(f'Adicionado na posição 2 da lista...')
        elif valores[2] < valor < valores[3]:
            valores.insert(3, valor)
            print(f'Adicionado na posição 3 da lista...')
        elif valor < valores[0]:
            valores.insert(0, valor)
            print(f'Adicionado na posição 0 da lista...')
        else:
            valores.append(valor)
            print(f'Adicionado ao final da lista...')
# Imprime a lista
print(f'-=-' * 20)
print(f'Os valores digitados em ordem foram {valores}')
