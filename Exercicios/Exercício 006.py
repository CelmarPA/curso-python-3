# ______ Exercício 006 ______

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print(f'O dobro de {n} vale {d}.')
print(f'O triplo de {n} vale {t}.')
print(f'A raiz quadrada de {n} é igual a {r:.2f}.')

# ______ Exercício 006 Outra solução______

n = int(input('Digite um número: '))

print(f'O dobro de {n} vale {n*2}.'
      f'O triplo de {n} vale {n*3}.'
      f'A raiz quadrada de {n} é igual a {pow(n, (1/2)):.2f}.')
