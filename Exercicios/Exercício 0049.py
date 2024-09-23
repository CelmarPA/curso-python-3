# ______ Exercício 0049 ______

# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m'}

# Titulo do programa
print(f'{cores["red"]}-=-' * 20)
print(f'{cores["green"]}{"Gerador de Tabuada v2.0":^60}')
print(f'{cores["red"]}-=-{cores["reset"]}' * 20)

# Solicita um número ao usuário
num = int(input('Digite um número para ver sua tabuada: '))

# Loop para gerar a tabuada
for i in range(1, 11):
    print(f'{num} x {i:2} = {num * i:2}')
