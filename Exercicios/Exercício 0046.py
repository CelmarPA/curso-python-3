# ______ Exercício 0046 ______

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

# Importação de bibliotecas
from time import sleep

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

for count in range(10, -1, -1):
    print(count)
    sleep(1)
print(f'{cores["red"]}BUM! {cores["blue"]}BUM! {cores["yellow"]}POOOW!{cores["reset"]}')
