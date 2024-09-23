# ______ Exercício 007 ______

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

media = (n1 + n2) / 2

print(f'A média entre {n1} e {n2} é igual a {media:.1f}.')

# ______ Exercício 007 outra solução ______

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

print(f'A média entra {n1} e {n2} é igual a {(n1+n2)/2:.1f}.')
