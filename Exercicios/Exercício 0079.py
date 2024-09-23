# ______ Exercício 0079 ______

# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Imprime o título do programa
print(f'{cores["blue"]}-=-' * 20)
print(f'{cores["yellow"]}{"Valores Únicos em Uma Lista":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Inicialização de lsitas
valores = list()

# Loop while para solicitação e validadação dos números e opções
while True:
    valor = int(input('Digite um valor: '))  # Solicita um valor ao usuário
    if valor not in valores:  # Verifica se o valor não está na lista
        valores.append(valor)
        print(f'Valor adicionado com sucesso...')
    else:  # Se o valor já estiver na lista ele não sera adicionado
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]  # Soliciata a opção de continuar ou não
    while opcao not in 'SN':  # Loop para validação da opção
        print('Opção inválida. Tente novamente!')
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':  # Quando a opção for não o programa incerrará o loop
        break
valores.sort()  # Coloca a lista em ordem crescente
print(f'-=-' * 20)
print(f'Você digitou os valores {valores}')  # Imprime a lista
