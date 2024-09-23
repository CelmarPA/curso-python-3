# ______ Exercício 00108 ______

# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
# valor monetário formatado.

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["blue"]}{"Formatando Moedas em Python":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Importação de Módulos
from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}.')
print(f'Diminuindo 15%, temos {moeda.moeda(moeda.diminuir(p, 15))}.')
