# ______ Exercício 0047 ______

# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for pair in range(2, 51, 2):
    print(f'{pair}', end=' ')
print(f'ACABOU!')

# ______ Exercício 0047 outra solução ______

for pair in range(1, 51):
    if pair % 2 == 0:
        print(f'{pair}', end=' ')
print('ACABOU!')
