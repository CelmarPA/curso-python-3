# ______ Exercício 0033 ______

# Faça um programa que leia três número e mostre qual é o maior e qual é o menor.

# Solicita ao usuário os número para analise
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

# Verificar quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verificar quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')
