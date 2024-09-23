# ______ Exercício 0067 ______

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["green"]}-=-' * 20)
print(f'{cores["blue"]}{"Tabuada v3.0":^60}')
print(f'{cores["green"]}-=-{cores["reset"]}' * 20)

# Loop while infinito para cálculo da tabuada
while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    print(f'-' * 40)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i:>2} = {num * i:>2}')
    print(f'-' * 40)
print(f'{cores["red"]}PROGRAMA TABUADA ENCERRADO!{cores["reset"]} Volte sempre!')
print(f'-' * 40)
