# ______ Exercício 0056 outra solução ______

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)
print(f'{cores["blue"]}{" Balança Avaliadora ":=^60}{cores["reset"]}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Inicialização das variáveis
soma_idade = 0
media = 0
maior_idade_homem = 0
nome_velho = 0
total_mulher_20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    soma_idade += idade
    # Definir o nome e a idade do homem mais velho
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    # Calula a quantidade de mulher com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1

# Calcula a média das idades
media = soma_idade / 4

# Imprime o resultado da análise
print(f'A média da idade do grupo é de {media:.2f} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama{nome_velho}.')
print(f'Ao todo são {total_mulher_20} mulheres com menos de 20 anos.;')
