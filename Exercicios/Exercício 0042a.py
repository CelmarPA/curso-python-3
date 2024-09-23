# ______ Exercício 0042 ______

# Refaça o DESAFIO 0035 dos triângulos, acrescentando o recuro de mostrar que tipo de triângulo será formado:
# -> Equilátero: tds os lados iguais
# -> Isósceles: dois lados iguais
# -> Escaleno: tds os lados diferentes

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m'}

# Título do programa
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{"Analisador de Triângulos v2.0":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if (s1 + s2) > s3 and (s1 + s3) > s2 and (s2 + s3) > s1:
    print(f'Os segmentos {cores["green"]}PODEM FORMAR{cores["reset"]} um triângulo ', end='')
    if s1 == s2 == s3:
        print(f'{cores["blue"]}EQUILÁTERO{cores["reset"]}!')
    elif s1 != s2 != s3 != s1:
        print(f'{cores["yellow"]}ESCALENO{cores["reset"]}!')
    else:
        print(f'{cores["magenta"]}ISÓSCELES{cores["reset"]}!')
else:
    print(f'Os segmentos {cores["red"]}NÃO PODEM FORMAR{cores["reset"]} um triângulo!')
